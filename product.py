import pytest
def product_details(name, product_id, category, price):
    result = (
        f"Product Name: {name}\n"
        f"Product ID: {product_id}\n"
        f"Price: {price}\n"
        f"quantity: {category}\n"
    )
    return result
if __name__ == "__main__":
    name = "Laptop"
    product_id = "P456"
    category = "Electronics"
    price = 1200
    print(product_details(name, product_id, category, price))