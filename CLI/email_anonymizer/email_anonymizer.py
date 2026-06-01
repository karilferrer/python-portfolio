def anonymize_email(email):
    # 1. Split the email into username and domain parts
    username, domain = email.split("@")
    
    # 2. Get the first character of the username
    first_char = username[0]
    
    # 3. Calculate the number of asterisks needed
    # We subtract 1 because the first character is not masked
    asterisks = "*" * (len(username) - 1)
    
    # 4. Combine everything back together using an f-string
    return f"{first_char}{asterisks}@{domain}"

# --- Test the function ---
input_email = input()
anonymous = anonymize_email(input_email)

print(anonymous)      # Output: a***@domain.org