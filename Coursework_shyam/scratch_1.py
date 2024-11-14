import os
import pandas as pd
import numpy as np
from openpyxl.styles.builtins import headline_1

os.chdir("/Coursework_shyam/Python_data/Python/")

data = pd.read_csv("diabetes.csv")
df_ODI_match = pd.read_csv("ODI-Batting_Cricket_Analytics.csv")
print(df_ODI_match.head())



def col_name(data):
    col_names = data.columns
    print(col_names)

col_name(df_ODI_match)

#Dimension of the data
print(df_ODI_match.shape)

df = df_ODI_match
df_match_date = pd.to_datetime(df['MatchDate'], dayfirst=True)
print(df_match_date.head())
date_2000 = pd.to_datetime('2/1/2000')

end_date = pd.to_datetime('1/1/2011')

print(date_2000)

df_date_india_2000 = df[(df["Country"] == "India") & (date_2000 < end_date)]
print(df_date_india_2000)

len_matched_country = len(df_date_india_2000)
print(f"Number of matched played by India:  ",len_matched_country)

#Top scorer for India in the year 2010
start_date = pd.to_datetime("1/1/2010")
end_date = pd.to_datetime("1/1/2011")

df_matches = df[(df["Country"]=="India") & (df_match_date > start_date) &  ( end_date > df_match_date ) ]
print(df_matches[["MatchDate"]])
num_matches = len(df_matches)

##grouping
df_player_scorer = df_matches.groupby(["Player"])["Runs"].sum()
print(f"Player {df_player_scorer.idxmax()}, Total Runs {df_player_scorer.max()}")


#Top 5 player
s_sorted = df_player_scorer.sort_values(ascending=False)
print(s_sorted.head())

#Matched played in the year 2010
df_India_matches = df_matches.groupby(["Versus"])
print(df_India_matches['Versus'].value_counts())

# print(df_India_matches['Player'].value_counts())


#################################################################################


print("\n"*4)
diabetes_data = np.genfromtxt('diabetes.csv',
                              delimiter=',', dtype='float', usecols=[0, 1, 2, 3, 4, 5, 6, 7], skip_header=1)
corr = np.corrcoef(diabetes_data[:, 1], diabetes_data[:, 5])
print("Correlation coefficient: ",corr[0,1])

print("Checking NaNs: ",np.isnan(diabetes_data).any())


#Import wine data
wine_quality = np.genfromtxt('winequality-red.csv',
                             delimiter=',', dtype='float', usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                             skip_header=1)
print(wine_quality.shape)

wine_quality[np.random.randint(len(wine_quality), size=20), np.random.randint(11, size=20)] = np.nan

print("Checking NaN values: ", np.isnan(wine_quality).any())
wine_quality[np.isnan(wine_quality)] =0

print("Checking NaN values, After replacing it with '0': ", np.isnan(wine_quality).any())
