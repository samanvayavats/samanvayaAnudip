# 16-validateUsernameAndPassword
username = input("Enter your username: ")
# Validate the username to ensure it is not empty
if not username:
    print("Username cannot be empty.")
    exit()
password = input("Enter your password: ")
# Validate the password to ensure it is not empty
if not password:
    print("Password cannot be empty.")
    exit()
# Validate the username and password
if username == "admin" and password == "password123":
    print("Login successful!")
else:
    print("Invalid username or password. Please try again.")

# output
# Enter your username: admin
# Enter your password: password123
# Login successful!