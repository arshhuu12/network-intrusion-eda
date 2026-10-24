# Data Cleaning Decisions and Validation

## 1. Objective

This document records the preprocessing and data-cleaning decisions for the comparative exploratory analysis of NSL-KDD and UNSW-NB15.

The objective is to preserve data integrity, avoid unsupported modifications, and ensure that analytical results are reproducible.

## 2. Guiding Principles

The following principles guide all preprocessing decisions:

1. Preserve the original raw datasets.
2. Maintain the supplied training and testing partitions.
3. Investigate unusual values before treating them as errors.
4. Avoid removing records without documented justification.
5. Keep preprocessing steps consistent and reproducible.
6. Clearly distinguish original variables from derived analytical variables.

## 3. Cleaning Decision Log

| Issue | M3 Finding | Decision | Justification |
|---|---|---|---|
| Missing values | No detected missing cells | No imputation | No missing values were identified by the implemented checks |
| Blank text values | No blank or whitespace-only cells | No replacement | No affected cells were detected |
| Duplicate records | Substantial repetition in UNSW-NB15 | Retain duplicates | Repetition may reflect meaningful traffic patterns; removal would change observed distributions |
| Repeated feature vectors | Present in both datasets | Retain records | Identical features do not necessarily indicate invalid observations |
| Conflicting feature labels | Multiple patterns identified | Retain and document | Insufficient evidence to determine which labels, if any, are incorrect |
| Negative duration or byte counts | None detected in selected features | No correction | Checked values satisfied non-negativity constraints |
| NSL-KDD rate values | All checked values within 0–1 | No correction | Values satisfied the tested range constraints |
| UNSW-NB15 binary labels | Only 0 and 1 detected | No correction | Binary labels satisfied the expected value constraint |
| UNSW-NB15 category-label consistency | No mismatches detected | No correction | Checked labels were internally consistent |
| Extreme numerical values | Large maxima observed | Investigate during EDA | Extreme values may represent meaningful network behavior |
| Dataset-specific schemas | Different feature names and definitions | Analyze separately | Direct feature comparisons require semantic compatibility |

## 4. Planned Analytical Transformations

The following transformations may be used for analysis without modifying raw files.

### 4.1 Binary Traffic Class

For NSL-KDD:

- `normal` is mapped to `Normal`.
- All other attack-type labels are mapped to `Attack`.

For UNSW-NB15:

- `label = 0` is mapped to `Normal`.
- `label = 1` is mapped to `Attack`.

These derived classes enable comparison of normal and malicious traffic proportions.

### 4.2 Numerical Visualization

Highly skewed numerical features may be displayed using logarithmic transformations or logarithmic axes when appropriate.

Such transformations will be documented and will not overwrite the original measurements.

### 4.3 Categorical Visualization

Category frequencies and percentages may be calculated for visualization.

Rare categories will not be removed solely because they occur infrequently.

## 5. Data Preservation Policy

The original NSL-KDD and UNSW-NB15 files will remain unchanged in `data/raw/`.

The primary exploratory analysis will use the original supplied records.

Any derived datasets or analytical outputs will be stored separately.

## 6. Validation Requirements

Before proceeding with exploratory analysis, the workflow should confirm that:

- Original record counts remain unchanged.
- Original feature values remain unchanged.
- Training and testing partitions remain separate.
- Derived binary classes are assigned correctly.
- No unexpected missing values are introduced.
- No duplicate records are removed unintentionally.

## 7. Limitations

The cleaning policy is based on the data-quality checks completed during M3.

These checks do not establish that every value is semantically valid.

Additional findings during exploratory analysis may require further investigation or updates to this decision log.

## 8. Conclusion

The current evidence does not justify deleting duplicate records, correcting labels, or removing extreme numerical observations.

The project will therefore prioritize non-destructive analytical transformations and transparent documentation.

This approach preserves the characteristics of the original datasets while supporting reproducible exploratory analysis.