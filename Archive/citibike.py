from IPython.display import display
import pandas as pd
from pathlib import Path
pdf=pd.re
citibike=pd.read_csv('citibike-tripdata.csv', sep=',')
#citibike.info()
#display(citibike[citibike['start station id'].isna()].shape[0])
#display(citibike['start station id'].value_counts())
#display(citibike['bikeid'].value_counts())
#display(citibike['usertype'].value_counts(normalize=True))
#display(citibike['gender'].value_counts())
#display(citibike[citibike['gender']==citibike['gender'].mode()].shape[0])
#display(citibike['end station name'].mode())
citibike.drop(['start station id','end station id'], axis=1,inplace=True)
citibike['age']=2018-citibike['birth year']
#display(citibike[citibike['age']>60].shape[0])
citibike['starttime']=pd.to_datetime(citibike['starttime'])
citibike['stoptime']=pd.to_datetime(citibike['stoptime'])
citibike['trip duration']=citibike['stoptime']-citibike['starttime']
#display(citibike.loc[3,['trip duration']])
#citibike.info()
weekday = citibike['starttime'].dt.dayofweek
citibike['weekend'] = weekday.apply(lambda x: 1 if x ==5 or x == 6 else 0)
#display(citibike['weekend'].sum())
def get_time_of_day(time):
    if 0 <= time <= 6:
        return 'night'
    elif 6 < time <= 12:
        return 'morning'
    elif 12 < time <= 18:
        return 'day'
    elif 18 < time <= 23:
        return 'evening'
    else:
        return 'else'
citibike['time_of_day'] = citibike['starttime'].dt.hour.apply(get_time_of_day)
a = citibike[citibike['time_of_day'] == 'day'].shape[0]
b = citibike[citibike['time_of_day'] == 'night'].shape[0]
print(round(a / b))