import random
import csv

# Define the number of users and products
num_users = 100
num_products = 15

# Define the rating range
min_rating = 1
max_rating = 5

# Generate user behavior data
user_behavior = []
for user_id in range(1, num_users + 1):
    for product_id in range(1, num_products + 1):
        rating = random.randint(min_rating, max_rating)
        user_behavior.append([user_id, product_id, rating])

# Save user behavior data to a CSV file
with open('user_behavior.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['user_id', 'product_id', 'rating'])
    writer.writerows(user_behavior)
