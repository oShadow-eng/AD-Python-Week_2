"""
Day 10 Activity: Outliers Practice
Tasks:
1) Implement IQR-based outlier detection
2) Implement z-score detection
3) Compare strategies: no handling, IQR capping, log1p transform
"""

import numpy as np
import pandas as pd

# Sample heavy-tailed data
np.random.seed(10)
values = np.concatenate([np.random.lognormal(10, 0.5, 1000), [1e7, 2e7]])

df = pd.DataFrame({"income": values})

#Task 1: Implement IQR-based outlier detection
def iqr_bounds(series, k=1.5):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    return Q1 - k * IQR, Q3 + k * IQR
lower, upper = iqr_bounds(df["income"])
mask_iqr = (df["income"] < lower) | (df["income"] > upper)

#Task 2: Implement z-score detection
income_z = df["income"].astype(float)
mean, std = income_z.mean(), income_z.std(ddof=0)
df["income"] = (income_z - mean) / std
mask_z = df["income"].abs() > 3

#Task 3: Apply capping and log1p transformation
low, up = iqr_bounds(df["income"], k=1.5)

df_no_out = df[~(df["income"] < lower) | (df["income"] > upper)]
df_capped = df.copy()
df_capped["income"] = df_capped["income"].clip(lower=low, upper=up)
df_trans= df.copy()
df_trans["income"] = np.log1p(df_trans["income"])

print(df)
print("z-score outliers:", df[mask_z])
print(df_no_out)
print(df_capped)
print(df_trans["income"])
# TODO: Implement iqr_bounds and detect_outliers_iqr
# TODO: Implement detect_outliers_zscore
# TODO: Apply capping and log1p transformation
