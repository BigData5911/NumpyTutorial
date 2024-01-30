import pandas as pd

scores = {'Name': ['a', 'b', 'c', 'd'],
          'Score': [90, 80, 95, 20]}

df = pd.DataFrame(scores)
print(df)
df.to_csv('scores.csv', index=False, sep='\t')