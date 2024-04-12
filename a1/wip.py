#%%
import pandas as pd

df = pd.read_csv('dictionary.csv', encoding='utf-8')

df.head()

#%%

kategori = 'fiil'

df = df[df['kategori'] == kategori]

# reset the index
df = df.reset_index(drop=True)

df.loc[0, 'kelime']