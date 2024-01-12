import random

class Simulation:
    def __init__(self, doornum):
        """
        Initialize Simulation object.

        Parameters:
        - doornum: An integer representing the number of doors used in the game.
        """
        self.numdoors = doornum

    def set_random_doors(self):
        """
        Set random doors for the game.

        Returns:
        - List containing doors with one door having a "car" and others having "zonk".
        """
        doors = ["zonk"] * self.numdoors
        car_index = random.randint(0, self.numdoors - 1)
        doors[car_index] = "car"
        return doors

    def choose_doors(self):
        """
        Choose doors for the game.

        Returns:
        - Tuple of contestant door and alternate door.
        """
        doors = self.set_random_doors()
        contestant_door = random.choice(doors)
        doors.remove(contestant_door)
        alternate_door = random.choice(doors)
        return contestant_door, alternate_door

    def play_game(self, switch=False, iterations=1):
        """
        Play the Monty Hall game.

        Parameters:
        - switch: A boolean indicating whether the contestant switches doors (default is False).
        - iterations: An integer representing the number of times the game will be played (default is 1).

        Returns:
        - Win percentage as a decimal (float).
        """
        wins = 0

        for _ in range(iterations):
            contestant_door, alternate_door = self.choose_doors()
            doors = self.set_random_doors()
            
            contestant_index = doors.index(contestant_door)
            # Monty opens a door with a "zonk"
            doors.remove("zonk")

            if switch:
                # If switching, contestant switches to the remaining unopened door
                contestant_door = doors[0]

            if contestant_door == "car":
                wins += 1


        win_percentage = wins / iterations if iterations > 0 else 0.0
        return win_percentage 

if __name__ == "__main__":
    simulation = Simulation(doornum=3)

    switch_win_percentage= simulation.play_game(switch=True, iterations=1000)
    print(switch_win_percentage)
    print(f"Win Percentage (Switching Doors): {switch_win_percentage:.2%}")
    print(f"Lose Percentage (Switching Doors): {(1 - (switch_win_percentage)):.2%}")

    # Not switching doors
    no_switch_win_percentage = simulation.play_game(switch=False, iterations=1000)
    print(f"Win Percentage (Not Switching Doors): {no_switch_win_percentage:.2%}")
    print(f"Lose Percentage (Not Switching Doors): {(1 - (no_switch_win_percentage)):.2%}")
