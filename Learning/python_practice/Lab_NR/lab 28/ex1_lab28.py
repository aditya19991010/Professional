import pandas as pd
import os

from matplotlib.patheffects import Normal

os.chdir("/home/ibab/PycharmProjects/Work/Coursework_shyam/Python_data/Python/")

diabetes_data = pd.read_csv("diabetes.csv")
print(diabetes_data.columns)

print("The first 10 rows\n",diabetes_data.head(10))

BP_col = diabetes_data[["BloodPressure"]]
print(BP_col.mean())

print(diabetes_data.columns.get_loc("BloodPressure"))
col2_3_4 = diabetes_data.iloc[:, 3:6]
print(col2_3_4)

#min-max normalization
BP = diabetes_data.iloc[:,2]
print(BP.head())
#
# NormalizedBP = pd.DataFrame()
# NormalizedBP = (BP-min(BP))/(max(BP)-min(BP))
# NormalizedBP = pd.DataFrame(NormalizedBP, columns=['NormalizedBP'])

min_BP = diabetes_data['BloodPressure'].min()
max_BP = diabetes_data['BloodPressure'].max()

# Applying min-max normalization and adding the result to a new column
diabetes_data['NormalizedBP'] = (diabetes_data['BloodPressure'] - min_BP) / (max_BP - min_BP)

print(diabetes_data['NormalizedBP'])


def categorize_age(age):
    if 1 > age > 18:
        return "youth"
    if 19 > age > 50:
        return "Adult"
    if age > 50:
        return "Senior"


def age_category():
    diabetes_data['age_category'] = diabetes_data['Age'].apply(age_category)

print(diabetes_data.head())