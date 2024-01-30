# Import module
import pandas as pd
 
# Creating Data
car_selling_data = {'Brand': ['Maruti', 'Maruti', 'Maruti', 
                              'Maruti', 'Hyundai', 'Hyundai', 
                              'Toyota', 'Mahindra', 'Mahindra', 
                              'Ford', 'Toyota', 'Ford'],
                    'Year':  [2010, 2011, 2009, 2013, 
                              2010, 2011, 2011, 2010,
                              2013, 2010, 2010, 2011],
                    'Sold': [6, 7, 9, 8, 3, 5, 
                             2, 8, 7, 2, 4, 2]}
 
# Creating Dataframe of car_selling_data
df = pd.DataFrame(car_selling_data)

# Group the data when the Brand is Maruti
grouped = df.groupby('Brand')
# print(grouped, "\n\n")
# Sum the count of Maruti sold
print(grouped.get_group('Maruti')['Sold'].sum())