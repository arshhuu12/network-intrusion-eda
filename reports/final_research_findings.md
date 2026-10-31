# Comparative Exploratory Data Analysis of NSL-KDD and UNSW-NB15 for Network Intrusion Detection

## 1. Executive Summary

This project presents a comparative exploratory data analysis (EDA) of two network intrusion detection datasets: NSL-KDD and UNSW-NB15.

The study investigates dataset composition, data quality, class imbalance, attack categories, numerical and categorical traffic characteristics, feature relationships, and differences between training and testing partitions.

The analysis identifies substantial differences between the datasets.

NSL-KDD contains no exact duplicate records in its training partition, whereas 38.55% of UNSW-NB15 training records are exact duplicates when the record identifier is excluded.

NSL-KDD also contains 17 attack types in testing that are absent from training. UNSW-NB15 contains the same nine broad attack categories in both partitions.

Both datasets exhibit differences in attack prevalence and selected feature distributions between training and testing.

These findings demonstrate why understanding dataset characteristics is essential before developing or evaluating network intrusion detection systems.

No machine-learning model was trained or evaluated in this project.

## 2. Introduction

Network intrusion detection systems aim to identify potentially malicious activity in computer networks.

Public intrusion detection datasets are frequently used to study network traffic and evaluate detection techniques.

However, dataset quality, class composition, attack coverage, and feature distributions can influence how evaluation results are interpreted.

Exploratory data analysis provides a systematic approach to understanding these characteristics.

This project examines NSL-KDD and UNSW-NB15 to identify important similarities, differences, and limitations relevant to intrusion detection research.

## 3. Research Objectives

The objectives of this study are:

1. Examine the structure and composition of NSL-KDD and UNSW-NB15.
2. Assess missing values, duplicate records, and selected data-quality characteristics.
3. Investigate normal and attack traffic distributions.
4. Analyze attack types and attack categories.
5. Explore numerical and categorical network traffic features.
6. Examine correlations and class-specific feature relationships.
7. Compare training and testing partitions.
8. Summarize evidence-based findings and limitations.

## 4. Dataset Description

### 4.1 NSL-KDD

NSL-KDD contains network connection records labeled as normal traffic or specific attack types.

The analyzed training partition contains 125,973 records and 43 columns.

The testing partition contains 22,544 records and 43 columns.

The dataset includes numerical and categorical network traffic features, an attack-type label, and a difficulty-level field.

### 4.2 UNSW-NB15

UNSW-NB15 contains network traffic records with numerical and categorical features, a binary traffic label, and an attack-category label.

The analyzed training partition contains 175,341 records and 45 columns.

The testing partition contains 82,332 records and 45 columns.

The dataset includes nine broad attack categories in addition to normal traffic.

### 4.3 Dataset Comparison

| Characteristic | NSL-KDD | UNSW-NB15 |
|---|---:|---:|
| Training records | 125,973 | 175,341 |
| Testing records | 22,544 | 82,332 |
| Columns | 43 | 45 |
| Training attack proportion | 46.54% | 68.06% |
| Testing attack proportion | 56.92% | 55.06% |

The datasets use different feature definitions, attack taxonomies, and collection methodologies. Their values should therefore not be treated as directly interchangeable.

## 5. Methodology

The study followed a structured EDA workflow.

### 5.1 Dataset Inspection

The datasets were loaded using Python and Pandas.

Dataset dimensions, column types, labels, and basic characteristics were examined.

### 5.2 Data-Quality Assessment

The analysis investigated missing values, blank strings, duplicate records, feature-only duplicates, and selected validity conditions.

Original dataset records were preserved.

### 5.3 Univariate Analysis

Class proportions, attack categories, numerical distributions, and categorical feature frequencies were investigated.

### 5.4 Bivariate and Multivariate Analysis

Selected numerical features were compared across normal and attack traffic.

Categorical attack rates were calculated.

Spearman correlation was used to investigate monotonic feature relationships.

Class-specific relationships were examined separately.

### 5.5 Train–Test Comparison

Training and testing partitions were compared using:

- Binary class proportions.
- Attack-category coverage and frequencies.
- Numerical feature medians and percentiles.
- Kolmogorov–Smirnov statistics.
- Total Variation Distance for categorical distributions.

### 5.6 Visualization

Matplotlib and Seaborn were used to create distribution plots, categorical comparisons, correlation heatmaps, and summary visualizations.

## 6. Results and Discussion

### 6.1 Data Quality

All four analyzed dataset partitions contained zero Pandas missing cells and zero blank-string entries in the performed checks.

NSL-KDD contained no exact duplicate records in either partition.

UNSW-NB15 contained 67,601 exact duplicate training records, representing 38.55% of the training partition, when the identifier column was excluded.

Its testing partition contained 26,387 exact duplicate records, representing approximately 32.05%.

These findings indicate substantial differences in record repetition between the datasets.

Duplicate records were retained to preserve the supplied dataset distributions.

The analysis does not establish whether removing duplicates would improve intrusion detection performance.

### 6.2 Class Distribution

NSL-KDD training data contains 53.46% normal records and 46.54% attack records.

Its testing partition contains 43.08% normal records and 56.92% attack records.

UNSW-NB15 training data contains 31.94% normal records and 68.06% attack records.

Its testing partition contains 44.94% normal records and 55.06% attack records.

Therefore, NSL-KDD's attack proportion increases by 10.38 percentage points from training to testing, while UNSW-NB15's decreases by 13.00 percentage points.

These differences demonstrate changes in class composition between the supplied partitions.

### 6.3 Attack Composition

NSL-KDD contains 22 attack types in training and 37 in testing.

Twenty attack types are shared.

Seventeen attack types appear only in testing, while two appear only in training.

The neptune attack accounts for 70.30% of training attacks but only 36.29% of testing attacks.

Other attack types, including guess_passwd and warezmaster, become substantially more prominent in testing.

UNSW-NB15 contains the same nine broad attack categories in both partitions.

However, category proportions differ. Generic accounts for 33.52% of training attacks and 41.63% of testing attacks.

These findings reveal differences in attack-label composition and coverage.

### 6.4 Numerical Traffic Characteristics

Selected duration and byte-count features exhibit strongly right-skewed distributions.

Class-specific comparisons reveal differences in typical traffic characteristics.

For example, the median source-byte count in NSL-KDD training data is 233 for normal records and 0 for attack records.

In UNSW-NB15, the corresponding medians are 1,470 and 200.

These differences describe the supplied data and should not be interpreted as universal characteristics of malicious network traffic.

### 6.5 Categorical Features and Attack Rates

Several categorical features show substantial differences in observed attack rates.

In NSL-KDD training data, ICMP has an attack rate of 84.21%, while UDP has an attack rate of 17.07%.

The S0 connection flag has an attack rate of 98.98%, compared with 15.41% for SF.

In UNSW-NB15 training data, INT has an attack rate of 93.05%, while CON has an attack rate of 8.01%.

These results demonstrate associations between selected categorical features and traffic labels.

They do not establish causal relationships.

### 6.6 Feature Correlations

Spearman correlation analysis identified strong relationships among selected numerical features.

In NSL-KDD, same_srv_rate and diff_srv_rate have a correlation of approximately −0.920.

In UNSW-NB15, dbytes and dpkts have a correlation of approximately +0.990.

Class-specific analysis also demonstrated that aggregate correlations may differ from within-class relationships.

For example, NSL-KDD src_bytes and dst_bytes have a combined Spearman correlation of approximately +0.700, compared with +0.312 for normal records and +0.353 for attack records.

These findings highlight the importance of considering traffic classes when interpreting feature relationships.

### 6.7 Numerical Train–Test Distribution Differences

Kolmogorov–Smirnov statistics were calculated for six selected numerical features.

| Dataset | Feature | KS Statistic |
|---|---|---:|
| NSL-KDD | duration | 0.0769 |
| NSL-KDD | src_bytes | 0.0817 |
| NSL-KDD | dst_bytes | 0.1241 |
| UNSW-NB15 | dur | 0.0890 |
| UNSW-NB15 | sbytes | 0.0466 |
| UNSW-NB15 | dbytes | 0.0437 |

NSL-KDD destination bytes exhibit the largest KS statistic among the selected features.

These results indicate differences between the empirical training and testing distributions.

However, the KS statistic alone does not establish operational significance.

### 6.8 Categorical Train–Test Distribution Differences

Total Variation Distance was calculated for six selected categorical features.

| Dataset | Feature | TVD |
|---|---|---:|
| NSL-KDD | service | 0.2049 |
| NSL-KDD | flag | 0.1906 |
| NSL-KDD | protocol_type | 0.0223 |
| UNSW-NB15 | proto | 0.0677 |
| UNSW-NB15 | state | 0.0548 |
| UNSW-NB15 | service | 0.0357 |

NSL-KDD service and flag exhibit the largest categorical distribution differences among the selected features.

In contrast, NSL-KDD protocol_type exhibits the smallest difference.

This demonstrates that distribution stability varies across features within the same dataset.

## 7. Major Research Insights

### Insight 1: Dataset quality differs substantially

NSL-KDD and UNSW-NB15 exhibit markedly different levels of exact record duplication.

This highlights the importance of inspecting dataset quality before conducting downstream analysis.

### Insight 2: Attack-label coverage differs

NSL-KDD contains test-only attack types, while UNSW-NB15 contains the same nine broad attack categories across both partitions.

This distinction is relevant when interpreting attack coverage during evaluation.

### Insight 3: Class composition changes across partitions

Both datasets exhibit changes in attack prevalence between training and testing.

The direction of change differs.

### Insight 4: Feature distributions are not equally stable

Some features show substantially larger train–test distribution differences than others.

Evaluating only overall class proportions would miss these differences.

### Insight 5: Feature relationships require careful interpretation

Strong correlations exist among selected features, but combined-data relationships can differ from class-specific relationships.

Correlation alone does not establish causation or feature redundancy.

## 8. Limitations

This study has several limitations.

1. The findings describe the supplied dataset partitions rather than live network environments.
2. NSL-KDD and UNSW-NB15 use different feature definitions and attack taxonomies.
3. Only selected numerical features were included in the detailed correlation and distribution-shift analyses.
4. Observed attack proportions should not be interpreted as real-world attack prevalence.
5. Duplicate records were retained, and their effects on model performance were not evaluated.
6. No machine-learning model was trained or tested.
7. Statistical associations do not establish causation.
8. Train–test distribution differences do not independently establish model performance degradation.
9. Changes in class proportions may contribute to observed differences in feature distributions.

## 9. Conclusion

This project conducted a structured comparative exploratory data analysis of NSL-KDD and UNSW-NB15.

The analysis identified differences in data quality, attack composition, class balance, feature relationships, and training–testing distributions.

NSL-KDD exhibits test-only attack labels and substantial changes in selected categorical distributions.

UNSW-NB15 exhibits considerable exact record duplication and changes in class composition and selected feature distributions.

The findings demonstrate that intrusion detection datasets should be examined carefully before drawing conclusions from downstream detection experiments.

The project provides a reproducible exploratory foundation for future intrusion detection research.

## 10. Future Work

Potential extensions include:

1. Investigating feature distributions separately within normal and attack classes across training and testing partitions.
2. Examining the sensitivity of downstream analysis to duplicate-record handling.
3. Evaluating additional numerical and categorical features.
4. Studying differences among individual attack categories.
5. Developing and evaluating intrusion detection models as a separate future phase.

## 11. Research Reference

The project was informed by the IEEE conference paper:

*Analysis of Data Mining Techniques on KDD-Cup'99, NSL-KDD and UNSW-NB15 Datasets for Intrusion Detection.*

The paper provides related research context. The exploratory analyses and findings presented here are based on the project's own dataset investigations.