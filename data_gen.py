from faker import Faker
import pandas as pd

fake = Faker()

# generate user data
user_data = {'user_id': [f'u{i+1}' for i in range(100)]}
users = pd.DataFrame(user_data)

# generate product data
product_data = {'product_id': [f'p{i+1}' for i in range(20)],
                'product_name': [fake.word() for i in range(20)],
                'product_category': [fake.word() for i in range(20)]}
products = pd.DataFrame(product_data)

# generate web usage data
web_data = {'user_id': [fake.random_element(elements=users['user_id']) for i in range(1000)],
            'product_id': [fake.random_element(elements=products['product_id']) for i in range(1000)],
            'category': [fake.word() for i in range(1000)],
            'feature1': [fake.random_int(min=1, max=100) for i in range(1000)],
            'feature2': [fake.random_int(min=1, max=100) / 100 for i in range(1000)],
            'feature3': [fake.word() for i in range(1000)],
            'feature4': [fake.boolean() for i in range(1000)],
            'feature5': [fake.random_int(min=1, max=100) / 1000 for i in range(1000)],
            'action': [fake.random_element(elements=['view', 'add to cart', 'purchase']) for i in range(1000)],
            'count': [fake.random_int(min=1, max=10) for i in range(1000)],
            'rating': [fake.random_int(min=1, max=5) for i in range(1000)]}

web_usage = pd.DataFrame(web_data)

# join web usage data with product data
web_usage = pd.merge(web_usage, products, on='product_id', how='left')

# print the resulting dataset)
web_usage.to_csv('web_usage_data.csv', index=False)
data=pd.read_csv('web_usage_data.csv')
data.head()
