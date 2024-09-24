import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from tabulate import tabulate
pd.options.display.width = 0
pd.set_option('display.max_rows', None)

df = pd.read_csv('vgsales/vgsales.csv')

df_clean_data = pd.read_csv('clean-data/clean-data.csv')
#df_clean_data['Year'] = df['Year'].astype(int)
print(df_clean_data.head(10))
#print(df[df.isnull().any(axis=1)]["Name"])
# Tratando NULLS
df['Publisher'] = df['Publisher'].fillna('Unknown')
df['Year'] = df['Year'].fillna(0000)

# Modificando o tipo do Year
df['Year'] = df['Year'].astype(int)

#print(df.head(10))