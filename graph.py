import matplotlib.pyplot as plt


sales_data = {
    'Product A': 150,
    'Product B': 200,
    'Product C': 80,
    'Product D': 120,
}


products = list(sales_data.keys())
sales = list(sales_data.values())

# Create a bar chart
plt.bar(products, sales, color='blue')


plt.title("Sales Summary")
plt.xlabel("Products")
plt.ylabel("Number of Units Sold")


plt.show()
