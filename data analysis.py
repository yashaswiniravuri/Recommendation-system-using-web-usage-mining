import pandas as pd

# load the data
data = pd.read_csv('web_usage_data.csv')

# get the total number of unique users
unique_users = len(data['user_id'].unique())
print(f'Total number of unique users: {unique_users}')

# get the total number of unique products
unique_products = len(data['product_id'].unique())
print(f'Total number of unique products: {unique_products}')

# get the total number of actions (views, adds to cart, purchases)
total_actions = len(data)
print(f'Total number of actions: {total_actions}')

# calculate the average rating per action
average_rating = data['rating'].mean()
print(f'Average rating per action: {average_rating}')

# calculate the average number of products viewed per user
average_products_viewed = data[data['action'] == 'view'].groupby('user_id')['product_id'].nunique().mean()
print(f'Average number of products viewed per user: {average_products_viewed}')

# calculate the average number of products added to cart per user
average_products_added_to_cart = data[data['action'] == 'add to cart'].groupby('user_id')['product_id'].nunique().mean()
print(f'Average number of products added to cart per user: {average_products_added_to_cart}')

# calculate the average number of products purchased per user
average_products_purchased = data[data['action'] == 'purchase'].groupby('user_id')['product_id'].nunique().mean()
print(f'Average number of products purchased per user: {average_products_purchased}')
