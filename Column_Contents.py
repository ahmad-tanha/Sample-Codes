#print the elements in the given column of a CSV data file
import pandas as pd
import numpy as np 

filename = input(/Sample-Codes/one.csv)
column_name = input()

df = pd.read_csv(filename)
col = df[column_name].values 
print(col)
