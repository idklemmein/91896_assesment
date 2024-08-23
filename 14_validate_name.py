# function to validate users name (no digits allowed)
def validate_name(question):
    while True:
        response = input(question).strip()
        if response == "":
            print("Sorry, this field cannot be blank")
        elif all(letters.isalpha() or letters.isspace() for letters in response):
            return response
        else:
            print("Invalid input. Please enter letters only.")

# Test
if __name__ == "__main__":
    name = validate_name("Please enter your name: ")
    print(f"Name entered: {name}")