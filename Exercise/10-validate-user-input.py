# validate user inpout exercise
# 1. usernami is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

print("Username mustn't contain spaces and digits.")
print("Max length is 12 characters.")
username = str(input("Enter username: "))

if len(username) > 12:
    print("Your username contains too many characters.")
elif not username.isalpha():
    print("Username mustn't contain digits and spaces.")
else:
    print("Account has been created.")