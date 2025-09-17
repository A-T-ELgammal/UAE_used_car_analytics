import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 

    
def pieChart_plot(labels: pd.DataFrame, values: pd.DataFrame, plot_name: str):
    colors = sns.color_palette('pastel')
    plt.pie(values, colors= colors, autopct='%.2f%%', pctdistance= 0.8)
    plot_path = f'/home/ahmed/projects/data_analysis/projects/ouput/plotting_images/{plot_name}'
    plt.legend(labels)
    plt.savefig(plot_path)
    plt.show()
