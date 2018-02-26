"""
A/B Testing at Nosh Mish Mosh project from Learn Sample Size Determination with SciPy
"""

import noshmishmosh
import numpy as np

all_visitors = noshmishmosh.customer_visits

paying_visitors = noshmishmosh.purchasing_customers

total_visitor_count = len(all_visitors)
paying_visitor_count = len(paying_visitors)
print ("Total visitor count: %d"%(total_visitor_count))
print ("Paying visitor count: %d"%(paying_visitor_count))

baseline_percent = 100 * paying_visitor_count / total_visitor_count
print ("Baseline percent: %d"%(baseline_percent))

payment_history = noshmishmosh.money_spent

average_payment = np.mean(payment_history)
print ("Average payment:%.2f"%(average_payment))

new_customers_needed = np.ceil(1240 / average_payment)
print ("New customers needed: %d"%(new_customers_needed))

percentage_point_increase = 100.0 * new_customers_needed / total_visitor_count
print ("Percent point increase: %s"%(percentage_point_increase))

minimum_detectable_effect = percentage_point_increase / baseline_percent * 100.0
print ("Minimum detectable effect:%.2f"%(minimum_detectable_effect))

ab_sample_size = 290
print ("According to the sample size calulcator, the sample size should be %d people."%(ab_sample_size))