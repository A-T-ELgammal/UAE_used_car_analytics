import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
import DB_manager
import visualizer

data_path = '/home/ahmed/projects/data_analysis/projects/data/data_cleaned.csv'

#queries:
#From where you will find most of used cars
emirates_ranking_query = " SELECT emirate, COUNT(emirate) AS number_of_cars FROM uae_used_cars_cleaned GROUP BY emirate;"



def main():
    sql_connection = DB_manager.Sql_connection()
    # visualizer = visualizer()

    sql_connection.postgres_connect('postgres','123456', 'localhost', '5432', 'UAE_used_cars')
    
    emirares_df = sql_connection.query_df(emirates_ranking_query)
    emirares_df = emirares_df.sort_values('number_of_cars', ascending= False)
   
    print('--------------------')
    total_cars = emirares_df['number_of_cars'].sum()
    for record in range(emirares_df.shape[0]):
        if(emirares_df.iloc[record][1] * 100 / total_cars <= 5):
            emirares_df.iloc[record, 0] = "other"
    emirares_df = emirares_df.groupby('emirate', as_index= False)['number_of_cars'].sum()
    print('---------------------')
   
    print(emirares_df)
    visualizer.pieChart_plot(emirares_df['emirate'], emirares_df['number_of_cars'], 'emirates_ranknig_pie')
if __name__ == "__main__":
    main()