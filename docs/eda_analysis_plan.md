# EDA Analysis Plan — Version 1.0

**Purpose:** Translate four research questions into verifiable computations, figures and written findings before examining results.

## 1. Analysis register
| ID | RQ | Analysis | Method | Expected evidence |
|---|---|---|---|---|
| A01 | RQ1 | Dataset structure | Rows, columns, dtypes, role and grain of records | Dataset profile |
| A02 | RQ1 | Completeness | Missing counts and percentages per feature/split | Quality table; optional missingness figure |
| A03 | RQ1 | Duplicates | Full-row and feature-only duplicate counts, split-aware | Quality table and issue log |
| A04 | RQ1 | Validity and consistency | Selected documented constraints, category inspection, type checks | Rule-based audit |
| A05 | RQ2 | Binary class distribution | Counts and percentages, train and test separately | Class-frequency plots |
| A06 | RQ2 | Attack-group distribution | Category counts, rare-group shares; taxonomy-specific | Category plots |
| A07 | RQ3 | Numeric distributions | Summary statistics, histograms/ECDF, skew assessment | Distribution figures |
| A08 | RQ3 | Class-conditional distributions | Grouped summaries and box/violin/ECDF as appropriate | Class-wise comparisons |
| A09 | RQ3 | Categorical relationships | Cross-tabs and normalized proportions | Stacked/clustered bar charts |
| A10 | RQ3 | Numerical relationships | Selected correlation matrix; note nonlinear and label effects | Correlation heatmap |
| A11 | RQ4 | Train/test class shift | Absolute percentage-point differences in class shares | Train/test class comparison |
| A12 | RQ4 | Train/test feature shift | Selected numeric ECDF/quantiles and categorical proportions | Split-comparison figures |
| A13 | RQ1–4 | Cross-dataset synthesis | Compatible, well-defined metrics only | Comparison table and interpretation |
| A14 | RQ1–4 | Validation | Recompute denominators, percentages and row-count changes | Validation log |

## 2. Recommended core figures (12–16 total)
1. NSL-KDD train/test normal-versus-attack proportions.
2. UNSW-NB15 train/test normal-versus-attack proportions.
3. NSL-KDD attack-group distribution (within documented taxonomy).
4. UNSW-NB15 attack-category distribution.
5. NSL-KDD selected numeric feature distribution.
6. UNSW-NB15 selected numeric feature distribution.
7. NSL-KDD selected feature by binary label.
8. UNSW-NB15 selected feature by binary label.
9. NSL-KDD categorical feature versus class proportions.
10. UNSW-NB15 categorical feature versus class proportions.
11. NSL-KDD selected numerical correlation heatmap.
12. UNSW-NB15 selected numerical correlation heatmap.
13. NSL-KDD train/test selected numeric distribution comparison.
14. UNSW-NB15 train/test selected numeric distribution comparison.
15–16. Optional quality-summary or additional high-value shift figures, subject to measured findings.

**Figure selection rule:** Replace low-value plots with more informative ones based on actual data. Do not manufacture issues to fill figure quotas. Use consistent units and disclose any sampling, log scaling or filtering.

## 3. Data-quality decision protocol
For every detected issue: **measure → inspect context → determine whether issue is real → decide → document → validate**. Preserve immutable raw files. Treat duplicates and extreme traffic values as observations to investigate, not automatically delete.

## 4. Validation checklist
- Record file names, source and download date.
- Confirm column names and label mapping against documentation.
- Keep train/test identity explicit in tables and plots.
- Check class percentages sum to approximately 100% within each denominator.
- Verify group counts sum to the correct partition total.
- Report duplicate definitions (all columns vs features only).
- Verify that cleaning decisions do not silently remove rare attacks.
- Check saved figures against notebook computations.
- Document exclusions, transformations, random seeds and sampling.

## 5. Interpretation template
For each important result record:
- **Question:** Which RQ does it address?
- **Method:** What was calculated and on which partition?
- **Observation:** What exact numbers/patterns were measured?
- **Interpretation:** What might the pattern indicate?
- **Limitation:** What cannot be inferred?
- **Evidence:** Notebook cell/table/figure identifier.

## 6. Execution priorities
**Must-have:** A01–A09, A11–A14 and selected A10 correlations; 12 well-supported figures; written RQ answers.  
**If time remains:** Additional figures, formal distribution-distance metrics, PCA.  
**Not required:** Classifier training, dashboard, production deployment.

## 7. Exit gate for M0
M0 is complete when the charter, base-paper analysis and this plan are internally consistent, have been reviewed, and can guide dataset acquisition without ambiguity. Empirical results remain pending until M2–M8.
