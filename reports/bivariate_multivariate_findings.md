\# Bivariate and Multivariate Exploratory Data Analysis



\## 1. Objective



This analysis investigates relationships between numerical and categorical network traffic features in the NSL-KDD and UNSW-NB15 intrusion detection datasets.



The study examines differences between Normal and Attack traffic, categorical attack rates, numerical feature correlations, and class-specific feature relationships.



All analyses use the training partitions, with original records preserved.



\## 2. Numerical Features by Traffic Class



\### 2.1 NSL-KDD



The median source-byte count is 233 for Normal records and 0 for Attack records.



The median destination-byte count is 379 for Normal records and 0 for Attack records.



The 90th percentile of destination bytes among Attack records is 0, indicating that at least 90% of these records have zero destination bytes.



Although Attack records have lower median byte counts, their mean byte counts are substantially higher.



This difference demonstrates the influence of extreme observations on heavily skewed distributions.



\### 2.2 UNSW-NB15



The median source-byte count is 1,470 for Normal records and 200 for Attack records.



The median destination-byte count is 1,112 for Normal records and 0 for Attack records.



The median duration is approximately 0.039 for Normal records and approximately 0 for Attack records.



These results indicate differences in typical numerical traffic characteristics between the two classes.



\## 3. Categorical Features and Attack Rates



\### 3.1 NSL-KDD



The attack rates for the three protocol categories are:



| Protocol | Attack Rate |

|---|---:|

| TCP | 47.80% |

| UDP | 17.07% |

| ICMP | 84.21% |



ICMP has the highest attack rate among the protocol categories.



Connection flags show substantial differences in attack prevalence.



For example, S0 has an attack rate of 98.98%, while SF has an attack rate of 15.41%.



These findings indicate associations between connection characteristics and traffic labels in the training partition.



\### 3.2 UNSW-NB15



Selected protocol attack rates include:



| Protocol | Attack Rate |

|---|---:|

| TCP | 51.07% |

| UDP | 78.00% |

| UNAS | 100.00% |

| ARP | 0.00% |

| OSPF | 97.53% |



The UNAS protocol category contains 12,084 records, all labeled Attack in the training partition.



The ARP category contains 2,859 records, all labeled Normal.



These observations describe the supplied training data and should not be generalized to all network environments.



Connection-state attack rates also vary considerably.



INT has an attack rate of 93.05%, FIN has an attack rate of 52.23%, and CON has an attack rate of 8.01%.



\## 4. Numerical Feature Correlations



Spearman correlation was used to investigate monotonic relationships between selected numerical features.



\### 4.1 NSL-KDD



The strongest observed relationship among the selected features is between `same\_srv\_rate` and `diff\_srv\_rate`, with a Spearman correlation of −0.920.



Other notable relationships include:



\- `src\_bytes` and `same\_srv\_rate`: +0.753

\- `count` and `same\_srv\_rate`: −0.720

\- `src\_bytes` and `diff\_srv\_rate`: −0.705

\- `src\_bytes` and `dst\_bytes`: +0.700



These results reveal substantial relationships among service-related and traffic-volume features.



\### 4.2 UNSW-NB15



The strongest observed relationship is between `dbytes` and `dpkts`, with a Spearman correlation of +0.990.



Other notable relationships include:



\- `spkts` and `dpkts`: +0.910

\- `sbytes` and `spkts`: +0.901

\- `dbytes` and `spkts`: +0.888

\- `dur` and `rate`: −0.879



These findings indicate strong associations among several traffic-volume measurements.



High correlation does not establish that features are identical or redundant.



\## 5. Class-Specific Feature Relationships



\### 5.1 NSL-KDD



The Spearman correlation between `src\_bytes` and `dst\_bytes` is:



| Group | Correlation |

|---|---:|

| Combined records | +0.700 |

| Normal records | +0.312 |

| Attack records | +0.353 |



The combined correlation is substantially stronger than either class-specific correlation.



This demonstrates that correlations calculated across mixed traffic classes may not accurately describe relationships within individual classes.



\### 5.2 UNSW-NB15



The Spearman correlation between `sbytes` and `spkts` is:



| Group | Correlation |

|---|---:|

| Combined records | +0.901 |

| Normal records | +0.919 |

| Attack records | +0.849 |



Strong positive relationships exist within both traffic classes.



The relationship is somewhat stronger among Normal records.



\## 6. Key Findings



1\. Normal and Attack records differ in several numerical feature distributions.

2\. Median byte counts are lower among Attack records for the selected features in both datasets.

3\. Certain protocol and connection-state categories show high attack prevalence in the training partitions.

4\. Several numerical features exhibit strong positive or negative Spearman correlations.

5\. Combined-data correlations may differ substantially from class-specific correlations.

6\. Correlation patterns vary across datasets and traffic classes.



\## 7. Limitations



\- Findings are based on training partitions only.

\- Correlation does not establish causation.

\- Strong feature correlations do not automatically imply redundancy.

\- Category-specific attack rates may be influenced by dataset construction.

\- Rare categories may have unstable observed attack rates.

\- Scatterplots use samples for visualization, while correlation calculations use complete training partitions.

\- The selected numerical features represent a subset of all available features.

\- NSL-KDD and UNSW-NB15 use different feature definitions and collection methodologies.



\## 8. Conclusion



The bivariate and multivariate exploratory analysis identified important associations between network traffic characteristics and attack labels.



The results demonstrate the value of examining class-specific distributions and feature relationships rather than relying exclusively on aggregate statistics.



These findings provide a foundation for the subsequent comparison of training and testing partitions.

