# create funcs
def blank():
    for i in range(100):
        print()

# define vars
num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
pwd = ""
smp = ["0", "0", "0", "0", "0"]

# get pwd
pwd = str(input("Enter pwd (only num, 5 char): "))

# check pwd
if len(pwd) != 5:
    print("\n5 char only")
    exit()

# hack!
for i in range(5):
    for digit in num:
        smp[i] = digit
        blank()
        print(smp)
        if smp[i] == pwd[i]:
            break

print("The password was: ", end="")
print("".join(smp))
