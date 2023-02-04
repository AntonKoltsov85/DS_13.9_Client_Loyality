from IPython.display import display
import pandas as pd
from pathlib import Path

melb_df = pd.read_csv('melb_data_fe.csv', sep=',')
#melb_data.info()
melb_df['Date'] = pd.to_datetime(melb_df['Date'])
quarters = melb_df['Date'].dt.quarter
#display(quarters.value_counts())
cols_to_exclude = ['Date', 'Rooms', 'Bedroom', 'Bathroom', 'Car'] 
max_unique_count = 150 
for col in melb_df.columns: 
    if melb_df[col].nunique() < max_unique_count and col not in cols_to_exclude: 
        melb_df[col] = melb_df[col].astype('category')
#display(melb_df.info())
#display(melb_df.sort_values(by=['Distance', 'Price']).loc[::10, ['Distance', 'Price']])
mask1 = melb_df['AreaRatio'] < -0.8
mask2 = melb_df['Type'] == 'townhouse'
mask3 = melb_df['SellerG'] == 'McGrath'
#display(melb_df[mask1 & mask2 & mask3].sort_values(
 #   by=['Date', 'AreaRatio'],
 #   ascending=[True, False],
  #  ignore_index=True
#).loc[:, ['Date', 'AreaRatio']])
#melb_df.sort_values(['AreaRatio'],ascending=[False],inplace=True,ignore_index=True)
#melb_df.info()
#display(melb_df.loc[1558,['BuildingArea']])
mask4=melb_df['Type'] == 'townhouse'
mask5=melb_df['Rooms'] >2
#display(melb_df[mask4 & mask5].sort_values(
 #   by=['Rooms','MeanRoomsSquare'],
  #  ascending=[True,False],
   # ignore_index=True
#).loc[18,['Price']])
#display(melb_df.groupby(by='Type').mean())
#display(melb_df.groupby('MonthSale')['Price'].agg('describe'))
#display(melb_df.groupby('Regionname')['SellerG'].agg(['nunique',set]))
#display(melb_df.groupby('Rooms')['Price'].mean().sort_values(ascending=False))
#display(melb_df.groupby('Regionname')['Lattitude'].std().sort_values())
date1 = pd.to_datetime('2017-05-01')
date2 = pd.to_datetime('2017-09-01')
mask = (date1 <= melb_df['Date']) & (melb_df['Date']<= date2)
display(melb_df[mask].groupby('SellerG')['Price'].sum().sort_values(ascending=True))