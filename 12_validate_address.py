# user is asked for address if they pick delivery.
def validate_address(question):
    while True:
        response = input(question).strip()
        if response == "":
            print("Sorry, this field cannot be blank.")
        elif all(char.isalnum() or char.isspace() for char in response):
            return response
        else:
            print("Invalid input. Please enter letters, numbers, and spaces only.")

# Test
if __name__ == "__main__":
    address = validate_address("Please enter your address: ")
    print(f"Address entered: {address}")