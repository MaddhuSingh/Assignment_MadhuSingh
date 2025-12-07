def check_password_strength(password):
    function_valid = True  # assume valid

    if len(password) < 8:
        function_valid = False
    elif not any(char.isdigit() for char in password):
        function_valid = False
    elif not any(char.isupper() for char in password):
        function_valid = False
    elif not any(char.islower() for char in password):
        function_valid = False
    elif not any(char in "!@#$%^&*()-_+=" for char in password):
        function_valid = False

    return function_valid


password = input(str("Enter your password: "))
if check_password_strength(password):
    print("✅ Strong password! All security criteria met.")
else:
    print("❌ Weak password! Make sure it has:")
    print("- At least 8 characters")
    print("- Uppercase and lowercase letters")
    print("- At least one number")
    print("- At least one special character (!, @, #, $, %, etc.)")
