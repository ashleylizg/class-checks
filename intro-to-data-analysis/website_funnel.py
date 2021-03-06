"""
Cool T-Shirt Website Funnel for Page Visits
"""


import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

visits_cart = pd.merge(visits, cart, how='left')

count_null = visits_cart.cart_time.isnull().sum()

print(count_null)

percent_not_placed = 100 * (float(count_null) / len(visits_cart))

print(percent_not_placed)

cart_checkout = pd.merge(cart, checkout, how='left')

count_null_2 = cart_checkout.checkout_time.isnull().sum()

print(count_null_2)

percent_not_placed_2 = 100 * (float(count_null_2) / len(cart_checkout))

print(percent_not_placed_2)

all_data = visits.merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')

print(all_data.head())

count_null_3 = all_data.purchase_time.isnull().sum()

percent_not_placed_3 = 100 * (float(count_null_3) / len(all_data))

print(percent_not_placed_3)


all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time
print(all_data.time_to_purchase)
print(all_data.time_to_purchase.mean())
