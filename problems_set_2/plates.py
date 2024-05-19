def has_minimum_length(s):
    """
    Check if the string meets the minimum length requirement.
    """
    return len(s) >= 2

def has_maximum_length(s):
    """
    Check if the string meets the maximum length requirement.
    """
    return len(s) <= 6

def has_no_internal_numbers(s):
    """
    Check if the string has numbers only at the end.
    """
    return s[-1].isalpha() or s[-1] == '0'

def has_no_punctuation(s):
    """
    Check if the string has no periods, spaces, or punctuation marks.
    """
    return all(char.isalnum() for char in s)

def is_valid(s):
    """
    Check if the vanity plate meets all requirements.
    """
    return (
        has_minimum_length(s) and
        has_maximum_length(s) and
        has_no_internal_numbers(s) and
        has_no_punctuation(s)
    )

def main():
    """
    Main function to prompt the user for a vanity plate and output Valid or Invalid.
    """
    user_input = input("Enter a vanity plate: ")
    
    if is_valid(user_input):
        print("Valid")
    else:
        print("Invalid")

# Call the main function when the script is executed.
if __name__ == "__main__":
    main()
