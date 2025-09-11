import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd


used_cars = pd.read_csv('/home/ahmed/projects/data_analysis/projects/data/data_cleaned.csv',delimiter= ',')

print(used_cars.info())
print('--------------------------------')
print(used_cars.isnull())