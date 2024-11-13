import pandas as pd

df = pd.DataFrame(
    {
        "Name":[
            "Braud,Mr Owen",
            "Allen, Mr William",
            "Bonnell, Miss Elizabeth"
        ],
        "Age":[22,33,44],
        "Pincode":[58742,78742,98742],
        "Sex":["M", "M","F"]
    }
)

print(df["Age"])
print(type(df["Age"]))
print(df["Age"].max())

print("\nDescription\n",df.describe()) #summary statistics

import Python_data.Python

import csv
import os
titanic = pd.read_csv("/home/ibab/PycharmProjects/Work/Coursework_shyam/Python_data/Python/titanic.csv")
print(titanic.head())
print(titanic.dtypes)

#save as excel
import openpyxl
titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)

titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")
print(titanic)
print(titanic.info())
print(titanic.dtypes)
print(titanic.shape)

#selecting a subset of a df
age_sex = titanic[["PassengerId","Age","Sex"]]
print(age_sex.head())

#filtering rows
above_35 = titanic[titanic["Age"] > 35]
print(above_35.head())
#filtering based on criteria
class_23 = titanic[titanic["Pclass"].isin([2,3])]
print(class_23)

#selecting specific rows and columns

# adult_names = titanic[titanic["Age"] > 35, "Name"]
# print(adult_names

#groupby
df = pd.DataFrame({"Animal":["Falcon", "Falcon","Parrot", "Parrot"],
                   'Max speed': [ 240,250, 34.,36.]})

m = df.groupby(["Animal"]).mean()
print(m)

df_s = titanic[["Sex", "Age"]].groupby("Sex")
print(df_s.count())

print(df_s["Age"].mean())

df_sp = titanic.groupby(["Sex", "Pclass"])
print(df_sp["Fare"].mean())

