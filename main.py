import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from tabulate import tabulate
pd.options.display.width = 0

df = pd.read_csv('vgsales/vgsales.csv')



# Tratando NULLS
df['Publisher'] = df['Publisher'].fillna('Unknown')
df['Year'] = df['Year'].fillna(0000)

# Modificando o tipo do Year
df['Year'] = df['Year'].astype(int)

print(df.head(10))