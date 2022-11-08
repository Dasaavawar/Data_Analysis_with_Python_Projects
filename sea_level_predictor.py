import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
  
    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(x, y)
    
    # Create first line of best fit
    res_1 = linregress(x,y)
    print(res_1)
    x_pred1 = pd.Series([i for i in range(1880, 2051)])
    y_pred1 = res_1.intercept + (x_pred1 * res_1.slope)
    plt.plot(x_pred1, y_pred1, 'r')

    # Create second line of best fit
    df_2K = df[df['Year'] >= 2000]
    x_2 = df_2K['Year']
    y_2 = df_2K['CSIRO Adjusted Sea Level']
    res_2 = linregress(x_2, y_2)

    x_pred2 = pd.Series([i for i in range(2000, 2051)])
    y_pred2 = res_2.intercept + (x_pred2 * res_2.slope)
    plt.plot(x_pred2, y_pred2, 'g')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()