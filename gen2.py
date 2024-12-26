def blank():
    pass  # Removed the for loop to avoid unnecessary output

# Define variables
num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

# Get password from the user
pwd = input("Enter pwd (only num): ")

# Validate password
if not pwd.isdigit():
    print("\nInvalid input. Please enter only numeric characters.")
    exit()

# Initialize sample array with the same length as the password
smp = ["0"] * len(pwd)

# Brute force hack
for i in range(len(pwd)):
    for digit in num:
        smp[i] = digit
        print(smp)
        if smp[i] == pwd[i]:
            break

print("The password was:", "".join(smp))