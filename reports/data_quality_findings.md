# Data Quality Assessment: NSL-KDD and UNSW-NB15

## 1. Objective

This assessment examines the data-quality characteristics of the NSL-KDD and UNSW-NB15 intrusion detection datasets. The analysis focuses on missing values, duplicate records, repeated feature patterns, label consistency, basic feature validity, and differences between training and testing partitions.

The objective is to identify and document dataset characteristics that may influence exploratory data analysis and visualization.

## 2. Datasets Examined

The assessment covers four dataset partitions:

| Dataset | Records | Original columns |
|---|---:|---:|
| NSL-KDD Training | 125,973 | 43 |
| NSL-KDD Testing | 22,544 | 43 |
| UNSW-NB15 Training | 175,341 | 45 |
| UNSW-NB15 Testing | 82,332 | 45 |

A total of 406,190 records were examined.

The original training and testing partitions were preserved throughout the assessment.

## 3. Methodology

The analysis was performed using Python and Pandas in a Jupyter notebook.

The following checks were conducted:

1. **Missing-value assessment:** Identified missing values recognized by Pandas and empty or whitespace-only text fields.
2. **Duplicate-record assessment:** Identified repeated records. The UNSW-NB15 `id` field was excluded from duplicate comparisons because it functions as a record identifier.
3. **Repeated feature analysis:** Compared input feature values while excluding labels and metadata.
4. **Label-conflict assessment:** Identified feature patterns associated with multiple labels within each partition.
5. **Feature validity checks:** Examined negative durations and byte counts, NSL-KDD rate ranges, and UNSW-NB15 binary-label consistency.
6. **Train–test comparison:** Compared data-quality measurements and binary traffic-class distributions across partitions.

No records were deleted or modified during the assessment.

## 4. Key Findings

### 4.1 Missing Values

No Pandas-recognized missing values or blank/whitespace-only text cells were detected in any of the four partitions.

This result does not exclude the possibility of undocumented placeholders or other semantic data-quality issues.

### 4.2 Duplicate Records

| Dataset | Duplicate records | Duplicate rate |
|---|---:|---:|
| NSL-KDD Training | 0 | 0.00% |
| NSL-KDD Testing | 0 | 0.00% |
| UNSW-NB15 Training | 67,601 | 38.55% |
| UNSW-NB15 Testing | 26,387 | 32.05% |

NSL-KDD contained no exact duplicates when all original columns were compared.

UNSW-NB15 exhibited substantial record repetition after excluding its identifier column.

Repeated records were particularly concentrated in attack traffic. In the UNSW-NB15 training partition, 53.20% of attack records were duplicates of earlier records under the selected comparison, compared with 7.34% of normal records.

### 4.3 Repeated Feature Patterns

| Dataset | Repeated feature rows | Percentage |
|---|---:|---:|
| NSL-KDD Training | 16 | 0.0127% |
| NSL-KDD Testing | 57 | 0.2528% |
| UNSW-NB15 Training | 74,301 | 42.3751% |
| UNSW-NB15 Testing | 28,386 | 34.4775% |

Repeated feature vectors were detected even when the corresponding records differed in labels or metadata.

The results indicate considerably more feature-level repetition in the supplied UNSW-NB15 partitions than in NSL-KDD.

### 4.4 Label Conflicts

| Dataset | Conflicting feature patterns |
|---|---:|
| NSL-KDD Training | 15 |
| NSL-KDD Testing | 57 |
| UNSW-NB15 Training | 229 |
| UNSW-NB15 Testing | 6 |

For NSL-KDD, conflicts were defined as identical input features associated with different specific attack-type labels.

For UNSW-NB15, conflicts were defined as identical input features associated with different binary labels.

Because the label definitions differ, these counts should not be interpreted as directly equivalent measures of binary-label inconsistency.

Further investigation is required before classifying these observations as annotation errors.

### 4.5 Basic Feature Validity

The selected duration and byte-count features contained no negative values.

All 15 examined NSL-KDD proportion-based rate features fell within the expected range of 0 to 1.

UNSW-NB15 binary labels contained only values 0 and 1, and no mismatches were found between the binary labels and the corresponding Normal/attack-category classification.

Some numerical features exhibited large maximum values, which warrant further examination during distribution and outlier analysis.

### 4.6 Training and Testing Class Distributions

| Dataset | Training attack % | Testing attack % |
|---|---:|---:|
| NSL-KDD | 46.54% | 56.92% |
| UNSW-NB15 | 68.06% | 55.06% |

Both datasets exhibited differences in attack prevalence between their training and testing partitions.

These differences describe changes in class proportions and do not, by themselves, establish feature-distribution shift.

## 5. Interpretation

The assessment identified substantial differences in record repetition between NSL-KDD and UNSW-NB15.

UNSW-NB15 contained considerably more duplicate records and repeated feature vectors, particularly within attack traffic. NSL-KDD exhibited very low feature-level repetition and no exact duplicates under the selected full-record comparison.

These differences may influence frequency-based visualizations and descriptive statistics.

The findings support preserving the original datasets for the primary exploratory analysis while clearly documenting repetition and other quality characteristics.

## 6. Limitations

The assessment has several limitations:

- Missing-value checks may not detect undocumented placeholder values.
- Duplicate detection identifies repeated values, not necessarily erroneous observations.
- The analysis does not establish whether repeated traffic records represent genuine repeated network events.
- Feature-label conflict counts use different label granularities across the two datasets.
- Basic validity checks cover selected features rather than every possible domain constraint.
- Training and testing partitions were assessed separately; cross-partition overlap has not yet been measured.
- Class-prevalence differences alone do not establish broader statistical distribution shift.

## 7. Conclusion

The data-quality assessment found no missing or blank values under the implemented checks and no violations of the selected basic feature-validity constraints.

However, the datasets differed substantially in record repetition, feature-level redundancy, and training–testing class distributions.

These findings provide a foundation for subsequent exploratory analysis, including class-imbalance visualization, feature-distribution analysis, outlier investigation, and train–test comparisons.

The original datasets will be preserved to maintain reproducibility and avoid unsupported cleaning decisions.