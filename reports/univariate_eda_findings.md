# Univariate Exploratory Data Analysis: NSL-KDD and UNSW-NB15

## 1. Objective

This analysis examines the distributions of individual variables in the NSL-KDD and UNSW-NB15 intrusion detection datasets.

The study focuses on binary class composition, attack-type frequencies, numerical feature distributions, and categorical feature distributions.

All findings in this report are based on the supplied training partitions.

## 2. Binary Traffic Class Distribution

| Dataset | Normal Records | Attack Records | Attack Percentage |
|---|---:|---:|---:|
| NSL-KDD | 67,343 | 58,630 | 46.54% |
| UNSW-NB15 | 56,000 | 119,341 | 68.06% |

The UNSW-NB15 training partition contains a higher proportion of attack records than NSL-KDD.

These proportions describe the supplied datasets and should not be interpreted as real-world network attack prevalence.

## 3. Attack Label Distribution

### 3.1 NSL-KDD

The most frequent attack type is `neptune`, with 41,214 records.

This represents approximately 70.30% of NSL-KDD training attack records.

Other frequently occurring attack types include `satan`, `ipsweep`, `portsweep`, and `smurf`.

The results demonstrate substantial imbalance among individual attack types.

### 3.2 UNSW-NB15

The most frequent attack categories are:

| Attack Category | Records |
|---|---:|
| Generic | 40,000 |
| Exploits | 33,393 |
| Fuzzers | 18,184 |
| DoS | 12,264 |
| Reconnaissance | 10,491 |
| Analysis | 2,000 |
| Backdoor | 1,746 |
| Shellcode | 1,133 |
| Worms | 130 |

Generic and Exploits together account for approximately 61.5% of attack records.

Worms represents only approximately 0.11% of attack records.

The results indicate substantial differences in the representation of individual attack categories.

NSL-KDD attack names and UNSW-NB15 attack categories use different taxonomies and are therefore not directly equivalent.

## 4. Numerical Feature Distributions

Three numerical features were examined in each dataset.

### 4.1 NSL-KDD

| Feature | Median | Skewness |
|---|---:|---:|
| duration | 0 | 11.88 |
| src_bytes | 44 | 190.67 |
| dst_bytes | 0 | 290.05 |

### 4.2 UNSW-NB15

| Feature | Median | Skewness |
|---|---:|---:|
| dur | 0.002 | 7.50 |
| sbytes | 430 | 45.30 |
| dbytes | 164 | 39.76 |

All six examined numerical features exhibit positive skewness.

The mean values are substantially larger than the corresponding medians, indicating that relatively large observations influence the averages.

Logarithmic transformations were used for visualization without modifying the original data.

Extreme values were retained because their presence alone does not establish that they are invalid.

## 5. Categorical Feature Distributions

### 5.1 NSL-KDD

| Feature | Unique Categories | Most Common Value | Records |
|---|---:|---|---:|
| protocol_type | 3 | tcp | 102,689 |
| service | 70 | http | 40,338 |
| flag | 11 | SF | 74,945 |

TCP is the dominant protocol in the NSL-KDD training partition.

HTTP is the most frequently observed service, while SF is the most frequent connection flag.

### 5.2 UNSW-NB15

| Feature | Unique Categories | Most Common Value | Records |
|---|---:|---|---:|
| proto | 133 | tcp | 79,946 |
| service | 13 | - | 94,168 |
| state | 9 | INT | 82,275 |

TCP is the most frequent protocol, and INT is the most common connection state.

The service value `-` appears in 94,168 records, approximately 53.71% of the training partition.

This value requires interpretation using dataset documentation. It should not automatically be classified as missing or invalid.

## 6. Key Findings

1. Binary class composition differs between the two training datasets.
2. Individual attack labels are substantially imbalanced.
3. Neptune dominates NSL-KDD attack records.
4. Generic and Exploits dominate UNSW-NB15 attack records.
5. All six examined numerical features are strongly right-skewed.
6. TCP is the most frequent protocol in both training datasets.
7. UNSW-NB15 contains a frequently occurring special service value (`-`) requiring further investigation.

## 7. Limitations

- The analysis covers training partitions only.
- Different attack taxonomies limit direct category-level comparison.
- Numerical features with similar names may have different definitions.
- Skewness and extreme values do not independently establish data errors.
- The meaning of special categorical values requires dataset documentation.
- Univariate analysis cannot establish relationships between features and attack labels.

## 8. Conclusion

The univariate analysis identified important differences in class composition, attack-category frequencies, numerical distributions, and categorical feature representation.

The results highlight the importance of examining both overall attack prevalence and imbalance among individual attack types.

The findings provide a foundation for subsequent bivariate and multivariate analysis, including relationships between traffic features and attack labels.