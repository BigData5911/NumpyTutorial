import pandas as pd

scores = {'Name': ['a', 'b', 'c', 'd', 'e'],
          'Score': [90, 80, 95, 20, 90]}

df = pd.DataFrame(scores)

print(df.mode(), "mode")


print(df)
df.to_csv('scores.csv', index=False, sep='\t')