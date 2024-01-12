#Srinickethan Ramamoorthy - Navigator
#Eyosiyas Girma - Driver

import math

class Car:
    def __init__(self, x=0.0, y=0.0, heading=0.0):
        self.x = x
        self.y = y
        self.heading = heading % 360.0  # Ensure heading is between 0 and 360 degrees

    def turn(self, degrees):
        # Add the specified degrees and keep heading within 0 to 360 degrees
        self.heading = (self.heading + degrees) % 360.0

    def drive(self, distance):
        # Convert heading to radians
        radians = math.radians(self.heading)
        
        # Update x and y based on the given distance and heading
        self.x += distance * math.sin(radians)
        self.y -= distance * math.cos(radians)

def sanity_check():
    # Create an instance of the Car class
    my_car = Car()
    
    # Perform the specified operations
    my_car.turn(90)
    my_car.drive(10)
    my_car.turn(30)
    my_car.drive(20)
    
    # Print the final position and heading
    print(f"Final Position: ({my_car.x}, {my_car.y})")
    print(f"Final Heading: {my_car.heading} degrees")
    return my_car

# Run the sanity check
if __name__ == "__main__":
    sanity_check()  