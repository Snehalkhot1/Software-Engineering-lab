
# Experiment 9: Software Engineering Tools and Technologies
# Email and Password Login System using Python

# Fixed login credentials
correct_email = "student@gmail.com"
correct_password = "12345"

print("===================================")
print("       EMAIL AND PASSWORD LOGIN")
print("===================================")

# Accept input from the user
email = input("Enter Email: ")
password = input("Enter Password: ")

# Validate the entered credentials
if email == correct_email and password == correct_password:
    print("\nLogin Successful!")
    print("Welcome to the system.")
else:
    print("\nLogin Failed!")
    print("Invalid email or password.")

print("===================================")
