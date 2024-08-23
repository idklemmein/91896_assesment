# validate name was used as an example to test the not_blank function I have used in my base
def validate_name(question):
    while True:
        response = input(question).strip()
        if response == "":
            print("Sorry, this field cannot be blank") # error message if response = blank
        elif all(letters.isalpha() or letters.isspace() for letters in response): # allows only spcing and letters as a response
            return response
        else:
            print("Invalid input. Please enter letters only.")

# Test
if __name__ == "__main__":
    name = validate_name("Please enter your name: ")
    print(f"Name entered: {name}")
