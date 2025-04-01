import datetime

class Table:
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity
        self.is_reserved = False
        self.reservation_time = None
        self.customer_name = None

    def reserve(self, customer_name, reservation_time):
        if not self.is_reserved:
            self.is_reserved = True
            self.reservation_time = reservation_time
            self.customer_name = customer_name
            return True
        else:
            return False

    def cancel_reservation(self):
        if self.is_reserved:
            self.is_reserved = False
            self.reservation_time = None
            self.customer_name = None
            return True
        else:
            return False

    def __str__(self):
         if self.is_reserved:
             return f"Table {self.table_number} (Capacity: {self.capacity}) - Reserved by {self.customer_name} at {self.reservation_time}"
         else:
             return f"Table {self.table_number} (Capacity: {self.capacity}) - Available"


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.tables = []

    def add_table(self, table):
        self.tables.append(table)

    def display_tables(self):
        for table in self.tables:
            print(table)

    def find_available_table(self, required_capacity, reservation_time):
        available_tables = []
        for table in self.tables:
            if not table.is_reserved and table.capacity >= required_capacity:
                available_tables.append(table)

        if not available_tables:
            return None

        #Simple first available. more complex algorithms could be implemented.
        return available_tables[0]

    def make_reservation(self, customer_name, required_capacity, reservation_time):
        available_table = self.find_available_table(required_capacity, reservation_time)
        if available_table:
            if available_table.reserve(customer_name, reservation_time):
                print(f"Reservation successful for {customer_name} at Table {available_table.table_number} at {reservation_time}")
                return True
            else:
                print("Table already reserved.")
                return False

        else:
            print("No available tables matching the criteria.")
            return False

    def cancel_reservation(self, table_number):
        for table in self.tables:
            if table.table_number == table_number:
                if table.cancel_reservation():
                    print(f"Reservation for Table {table_number} cancelled.")
                    return True
                else:
                    print(f"Table {table_number} was not reserved.")
                    return False
        print(f"Table {table_number} not found.")
        return False



# Example usage:
restaurant = Restaurant("My Restaurant")
restaurant.add_table(Table(1, 2))
restaurant.add_table(Table(2, 4))
restaurant.add_table(Table(3, 6))

while True:
    print("\nRestaurant Table Reservation System")
    print("1. Display Tables")
    print("2. Make Reservation")
    print("3. Cancel Reservation")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        restaurant.display_tables()
    elif choice == "2":
        try:
            name = input("Enter customer name: ")
            capacity = int(input("Enter required capacity: "))
            time_str = input("Enter reservation time (YYYY-MM-DD HH:MM): ")
            reservation_time = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M")
            restaurant.make_reservation(name, capacity, reservation_time)
        except ValueError:
            print("Invalid input format.")

    elif choice == "3":
        try:
            table_num = int(input("Enter table number to cancel: "))
            restaurant.cancel_reservation(table_num)
        except ValueError:
            print("Invalid table number format.")
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")

print("Exiting...")