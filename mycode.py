import pandas as pd
import os 

data = { 
    'Name' : ['Alice', 'Bob', 'Charles'],
    'Age' : [25, 30, 35],
    'City' : ['New York', 'LosAngeles','Chikago']
}

df = pd.DataFrame(data)
print(df)
