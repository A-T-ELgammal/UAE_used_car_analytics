import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
import DB_manager
import visualizer

data_path = '/home/ahmed/projects/data_analysis/projects/data/data_cleaned.csv'

#queries:
#From where you will find most of used cars
sql_connection = DB_manager.Sql_connection()
sql_connection.postgres_connect('postgres','123456', 'localhost', '5432', 'UAE_used_cars')


def pieChart_emirates_rankning():

    emirates_ranking_query = " SELECT emirate, COUNT(emirate) AS number_of_cars FROM uae_used_cars_cleaned GROUP BY emirate;"
    emirates_df = sql_connection.query_df(emirates_ranking_query)
    emirates_df = emirates_df.sort_values('number_of_cars', ascending= False)
    
    total_cars = emirates_df['number_of_cars'].sum()    
    for record in range(emirates_df.shape[0]):
        if (emirates_df.iloc[record, 1] * 100 / total_cars) <= 5:
            emirates_df.iloc[record, 0] = 'other'    
    emirates_df = emirates_df.groupby('emirate', as_index= False)['number_of_cars'].sum() 
    visualizer.pieChart_plot(emirates_df['emirate'], emirates_df['number_of_cars'], 'emirates_ranknig_pie')
    
def bar_brand_ranking():
    brand_query = '''
    SELECT brand, COUNT(*) AS brand_count
    FROM uae_used_cars_cleaned
    GROUP BY brand
    ORDER BY model_count DESC;
    ''' 
    brand_ranking_df = sql_connection.query_df(brand_query)
    print(brand_ranking_df.head(5))

def main():
    # pieChart_emirates_rankning()
    bar_brand_ranking()
if __name__ == "__main__":
    main()