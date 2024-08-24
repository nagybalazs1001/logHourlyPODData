# import necessary libraries 
import pandas as pd 
import os 
import glob
import tkinter as tk
from tkinter import simpledialog
  

# COLLECTING CSVS
path = os.getcwd()  # Returns current working directory
csv_files = glob.glob(os.path.join(path, "**/*.csv"), recursive=True) # Combines all csv files in folders and subfolders
  
# FILTERING OUT CSVS
filteredList = [word for word in csv_files if 'AH_N' in word]

# LOOPING THROUGH CSVS
for f in filteredList: 
    df = pd.read_csv(f, encoding='ANSI', sep=';', skiprows=1) # Reads through all csv files with set conditions
            

# COLUMN SETTINGS
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

# sorting by date
df_new['Óra'] = pd.to_datetime(df_new['Óra'])
df_new.sort_values(by='Óra', ascending=False)

# print the content 
print(df_new)