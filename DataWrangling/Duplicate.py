
# import module
import pandas as pd
 
# initializing Data
student_data = {'Name': ['Amit', 'Praveen', 'Jagroop', 
                         'Rahul', 'Vishal', 'Suraj', 
                         'Rishab', 'Satyapal', 'Amit', 
                         'Rahul', 'Praveen', 'Amit'],
 
                'Roll_no': [23, 54, 29, 36, 59, 38, 
                            12, 45, 34, 36, 54, 23],
                'Email': ['xxxx@gmail.com', 'xxxxxx@gmail.com', 
                          'xxxxxx@gmail.com', 'xx@gmail.com', 
                          'xxxx@gmail.com', 'xxxxx@gmail.com', 
                          'xxxxx@gmail.com', 'xxxxx@gmail.com', 
                          'xxxxx@gmail.com', 'xxxxxx@gmail.com',
                          'xxxxxxxxxx@gmail.com', 'xxxxxxxxxx@gmail.com']}
 
data_df = pd.DataFrame(student_data)

non_duplicate = data_df[~data_df.duplicated('Roll_no', keep='first')]

print(non_duplicate)
print("\n")
print(data_df.duplicated('Roll_no', keep='first'))