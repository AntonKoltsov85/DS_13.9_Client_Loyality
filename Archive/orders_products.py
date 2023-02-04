from IPython.display import display
import pandas as pd
from pathlib import Path

orders=pd.read_csv('orders.csv', sep=';')
products=pd.read_csv('products.csv', sep=';')
#orders.info()
#products.info()
orders_products=orders.merge(products,how='left',left_on='ID товара',right_on='Product_ID')
#display(orders_products['Отменен'])
orders_products['Profit'] = orders_products['Price'] * orders_products['Количество'] 
display(orders_products[orders_products['Оплачен'] == 'Да'].groupby('ID Покупателя')['Profit'].sum().sort_values(ascending=False))