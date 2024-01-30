
# importing the module
import pandas as pd
 
# creating a DataFrame
df = pd.DataFrame([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']],
                  index =['row 1', 'row 2', 'row3'],
                  columns =['col 1', 'col 2', 'col3'])
 
# storing the data in JSON format
df.to_json('file.json', orient = 'split', compression = 'infer', index = 'true')
 
# reading the JSON file
df = pd.read_json('file.json', orient ='split', compression = 'infer')
 
# displaying the DataFrame
print(df)