from IPython.display import display
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

covid_data = pd.read_csv('covid_data.csv')
#display(covid_data.head())

vaccinations_data = pd.read_csv('country_vaccinations.csv')
vaccinations_data = vaccinations_data[
    ['country', 'date', 'total_vaccinations', 
     'people_vaccinated', 'people_vaccinated_per_hundred',
     'people_fully_vaccinated', 'people_fully_vaccinated_per_hundred',
     'daily_vaccinations', 'vaccines']
]
covid_data = covid_data.groupby(
    ['date', 'country'], 
    as_index=False
)[['confirmed', 'deaths', 'recovered']].sum()
covid_data['date'] = pd.to_datetime(covid_data['date'])

covid_data['active'] = covid_data['confirmed'] - covid_data['deaths'] - covid_data['recovered']

covid_data = covid_data.sort_values(by=['country', 'date'])
covid_data['daily_confirmed'] = covid_data.groupby('country')['confirmed'].diff()
covid_data['daily_deaths'] = covid_data.groupby('country')['deaths'].diff()
covid_data['daily_recovered'] = covid_data.groupby('country')['recovered'].diff()

#covid_data.info()
vaccinations_data['date'] = pd.to_datetime(vaccinations_data['date'])
#vaccinations_data.info()
#display(vaccinations_data['date'].min())
#display(vaccinations_data['date'].max())

covid_df=pd.merge(covid_data,vaccinations_data,how='left',left_on=['date','country'],right_on=['date','country'])
covid_df['death_rate']=covid_df['deaths']/covid_df['confirmed']*100
covid_df['recover_rate']=covid_df['recovered']/covid_df['confirmed']*100
#display(round(covid_df[covid_df['country']=='Russia']['recover_rate'].mean(),2))
grouped_cases=covid_df.groupby(['country'])['total_vaccinations'].last().nsmallest(5)
grouped_cases.plot(kind='bar')
#covid_df.info()
covid_df['confirmed_per_hundred']=covid_df['confirmed']/covid_df['population']*100
countries = ['Russia', 'Australia', 'Germany', 'Canada', 'United Kingdom']
croped_covid_df = covid_df[covid_df['country'].isin(countries)]
jointplot = sns.jointplot(
    data=croped_covid_df, 
    x='date', 
    y='confirmed_per_hundred',
    hue='country',
    xlim = (0, 40),
    ylim = (0, 0.1),
    height=8,
)