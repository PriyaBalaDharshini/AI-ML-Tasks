import json

file_path = "inventory.json"

# Task 1 — Read the inventory
with open(file_path, "r") as file:
    inventory = json.load(file)

print(f"Total number of books: {len(inventory)}")

# Task 2 — Update and save
new_book = {
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": 14.99,
    "in_stock": True,
}

inventory.append(new_book)

with open(file_path, "w") as file:
    json.dump(inventory, file)

# Task 3 — Display the inventory
with open(file_path, "r") as file:
    updated_inventory = json.load(file)

for book in updated_inventory:
    print(
        f"Title: {book['title']} | Author: {book['author']} | Price: ${book['price']}"
    )
