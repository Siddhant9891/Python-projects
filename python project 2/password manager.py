import random
import string

passwords = {}

# Loading existing password file
try:
    with open("passwords.txt", "r") as file:
        for line in file:
            website, pwd = line.strip().split(":")
            passwords[website] = pwd
except:
    pass


def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%&"
    password = "".join(random.choice(chars) for _ in range(8))  # Fix 1: `_in` → `_ in`
    return password


while True:
    print("\n-------Personal Password Manager-------")  # Fix 4: `n--` → `\n--`
    print("1. Save password")
    print("2. View passwords")
    print("3. Generate password")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        site = input("Enter website: ")
        pwd = input("Enter password: ")

        passwords[site] = pwd  # Fix 2: `password` → `passwords`

        with open("password.txt", "a") as file:
            file.write(f"{site}:{pwd}\n")

        print("Saved!")

    elif choice == "2":
        if not passwords:
            print("No data")
        else:                                         # Fix 5: dedented to align with `if`
            for site, pwd in passwords.items():      # Fix 3: `.item()` → `.items()`
                print(site, ":", pwd)

    elif choice == "3":
        print("Generated password:", generate_password())

    elif choice == "4":
        print("Ok bye")                              # Fix 6: moved inside the elif block
        break

    else:
        print("Invalid input")