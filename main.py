class Automobile:
    def __init__(self, make, model, color, year, mileage):
        self.__make = make
        self.__model = model
        self.__color = color
        self.__year = year
        self.__mileage = mileage

    def add_vehicle(self, inventory):
        inventory.append(self)

    @staticmethod
    def remove_vehicle(inventory, make, model, year):
        for i, car in enumerate(inventory):
            if car.__make == make and car.__model == model and car.__year == year:
                del inventory[i]
                print(f"Vehicle {make} {model} {year} removed from inventory.")
                return
        print("Vehicle not found in inventory.")

    def update_vehicle(self, **kwargs):
        for key, value in kwargs.items():
            if key == 'make':
                self.__make = value
            elif key == 'model':
                self.__model = value
            elif key == 'color':
                self.__color = value
            elif key == 'year':
                self.__year = int(value)
            elif key == 'mileage':
                self.__mileage = int(value)

    def __str__(self):
        return f"{self.__year} {self.__make} {self.__model} - {self.__color}, {self.__mileage} miles"

    @staticmethod
    def save_inventory(inventory):
        with open('vehicle_inventory.txt', 'w') as file:
            for car in inventory:
                file.write(str(car) + '\n')
        print("Inventory saved to file.")

    @staticmethod
    def load_inventory():
        inventory = []
        try:
            with open('vehicle_inventory.txt', 'r') as file:
                for line in file:
                    if line.strip() == "":
                        continue
                    parts = line.strip().split(' - ')
                    if len(parts) == 2:
                        year_make_model, color_mileage = parts
                        year, make, model = year_make_model.split()[:3]
                        color, mileage_str = color_mileage.split(', ')
                        mileage = int(mileage_str.replace('miles', '').strip())
                        car = Automobile(make, model, color, int(year), mileage)
                        inventory.append(car)
                    else:
                        print(f"Line format is incorrect: {line}")
        except FileNotFoundError:
            print("No existing inventory file found. Starting with an empty inventory.")
        return inventory

    @staticmethod
    def list_inventory(inventory):
        if not inventory:
            print("No vehicles in the inventory.")
        else:
            for car in inventory:
                print(car)


def main():
    inventory = Automobile.load_inventory()

    while True:
        print("\nCar Inventory Management System")
        print("1. Add a new vehicle")
        print("2. Remove a vehicle")
        print("3. Update vehicle attributes")
        print("4. List all vehicles")
        print("5. Save inventory to file")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            make = input("Enter the make of the vehicle: ")
            model = input("Enter the model of the vehicle: ")
            color = input("Enter the color of the vehicle: ")
            year = int(input("Enter the year of the vehicle: "))
            mileage = int(input("Enter the mileage of the vehicle: "))
            car = Automobile(make, model, color, year, mileage)
            car.add_vehicle(inventory)
            print("Vehicle added to inventory.")

        elif choice == '2':
            make = input("Enter the make of the vehicle to remove: ")
            model = input("Enter the model of the vehicle to remove: ")
            year = int(input("Enter the year of the vehicle to remove: "))
            Automobile.remove_vehicle(inventory, make, model, year)

        elif choice == '3':
            index = int(input("Enter the index of the vehicle to update (starting from 0): "))
            if 0 <= index < len(inventory):
                car = inventory[index]
                print("Enter new values (leave blank to keep current value):")
                make = input("New make: ") or car._Automobile__make
                model = input("New model: ") or car._Automobile__model
                color = input("New color: ") or car._Automobile__color
                year = input("New year: ") or car._Automobile__year
                mileage = input("New mileage: ") or car._Automobile__mileage
                car.update_vehicle(make=make, model=model, color=color, year=year, mileage=mileage)
                print("Vehicle updated.")
            else:
                print("Invalid index selected.")

        elif choice == '4':
            Automobile.list_inventory(inventory)

        elif choice == '5':
            Automobile.save_inventory(inventory)

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == '__main__':
    main()
