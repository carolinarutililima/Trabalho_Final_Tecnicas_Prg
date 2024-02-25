import pandas as pd
import numpy as np

# Objetivo: Média de preços de compra por consumidores de um mesmo estado
# order_id, customer_id, customer_state, customer_city, payment_value

customers = pd.read_csv("datasets/olist_customers_dataset.csv")
orders = pd.read_csv("datasets/olist_orders_dataset.csv")
payment = pd.read_csv("datasets/olist_order_payments_dataset.csv")
# print(customers, orders, payment)

customers_short = customers[['customer_id','customer_city', 'customer_state']]
orders_short = orders[['customer_id','order_id']]
payment_short = payment[['order_id', 'payment_value']]
# print(customers_short, orders_short, payment_short)

df = pd.merge(customers_short, orders_short, on="customer_id", how="inner")
df = pd.merge(df, payment_short, on="order_id", how="inner")
df = df[['order_id', 'customer_id', 'customer_state', 'customer_city', 'payment_value']]
print(df)

# print(df.isnull().sum().sum())
