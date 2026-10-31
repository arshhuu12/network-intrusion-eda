# ============================================================
# Network Intrusion Analytics
# M13.4 — Research Insights Page
# ============================================================

from pathlib import Path

import pandas as pd
import streamlit as st


# ------------------------------------------------------------
# 1. Page configuration
# ------------------------------------------------------------

st.set_page_config(
    page_title="Research Insights",
    page_icon="🔬",
    layout="wide"
)


# ------------------------------------------------------------
# 2. Project paths
# ------------------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parents[2]

REPORTS_DIR = PROJECT_DIR / "reports"

FIGURES_DIR = PROJECT_DIR / "figures" / "comparative"


# ------------------------------------------------------------
# 3. Required research files
# ------------------------------------------------------------

FINDINGS_PATH = (
    REPORTS_DIR / "research_findings_summary.csv"
)

INSIGHTS_PATH = (
    REPORTS_DIR / "research_insights_summary.csv"
)

REPORT_PATH = (
    REPORTS_DIR / "final_research_findings.md"
)

FIGURES = {
    "Attack Prevalence Comparison":
        FIGURES_DIR / "final_attack_prevalence_comparison.png",

    "Categorical Distribution Shift":
        FIGURES_DIR / "final_categorical_shift_comparison.png",

    "Attack Label Coverage":
        FIGURES_DIR / "final_attack_label_coverage.png"
}


# ------------------------------------------------------------
# 4. Cached research data loading
# ------------------------------------------------------------

@st.cache_data(show_spinner="Loading research findings...")
def load_research_data():

    findings = pd.read_csv(FINDINGS_PATH)

    insights = pd.read_csv(INSIGHTS_PATH)

    report_text = REPORT_PATH.read_text(
        encoding="utf-8"
    )

    return findings, insights, report_text


# ------------------------------------------------------------
# 5. Page header
# ------------------------------------------------------------

st.title("🔬 Research Insights")

st.markdown(
    """
    Explore the key findings from our comparative
    Exploratory Data Analysis of the **NSL-KDD**
    and **UNSW-NB15** cybersecurity datasets.

    This section presents research evidence,
    visual comparisons, and important
    observations about network intrusion data.
    """
)

st.divider()


# ------------------------------------------------------------
# 6. Verify required files
# ------------------------------------------------------------

required_files = [
    FINDINGS_PATH,
    INSIGHTS_PATH,
    REPORT_PATH
]

missing_files = [
    path for path in required_files
    if not path.exists()
]

if missing_files:

    st.error(
        "Some required research files are missing."
    )

    for path in missing_files:
        st.code(str(path))

    st.stop()


# ------------------------------------------------------------
# 7. Load research artifacts
# ------------------------------------------------------------

try:

    findings_df, insights_df, report_text = (
        load_research_data()
    )

except Exception as error:

    st.error(
        f"Unable to load research artifacts: {error}"
    )

    st.stop()


# ------------------------------------------------------------
# 8. Research overview
# ------------------------------------------------------------

st.header("📊 Research Overview")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Datasets Analyzed",
    "2"
)

col2.metric(
    "Research Findings",
    len(findings_df)
)

col3.metric(
    "Research Insights",
    len(insights_df)
)


# ------------------------------------------------------------
# 9. Comparative research visualizations
# ------------------------------------------------------------

st.header("📈 Comparative Visualizations")

st.write(
    """
    These figures were generated during the
    project's Exploratory Data Analysis phase.
    """
)

for figure_title, figure_path in FIGURES.items():

    st.subheader(figure_title)

    if figure_path.exists():

        st.image(
            str(figure_path),
            use_container_width=True
        )

    else:

        st.warning(
            f"Figure not found: {figure_path.name}"
        )


# ------------------------------------------------------------
# 10. Research findings
# ------------------------------------------------------------

st.header("📋 Research Findings")

st.write(
    """
    The following table contains findings
    documented during our research analysis.
    """
)

st.dataframe(
    findings_df,
    use_container_width=True,
    hide_index=True
)


# ------------------------------------------------------------
# 11. Research insights
# ------------------------------------------------------------

st.header("💡 Research Insights")

st.write(
    """
    These insights summarize important patterns,
    dataset characteristics, and limitations
    identified through our analysis.
    """
)

st.dataframe(
    insights_df,
    use_container_width=True,
    hide_index=True
)


# ------------------------------------------------------------
# 12. Research report
# ------------------------------------------------------------

st.header("📄 Detailed Research Report")

with st.expander(
    "Read the Complete Research Report",
    expanded=False
):

    st.markdown(report_text)


# ------------------------------------------------------------
# 13. Download research artifacts
# ------------------------------------------------------------

st.header("⬇️ Download Research Results")

download_col1, download_col2, download_col3 = (
    st.columns(3)
)

with download_col1:

    st.download_button(
        label="Download Findings CSV",
        data=findings_df.to_csv(index=False),
        file_name="research_findings.csv",
        mime="text/csv"
    )

with download_col2:

    st.download_button(
        label="Download Insights CSV",
        data=insights_df.to_csv(index=False),
        file_name="research_insights.csv",
        mime="text/csv"
    )

with download_col3:

    st.download_button(
        label="Download Research Report",
        data=report_text,
        file_name="research_report.md",
        mime="text/markdown"
    )


# ------------------------------------------------------------
# 14. Research limitations
# ------------------------------------------------------------

st.header("⚠️ Research Limitations")

st.warning(
    """
    These findings are based on benchmark
    cybersecurity datasets.

    Dataset characteristics, class distributions,
    and attack categories may differ from
    modern real-world network environments.

    The analysis should not be interpreted
    as evidence of production deployment readiness.
    """
)


# ------------------------------------------------------------
# 15. Footer
# ------------------------------------------------------------

st.divider()

st.caption(
    "Research Insights | "
    "Comparative EDA | "
    "NSL-KDD + UNSW-NB15"
)