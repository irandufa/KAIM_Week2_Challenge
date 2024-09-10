import pandas as pd
import numpy as np
import os
os.chdir('..')
import scipy.stats
from scipy.stats import zscore

def missing_value_handler(df):
    # Calculate missing values and percentages
    mis_value = df.isnull().sum()  # Total number of missing values
    mis_value_percent = 100 * df.isnull().sum() / len(df)  # Percentage of missing values
    mis_value_dtype = df.dtypes  # Data types of each column
    
    # Create a DataFrame with the calculated values
    mis_value_table = pd.concat([mis_value, mis_value_percent, mis_value_dtype], axis=1)
    
    # Rename the columns properly
    mis_value_table_run_column = mis_value_table.rename(columns={0: 'Missing Values', 1: '% of Total Values', 2: 'Dtypes'})
    
    # Filter out columns with no missing values and sort by the percentage of missing values
    mis_value_table_run_column = mis_value_table_run_column[mis_value_table_run_column['% of Total Values'] != 0].sort_values('% of Total Values', ascending=False).round(1)
    
    # Print the number of columns and columns with missing values
    print("Your selected dataframe has " + str(df.shape[1]) + " columns.\n" + 
          "There are " + str(mis_value_table_run_column.shape[0]) + " columns that have missing values.")
    
    return mis_value_table_run_column

