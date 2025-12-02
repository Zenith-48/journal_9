from product import product_details
def test_product_details():
   
    expected_output = (
        "Product Name: Laptop\n"
        "Product ID: P456\n"
        "Price: 1200\n"
        "quantity: Electronics\n"
    )
    assert product_details("Laptop","P456","Electronics","1200") == expected_output