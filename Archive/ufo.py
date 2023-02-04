from IPython.display import display
import pandas as pd
from pathlib import Path
import datetime

ufo_raw = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv', sep=',')
ufo_data=ufo_raw.copy()
ufo_data.info()
ufo_data['Time']=pd.to_datetime(ufo_data['Time'], dayfirst=True)
#display(ufo_data['Time'].dt.year.value_counts())
NV=ufo_data[ufo_data['State']=='NV']
display(NV['Time'].dt.date.diff().mean())