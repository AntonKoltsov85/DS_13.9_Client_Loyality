from IPython.display import display
import pandas as pd
from pathlib import Path

#stud_perf=pd.read_csv('students_performance.csv',sep=',')
melb_data = pd.read_csv('melb_data.csv', sep=',')
#melb_data.info()
#print(round(abs((melb_data['BuildingArea'].median()-melb_data['BuildingArea'].mean())/melb_data['BuildingArea'].mean())*100,0))
#print(melb_data['Bedroom'].mode())
#mask = melb_data['Price'] > 2000000
#display(mask)
#display(melb_data.loc[0:88,['Bathroom']])
#display(melb_data[melb_data['Rooms'] == 3])
#display(melb_data[(melb_data['Rooms'] == 3) & (melb_data['Price'] < 300000)].shape[0])
#display(melb_data[((melb_data['Rooms'] == 3) | (melb_data['BuildingArea'] > 100)) & (melb_data['Price'] < 300000)].shape[0])
#display(melb_data[melb_data['Type'] == 't']['Rooms'].max())
#mean_price = melb_data['Price'].mean()
#display(melb_data[melb_data['Price'] > mean_price]['BuildingArea'].median())
#mask_b=melb_data['Bathroom']==0
#display(melb_data[(melb_data['BuildingArea']==0)]['Price'].min())
#display(melb_data[(melb_data['Type'] == 'h')&(melb_data['Price'] <3000000)]['Regionname'])
#display(melb_data['Regionname'].value_counts())
#stud_perf.info()
#display(stud_perf.loc[155,['writing score']])
#display(stud_perf[stud_perf['lunch']=='standard']['math score'].mean())
#display(stud_perf[stud_perf['lunch']=='free/reduced']['math score'].mean())
#display(stud_perf['parental level of education'].value_counts(normalize=True))
#a=stud_perf[stud_perf['race/ethnicity']=='group A']['writing score'].median()
#c=stud_perf[stud_perf['race/ethnicity']=='group C']['writing score'].mean()
#display(stud_perf['race/ethnicity'].value_counts(normalize=True))
#print(abs(round((a-c),0)))
melb_df = melb_data.copy()
#total_rooms = melb_df['Rooms'] + melb_df['Bedroom'] + melb_df['Bathroom']
#display(total_rooms)
#melb_df['MeanRoomsSquare'] = melb_df['BuildingArea'] / total_rooms
#display(melb_df['MeanRoomsSquare'])
#diff_area = melb_df['BuildingArea'] - melb_df['Landsize']
#sum_area = melb_df['BuildingArea'] + melb_df['Landsize']
#melb_df['AreaRatio'] = diff_area/sum_area
#display(melb_df['AreaRatio'])
#melb_df.info()
melb_df['Date']=pd.to_datetime(melb_df['Date'], dayfirst=True)
#display(melb_df['Date'])
melb_df['WeekdaySale']=melb_df['Date'].dt.day_of_week
#display(melb_df['WeekdaySale'])
#Friday=melb_df[(melb_df['WeekdaySale'] ==5)].shape[0]
#Saturday=melb_df[(melb_df['WeekdaySale'] ==6)].shape[0]
#display(Friday+Saturday)

def get_weekend(weekday):
    if weekday in [5,6]:
        return 1
    else:
        return 0
    

melb_df['Weekend'] = melb_df['WeekdaySale'].apply(get_weekend)
#display(round(melb_df[melb_df['Weekend']==1]['Price'].mean(),0))

popular_sellers =melb_df['SellerG'].value_counts().nlargest(49).index
#print(popular_sellers)
melb_df['SellerG'] = melb_df['SellerG'].apply(lambda x: x if x in popular_sellers else 'other')
Nelson_min=melb_df[melb_df['SellerG']=='Nelson']['Price'].min()
Other_min=melb_df[melb_df['SellerG']=='other']['Price'].min()

#display(round(Nelson_min/Other_min,1))
#melb_df.info()
#memory usage: 2.6+ MB
popular_suburb =melb_df['Suburb'].value_counts().nlargest(119).index
melb_df['Suburb'] = melb_df['Suburb'].apply(lambda x: x if x in popular_suburb else 'other')
melb_df['Suburb'] = melb_df['Suburb'].astype('category')
#melb_df.info()

#display(melb_df.head())

melb_df.drop(['index'],axis=1,inplace=True)
#melb_df.info()
display(melb_df['Date'].dt.quarter.value_counts())