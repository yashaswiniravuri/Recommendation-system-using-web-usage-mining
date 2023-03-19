import pandas as pd
import random
import datetime
import random
import csv
# Define the start and end timestamps
start = datetime.datetime(2022, 2, 12, 0, 0, 0)
end = datetime.datetime(2022, 2, 12, 20, 0, 0)
# Define the list of user IDs and product IDs
user_ids = list(range(1, 101))
product_ids = list(range(1, 51))
# Generate the web usage data
data = []
while start < end:
    timestamp = start
    user_id = random.choice(user_ids)
    product_id = random.choice(product_ids)
    action = random.choice(['view', 'add to cart', 'purchase'])
    data.append((timestamp, user_id, product_id, action))
    start += datetime.timedelta(minutes=random.randint(1, 5))
# Save the web usage data to a CSV file
df = pd.DataFrame(data, columns=['Timestamp', 'User ID', 'Product ID', 'Action'])
df.to_csv('web_usage_data.csv', index=False)
dat=pd.read_csv('web_usage_data.csv')
print(dat)