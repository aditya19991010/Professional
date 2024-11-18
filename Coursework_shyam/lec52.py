import re
from os import PRIO_USER

import pandas as pd
from pyparsing import matchPreviousLiteral

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

###Count number of records by category
#number of passengers in each of the classes
print(titanic["Pclass"].value_counts())

##sorting by Fare
titanic_sorted_age = titanic.sort_values(by="Fare").head()
print(titanic_sorted_age)


#combine data from multiple files
# print(os.getcwd())
os.chdir("Python_data/Python/")
air_quality_no2_long = pd.read_csv("air_quality_no2_long.csv", parse_dates=True)
print(air_quality_no2_long.shape)
print(air_quality_no2_long.columns)
air_quality_pm25 = pd.read_csv("air_quality_pm25_long.csv", parse_dates=True)
print(air_quality_pm25.shape)

air_quality_pm25 = air_quality_pm25[["date.utc", "location", "parameter", "value"]]

air_quality = pd.concat([air_quality_no2_long,air_quality_pm25], axis=0)
print(air_quality.shape)


## Join tables using a common identifier
df1 = pd.DataFrame({'a':['foo','bar'], 'b':[1,2]})
df2 = pd.DataFrame({'a':['foo','baz'], 'b':[3,4]})

#join - common type {inner_join, left_join, right_join}, cross_join
# Take commons between two columns
# https://pandas.pydata.org/docs/user_guide/merging.html

df_inner = df1.merge(df2,how="inner", on='a')
print("Inner\n",df_inner)
df_left = df1.merge(df2,how="left", on='a')
print("Left\n",df_left)
df_right = df1.merge(df2,how="right", on='a')
print("right\n",df_right)

df1 = pd.DataFrame({'a':['foo','bar']})
df2 = pd.DataFrame({'b':[1,2]})

df_cross = df1.merge(df2,how="cross")
print(df_cross)


##Regular expressions (Regex)
# result - re.match(patter,sources)


print(re.match('Ro', "Rohit Sharma"))

#compile to speed ip the search
pattern = re.compile("Rohit")
result = pattern.match("Rohit Sharma")
print(result)

#to return the span information
if result:
    print(result.group())


# '.*' used as a wildcard for searching

source = "Sachin Ramesh Tendulkar"
m = re.match('.*Ten', source)
if m:
    print(m.group())

# findall() returns a list of all non-overlapping matches, if any.
sources = "It was a good match against Australia with food cricket display"
pattern = re.compile("g.*d")

result = pattern.findall(sources)

print(result)

result = pattern.split(sources)

print(result)


# result = re.findall( "It was a good match against Australia with food cricket display")
print(result)

# result = re.sub("good",  "It was a good match against Australia with food cricket display")


import string
printable = string.printable
print(len(printable))
print(printable[0:50])


m = re.findall('\\d',printable) #search for the digit
if m:
    print(m)

m = re.findall('\\w', printable) #digit or character
if m:
    print(m)

m = re.findall("\\s", printable)
print(m)

source = '''I wish I may, I wish I might Have a dish of fish tonight'''
m = re.findall('wish',source)
print(m)

m = re.findall('wish|fish',source)
print(m)

m = re.findall('^I',source) #check for the begining
print(m)

m = re.findall('[wf]ish',source)  #find word with 1st letter either w or f
print(m)


m = re.findall('[wsh]+',source)  #find word with 1st letter either w or f
print(m)

m = re.findall('[wsh]',source)  #find word with 1st letter either w or f
print(m)


##lec53
m = re.findall('I (?=wish)',source)  #find word I before 'wish'
print(m)

m = re.findall('(?<=I) wish',source)  #find 'wish' preceeded by I
print(m)

m = re.findall('\bfish',source)  #\b means backspace
print(m)


m = re.findall(r'\bfish',source)  #use r in pattern always to consider literal meaning of regex \b unlike \n as newline
print(m)



m = re.search(r'(. dish\b).*(\bfish)',source)  #
print(m.group())
print(m.groups())

m = re.search(r'(?P<DISH>. dish\b).*(\bfish)',source)  #
print(m.group())
print(m.groups())

print(m.group('DISH'))

#Finding motif
import sys
DNA = 'ACGGGGGCAATCATGTGATCGATCGATAATAA'
print("DNA seq - ", DNA)

motif = r'ATG.*?TAA' #With *? checks on as few as possible and .* as many as possible
print('Motif: ', motif)

try:
    re.compile(motif)
except:
    print('Invalid regex, exiting the program.')
    sys.exit()

match = re.search(motif, DNA)
if match:
    print(' Found the motif:', match.group())
    print(' Starting at index:', match.start())
    print(' Ending at index:', match.end())
