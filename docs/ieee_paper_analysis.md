# IEEE Base Paper Analysis — Version 1.0

## 1. Bibliographic information
**Title:** Analysis of Data Mining Techniques on KDD-Cup'99, NSL-KDD and UNSW-NB15 Datasets for Intrusion Detection  
**Authors:** Aseel Shehadeh, Hanan ALTaweel, Abdallah Qusef  
**Venue:** 2023 24th International Arab Conference on Information Technology (ACIT), IEEE  
**DOI:** 10.1109/ACIT58888.2023.10453884

## 2. Research problem and purpose
The reference paper investigates the use of selected data-mining classification techniques for network intrusion detection, examining results across three benchmark datasets. Its primary focus is **classification performance**, not comprehensive exploratory visualization or systematic data-quality profiling.

## 3. Datasets and techniques
- **Datasets:** KDD-Cup'99, NSL-KDD, UNSW-NB15.
- **Classifiers:** Random Forest (RF), K-Nearest Neighbors (KNN; K=3 in the reported setup) and Naive Bayes (NB).
- **Software:** WEKA.
- **Reported evaluation metrics:** Accuracy, precision, recall and F-measure.

The paper's evaluation setups are not identical across datasets; therefore, its reported scores must not be treated as a controlled, apples-to-apples measurement of inherent dataset difficulty.

## 4. Main reported finding
The authors report Random Forest as the strongest overall method among the selected classifiers in their experiments. This is a finding **of their study under its methods**, not a universal ranking of algorithms or proof that dataset properties caused a given result.

## 5. Limitations and future direction
The paper is restricted to selected datasets and classification approaches. Its future-work discussion motivates further investigation of dataset characteristics, including data quality and complexity, alongside potential exploration of additional techniques.

**Research-integrity note:** A future-work suggestion is a valid motivation, but not by itself evidence that no prior EDA study exists. We describe our work as an *EDA-focused extension motivated by the paper*, not as a proven novel discovery.

## 6. Relationship to our project
| Dimension | Reference paper | Our project |
|---|---|---|
| Central question | How do selected classifiers perform? | What dataset characteristics are visible through systematic EDA? |
| Data | KDD-Cup'99, NSL-KDD, UNSW-NB15 | NSL-KDD, UNSW-NB15 |
| Main methods | RF, KNN, NB | Profiling, quality checks, descriptive statistics, visualization |
| Outputs | Classification metrics and comparisons | Data-quality metrics, class distributions, feature patterns, train/test comparisons |
| Contribution | Comparative classification experiment | Reproducible, interpretable dataset-characteristics analysis |
| Claims permitted | Model results under reported setup | Descriptive patterns and carefully bounded comparisons |

## 7. Research mapping
- **RQ1:** Investigates data quality and documented constraints.
- **RQ2:** Investigates class representation and imbalance.
- **RQ3:** Investigates feature distributions and relationships.
- **RQ4:** Investigates differences between documented train/test partitions.

## 8. What we will not claim
- That we reproduced the original WEKA experiments.
- That our EDA demonstrates a causal effect on accuracy or F1.
- That NSL-KDD and UNSW-NB15 have identical attack taxonomies or feature meanings.
- That these historical benchmarks represent today's live network traffic.
- That this extension is the first such EDA study without a separate literature review.

## 9. Points to verify when preparing the final academic report
Check the PDF's exact section/page references for evaluation splits, reported numeric scores, and the authors' wording of future work. Use direct citations to the base paper in the final report. Do not copy performance values into the report until checked against the supplied PDF.

## Primary reference
Shehadeh, A., ALTaweel, H., & Qusef, A. (2023). *Analysis of Data Mining Techniques on KDD-Cup'99, NSL-KDD and UNSW-NB15 Datasets for Intrusion Detection*. IEEE ACIT. https://doi.org/10.1109/ACIT58888.2023.10453884
