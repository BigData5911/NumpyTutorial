import pandas as pd

df = pd.read_csv("scores.csv", 
                 sep='\t', 
                 header=0, 
                 index_col=['Score'],
                 skiprows=[1,5],
                 usecols=['Name', 'Score'],
                 nrows=2)

print(df.head())