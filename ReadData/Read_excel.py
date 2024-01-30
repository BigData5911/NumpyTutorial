import pandas as pd

file = 'example.xlsx'

sheetOneData = pd.read_excel(file, sheet_name=0, index_col=0)
sheetTwoData = pd.read_excel(file, sheet_name=1, index_col=0)

print(pd.concat([sheetOneData, sheetTwoData]))


print(sheetOneData.head(1))
print(sheetTwoData.tail(2))

sorted_col = sheetOneData.sort_values(by='math', ascending=True)

print(sorted_col.head(3))
print(sheetOneData["infor"].head(3))

print(sheetOneData.describe())

sheetOneData['TotalMark'] = sheetOneData['math'] + sheetOneData['infor'] + sheetOneData['physics']

sheetOneData.to_excel('TotalMark.xlsx')
