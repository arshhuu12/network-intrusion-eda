from pathlib import Path

import pandas as pd
import streamlit as st


# ============================================================
# 1. Page configuration
# ============================================================

st.set_page_config(
    page_title="Dataset Explorer",
    page_icon="📁",
    layout="wide"
)


# ============================================================
# 2. Project paths
# ============================================================

PROJECT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_DIR / "data" / "raw"


# ============================================================
# 3. Dataset configuration
# ============================================================

DATASETS = {
    "UNSW-NB15": {
        "Training": DATA_DIR / "unsw_nb15" / "UNSW_NB15_training-set.csv",
        "Testing": DATA_DIR / "unsw_nb15" / "UNSW_NB15_testing-set.csv",
    },
    "NSL-KDD": {
        "Training": DATA_DIR / "nsl_kdd" / "KDDTrain+.txt",
        "Testing": DATA_DIR / "nsl_kdd" / "KDDTest+.txt",
    }
}


# ============================================================
# 4. NSL-KDD column names
# ============================================================

NSL_KDD_COLUMNS = [
    "duration", "protocol_type", "service", "flag",
    "src_bytes", "dst_bytes", "land", "wrong_fragment",
    "urgent", "hot", "num_failed_logins", "logged_in",
    "num_compromised", "root_shell", "su_attempted",
    "num_root", "num_file_creations", "num_shells",
    "num_access_files", "num_outbound_cmds",
    "is_host_login", "is_guest_login", "count",
    "srv_count", "serror_rate", "srv_serror_rate",
    "rerror_rate", "srv_rerror_rate", "same_srv_rate",
    "diff_srv_rate", "srv_diff_host_rate",
    "dst_host_count", "dst_host_srv_count",
    "dst_host_same_srv_rate",
    "dst_host_diff_srv_rate",
    "dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate",
    "dst_host_serror_rate",
    "dst_host_srv_serror_rate",
    "dst_host_rerror_rate",
    "dst_host_srv_rerror_rate",
    "attack_type", "difficulty_level"
]


# ============================================================
# 5. Cached dataset loading
# ============================================================

@st.cache_data(show_spinner="Loading selected dataset...")
def load_dataset(dataset_name, split_name):

    file_path = DATASETS[dataset_name][split_name]

    if not file_path.exists():
        raise FileNotFoundError(
            f"Dataset file not found: {file_path}"
        )

    if dataset_name == "NSL-KDD":

        df = pd.read_csv(
            file_path,
            header=None,
            names=NSL_KDD_COLUMNS
        )

        df["binary_label"] = (
            df["attack_type"] != "normal"
        ).astype(int)

    else:

        df = pd.read_csv(file_path)

        df["binary_label"] = df["label"].astype(int)

    return df


# ============================================================
# 6. Page header
# ============================================================

st.title("📁 Interactive Dataset Explorer")

st.write(
    """
    Explore the NSL-KDD and UNSW-NB15 cybersecurity
    benchmark datasets.

    Select a dataset and partition to inspect
    its structure, quality, and attack distribution.
    """
)


# ============================================================
# 7. Dataset selection
# ============================================================

col1, col2 = st.columns(2)

with col1:
    dataset_name = st.selectbox(
        "Select Dataset",
        ["UNSW-NB15", "NSL-KDD"]
    )

with col2:
    split_name = st.selectbox(
        "Select Partition",
        ["Training", "Testing"]
    )


# ============================================================
# 8. Load selected dataset
# ============================================================

try:
    df = load_dataset(dataset_name, split_name)

except Exception as error:

    st.error(
        f"Unable to load dataset: {error}"
    )

    st.stop()


# ============================================================
# 9. Dataset overview
# ============================================================

st.subheader("📊 Dataset Overview")

total_rows = len(df)
total_columns = len(df.columns)

missing_cells = int(df.isna().sum().sum())

duplicate_rows = int(df.duplicated().sum())

metric1, metric2, metric3, metric4 = st.columns(4)

metric1.metric("Records", f"{total_rows:,}")
metric2.metric("Columns", total_columns)
metric3.metric("Missing Cells", f"{missing_cells:,}")
metric4.metric("Duplicate Rows", f"{duplicate_rows:,}")

st.caption(
    "The binary_label column is derived for dashboard "
    "analysis and is not part of the original raw dataset."
)


# ============================================================
# 10. Preview records
# ============================================================

st.subheader("🔍 Preview Dataset")

preview_rows = st.slider(
    "Number of records to display",
    min_value=5,
    max_value=100,
    value=10,
    step=5
)

st.dataframe(
    df.head(preview_rows),
    use_container_width=True
)


# ============================================================
# 11. Column information
# ============================================================

st.subheader("🧾 Column Information")

column_info = pd.DataFrame({
    "Column": df.columns,
    "Data Type": df.dtypes.astype(str).values,
    "Missing Values": df.isna().sum().values,
    "Unique Values": df.nunique(dropna=False).values
})

st.dataframe(
    column_info,
    use_container_width=True
)


# ============================================================
# 12. Attack distribution
# ============================================================

st.subheader("🚨 Normal vs Attack Distribution")

label_counts = (
    df["binary_label"]
    .value_counts()
    .reindex([0, 1], fill_value=0)
)

label_chart_df = pd.DataFrame({
    "Traffic Type": ["Normal", "Attack"],
    "Records": [
        int(label_counts.loc[0]),
        int(label_counts.loc[1])
    ]
})

st.bar_chart(
    label_chart_df.set_index("Traffic Type")
)

normal_count = int(label_counts.loc[0])
attack_count = int(label_counts.loc[1])

normal_percentage = (
    normal_count / total_rows * 100
)

attack_percentage = (
    attack_count / total_rows * 100
)

col_normal, col_attack = st.columns(2)

col_normal.metric(
    "Normal Traffic",
    f"{normal_count:,}",
    f"{normal_percentage:.2f}%"
)

col_attack.metric(
    "Attack Traffic",
    f"{attack_count:,}",
    f"{attack_percentage:.2f}%"
)


# ============================================================
# 13. Missing-value analysis
# ============================================================

st.subheader("🧹 Missing-Value Analysis")

missing_summary = (
    df.isna()
    .sum()
    .sort_values(ascending=False)
)

missing_summary = missing_summary[
    missing_summary > 0
]

if missing_summary.empty:

    st.success(
        "No missing values detected in this dataset."
    )

else:

    st.dataframe(
        missing_summary.rename("Missing Count"),
        use_container_width=True
    )


# ============================================================
# 14. Footer
# ============================================================

st.divider()

st.caption(
    f"Dataset: {dataset_name} | "
    f"Partition: {split_name} | "
    "Read-only exploration"
)