#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 12:54:12 2020

@author: rootstrap
"""

import pandas as pd
import matplotlib.pyplot as plt
import geopandas
from matplotlib import cm


#plot countries
def plot(df, title, country_column_name, column_name, legend=False):
    world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
    merged_inner = pd.merge(left=world, right=df, left_on='name',right_on=country_column_name, how='inner')
    cmap = cm.get_cmap('Spectral')
    ax = world.plot(figsize=(20,5), linewidth=0.25, edgecolor='white', color='lightgrey')
    ax.set_title(title)
    merged_inner.plot(column=column_name, ax=ax, cmap=cmap, legend=legend)
    plt.show()

def update_values(df, column, current_values, new_values):
    for current_value,new_value in zip(current_values, new_values):
        df.loc[df[df[column]==current_value].index,column] = new_value