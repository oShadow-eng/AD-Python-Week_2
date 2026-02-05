# AD-Python-Week_2"""
Day 6 Activity: Missing Values Practice
Tasks:
1) Load/define a partially observed dataset
2) Normalize missing tokens to NaN
3) Produce missingness summary (per-column %, per-row)
4) Build Version A: drop rows with missing in key cols
5) Build Version B: impute + indicators
6) Compare basic metrics between A and B
"""

import numpy as np
import pandas as pd

# Sample raw dataset (replace or load your own)
raw = {
    "age": [25, "N/A", 40, 33, "?"],
    "income": [50000, 60000, None, "unknown", 80000],
    "churned": [0, 1, 0, 1, 0],
}

#Task 1: Load/define a partially observed dataset
df_raw = pd.DataFrame(raw)

#Task 2: Normalize missing tokens to NaN
df = df_raw.replace(["N/A", "NA", "not reported", "unknown", "?"], np.nan)

#Task 3: Produce missingness summary (per-column %, per-row)
def missing_summary(df: pd.DataFrame) -> pd.DataFrame:
    total = df.isna().sum()
    pet = (df.isna().mean() * 100).round(1)
    return(pd.DataFrame({"Total Missing": total, "Percent Missing": pet})).sort_values("Percent Missing", ascending=False)
summary = missing_summary(df)
df['Percent Missing'] = df.isna().sum(axis=1)

#Task 4: Build Version A: drop rows with missing in key cols (e.g., age, income)
critical_cols = ["age", "income"]
df_drop_any = df.dropna(how = "any")
df_drop_crit = df.dropna(subset=critical_cols)

#Task 5: Build Version B: impute + indicators
df_imp = df.copy()
df_imp["income"] = pd.to_numeric(df_imp["income"], errors='coerce')

df_imp["age_mean_imp"] = df_imp["age"].fillna(df_imp["age"].mean())
df_imp["age_median_imp"] = df_imp["age"].fillna(df_imp["age"].median())

mode_income = df_imp["income"].mode(dropna=True)[0]
df_imp["income_mode_imp"] = df_imp["income"].fillna(mode_income)

df_imp["age_missing"] = df_imp["age"].isna().astype(int)
df_imp["income_missing"] = df_imp["income"].isna().astype(int)




print(df)
print("Original:", df.shape, "Drop Any:", df_drop_any.shape, "Drop Critical:", df_drop_crit.shape)

#Task 6: Compare basic metrics between A and B
print("Version A stats:\n", df_drop_crit[critical_cols].describe())
print("\nVersion B stats:\n", df_imp[critical_cols].describe())


# TODO: Normalize custom missing tokens to NaN
# df = df_raw.replace(["N/A", "NA", "not reported", "unknown", "?"], np.nan)

# TODO: Create missing_summary(df) returning per-column and per-row missingness

# TODO: Version A: drop rows with missing in key columns (e.g., age, income)

# TODO: Version B: impute numeric columns + add missing indicators

# TODO: Compare basic statistics or a simple model between A and B
