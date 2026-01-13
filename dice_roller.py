import random

print("🎲 Dice Roller")

while True:
    dice = random.randint(1, 6)
    print(f"\nYou rolled: {dice}")

    again = input("Roll again? (y/n): ").lower()
    if again != "y":
        print("👋 Done!")
        break