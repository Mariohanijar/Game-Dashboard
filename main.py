import pandas as pd
import numpy as np

pd.options.display.width = 0
pd.set_option('display.max_rows', None)

df = pd.read_csv('vgsales/vgsales.csv')

# Substituir "Unknown" por NaN na coluna 'publisher'
df['Publisher'] = df['Publisher'].replace("Unknown", np.nan)

#Adicionando arquivos com os dados tratados
df_clean_data_year = pd.read_csv('clean-data/clean-data-year.csv')
df_clean_data_publisher = pd.read_csv('clean-data/clean-data-publisher.csv')

# Tratando NULLS
df = pd.merge(df, df_clean_data_year, on="Name", how="left", suffixes=("", "_comp"))
df['Year'] = df['Year'].fillna(df['Year_comp'])
df.drop(columns=['Year_comp'], inplace=True)

df = pd.merge(df, df_clean_data_publisher, on="Name", how="left", suffixes=("", "_comp"))
df['Publisher'] = df['Publisher'].fillna(df['Publisher_comp'])
df.drop(columns=['Publisher_comp'], inplace=True)

# Modificando o tipo do Year
df['Year'] = df['Year'].astype(int)

#Excluindo todas as duplicatas
df = df.drop_duplicates()

# Excluir anos que estão com muita falta de dados
df = df[df.Year != 2017]
df = df[df.Year != 2020]

# Salvar o dataframa tratado
csv_file_path = "clean-data/clean-dataframe.csv"
df.to_csv(csv_file_path, index=False)

