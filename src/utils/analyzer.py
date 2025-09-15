import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
import DB_manager

used_cars = pd.read_csv('/home/ahmed/projects/data_analysis/projects/data/data_cleaned.csv',delimiter= ',')


# def emirates_ranking():
    emirates_ranking_query = " SELECT emirate, COUNT(emirate) AS number_of_cars FROM uae_used_cars_cleaned GROUP BY emirate;"
    emirares_df = pd.read_sql(emirates_ranking_query, engine)
    emirares_df = emirares_df.sort_values('number_of_cars', ascending= False)
    palette = sns.color_palette("Set2", len(emirares_df))

    sns.barplot(data= emirares_df, x= 'number_of_cars', y= 'emirate', palette = palette)
    plt.title('emirates_ranking_of_used_cars')
    plt.xlabel('used_cars_available')
    plt.ylabel('Emirate')
    plt.savefig('/home/ahmed/projects/data_analysis/projects/ouput/plotting_images/emirates_ranking.png', dpi = 300, bbox_inches = 'tight')
    plt.show()

def main():
    sql_connection = DB_manager.Sql_connection()
    sql_connection.postgres_connect('postgres','123456', 'localhost', '5432', 'UAE_used_cars')
    # emirates_ranking()

if __name__ == "__main__":
    main()