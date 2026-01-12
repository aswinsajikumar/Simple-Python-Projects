import random
import string

print("🔐 Password Generator")

while True:
    length = int(input("\nEnter password length: "))

    print("Choose what to include:")
    print("1 - Letters")
    print("2 - Letters + Numbers")
    print("3 - Letters + Numbers + Symbols")

    choice = input("Enter option (1/2/3): ")

    if choice == "1":
        chars = string.ascii_letters
    elif choice == "2":
        chars = string.ascii_letters + string.digits
    elif choice == "3":
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
    else:
        print("Invalid choice")
        continue

    password = "".join(random.choice(chars) for _ in range(length))

    print("\nYour password is:")
    print(password)

    again = input("\nIs this enough? Generate another? (y/n): ").lower()
    if again != "y":
        print("👋 Done. Stay secure!")
        break
