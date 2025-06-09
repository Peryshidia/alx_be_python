def display_menu():
    """Display the main menu options."""
    print("\n=== Shopping List Manager ===")
    print("1. Add item to list")
    print("2. Remove item from list")
    print("3. View shopping list")
    print("4. Exit")
    print("===========================")

def add_item(shopping_list: list) -> None:
    """Add an item to the shopping list."""
    item = input("Enter the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"'{item}' has been added to your shopping list.")
    else:
        print("Item name cannot be empty.")

def remove_item(shopping_list: list) -> None:
    """Remove an item from the shopping list."""
    if not shopping_list:
        print("Your shopping list is empty.")
        return
    
    item = input("Enter the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from your shopping list.")
    else:
        print(f"'{item}' was not found in your shopping list.")

def view_list(shopping_list: list) -> None:
    """Display all items in the shopping list."""
    if not shopping_list:
        print("Your shopping list is empty.")
        return
    
    print("\nYour Shopping List:")
    for index, item in enumerate(shopping_list, 1):
        print(f"{index}. {item}")

def main():
    """Main function to run the shopping list manager."""
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        match choice:
            case "1":
                add_item(shopping_list)
            case "2":
                remove_item(shopping_list)
            case "3":
                view_list(shopping_list)
            case "4":
                print("Thank you for using Shopping List Manager. Goodbye!")
                break
            case _:
                print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()