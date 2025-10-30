def mystery(n: int = 3) -> str:
    if n > 0:
        result = input("Enter something: ")  # ask for input
        if result:
            return result                    # return the input if not empty
        return mystery(n - 1)                # try again (recursion)
    return ''                                # return empty string if all tries fail


# Example usage
user_input = mystery()
if user_input:
    print(f"You entered: {user_input}")
else:
    print("No input given after 3 tries.")
