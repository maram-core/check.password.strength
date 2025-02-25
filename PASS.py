import re  # This imports the 're' module, which helps with searching for patterns in the text

def check_password_strength(password):
    # Checking different password rules
    
    # The password should be at least 8 characters long
    length_error = len(password) < 8 
    
    # The password should have at least one lowercase letter
    lowercase_error = not re.search(r"[a-z]", password)
    
    # The password should have at least one uppercase letter
    uppercase_error = not re.search(r"[A-Z]", password)
    
    # The password should have at least one number
    digit_error = not re.search(r"\d", password)
    
    # The password should have at least one special character (like !, @, #, etc.)
    special_char_error = not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
    
    # Let's put all the errors into a list so we can check them
    errors = [length_error, lowercase_error, uppercase_error, digit_error, special_char_error]
    
    # Now, let's check how many rules the password is breaking
    if all(errors):  # If all conditions are True, it means the password is really weak
        return " Very Weak: Password must contain uppercase, lowercase letters, numbers, and special characters!"
    elif sum(errors) >= 3:  # If 3 or more rules are broken, it's weak
        return " Weak: Try adding a mix of characters to improve security."
    elif sum(errors) == 2:  # If 2 rules are broken, it's medium
        return " Medium: Add more complexity for better security."
    else:  # If less than 2 rules are broken, it's strong
        return "✅ Strong: Your password is secure!"

# Ask the user to enter their password
password = input(" Enter your password: ")

# Print the result based on the password entered
print(check_password_strength(password))
