# ============================================================
# Network Intrusion Detection — Streamlit Dashboard
# M13.1: Application Foundation
# ============================================================

from pathlib import Path
import streamlit as st


# ------------------------------------------------------------
# 1. Project paths
# ------------------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parents[1]

REPORTS_DIR = PROJECT_DIR / "reports"
FIGURES_DIR = PROJECT_DIR / "figures"
MODELS_DIR = PROJECT_DIR / "models"


# ------------------------------------------------------------
# 2. Page configuration
# ------------------------------------------------------------

st.set_page_config(
    page_title="Network Intrusion Analytics",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ------------------------------------------------------------
# 3. Application header
# ------------------------------------------------------------

st.title("🛡️ Network Intrusion Analytics")

st.markdown(
    """
    **A Research-Driven Cybersecurity Analytics Dashboard**

    Exploratory Data Analysis, Comparative Research,
    and Machine Learning-Based Intrusion Classification.
    """
)

st.divider()


# ------------------------------------------------------------
# 4. Sidebar
# ------------------------------------------------------------

with st.sidebar:

    st.header("🛡️ Project Navigation")

    st.info(
        "Network Intrusion Detection "
        "using NSL-KDD and UNSW-NB15"
    )

    st.markdown("### Project Components")

    st.markdown(
        """
        - Dataset Exploration
        - Research Visualizations
        - Model Evaluation
        - Batch Intrusion Prediction
        """
    )

    st.divider()

    st.caption(
        "Academic research and portfolio demonstration."
    )


# ------------------------------------------------------------
# 5. Project overview
# ------------------------------------------------------------

st.header("📊 Project Overview")

st.write(
    """
    This project investigates network intrusion patterns
    using two cybersecurity benchmark datasets:

    **NSL-KDD** and **UNSW-NB15**.

    It combines exploratory data analysis, comparative
    visualization, and machine learning to study
    network attack characteristics and classification
    performance.
    """
)


# ------------------------------------------------------------
# 6. Dataset summary
# ------------------------------------------------------------

st.subheader("📁 Datasets Analyzed")

col1, col2 = st.columns(2)

with col1:

    st.metric(
        label="NSL-KDD Records",
        value="148,517"
    )

    st.caption(
        "125,973 training + 22,544 testing records"
    )

with col2:

    st.metric(
        label="UNSW-NB15 Records",
        value="257,673"
    )

    st.caption(
        "175,341 training + 82,332 testing records"
    )


# ------------------------------------------------------------
# 7. Machine learning summary
# ------------------------------------------------------------

st.subheader("🤖 Machine Learning Model")

model_col1, model_col2, model_col3 = st.columns(3)

with model_col1:

    st.metric(
        label="Selected Algorithm",
        value="Random Forest"
    )

with model_col2:

    st.metric(
        label="Decision Threshold",
        value="0.45"
    )

with model_col3:

    st.metric(
        label="Official Test Accuracy",
        value="84.79%"
    )


# ------------------------------------------------------------
# 8. Research findings
# ------------------------------------------------------------

st.subheader("🔬 Key Research Findings")

st.success(
    "The selected Random Forest achieved "
    "99.40% attack recall on the official "
    "UNSW-NB15 test dataset."
)

st.warning(
    "The official test false-positive rate "
    "was 33.12%, indicating a substantial "
    "false-alarm limitation."
)

st.info(
    "A supplementary evaluation excluding "
    "exact training-feature overlaps achieved "
    "83.75% accuracy and 99.32% attack recall."
)


# ------------------------------------------------------------
# 9. Application scope
# ------------------------------------------------------------

st.subheader("🎯 Application Scope")

st.write(
    """
    This dashboard will provide:

    1. Interactive dataset exploration.
    2. Comparative cybersecurity visualizations.
    3. Machine learning performance analysis.
    4. CSV-based batch intrusion predictions.

    **Important:** This is an offline research
    and demonstration application.

    It is not a real-time intrusion detection system
    or a production security monitoring solution.
    """
)


# ------------------------------------------------------------
# 10. Footer
# ------------------------------------------------------------

st.divider()

st.caption(
    "Network Intrusion Analytics | "
    "NSL-KDD + UNSW-NB15 | "
    "EDA + Machine Learning + Streamlit"
)