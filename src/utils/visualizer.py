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

def barChart_plot(values: pd.DataFrame, labels: pd.DataFrame, x_name: str, y_name: str, title: str):
    ax = sns.barplot(x= values, y= labels)
    plt.xlabel(x_name, fontsize=12, fontweight='bold')
    plt.yticks(fontsize=8, fontweight='bold')
    plt.tick_params(axis= 'y', pad = 12)
    plt.ylabel(y_name)
    plt.title(title)
    plt.savefig(f'/home/ahmed/projects/data_analysis/projects/ouput/plotting_images/{title}')
    plt.show()
