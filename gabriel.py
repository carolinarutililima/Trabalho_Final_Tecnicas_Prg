import pandas as pd
import numpy as np
log = False

if log: print('Objetivo: Média de preços de compra por consumidores de um mesmo estado')
if log: print('Com indices: [order_id, customer_id, customer_state, customer_city, payment_value]')

customers = pd.read_csv("datasets/olist_customers_dataset.csv")
orders = pd.read_csv("datasets/olist_orders_dataset.csv")
payment = pd.read_csv("datasets/olist_order_payments_dataset.csv")
if log: print(f'\nTabelas usadas: \n\nolist_customers_dataset: \n{customers}\n\nolist_orders_dataset: \n{orders}\n\nolist_order_payments_dataset: \n{payment}')

customers_short = customers[['customer_id','customer_city', 'customer_state']]
orders_short = orders[['customer_id','order_id']]
payment_short = payment[['order_id', 'payment_value']]
if log: print(f'\nTabelas formatadas: \n{customers_short} \n{orders_short} \n{payment_short}')

df = pd.merge(customers_short, orders_short, on="customer_id", how="inner")
df = pd.merge(df, payment_short, on="order_id", how="inner")
df = df[['order_id', 'customer_id', 'customer_state', 'customer_city', 'payment_value']]
if log: print(f'\nTabela para análise: \n{df}')

if log: print(f'\nQuantidade de nulos: {df.isnull().sum().sum()}')

payment_by_state = df.groupby('customer_state').mean()
print(f'\nMédia dos valores das compras por estado: \n{payment_by_state}')
