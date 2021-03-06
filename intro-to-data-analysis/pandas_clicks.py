import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

ad_clicks.groupby('utm_source').user_id.count().reset_index

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()

clicks_pivot = clicks_by_source.pivot(columns = 'is_click', index = 'utm_source', values = 'user_id').reset_index()

clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False]) 

viewers = ad_clicks.groupby('experimental_group').is_click.count()

viewer_percentage = ad_clicks.groupby(['is_click', 'experimental_group'])['user_id'].count().reset_index()

viewer_percentage_pivot = viewer_percentage.pivot(columns = 'is_click', index = 'experimental_group', values = 'user_id').reset_index()

viewer_percentage_pivot['percent_of_clicked'] = viewer_percentage_pivot[True] / (viewer_percentage_pivot[True] + viewer_percentage_pivot[False])

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A'].reset_index()
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B'].reset_index()

a_day = a_clicks.groupby(['is_click', 'day'])['user_id'].count().reset_index()

a_day_pivot = a_day.pivot(columns = 'is_click', index = 'day', values = 'user_id')

b_day = b_clicks.groupby(['is_click', 'day'])['user_id'].count().reset_index()

b_day_pivot = b_day.pivot(columns = 'is_click', index = 'day', values = 'user_id')


a_day_pivot['Percent_of_Users'] = a_day_pivot[True] / (a_day_pivot[True] + a_day_pivot[False])

round_number = lambda x: '{}%'.format(round(x*100,2))

a_day_pivot['Percent_Users_Rounded'] = a_day_pivot.Percent_of_Users.apply(round_number)

b_day_pivot['Percent_of_Users'] = b_day_pivot[True] / (b_day_pivot[True] + b_day_pivot[False])

b_day_pivot['Percent_Users_Rounded'] = b_day_pivot.Percent_of_Users.apply(round_number)

print(a_day_pivot)
print(b_day_pivot)
