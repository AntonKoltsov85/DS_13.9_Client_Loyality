from IPython.display import display
import pandas as pd
from pathlib import Path

ratings1=pd.read_csv('Users\user\Documents\Programming\IDE\data\movies_data\ratings1.csv', sep=',')
display(ratings1.value_counts())