# import necessary libraries 
import pandas as pd 
import os 
import glob
import tkinter as tk
from tkinter import simpledialog
  

# use glob to get all the csv files in the folder
path = os.getcwd() 
csv_files = glob.glob(os.path.join(path, "*.csv")) 
  
# loop over the list of csv files 
for f in csv_files: 
      
    # read the csv files 
    df = pd.read_csv(f, encoding='ANSI', sep=';', skiprows=1) 
            

# set columns in base table
df.columns = ['Óra', 'Elosztó', 'POD', 'Óra száma', 'm3', 'K', 'V', 'kWh']
df['m3'] = df['m3'].str.replace(',', '.').astype(float)
df['kWh'] = df['kWh'].str.replace(',', '.').astype(float)
# modify base column types
df['kWh'].apply(pd.to_numeric)
df['Óra'].apply(pd.to_datetime)
   
# POPUP
ROOT = tk.Tk()
ROOT.withdraw()
# the input dialog
podname = simpledialog.askstring(title="Insert POD",
                                  prompt="Insert the required POD:")

# Export table
df_new = df.loc[(df['POD'] == podname)]

# export to csv
df_new.to_csv(f'Hourly historical data - {podname}.csv', sep=',', index=False, encoding='ANSI')

# print the content 
print(df_new)
