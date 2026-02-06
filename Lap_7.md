"""
Day 7 Activity: Imputation Practice
Tasks:
1) Implement fit_imputer(train_df) returning medians/modes
2) Implement transform_imputer(df, params)
3) Add missing indicators optionally
4) Compare behavior with/without indicators
"""

import pandas as pd

# Sample dataset
train = pd.DataFrame({
    "age": [25, None, 40, 33],
    "city": ["NY", "SF", None, "NY"],
})

test = pd.DataFrame({
    "age": [None, 50],
    "city": ["SF", None],
})

#Task 1: Implement fit_imputer
print('Task 1\n')
df_demo_train = train.copy()
def Task1():
    train_medians = df_demo_train['age'].median()
    train_modes = df_demo_train['city'].mode()[0]
    return train_medians, train_modes
print(f'Medians: {Task1()[0]}, \nModes: {Task1()[1]}')

#Task 2: Implement transform_imputer
print('\nTask 2 \n')
train_failed = train.copy()
def Task2(df):
    df['age'] = df['age'].fillna(Task1()[0])
    df['city'] = df['city'].fillna(Task1()[1])
    return df
print(f'Transformed Train:\n{Task2(train_failed)}')

#Task 3: Add missing indicators optionally
print('\nTask 3\n')
train_with_indicators = train.copy()
def Task3(df, add_indicators=True):
    if add_indicators:
        df['age_missing'] = df['age'].isnull().astype(int)
        df['city_missing'] = df['city'].isnull().astype(int)
    return Task2(df)
print(f'Transformed Train with Indicators:\n{Task3(train_with_indicators)}')

#Task 4: Compare behavior with/without indicators
print('\nTask 4\n')
train_no_indicators = train.copy()
def Task4():
    print('Without Indicators:')
    print(Task2(train_no_indicators))
    print('\nWith Indicators:')
    print(Task3(train_with_indicators))
Task4()


# TODO: Implement fit_imputer
# def fit_imputer(train_df, num_cols, cat_cols):
#     ...

# TODO: Implement transform_imputer
# def transform_imputer(df, params, add_indicators=True):
