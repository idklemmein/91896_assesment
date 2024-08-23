
# function to diffrenciate cash and credit, credit adds a 5% surcharge whilst cash has no surcharge
def process_payment(total_price):
    print(f"Your total is ${total_price:.2f}.")
    payment_method = string_checker("Would you like to pay by cash or credit? ", ["cash", "credit"])
    if payment_method == "cash":
        print("Please have your cash ready upon delivery or pickup.")
    else:
        # 5% surcharge added if credit is selected
        surcharge = total_price * 0.05
        print(f"There is a 5% surcharge which is ${surcharge:.2f}, The total price is: ${total_price + surcharge:.2f}")
        print("Please swipe your card when the delivery arrives or at the counter upon pickup.")


# # Checks that user has a valid response (e.g. yes/no, cash/credit) based on the list of options.
def string_checker(question, valid_ans):
    while True:
        error = f"Enter a valid response from {valid_ans}"
        user_response = input(question).lower()
        if user_response in valid_ans or user_response in [item[0] for item in valid_ans]:
            return valid_ans[[item[0] for item in valid_ans].index(user_response)] if user_response in [item[0] for item in valid_ans] else user_response
        print(error)
# Test
if __name__ == "__main__":
    process_payment(50) # example total price