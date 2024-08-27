# "P1: Klasser" Wilhelm Mornils Flender
import os 

class Car: 
    def __init__(self, make, model, color) :
        self.make = make
        self.model = model
        self.color = color

    def view_cars(self) :
        return f"{self.make} - {self.model} ({self.color})"


def main():
    os.system("cls")

    cars = [] 

    while True:
        print("\n1. Add a car")
        print("2. View cars")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            make = input("Enter the car's make/brand: ")
            model = input("Enter the car's model: ")
            color = input("Enter the car's color: ")

            cars.append(Car(make, model, color))
            print(f"\n{make} - {model} ({color}) added into the garage")

        elif choice == "2":
            if not cars:
                print("\nGarage is empty")
            else:
                print("\nCars currently in garage:")
                for i, car in enumerate(cars, start=1):
                    print(f"{i}. {car.view_cars()}")

        elif choice == "3":
            print("\nExiting")
            break

        else:
            print("\nInvalid")


if __name__ == "__main__":
    main() 
