# import pandas package
import pandas as pd

#----------------------------------------Data Wrangling with merge operation

# creating DataFrame for Student Details
details = pd.DataFrame({
    'ID': [101, 102, 103, 104, 105, 106, 
           107, 108, 109, 110],
    'NAME': ['Jagroop', 'Praveen', 'Harjot', 
             'Pooja', 'Rahul', 'Nikita',
             'Saurabh', 'Ayush', 'Dolly', "Mohit"],
    'BRANCH': ['CSE', 'CSE', 'CSE', 'CSE', 'CSE', 
               'CSE', 'CSE', 'CSE', 'CSE', 'CSE']})
 
 # Creating Dataframe for Fees_Status
fees_status = pd.DataFrame(
    {'ID': [101, 102, 103, 104, 105, 
            106, 107, 108, 109, 110],
     'PENDING': ['5000', '250', 'NIL', 
                 '9000', '15000', 'NIL',
                 '4500', '1800', '250', 'NIL']})

data_merged = pd.merge(details, fees_status, on='ID', how='right')

print(data_merged, type(data_merged), "\nThis is the data after merge operation\n")