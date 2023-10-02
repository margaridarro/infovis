# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 10:57:37 2023

@author: marga
"""

import pandas as pd

# Read CSV files into dataframes
'''
df1 = pd.read_csv('vuelos_margarida_2.csv')
df2 = pd.read_csv('airports.csv')

merged_df = pd.merge(df1, df2, on='id')

#df2 = pd.read_csv('airports.csv')'''

df1 = pd.read_csv('vuelos_margarida_merged_1.csv')
df2 = pd.read_csv('airports.csv')

merged_df_final = pd.merge(df1, df2, on='id')

merged_df_final.to_csv('vuelos_margarida_merged_2.csv')

