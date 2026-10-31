# ============================================================
# Network Intrusion Analytics
# M13.5 — Model Performance Dashboard
# ============================================================

from pathlib import Path

import pandas as pd
import streamlit as st


# ------------------------------------------------------------
# 1. Page configuration
# ------------------------------------------------------------

st.set_page_config(
    page_title="Model Performance",
    page_icon="🤖",
    layout="wide"
)


# ------------------------------------------------------------
# 2. Project paths
# ------------------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parents[2]

ML_REPORTS_DIR = PROJECT_DIR / "reports" / "ml"


# ------------------------------------------------------------
# 3. Report paths
# ------------------------------------------------------------

REPORT_FILES = {
    "comparison": ML_REPORTS_DIR / "unsw_model_comparison.csv",
    "selected": ML_REPORTS_DIR / "unsw_selected_model_config.csv",
    "official": ML_REPORTS_DIR / "unsw_final_test_metrics.csv",
    "confusion": ML_REPORTS_DIR / "unsw_final_test_confusion_matrix.csv",
    "non_overlap": ML_REPORTS_DIR / "unsw_non_overlap_test_metrics.csv",
}


# ------------------------------------------------------------
# 4. Load saved reports
# ------------------------------------------------------------

@st.cache_data(show_spinner="Loading ML evaluation reports...")
def load_reports():

    reports = {}

    for name, path in REPORT_FILES.items():

        if not path.exists():
            raise FileNotFoundError(
                f"Missing ML report: {path}"
            )

        reports[name] = pd.read_csv(path)

    return reports


# ------------------------------------------------------------
# 5. Page header
# ------------------------------------------------------------

st.title("🤖 Machine Learning Performance")

st.write(
    """
    Evaluate the selected Random Forest intrusion
    classifier using development validation,
    official UNSW-NB15 test results, and
    supplementary non-overlapping test analysis.
    """
)

st.divider()


# ------------------------------------------------------------
# 6. Read reports
# ------------------------------------------------------------

try:
    reports = load_reports()

except Exception as error:

    st.error(f"Unable to load ML reports: {error}")

    st.stop()


comparison_df = reports["comparison"]
selected_df = reports["selected"]
official_df = reports["official"]
confusion_df = reports["confusion"]
non_overlap_df = reports["non_overlap"]


# ------------------------------------------------------------
# 7. Show model configuration
# ------------------------------------------------------------

st.header("⚙️ Selected Model Configuration")

st.write(
    """
    The Random Forest model and decision threshold
    were selected using development validation data.

    The official test dataset was not used to
    choose the classification threshold.
    """
)

st.dataframe(
    selected_df,
    use_container_width=True,
    hide_index=True
)


# ------------------------------------------------------------
# 8. Development model comparison
# ------------------------------------------------------------

st.header("📊 Development Model Comparison")

st.write(
    """
    Logistic Regression was used as a baseline.

    Random Forest was evaluated as an alternative
    classifier using the same development split.
    """
)

st.dataframe(
    comparison_df,
    use_container_width=True,
    hide_index=True
)


# ------------------------------------------------------------
# 9. Official test metrics
# ------------------------------------------------------------

st.header("🎯 Official Test Performance")

st.caption(
    "UNSW-NB15 official test partition — 82,332 records."
)

st.dataframe(
    official_df,
    use_container_width=True,
    hide_index=True
)


# ------------------------------------------------------------
# 10. Confusion matrix
# ------------------------------------------------------------

st.header("🧩 Official Test Confusion Matrix")

st.write(
    """
    The confusion matrix summarizes correct
    and incorrect predictions.

    **Normal = 0 | Attack = 1**
    """
)

st.dataframe(
    confusion_df,
    use_container_width=True
)

st.info(
    """
    **True Negative (TN):** Normal traffic correctly
    predicted as normal.

    **False Positive (FP):** Normal traffic incorrectly
    predicted as an attack.

    **False Negative (FN):** Attack traffic incorrectly
    predicted as normal.

    **True Positive (TP):** Attack traffic correctly
    predicted as an attack.
    """
)


# ------------------------------------------------------------
# 11. Non-overlapping test evaluation
# ------------------------------------------------------------

st.header("🔬 Non-Overlapping Test Evaluation")

st.write(
    """
    The official UNSW-NB15 test dataset contains
    records whose feature vectors exactly match
    feature vectors in the training dataset.

    To investigate this issue, we performed
    supplementary evaluation after excluding
    those exact feature overlaps.

    The trained model and selected threshold
    were not modified.
    """
)

st.dataframe(
    non_overlap_df,
    use_container_width=True,
    hide_index=True
)


# ------------------------------------------------------------
# 12. Key interpretation
# ------------------------------------------------------------

st.header("💡 Interpretation")

st.success(
    """
    The selected Random Forest demonstrated
    high attack recall on the official test dataset.
    """
)

st.warning(
    """
    However, the model produced a substantial
    number of false positives.

    A high false-positive rate can generate
    excessive security alerts and reduce
    operational usefulness.
    """
)

st.info(
    """
    The non-overlapping evaluation provides
    additional evidence about performance
    on records without exact training-feature
    matches.

    It does not establish that the model will
    generalize to real-world network traffic.
    """
)


# ------------------------------------------------------------
# 13. Downloads
# ------------------------------------------------------------

st.header("⬇️ Download Evaluation Reports")

col1, col2 = st.columns(2)

with col1:

    st.download_button(
        "Download Official Test Metrics",
        data=official_df.to_csv(index=False),
        file_name="unsw_official_test_metrics.csv",
        mime="text/csv"
    )

with col2:

    st.download_button(
        "Download Non-Overlapping Metrics",
        data=non_overlap_df.to_csv(index=False),
        file_name="unsw_non_overlap_metrics.csv",
        mime="text/csv"
    )


# ------------------------------------------------------------
# 14. Footer
# ------------------------------------------------------------

st.divider()

st.caption(
    "Model Performance | "
    "Random Forest | "
    "UNSW-NB15 | "
    "Offline Benchmark Evaluation"
)