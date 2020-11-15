import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os




def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
          pd.read_csv(url_or_path_to_csv_file)
          .isnull().any()
          .dropna(axis = 0, how= 'any')
          .dropna(columns = 'Index', errors='ignore')
          .rename(columns = {'instant':'Index', 'dteday':'Date', 'season':'Season', 'yr':'Year', 'mnth':'Month',
                             'hr':'Hour', 'holiday':'Holiday', 'weekday':'Week_day', 'workingday':'Working_day',
                             'weathersit':'Weather', 'temp':'Temperature', 'atemp':'FeelTemp', 'hum':'Humidity',
                             'windspeed':'Wind_speed', 'casual':'Casual_users', 'registered':'Registered_users',
                             'cnt': 'Total_users'} , errors = 'ignore') 
              
          .assign(color_filter=lambda x: np.where((x.hue>2) & (x.ci>8), 2, 1))
          .sort_values('dteday', ascending=False)
          .sort_values('cnt', ascending=True)
          .sort_values('windspeed', ascendting=True)
          
          
          
      )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
            df1
            .isnull().any()
            .assign(Casual_ratio= lambda x:x['Casual_users']/ x['Total_users'])
            .assign(AverageTemp = lambda x : (x['FeelTemp'] + x['Temperature']) / 2)
            .isnull().any()
            .rename(columns= {})
            
      )

    # Make sure to return the latest dataframe

    return df2