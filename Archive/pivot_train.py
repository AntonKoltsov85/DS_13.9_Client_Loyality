from IPython.display import display
import pandas as pd
from pathlib import Path

melb_df = pd.read_csv('melb_data_fe.csv', sep=',')
display(melb_df.pivot_table(
    values='Price',
    index=['SellerG'],
    columns='Type',
    aggfunc='median',
    fill_value=0
))