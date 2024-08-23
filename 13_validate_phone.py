# function to validate users phone number (max 14 digits)
def validate_phone(question):
    while True:
        response = input(question).strip()
        if response.isdigit() and len(response) <= 14:
            return response
        else:
            print("Invalid input. Please enter digits only, with a maximum of 14 digits.")

# Test
if __name__ == "__main__":
    phone = validate_phone("Please enter your phone number (max 14 digits): ")
    print(f"Phone number entered: {phone}")