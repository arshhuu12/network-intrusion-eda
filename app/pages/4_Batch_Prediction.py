# ============================================================
# Network Intrusion Analytics
# M14.2 — CSV Batch Prediction Page
# ============================================================


from pathlib import Path
import hashlib
import numpy as np
import pandas as pd
import streamlit as st


# ------------------------------------------------------------
# 1. Page configuration
# ------------------------------------------------------------

st.set_page_config(
    page_title="Batch Intrusion Prediction",
    page_icon="🛡️",
    layout="wide"
)


# ------------------------------------------------------------
# 2. Import prediction engine
# ------------------------------------------------------------

import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[2]

APP_DIR = PROJECT_DIR / "app"

# Make the app directory available for imports.
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from utils.prediction import (
    load_model,
    validate_input,
    get_prediction_summary
)


# ------------------------------------------------------------
# 3. Application settings
# ------------------------------------------------------------

MAX_UPLOAD_MB = 20
MAX_RECORDS = 100_000
BATCH_SIZE = 5_000


# ------------------------------------------------------------
# 4. Cache the trained model
# ------------------------------------------------------------

@st.cache_resource(show_spinner="Loading trained model...")
def get_cached_model():
    return load_model()


# ------------------------------------------------------------
# 5. Page header
# ------------------------------------------------------------

st.title("🛡️ Batch Intrusion Prediction")

st.write(
    """
    Upload network traffic records in CSV format
    and classify them using the trained
    **UNSW-NB15 Random Forest model**.

    This tool performs offline batch classification.
    It does not monitor live network traffic.
    """
)

st.divider()


# ------------------------------------------------------------
# 6. Load model
# ------------------------------------------------------------

try:
    pipeline, metadata = get_cached_model()

except Exception as error:
    st.error(f"Unable to load trained model: {error}")
    st.stop()


required_features = metadata["feature_columns"]
threshold = float(metadata["threshold"])


# ------------------------------------------------------------
# 7. Model information
# ------------------------------------------------------------

st.header("⚙️ Prediction Configuration")

col1, col2, col3 = st.columns(3)

col1.metric("Model", metadata["model_name"])
col2.metric("Required Features", len(required_features))
col3.metric("Decision Threshold", f"{threshold:.2f}")

with st.expander("View Required Input Features"):
    st.write(required_features)


# ------------------------------------------------------------
# 8. Upload instructions
# ------------------------------------------------------------

st.header("📤 Upload Network Traffic CSV")

st.info(
    """
    Your CSV must contain the 42 UNSW-NB15
    model input features.

    Additional columns such as `id`, `label`,
    or `attack_cat` are allowed but are
    not used as prediction inputs.

    Missing required feature columns will
    cause validation to fail.
    """
)


# ------------------------------------------------------------
# 9. File upload
# ------------------------------------------------------------

uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"],
    accept_multiple_files=False
)

if uploaded_file is None:
    st.info("Upload a CSV file to begin.")
    st.stop()

# ------------------------------------------------------------
# Identify uploaded file by its contents
# ------------------------------------------------------------

uploaded_bytes = uploaded_file.getvalue()

uploaded_file_hash = hashlib.sha256(
    uploaded_bytes
).hexdigest()
# ------------------------------------------------------------
# 10. File size validation
# ------------------------------------------------------------

file_size_mb = uploaded_file.size / (1024 ** 2)

if file_size_mb > MAX_UPLOAD_MB:
    st.error(
        f"File is too large: {file_size_mb:.2f} MB. "
        f"Maximum allowed size: {MAX_UPLOAD_MB} MB."
    )
    st.stop()


# ------------------------------------------------------------
# 11. Read uploaded CSV
# ------------------------------------------------------------

try:
    uploaded_df = pd.read_csv(uploaded_file)

except Exception as error:
    st.error(f"Unable to read CSV: {error}")
    st.stop()


if uploaded_df.empty:
    st.error("The uploaded CSV contains no records.")
    st.stop()


if len(uploaded_df) > MAX_RECORDS:
    st.error(
        f"CSV contains {len(uploaded_df):,} records. "
        f"Maximum allowed: {MAX_RECORDS:,}."
    )
    st.stop()


# ------------------------------------------------------------
# 12. Input validation
# ------------------------------------------------------------

try:
    X = validate_input(uploaded_df, metadata)

except (ValueError, TypeError) as error:
    st.error(f"Input validation failed: {error}")
    st.stop()


st.success("CSV uploaded and validated successfully!")


# ------------------------------------------------------------
# 13. Upload overview
# ------------------------------------------------------------

st.header("📋 Uploaded Data Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Records", f"{len(uploaded_df):,}")
col2.metric("Uploaded Columns", len(uploaded_df.columns))
col3.metric("Validated Model Features", X.shape[1])


st.subheader("Preview Uploaded Records")

st.dataframe(
    uploaded_df.head(10),
    use_container_width=True,
    hide_index=True
)


# ------------------------------------------------------------
# 14. Batch prediction function
# ------------------------------------------------------------

def run_batch_predictions(X, pipeline, threshold):

    probabilities_list = []

    total_records = len(X)

    progress_bar = st.progress(
        0,
        text="Running batch predictions..."
    )

    for start in range(0, total_records, BATCH_SIZE):

        end = min(start + BATCH_SIZE, total_records)

        batch = X.iloc[start:end]

        batch_probabilities = (
            pipeline.predict_proba(batch)[:, 1]
        )

        probabilities_list.append(batch_probabilities)

        progress = end / total_records

        progress_bar.progress(
            progress,
            text=f"Processed {end:,} of {total_records:,} records"
        )

    probabilities = np.concatenate(probabilities_list)

    predictions = (
        probabilities >= threshold
    ).astype(int)

    return probabilities, predictions


# ------------------------------------------------------------
# 15. Run prediction button
# ------------------------------------------------------------

st.divider()

if st.button(
    "🚀 Run Intrusion Predictions",
    type="primary",
    use_container_width=True
):

    try:

        probabilities, predictions = (
            run_batch_predictions(
                X,
                pipeline,
                threshold
            )
        )

        results_df = uploaded_df.copy()

        results_df["attack_probability"] = probabilities

        results_df["predicted_label"] = predictions

        results_df["prediction"] = np.where(
            predictions == 1,
            "Attack",
            "Normal"
        )

        st.session_state["prediction_results"] = results_df

        st.session_state["prediction_file_hash"] = (
            uploaded_file_hash
        )

    except Exception as error:

        st.error(f"Prediction failed: {error}")
        st.stop()


# ------------------------------------------------------------
# 16. Display prediction results
# ------------------------------------------------------------

results_df = st.session_state.get(
    "prediction_results"
)

result_file_hash = st.session_state.get(
    "prediction_file_hash"
)

if (
    results_df is not None
    and result_file_hash == uploaded_file_hash
):

    st.header("📊 Prediction Results")

    summary = get_prediction_summary(results_df)

    metric1, metric2, metric3, metric4 = st.columns(4)

    metric1.metric(
        "Total Records",
        f"{summary['total_records']:,}"
    )

    metric2.metric(
        "Predicted Attacks",
        f"{summary['attack_count']:,}"
    )

    metric3.metric(
        "Predicted Normal",
        f"{summary['normal_count']:,}"
    )

    metric4.metric(
        "Predicted Attack Rate",
        f"{summary['attack_percentage']:.2f}%"
    )

    st.subheader("Normal vs Attack Predictions")

    chart_df = pd.DataFrame({
        "Traffic Type": ["Normal", "Attack"],
        "Records": [
            summary["normal_count"],
            summary["attack_count"]
        ]
    })

    st.bar_chart(
        chart_df.set_index("Traffic Type")
    )

    st.subheader("Prediction Table")

    display_columns = [
        "attack_probability",
        "predicted_label",
        "prediction"
    ]

    st.dataframe(
        results_df[display_columns].head(100),
        use_container_width=True,
        hide_index=True
    )

    st.caption(
        "Showing the first 100 prediction results."
    )

    st.download_button(
        label="⬇️ Download Prediction Results",
        data=results_df.to_csv(index=False),
        file_name="intrusion_predictions.csv",
        mime="text/csv",
        use_container_width=True
    )

    st.warning(
        """
        Predictions are generated using a
        benchmark-trained model.

        An attack prediction is not proof
        of malicious activity.

        The model has a substantial false-positive
        rate on the official test dataset.
        """
    )