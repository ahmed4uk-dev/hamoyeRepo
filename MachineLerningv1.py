import pandas as pd


"""Intro to python for machine learning"""


df = pd.read_csv("FoodBalanceSheets_E_Africa_NOFLAG.csv", encoding = "latin-1")
# First 5 rows
print(df.head())
