# function to calculate the order
def calculate_price(prices, delivery_surcharge):
    total_price = sum(prices)
    total_price += delivery_surcharge
    return total_price

# Test
if __name__ == "__main__":
    price_list = [10, 20, 30] # set example of total cost after order
    delivery_surcharge = 5 # surcharge if user picks delivery
    total = calculate_price(price_list, delivery_surcharge)
    print(f"Total price: ${total}")