# this code is used as an I. D checker for both the toppings menu and pizza menu. It checks if the user
# has entered any number from 1-10 and it will not accept any other number
def num_check(question, min_value=None, max_value=None):
    while True:
        try:
            response = int(input(question))
            if (min_value is not None and response < min_value) or (max_value is not None and response > max_value):
                print(f"Please enter a number between {min_value} and {max_value}.")
            else:
                return response
        except ValueError:
            print("Please enter an integer.")

#Main Routine

user_order_id = num_check("Please enter the number of the pizza you want to order (1-10): ", min_value=1, max_value=10)