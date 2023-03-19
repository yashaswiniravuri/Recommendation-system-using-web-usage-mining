import csv

# Define the number of products
num_products = 15

# Generate product data
products = []
for product_id in range(1, num_products + 1):
    product_name = f"Product {product_id}"
    product_category = f"Category {product_id % 3}"
    products.append([product_id, product_name, product_category])

# Save product data to a CSV file
with open('products.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['product_id', 'product_name', 'product_category'])
    writer.writerows(products)
