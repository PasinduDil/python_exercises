# Name: [Your Name]
# Student Number: [Your Student Number]

import json

# Function to repeatedly prompt for input until something other than whitespace is entered.
def input_something(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value

# Function to repeatedly prompt for input until a float with a minimum of 0 is entered.
def input_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
        except ValueError:
            pass

# Function to save data to "data.txt" in JSON format.
def save_data(data):
    with open("data.txt", "w") as file:
        json.dump(data, file, indent=4)

# Load or initialize data from "data.txt".
try:
    with open("data.txt", "r") as file:
        data = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    data = []

# Main program loop.
print('Welcome to the Fruit Quiz Admin Program.')
while True:
    print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
    choice = input('> ').lower()

    if choice == 'a':  # Add a new fruit.
        name = input_something("Enter fruit name: ")
        if any(fruit['name'].lower() == name.lower() for fruit in data):
            print("Fruit already exists!")
            continue
        energy = input_float("Enter energy (calories per 100g): ")
        fibre = input_float("Enter dietary fibre (grams per 100g): ")
        sugar = input_float("Enter sugar (grams per 100g): ")
        potassium = input_float("Enter potassium (milligrams per 100g): ")
        data.append({"name": name, "energy": energy, "fibre": fibre, "sugar": sugar, "potassium": potassium})
        save_data(data)
        print("Fruit added!")

    elif choice == 'l':  # List all fruits.
        if not data:
            print("No fruit saved.")
        else:
            for i, fruit in enumerate(data, 1):
                print(f"{i}. {fruit['name']}")

    elif choice == 's':  # Search for fruits.
        if not data:
            print("No fruit saved.")
            continue
        term = input_something("Enter search term: ").lower()
        found = False
        for i, fruit in enumerate(data, 1):
            if term in fruit['name'].lower():
                print(f"{i}. {fruit['name']}")
                found = True
        if not found:
            print("No results found.")

    elif choice == 'v':  # View a fruit's details.
        if not data:
            print("No fruit saved.")
            continue
        index = input("Enter index number: ")
        if not index.isdigit() or int(index) < 1 or int(index) > len(data):
            print("Invalid index number.")
            continue
        fruit = data[int(index) - 1]
        print(f"Name: {fruit['name']}")
        print(f"Energy: {fruit['energy']} calories/100g")
        print(f"Fibre: {fruit['fibre']} grams/100g")
        print(f"Sugar: {fruit['sugar']} grams/100g")
        print(f"Potassium: {fruit['potassium']} milligrams/100g")

    elif choice == 'd':  # Delete a fruit.
        if not data:
            print("No fruit saved.")
            continue
        index = input("Enter index number: ")
        if not index.isdigit() or int(index) < 1 or int(index) > len(data):
            print("Invalid index number.")
            continue
        del data[int(index) - 1]
        save_data(data)
        print("Fruit deleted!")

    elif choice == 'q':  # Quit the program.
        print("Goodbye!")
        break

    else:  # Invalid choice.
        print("Invalid choice.")