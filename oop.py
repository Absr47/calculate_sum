# --- Assignment 1: Design Your Own Class & Inheritance ---
# This is the base class. All other vehicle types will inherit from this class.
# It defines common attributes and methods for all vehicles.
class Vehicle:
    """
    A base class to represent a generic vehicle.
    """
    def __init__(self, make, model, year):
        """
        The constructor method, used to initialize a new Vehicle object.
        It sets the initial state (attributes) of the object.
        'self' refers to the specific instance of the class being created.
        """
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0  # Initial speed is always 0

    def display_info(self):
        """
        A method to print the basic information about the vehicle.
        """
        print(f"Vehicle: {self.year} {self.make} {self.model}")

    # This is a general method that will be overridden in the child classes.
    # It sets the stage for our polymorphism example.
    def move(self):
        """
        A generic method for movement.
        """
        print("This vehicle is moving.")

# --- Child Classes with Inheritance and Unique Methods ---
# 'Car' is a child class that inherits from the 'Vehicle' parent class.
# It automatically gets all the attributes and methods from 'Vehicle'.
class Car(Vehicle):
    """
    A class to represent a car, inheriting from Vehicle.
    """
    def __init__(self, make, model, year, num_doors):
        """
        The constructor for a Car.
        'super().__init__()' calls the constructor of the parent class (Vehicle)
        to handle the common attributes.
        """
        super().__init__(make, model, year)
        self.num_doors = num_doors

    # --- Activity 2: Polymorphism Challenge ---
    # This method overrides the generic 'move' method from the parent class.
    # When we call 'move()' on a Car object, this specific version will run.
    def move(self):
        """
        Overrides the move() method to represent a car's movement.
        """
        print(f"{self.make} {self.model} is driving 🚗")

# 'Plane' is another child class, also inheriting from 'Vehicle'.
class Plane(Vehicle):
    """
    A class to represent a plane, inheriting from Vehicle.
    """
    def __init__(self, make, model, year, max_altitude):
        super().__init__(make, model, year)
        self.max_altitude = max_altitude
    
    # This also overrides the move() method, providing a unique behavior.
    def move(self):
        """
        Overrides the move() method to represent a plane's movement.
        """
        print(f"{self.make} {self.model} is flying ✈️")

# 'Boat' is another child class, demonstrating the flexibility of polymorphism.
class Boat(Vehicle):
    """
    A class to represent a boat, inheriting from Vehicle.
    """
    def __init__(self, make, model, year, vessel_type):
        super().__init__(make, model, year)
        self.vessel_type = vessel_type

    def move(self):
        """
        Overrides the move() method to represent a boat's movement.
        """
        print(f"{self.make} {self.model} is sailing 🚢")

# --- Main Program Logic ---
if __name__ == "__main__":
    # Create instances of each class with unique values
    my_car = Car(make="Tesla", model="Model 3", year=2023, num_doors=4)
    my_plane = Plane(make="Boeing", model="747", year=2015, max_altitude=45000)
    my_boat = Boat(make="Catalina", model="320", year=2008, vessel_type="Sailboat")

    print("--- Demonstrating Inheritance and Methods ---")
    my_car.display_info()
    my_plane.display_info()
    my_boat.display_info()
    print("-" * 40)

    # Put the different objects into a list
    vehicles = [my_car, my_plane, my_boat]

    print("--- Demonstrating Polymorphism ---")
    # Loop through the list and call the 'move' method on each object.
    # The same method call (vehicle.move()) behaves differently
    # depending on the type of object it is called on.
    for vehicle in vehicles:
        vehicle.move()
