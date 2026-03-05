import pandas as pd
import numpy as np

df=pd.read_csv("amazon.csv")
print(df.isnull())
print(df.isnull().sum())
