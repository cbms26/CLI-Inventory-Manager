# I need to import these modules to work with files
import csv
import os

# This is where I will save my inventory data
inventory_file_name = "inventory.csv"

# I will use a list to store all my inventory items
# Each item will be stored as a dictionary with name, quantity, and price
inventory_items = []

# This function will load the inventory from the file when the program starts
def load_inventory_from_file():
    # I need to make the inventory_items list available to change
    global inventory_items
    
    # First I check if the file exists
    if os.path.exists(inventory_file_name):
        # Open the file and read it
        file = open(inventory_file_name, 'r')
        reader = csv.reader(file)
        
        # Skip the first row because it has headers
        first_row = True
        for row in reader:
            if first_row:
                first_row = False
                continue
            
            # Check if the row has 3 parts (name, quantity, price)
            if len(row) == 3:
                item_name = row[0]
                # Convert quantity to number
                item_quantity = int(row[1])
                # Convert price to decimal number
                item_price = float(row[2])
                
                # Create a dictionary to store this item
                item_dict = {
                    'name': item_name,
                    'quantity': item_quantity,
                    'price': item_price
                }
                
                # Add this item to my list
                inventory_items.append(item_dict)
        
        file.close()
        print("Inventory loaded from file successfully!")
    else:
        print("No previous inventory file found. Starting fresh!")

# This function will save all items to the file
def save_inventory_to_file():
    # Open file for writing
    file = open(inventory_file_name, 'w', newline='')
    writer = csv.writer(file)
    
    # Write the header row first
    writer.writerow(['Name', 'Quantity', 'Price'])
    
    # Write each item to the file
    for item in inventory_items:
        writer.writerow([item['name'], item['quantity'], item['price']])
    
    file.close()
    print("Inventory saved to file successfully!")

# This function adds a new item to the inventory
def add_new_item():
    # I need to make the inventory_items list available to change
    global inventory_items
    
    print("\n--- Adding New Item ---")
    
    # Get item name from user
    item_name = input("Enter item name: ")
    
    # Get quantity from user and keep asking until they give a valid number
    while True:
        quantity_input = input("Enter quantity (whole number): ")
        if quantity_input.isdigit():
            item_quantity = int(quantity_input)
            break
        else:
            print("Please enter a valid whole number for quantity!")
    
    # Get price from user and keep asking until they give a valid number
    while True:
        price_input = input("Enter price (e.g., 12.99): ")
        # I will check if this can be converted to a float
        try:
            item_price = float(price_input)
            break
        except:
            print("Please enter a valid price!")
    
    # Create a dictionary to store this new item
    new_item = {
        'name': item_name,
        'quantity': item_quantity,
        'price': item_price
    }
    
    # Add the new item to my list
    inventory_items.append(new_item)
    print(f"Item '{item_name}' added successfully!")

# This function shows all items in the inventory
def show_all_items():
    # Check if the inventory is empty
    if len(inventory_items) == 0:
        print("\n-- The inventory is currently empty. --")
        return
    
    print("\n--- Current Inventory ---")
    # Go through each item and print it
    for item in inventory_items:
        print(f"Name: {item['name']} | Quantity: {item['quantity']} | Price: ${item['price']:.2f}")
    print("-------------------------")

# This function removes an item from the inventory
def remove_an_item():
    # I need to make the inventory_items list available to change
    global inventory_items
    
    name_to_remove = input("Enter the NAME of the item to remove: ")
    
    # I will create a new list without the item I want to remove
    new_inventory_list = []
    item_was_found = False
    
    # Go through each item in the current list
    for item in inventory_items:
        # Check if this is the item I want to remove
        if item['name'].lower() == name_to_remove.lower():
            item_was_found = True
            # Don't add this item to the new list (this removes it)
        else:
            # Add this item to the new list
            new_inventory_list.append(item)
    
    # Replace the old list with the new list
    inventory_items = new_inventory_list
    
    # Tell the user what happened
    if item_was_found:
        print(f"Item '{name_to_remove}' removed successfully!")
    else:
        print(f"Item '{name_to_remove}' not found in inventory.")

# This function shows the main menu
def show_menu():
    print("\n---------------------------------------")
    print("Welcome to the Simple Inventory Manager!")
    print("---------------------------------------")
    print("1. Add new item")
    print("2. View all items")
    print("3. Remove item")
    print("4. Exit and Save")
    print("---------------------------------------")

# This is the main function that runs the program
def start_program():
    # First, load any existing inventory from file
    load_inventory_from_file()
    
    # Keep the program running until user wants to exit
    program_running = True
    while program_running:
        show_menu()
        
        user_choice = input("Enter your choice: ")
        
        # Check what the user chose
        if user_choice == '1':
            add_new_item()
        elif user_choice == '2':
            show_all_items()
        elif user_choice == '3':
            remove_an_item()
        elif user_choice == '4':
            save_inventory_to_file()
            program_running = False
            print("\nThank you for using the Inventory Manager. Goodbye!")
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")

# This runs the program when I run this file
if __name__ == "__main__":
    start_program()
