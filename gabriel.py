import pandas as pd
import numpy as np

customers = pd.read_csv("datasets/olist_customers_dataset.csv")
orders = pd.read_csv("datasets/olist_orders_dataset.csv")
payment = pd.read_csv("datasets/olist_order_payments_dataset.csv")

# print(customers, orders, payment)

# Objetivo: Média de preços de compra por consumidores de um mesmo estado
# order_id, customer_id, payment_value, customer_state

print(customers.isnull().sum().sum())
