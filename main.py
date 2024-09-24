import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from tabulate import tabulate
pd.options.display.width = 0
pd.set_option('display.max_rows', None)

df = pd.read_csv('vgsales/vgsales.csv')

df_clean_data_year = pd.read_csv('clean-data/clean-data.csv')
df_clean_data_publisher = pd.read_csv('clean-data/clean-data-publisher.csv')


df_atualizada = pd.merge(df, df_clean_data_year, on="Name", how="left", suffixes=("", "_comp"))
df_atualizada['Year'] = df_atualizada['Year'].fillna(df_atualizada['Year_comp'])
df_atualizada.drop(columns=['Year_comp'], inplace=True)


df_atualizada2 = pd.merge(df_atualizada, df_clean_data_publisher, on="Name", how="left", suffixes=("", "_comp"))
df_atualizada2['Publisher'] = df_atualizada2['Publisher'].fillna(df_atualizada2['Publisher_comp'])
df_atualizada2.drop(columns=['Publisher_comp'], inplace=True)

#print(df_atualizada.groupby(['Year'])['Global_Sales'].sum())
#print(df.groupby(['Year'])['Global_Sales'].sum())




#print(df_atualizada2[df_atualizada2.isnull().any(axis=1)])
print(df_atualizada2[(df_atualizada2['Publisher'] == "Unknown")])
#print(df_atualizada2.isnull().sum())
# Tratando NULLS
df['Publisher'] = df['Publisher'].fillna('Unknown')
df['Year'] = df['Year'].fillna(0000)

# Modificando o tipo do Year
df['Year'] = df['Year'].astype(int)

#print(df.head(10))