import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 

    
def pieChart_plot(labels: pd.DataFrame, values: pd.DataFrame, plot_name: str):
    colors = sns.color_palette('bright6')
    plt.pie(values, labels=labels, colors= colors, autopct='%.2f%%', pctdistance= 0.8)
    plot_path = f'/home/ahmed/projects/data_analysis/projects/ouput/plotting_images/{plot_name}'
    plt.savefig(plot_path)
    plt.show()
