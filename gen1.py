def blank():
    pass  # Removed the for loop to avoid unnecessary output

# Define variables
num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
pwd = ""
smp = ["0", "0", "0", "0", "0"]

# Get password from the user
pwd = input("Enter pwd (only num, 5 char): ")

# Validate password
if len(pwd) != 5 or not pwd.isdigit():
    print("\nInvalid input. Please enter exactly 5 numeric characters.")
    exit()

# Brute force hack
for i in range(5):
    for digit in num:
        smp[i] = digit
        print(smp)
        if smp[i] == pwd[i]:
            break

print("The password was:", "".join(smp))