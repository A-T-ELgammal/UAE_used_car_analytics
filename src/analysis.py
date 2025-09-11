import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
import sqlalchemy 

used_cars = pd.read_csv('/home/ahmed/projects/data_analysis/projects/data/data_cleaned.csv',delimiter= ',')

postgresql_user = 'postgres'
postgresql_password = '123456'
host = 'localhost'
port = '5432'
database = 'UAE_used_cars'

connection_request = f'postgresql+psycopg2://{postgresql_user}:{postgresql_password}@{host}:{port}/{database}'
engine = sqlalchemy.create_engine(connection_request)

try:
    with engine.connect() as connection:
        print('Successfully connected to the PostgreSQL database')
except exption as ex:
    print(f'failed to connect to postgreql due to this {ex}')