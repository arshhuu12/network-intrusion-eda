# Network Intrusion Detection: Comparative EDA, Machine Learning and Interactive Analytics

**A research-oriented cybersecurity data analytics project using NSL-KDD and UNSW-NB15, featuring exploratory data analysis, Random Forest classification, and an interactive Streamlit dashboard.**

## 1. Project Overview

Network intrusion detection is an important component of cybersecurity. An intrusion detection system aims to identify suspicious or malicious network activity.

However, developing reliable detection models requires more than achieving high classification accuracy. Dataset quality, class imbalance, duplicate records, distribution differences, and false-positive rates can substantially affect model evaluation.

This project investigates these challenges through comparative exploratory data analysis of two benchmark intrusion detection datasets:

- **NSL-KDD**
- **UNSW-NB15**

The project also implements a Random Forest classifier using UNSW-NB15 and provides an interactive Streamlit application for exploring research findings, examining model performance, and generating batch predictions.

The work is motivated by an IEEE research paper comparing data-mining techniques for network intrusion detection.

## 2. Research Objectives

The main objectives are to:

1. Examine the structure and characteristics of NSL-KDD and UNSW-NB15.
2. Evaluate missing values, duplicate records, and data quality.
3. Investigate normal and attack traffic distributions.
4. Explore numerical and categorical feature relationships.
5. Analyze differences between training and testing datasets.
6. Identify limitations that may affect intrusion detection model evaluation.
7. Develop and evaluate a baseline machine-learning classifier.
8. Communicate research findings through visualizations and an interactive dashboard.

## 3. Datasets

### NSL-KDD

NSL-KDD is a benchmark dataset commonly used in network intrusion detection research.

| Partition | Records |
|---|---:|
| Training | 125,973 |
| Testing | 22,544 |
| Total | 148,517 |

### UNSW-NB15

UNSW-NB15 contains network traffic records representing normal activity and several attack categories.

| Partition | Records |
|---|---:|
| Training | 175,341 |
| Testing | 82,332 |
| Total | 257,673 |

### Dataset Usage

Both datasets are used for comparative exploratory data analysis.

The Random Forest classification component is trained and evaluated using the official UNSW-NB15 training and testing partitions.

Raw datasets are excluded from version control because of their size and to keep the repository focused on code, analysis, and reproducible research artifacts.

## 4. Exploratory Data Analysis

The project follows a structured analytical workflow.

### Data Understanding

- Dataset dimensions and feature types
- Numerical and categorical variables
- Target-label definitions
- Training and testing partitions

### Data Quality Assessment

- Missing-value analysis
- Duplicate-record analysis
- Data validation
- Class distribution inspection

### Univariate Analysis

- Numerical feature distributions
- Categorical feature frequencies
- Normal and attack class prevalence
- Distribution characteristics and outliers

### Bivariate and Multivariate Analysis

- Feature relationships
- Relationships between features and attack labels
- Correlation analysis
- Comparative visualizations

### Train-Test Comparison

- Class distribution differences
- Feature distribution changes
- Categorical distribution changes
- Potential implications for model generalization

### Research Synthesis

The analytical findings are consolidated into research summaries, comparative figures, and a final research report.

## 5. Key Research Findings

### Duplicate Records

The NSL-KDD partitions contained no exact duplicate records in the performed analysis.

UNSW-NB15 contained substantial duplication:

| Partition | Duplicate Records | Percentage |
|---|---:|---:|
| UNSW-NB15 Training | 67,601 | 38.55% |
| UNSW-NB15 Testing | 26,387 | 32.05% |

These findings highlight the importance of investigating duplicate records when interpreting model performance.

### Class Distribution

The proportion of attack traffic differs across datasets and partitions.

For example, attack traffic represents approximately:

- **46.54%** of NSL-KDD training records.
- **68.06%** of UNSW-NB15 training records.

These differences affect how evaluation metrics should be interpreted.

### Train-Test Feature Overlap

The UNSW-NB15 analysis identified **8,541 official test records** whose feature vectors also appeared in the training data.

This represents approximately **10.37%** of the official test partition.

A separate evaluation on non-overlapping test records was performed to investigate the model's behavior beyond these shared feature patterns.

## 6. Machine Learning Methodology

### Classification Task

The project performs binary network intrusion classification:

| Label | Meaning |
|---|---|
| 0 | Normal traffic |
| 1 | Attack traffic |

### Input Features

The model uses **42 UNSW-NB15 features**:

- 39 numerical features
- 3 categorical features: `proto`, `service`, and `state`

Identifier and target-related columns are excluded from the model inputs to prevent target leakage.

### Preprocessing

The machine-learning pipeline includes:

- Numerical missing-value imputation
- Categorical missing-value imputation
- One-hot encoding of categorical features
- Random Forest classification

Preprocessing and classification are combined in a saved scikit-learn pipeline.

### Model Development

Logistic Regression and Random Forest were evaluated during model development.

Random Forest was selected based on validation performance.

The classification threshold was selected using development validation data and fixed at **0.45** before final evaluation on the official test partition.

## 7. Model Evaluation

### Official UNSW-NB15 Test Results

The selected Random Forest achieved:

| Metric | Result |
|---|---:|
| Accuracy | 84.79% |
| Precision | 78.62% |
| Attack Recall | 99.40% |
| F1 Score | 87.80% |
| Average Precision | 98.74% |
| False-Positive Rate | 33.12% |

### Confusion Matrix

| Actual / Predicted | Normal | Attack |
|---|---:|---:|
| Normal | 24,745 | 12,255 |
| Attack | 270 | 45,062 |

The model detects most attack records in the official test dataset.

However, its false-positive rate is substantial: approximately one-third of normal test records are incorrectly classified as attacks.

**High attack recall should not be interpreted as evidence of production readiness.**

### Non-Overlapping Test Evaluation

An additional evaluation excluded official test records whose feature vectors appeared in the training partition.

| Metric | Result |
|---|---:|
| Evaluation records | 73,791 |
| Accuracy | 83.75% |
| Precision | 76.41% |
| Attack Recall | 99.32% |
| F1 Score | 86.37% |
| Average Precision | 98.35% |
| False-Positive Rate | 33.02% |

This evaluation provides additional insight into generalization beyond overlapping feature patterns.

## 8. Interactive Streamlit Dashboard

The project includes an interactive Streamlit application with five sections.

### Research Overview

Introduces the research objectives, datasets, model results, and limitations.

### Dataset Explorer

Allows users to explore the NSL-KDD and UNSW-NB15 datasets, including:

- Dataset dimensions
- Missing values
- Duplicate records
- Data previews
- Class distributions

### Research Insights

Presents comparative visualizations, analytical summaries, and downloadable research findings.

### Model Performance

Displays model comparison results, selected model configuration, official test metrics, confusion matrix, and non-overlapping test evaluation.

### Batch Prediction

Allows users to upload UNSW-NB15-compatible CSV files and generate binary intrusion predictions.

Features include:

- Required-feature validation
- Numerical and categorical input validation
- Batch prediction
- Attack probability estimates
- Configurable decision threshold stored in model metadata
- Prediction summaries
- Downloadable CSV results
- Protection against displaying predictions from a previously uploaded file

The dashboard performs batch classification of uploaded records. It does not capture live network traffic.

## 9. Technology Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Data Analysis | pandas, NumPy |
| Statistical Analysis | SciPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | scikit-learn |
| Model Serialization | joblib |
| Interactive Dashboard | Streamlit |
| Research Environment | JupyterLab |
| Version Control | Git, GitHub |

The development environment uses Python 3.12.3.

## 10. Installation and Setup

### Prerequisites

- Python 3.12
- Git
- A Python-compatible terminal

### Clone the Repository

```bash
git clone https://github.com/arshhuu12/network-intrusion-eda.git
cd network-intrusion-eda
```

### Create a Virtual Environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

### Launch JupyterLab

```powershell
python -m jupyter lab
```

### Launch the Streamlit Dashboard

From the project root:

```powershell
python -m streamlit run app/app.py
```

The application will display a local address in the terminal.

Open that address in your browser.

## 11. Dataset Availability and Setup

The original NSL-KDD and UNSW-NB15 datasets are not included in this GitHub repository.

Users must download the datasets separately to reproduce the complete exploratory analysis and use the Dataset Explorer.

### Required Dataset Files

The project expects four files:

**NSL-KDD**
- `KDDTrain+.txt`
- `KDDTest+.txt`

**UNSW-NB15**
- `UNSW_NB15_training-set.csv`
- `UNSW_NB15_testing-set.csv`

### Dataset Directory Structure

Place the files in the following directories:

```text
network-intrusion-eda/
│
├── data/
│   └── raw/
│       ├── nsl_kdd/
│       │   ├── KDDTrain+.txt
│       │   └── KDDTest+.txt
│       │
│       └── unsw_nb15/
│           ├── UNSW_NB15_training-set.csv
│           └── UNSW_NB15_testing-set.csv
```

The directory names and filenames must match exactly because the notebooks and Streamlit Dataset Explorer reference these paths.

### Dataset Sources

**NSL-KDD**

Obtain the NSL-KDD benchmark dataset from the University of New Brunswick's Canadian Institute for Cybersecurity dataset resources.

**UNSW-NB15**

Obtain the official UNSW-NB15 training and testing CSV files from the UNSW Canberra Cyber cybersecurity dataset resources.

Use the supplied training and testing partitions rather than creating new random splits for the final benchmark evaluation.

### Create Dataset Directories

From the project root, run:

```powershell
New-Item -ItemType Directory -Force data/raw/nsl_kdd
New-Item -ItemType Directory -Force data/raw/unsw_nb15
```

Copy the downloaded files into their corresponding directories.

### Verify Dataset Files

Run:

```powershell
@'
from pathlib import Path

required_files = [
    "data/raw/nsl_kdd/KDDTrain+.txt",
    "data/raw/nsl_kdd/KDDTest+.txt",
    "data/raw/unsw_nb15/UNSW_NB15_training-set.csv",
    "data/raw/unsw_nb15/UNSW_NB15_testing-set.csv",
]

for filename in required_files:
    path = Path(filename)

    if not path.is_file():
        raise FileNotFoundError(filename)

    print(f"FOUND: {filename}")

print("All four dataset files are available.")
'@ | python
```

### Dataset-Dependent Features

The Dataset Explorer requires the original datasets.

Research findings and model-performance pages use saved report artifacts.

The Batch Prediction page uses the saved Random Forest pipeline and accepts CSV files containing the 42 required model features.

The application is intended for research and demonstration, not real-time network monitoring.

## 12. Research Notebooks

The research workflow is organized into the following notebooks:

| Notebook | Purpose |
|---|---|
| `00_environment_check.ipynb` | Environment verification |
| `01_data_understanding.ipynb` | Dataset structure and initial inspection |
| `02_data_quality.ipynb` | Missing values and duplicate analysis |
| `03_data_validation.ipynb` | Data validation |
| `04_univariate_eda.ipynb` | Univariate exploratory analysis |
| `05_bivariate_eda.ipynb` | Bivariate analysis |
| `06_train_test_comparison.ipynb` | Training and testing distribution comparison |
| `07_research_synthesis.ipynb` | Consolidated research findings |
| `08_ml_feasibility.ipynb` | Machine-learning development and evaluation |

## 13. Project Limitations

This project has several important limitations:

1. The machine-learning model is evaluated using benchmark datasets rather than live network traffic.
2. The official test false-positive rate is relatively high.
3. Dataset characteristics may differ from modern operational networks.
4. The model performs binary classification rather than identifying individual attack categories.
5. The Streamlit application is designed for research exploration and batch prediction.
6. The project does not provide real-time packet capture, network monitoring, or automated incident response.
7. Additional external validation would be necessary before considering operational deployment.

The application is intended as an academic research and data analytics demonstration, not a production intrusion detection system.

## 14. Future Improvements

Potential extensions include:

- False-positive reduction through additional model development
- Evaluation on newer network intrusion datasets
- Model calibration and further threshold analysis using separate validation data
- Additional generalization and robustness testing
- Multiclass attack classification
- Expanded automated testing
- Deployment of the research dashboard

## 15. Research Reference

Shehadeh, A., ALTaweel, H., and Qusef, A.

*Analysis of Data Mining Techniques on KDD-Cup'99, NSL-KDD and UNSW-NB15 Datasets for Intrusion Detection.*

IEEE ACIT, 2023.

DOI: **10.1109/ACIT58888.2023.10453884**

## 16. Project Purpose

This project demonstrates practical skills in:

- Exploratory data analysis
- Data quality assessment
- Statistical visualization
- Comparative dataset analysis
- Machine-learning experimentation
- Model evaluation and interpretation
- Python application development
- Interactive dashboard development
- Research documentation

The central goal is to demonstrate a structured, evidence-based approach to cybersecurity data analytics while communicating both the capabilities and limitations of machine-learning-based intrusion detection.