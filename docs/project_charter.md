# Project Charter — Version 1.0

**Project:** Comparative Data Quality Assessment and Exploratory Visual Analytics of NSL-KDD and UNSW-NB15 Intrusion Detection Datasets  
**Domain:** Data Science, Exploratory Data Analysis, Data Visualization, Cybersecurity Data  
**Duration:** Seven days; approximately 35–42 focused hours  
**Status:** Baseline scope approved for implementation; dataset details subject to verification on acquisition.

## 1. Research foundation
This project is motivated by Shehadeh, ALTaweel and Qusef (2023), *Analysis of Data Mining Techniques on KDD-Cup'99, NSL-KDD and UNSW-NB15 Datasets for Intrusion Detection*, IEEE ACIT, DOI: 10.1109/ACIT58888.2023.10453884. The study compares intrusion-detection classifiers and recommends deeper investigation of dataset characteristics such as quality and complexity. Our project investigates these characteristics through EDA and visualization; it does **not** reproduce the paper's classification experiments or claim a newly established research gap.

## 2. Problem statement
Network intrusion-detection studies use benchmark datasets whose data quality, class composition, feature distributions and train/test characteristics can influence how subsequent analyses are interpreted. These properties may be overlooked when attention is concentrated on classifier performance. This project systematically profiles two established datasets, investigates their within-dataset patterns, and compares compatible dataset-level characteristics to support informed interpretation and future research.

## 3. Main objective
To investigate and compare the data-quality characteristics, class distributions, feature relationships and training–testing differences of NSL-KDD and UNSW-NB15 using reproducible EDA and visual analytics.

## 4. Specific objectives
1. **Dataset understanding:** Document the origin, schema, labels and official train/test partitions of both datasets.
2. **Data quality:** Assess completeness, duplication, consistency and selected documented validity constraints.
3. **Exploratory analysis:** Examine class imbalance, numerical distributions, categorical patterns and selected feature relationships.
4. **Comparative analysis:** Compare compatible dataset-level properties and evaluate train/test distribution differences within each dataset.
5. **Communication and reproducibility:** Produce meaningful figures, verified findings, documented decisions and runnable notebooks.

## 5. Research questions
- **RQ1:** What data-quality characteristics are present in NSL-KDD and UNSW-NB15?
- **RQ2:** How are normal and malicious traffic classes distributed within each dataset?
- **RQ3:** What statistical patterns and feature relationships can be identified?
- **RQ4:** How do class distributions and selected feature characteristics differ between each dataset's training and testing partitions?

## 6. Data scope
- **NSL-KDD:** Documented `KDDTrain+` and `KDDTest+` partitions (commonly 125,973 and 22,544 rows; 41 input features). Confirm counts, schema and any extra label/difficulty fields after loading.
- **UNSW-NB15:** Official training and testing CSV partitions (commonly 175,341 and 82,332 rows). Verify exact columns, label conventions and feature count from the selected files and official documentation.
- Analyze the two datasets separately where feature semantics or attack taxonomies differ. Cross-dataset comparison is restricted to compatible metrics (e.g., missingness rates, class proportions, categorical/numerical feature counts) with appropriate context.

## 7. Methodology
1. Establish research questions, source documentation and dataset provenance.
2. Download documented partitions; retain unmodified raw files.
3. Profile schema, record grain, types, labels and split characteristics.
4. Audit missingness, duplication, selected validity constraints and unusual values.
5. Record decisions; apply only justified preprocessing and validate changes.
6. Conduct univariate, bivariate and selected multivariate EDA.
7. Compare within-dataset train/test distributions and compatible cross-dataset properties.
8. Produce labeled visualizations, verify numerical claims and document limitations.

**Analysis convention:** Unless explicitly stated otherwise, report findings for each partition separately and label figures with the dataset and split. Do not merge train and test for modeling; any pooled descriptive summaries must be clearly identified. Do not treat unusual attack-related values as errors without evidence.

## 8. Tools
Python, Jupyter Notebook, pandas, NumPy, Matplotlib, seaborn; SciPy/scikit-learn only if needed for selected statistics or optional dimensionality reduction; Git/GitHub and Markdown.

## 9. In scope / out of scope
**In scope:** Dataset profiling; quality audit; class distributions; selected univariate/bivariate/multivariate analyses; train/test comparisons; approximately **12–16** final meaningful figures; findings report; reproducible repository and academic presentation.

**Out of scope:** Production intrusion-detection system; live traffic; extensive classifier benchmarking; deep learning; hyperparameter tuning; cloud deployment; full KDD-Cup'99 analysis. Machine learning is optional future work, not a completion requirement.

## 10. Measurable acceptance criteria
| Area | Minimum evidence |
|---|---|
| Dataset understanding | Both train/test partitions profiled; source, row grain, column roles and label meanings documented |
| Data quality | Missingness, duplicate rates, dtypes and selected validity checks measured per relevant partition |
| Class distribution | Counts and percentages for normal/attack and documented attack groups; denominators stated |
| Univariate | At least three meaningful features per dataset examined |
| Bivariate | At least two interpretable relationships per dataset examined |
| Multivariate | Selected numerical correlation analysis with caveats |
| Train/test | Class proportions and at least two selected feature distributions compared within each dataset |
| Visualization | 12–16 legible, labeled, evidence-backed final figures; no filler charts |
| Validation | Key counts, percentages and transformations checked and recorded |
| Reproducibility | Environment requirements, download instructions, execution order and clean repository documented |
| Reporting | All four RQs addressed, including limitations and non-causal interpretation |

## 11. Deliverables
- `docs/project_charter.md`, `docs/ieee_paper_analysis.md`, `docs/eda_analysis_plan.md`
- Dataset profiles and data-quality issue/decision log
- Reproducible Jupyter notebooks and selected reusable Python functions
- 12–16 final visualizations with interpretations
- Verified findings and methodology reports
- README, dependency list, `.gitignore`, academic report and presentation

## 12. Risks and safeguards
- **Different schemas/taxonomies:** Compare only semantically compatible quantities.
- **Historical benchmark limitations:** Avoid generalizing to contemporary production networks.
- **Data leakage:** Keep official partitions identifiable; never fit transformations across test data for predictive claims.
- **Misleading cleaning:** Preserve raw data and record every modification.
- **Limited time/8 GB RAM:** Prefer official subsets, targeted feature selections and memory-aware plotting; drop optional PCA/ML first.
- **Unsupported causal claims:** EDA describes patterns; it does not establish impacts on classifier performance.

## 13. Definition of done
All four research questions have evidence-backed answers; code reruns with documented inputs; figures and tables match verified calculations; methodological choices and limitations are explained; final academic report and repository are ready for review.

## Primary reference
Shehadeh, A., ALTaweel, H., & Qusef, A. (2023). *Analysis of Data Mining Techniques on KDD-Cup'99, NSL-KDD and UNSW-NB15 Datasets for Intrusion Detection*. 24th International Arab Conference on Information Technology (ACIT). IEEE. https://doi.org/10.1109/ACIT58888.2023.10453884
