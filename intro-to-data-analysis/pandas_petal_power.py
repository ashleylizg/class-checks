import codecademylib
import pandas as pd
inventory = pd.read_csv('inventory.csv')
inventory.head(10)
staten_island = inventory.loc[:11]
product_request = staten_island.product_description
seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]
quantity = inventory.quantity
get_inventory = lambda x: True if x > 0 else False
inventory['in_stock'] = inventory.quantity.apply(get_inventory) 
inventory['total_value'] = inventory['price']*inventory['quantity']
product_type = inventory.product_type
product_description = inventory.product_description
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)
inventory['full description'] = inventory.apply(combine_lambda, axis = 1)
print(inventory)
