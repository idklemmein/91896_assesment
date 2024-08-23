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
    response = string_checker("Do you want to continue? (y/n): ", ["yes", "no"])
    print(f"You selected: {response}")
