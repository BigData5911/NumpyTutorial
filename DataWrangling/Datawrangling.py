# import pandas package
import pandas as pd

# Assign data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 
                 'Anuj', 'Ravi', 'Natasha', 'Riya'],
        'Age': [17, 17, 18, 17, 18, 17, 17],
        'Gender': ['M', 'F', 'M', 'M', 'M', 'F', 'F'],
        'Marks': [90, 76, 'NaN', 74, 65, 'NaN', 71]}

data_df = pd.DataFrame(data)

print(data_df, "\nThis is the dataframe of data\n")

# -----------------------------------Dealing with missing value of Marks
data_df['Marks'] = pd.to_numeric(data_df['Marks'], errors='coerce')

print(data_df, "\nThis is the dataframe after converting NaN string to float\n")

avg_marks = data_df['Marks'].mean()

print(avg_marks, "\nThis is average of marks after dealing with NaN string into float\n")

data_df.loc[:, 'Marks'] = data_df['Marks'].fillna(avg_marks)

print(data_df, "\nThis is the dataframe after filling NaN values with mean\n")

# --------------------------------------Data replacing in Data wrangling

# using replaing fucntoin in dataframe
# data_df['Gender'].replace(['M', 'F'], [1, 0], inplace=True)

# another way using the map func in series of pandas
data_df['Gender'] = data_df['Gender'].map({'M': 1, 'F': 0}).astype(float)

print(data_df, "\nThis is the dataframe after replacing M and F with 1 and 0\n")

# --------------------------------------filtering the data

# filtering the score data
data_df = data_df[data_df['Marks'] > 75.0].copy()
# filtering the age column
data_df.drop('Age', axis=1, inplace=True)

print(data_df, "\nThis is the dataframe after filtering by score of data and dropping the age column\n")


