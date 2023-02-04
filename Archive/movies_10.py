from IPython.display import display
import pandas as pd
from pathlib import Path
import re

def get_year_release(arg):
    #находим все слова по шаблону "(DDDD)"
    candidates = re.findall(r'\(\d{4}\)', arg) 
    # проверяем число вхождений
    if len(candidates) > 0:
        #если число вхождений больше 0,
	#очищаем строку от знаков "(" и ")"
        year = candidates[0].replace('(', '')
        year = year.replace(')', '')
        return int(year)
    else:
        #если год не указан, возвращаем None
        return None
ratings1=pd.read_csv('ratings_movies.csv', sep=',')
ratings1['date']=pd.to_datetime(ratings1['date'])
ratings1['year_rating']=ratings1['date'].dt.year
ratings1['year_release'] = ratings1['title'].apply(get_year_release)
mask1=ratings1['year_release']==1999
#display(ratings1[mask1].groupby('title')['rating'].mean().sort_values())
mask2=ratings1['year_release']==2010
#display(ratings1[mask2].groupby('genres')['rating'].mean().sort_values())
#ratings1.info()
#display(ratings1.groupby('userId')['genres'].nunique().sort_values(ascending=False))
#display(ratings1.groupby('userId')['rating'].agg(
 #   ['count', 'mean']
#).sort_values(['count', 'mean'], ascending=[True, False]))
mask = ratings1['year_release'] == 2018
grouped = ratings1[mask].groupby('genres')['rating'].agg(
    ['mean', 'count']
)
#display(grouped[grouped['count']>10].sort_values(
  #  by='mean',
 #   ascending=False
#))

display(ratings1[ratings1['genres']=='Comedy'].pivot_table(
    values='rating',
    index=['year_rating'],
    columns='genres',
    aggfunc='mean',
    fill_value=0,
    ).sort_values)