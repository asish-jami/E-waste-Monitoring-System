import datetime

class E_WasteItem:
    def __init__(self, name, organization, purchase_date, condition):
        self.name = name
        self.organization = organization
        self.purchase_date = purchase_date
        self.condition = condition

    def __str__(self):
        return f"{self.name} (from {self.organization}) - Condition: {self.condition}"

# Collect E-waste data
e_waste_items = []

def collect_data():
    name = input("Enter electronic item name: ")
    organization = input("Enter organization: ")
    purchase_date = input("Enter purchase date (YYYY-MM-DD): ")
    condition = input("Enter item condition (Recycle/Dispose/Replace): ")
    
    # Convert purchase date to a datetime object
    try:
        purchase_date = datetime.datetime.strptime(purchase_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please enter date in YYYY-MM-DD format.")
        return
    
    # Create a new E-waste item and add it to the list
    item = E_WasteItem(name, organization, purchase_date, condition)
    e_waste_items.append(item)

def print_summary():
    recycle_count = 0
    dispose_count = 0
    replace_count = 0

    # Count items based on their condition
    for item in e_waste_items:
        if item.condition.lower() == 'recycle':
            recycle_count += 1
        elif item.condition.lower() == 'dispose':
            dispose_count += 1
        elif item.condition.lower() == 'replace':
            replace_count += 1

    # Print the summary of the results
    print("\nE-Waste Monitoring Summary:")
    print(f"Total items to recycle: {recycle_count}")
    print(f"Total items to dispose: {dispose_count}")
    print(f"Total items to replace: {replace_count}")

def main():
    while True:
        # Collect E-waste data from the user
        collect_data()
        # Ask if the user wants to add more items
        choice = input("Do you want to enter more items? (yes/no): ").strip().lower()
        if choice == 'no':
            break
    
    # Print a summary of the entered data
    print_summary()

if __name__ == "__main__":
    main()
