# Train–Test Comparative Exploratory Data Analysis

## 1. Objective

This analysis compares the training and testing partitions of the NSL-KDD and UNSW-NB15 network intrusion detection datasets.

The objective is to identify differences in binary class proportions, attack-category composition, numerical feature distributions, and categorical feature distributions.

These comparisons provide insight into the characteristics of the supplied dataset partitions and potential challenges when evaluating intrusion detection systems.

All original records were preserved.

## 2. Dataset Partitions

| Dataset | Partition | Records |
|---|---|---:|
| NSL-KDD | Training | 125,973 |
| NSL-KDD | Testing | 22,544 |
| UNSW-NB15 | Training | 175,341 |
| UNSW-NB15 | Testing | 82,332 |

The analyses were conducted separately for each dataset because the datasets use different feature definitions and attack taxonomies.

## 3. Binary Class Distribution Comparison

### 3.1 NSL-KDD

Normal traffic represents 53.46% of training records and 43.08% of testing records.

Attack traffic increases from 46.54% in training to 56.92% in testing.

This represents an increase of 10.38 percentage points in the attack proportion.

### 3.2 UNSW-NB15

Normal traffic represents 31.94% of training records and 44.94% of testing records.

Attack traffic decreases from 68.06% in training to 55.06% in testing.

This represents a decrease of 13.00 percentage points in the attack proportion.

### Finding

Both datasets exhibit changes in class composition between training and testing partitions, but the direction of change differs.

These differences may influence evaluations of intrusion detection systems, particularly when class-dependent metrics are considered.

## 4. Attack-Category Comparison

### 4.1 NSL-KDD

The training partition contains 22 attack types, while the testing partition contains 37.

Twenty attack types appear in both partitions.

Seventeen attack types appear only in testing:

apache2, httptunnel, mailbomb, mscan, named, processtable, ps, saint, sendmail, snmpgetattack, snmpguess, sqlattack, udpstorm, worm, xlock, xsnoop, and xterm.

Two attack types appear only in training:

spy and warezclient.

The share of neptune among attack records decreases from 70.30% in training to 36.29% in testing.

In contrast, guess_passwd increases from 0.09% to 9.59%, and warezmaster increases from 0.03% to 7.36%.

These findings indicate substantial differences in attack-label composition.

### 4.2 UNSW-NB15

All nine attack categories appear in both training and testing partitions.

However, their proportions differ.

Generic increases from 33.52% to 41.63% of attack records.

Exploits decreases from 27.98% to 24.56%, while Fuzzers decreases from 15.24% to 13.37%.

### Finding

NSL-KDD includes test-only attack labels, whereas UNSW-NB15 contains the same nine broad attack categories in both partitions.

Both datasets exhibit changes in attack-category proportions.

The presence of a test-only attack label does not necessarily imply that every associated traffic pattern is completely absent from training.

## 5. Numerical Feature Distribution Comparison

The Kolmogorov–Smirnov statistic was used to compare selected numerical feature distributions.

| Dataset | Feature | KS Statistic |
|---|---|---:|
| NSL-KDD | duration | 0.0769 |
| NSL-KDD | src_bytes | 0.0817 |
| NSL-KDD | dst_bytes | 0.1241 |
| UNSW-NB15 | dur | 0.0890 |
| UNSW-NB15 | sbytes | 0.0466 |
| UNSW-NB15 | dbytes | 0.0437 |

Among the six selected features, NSL-KDD destination bytes have the highest KS statistic.

The median destination-byte count increases from 0 in training to 46 in testing.

For UNSW-NB15, duration has the highest KS statistic among the three selected numerical features.

The median duration increases from approximately 0.0016 in training to 0.0141 in testing.

These results demonstrate measurable differences between the empirical numerical distributions.

The statistical significance of these differences should not be confused with their practical magnitude.

## 6. Categorical Feature Distribution Comparison

Total Variation Distance (TVD) was used to compare categorical feature proportions.

| Dataset | Feature | TVD |
|---|---|---:|
| NSL-KDD | service | 0.2049 |
| NSL-KDD | flag | 0.1906 |
| NSL-KDD | protocol_type | 0.0223 |
| UNSW-NB15 | proto | 0.0677 |
| UNSW-NB15 | state | 0.0548 |
| UNSW-NB15 | service | 0.0357 |

### 6.1 NSL-KDD

The service feature exhibits the largest categorical distribution difference, with a TVD of 0.2049.

Telnet increases from 1.87% to 7.21%, while pop_3 increases from 0.21% to 4.52%.

Connection flags also show substantial differences.

S0 decreases from 27.67% to 8.93%, while REJ increases from 8.92% to 17.08%.

In contrast, protocol_type has a relatively low TVD of 0.0223.

### 6.2 UNSW-NB15

The proto feature has the highest TVD among the selected UNSW-NB15 categorical features, at 0.0677.

TCP increases from 45.59% to 52.34%.

The INT connection state decreases from 46.92% to 41.49%.

The recorded service category '-' increases from 53.71% to 57.27%.

The '-' category was retained rather than automatically classified as missing data.

## 7. Key Findings

1. Both datasets exhibit changes in attack prevalence between training and testing partitions.
2. NSL-KDD contains 17 attack types in testing that are absent from training.
3. UNSW-NB15 contains the same nine attack categories in both partitions, although their proportions differ.
4. Selected numerical features show measurable distribution differences.
5. NSL-KDD service and connection-flag distributions exhibit larger categorical shifts than the other selected categorical features.
6. Feature-distribution differences vary substantially across features and datasets.
7. Aggregate feature differences may partly reflect changes in the proportions of Normal and Attack records.

## 8. Limitations

- The analysis examines the supplied dataset partitions rather than live network traffic.
- Numerical comparisons focus on six selected features.
- The KS statistic measures empirical distribution differences but does not establish their operational significance.
- TVD summarizes differences in category proportions but does not explain their causes.
- The observed differences do not establish that a trained detection model would perform poorly.
- Changes in class composition may contribute to observed feature-distribution differences.
- The datasets have different collection procedures, feature definitions, and attack taxonomies.
- No machine-learning model was trained or evaluated in this study.

## 9. Conclusion

The train–test comparative analysis identified meaningful differences in class composition, attack-category distributions, and selected network traffic features.

NSL-KDD exhibits substantial differences in attack-type coverage and selected categorical distributions.

UNSW-NB15 exhibits changes in class proportions and feature distributions despite having the same nine broad attack categories in both partitions.

These findings highlight the importance of understanding dataset partition characteristics before interpreting intrusion detection evaluation results.