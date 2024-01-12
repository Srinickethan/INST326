
"""Create routes between cities on a Map"""
import sys
import argparse


# Define the City class
class City:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}

    def __repr__(self):
        return self.name

    def add_neighbor(self, neighbor, distance, interstate):
        self.neighbors[neighbor] = (distance, interstate)

# Define the Map class
class Map:
    def __init__(self, connections):
        self.cities = []
        for city, city_data in connections.items():
            city_obj = City(city)
            self.cities.append(city_obj)

            for neighbor, distance, interstate in city_data:
                neighbor_city = next((c for c in self.cities if c.name == neighbor), None)
                if neighbor_city is None:
                    neighbor_city = City(neighbor)
                    self.cities.append(neighbor_city)
                city_obj.add_neighbor(neighbor_city, distance, interstate)

    def __repr__(self):
        city_list = [city.name for city in self.cities]
        return f"Map with cities: {', '.join(city_list)}"
    
# Add the bfs function to the Map class
def bfs(start, goal):
    # Create a list to keep track of explored nodes 
    explored = []
    # Create a queue with the starting node
    queue = [[start]]

# Check if the starting node is the goal node itself
    if start == goal:
        return [start]

    while queue:
        path = queue.pop(0) # Get the first path from the queue
        node = path[-1] # Get the last path from the queue

        if node not in explored:
            neighbors = node.neighbors # Get the neighbours of the current node
            for neighbor, (unused_distance, unused_interstate) in neighbors.items(): #Loop through the neighbours
                new_path = list(path) # Creating new path by extending the current path
                new_path.append(neighbor)

                queue.append(new_path) # Add the new path to the queue

                if neighbor == goal: # Checking if neighbour is the goal
                    return [str(city) for city in new_path]

            explored.append(node) # Mark the current node as explored

        # Print the current state of the search
    print("Current search state:")
    print("Explored:", [str(city) for city in explored])
    print("Queue:", [[str(city) for city in path] for path in queue])

    return None
# Attach the bfs method to the Map class
Map.bfs = bfs

# Define the main function
def main(starting_city, destination_city, connections):
    map_obj = Map(connections)
    instructions = map_obj.bfs(starting_city, destination_city)

    if instructions is not None:
        output = ""
        for idx, city in enumerate(instructions):
            if idx == 0:
                output += f"Starting at {city}\n"
            elif idx < len(instructions) - 1:
                next_city = instructions[idx + 1]
                current_city_obj = next((c for c in map_obj.cities if c.name == city), None)
                next_city_distance, next_city_interstate = current_city_obj.neighbors[next_city]
                output += f"Drive {next_city_distance} miles on {next_city_interstate} towards {next_city}, then\n"
            else:
                output += "You will arrive at your destination"
        print(output)
    else:
        print("No path found between the given cities.")

def parse_args(map_obj):
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Shortest Route Finder")
    parser.add_argument("--starting_city", type=str, help="The starting city")
    parser.add_argument("--destination_city", type=str, help="The destination city")
    args = parser.parse_args()

    # Find the City objects for the specified cities
    starting_city_obj = next((city for city in map_obj.cities if city.name == args.starting_city), None)
    destination_city_obj = next((city for city in map_obj.cities if city.name == args.destination_city), None)

    if starting_city_obj is None or destination_city_obj is None:
        print("Invalid starting or destination city.")
        sys.exit(1)

    return starting_city_obj, destination_city_obj


if __name__ == "__main__":
    connections = {
"Baltimore": [("Washington", 39, "95"), ("Philadelphia", 106, "95")],
"Washington": [("Baltimore", 39, "95"), ("Fredericksburg", 53, "95"), ("Bedford", 137, "70")],
"Fredericksburg": [("Washington", 53, "95"), ("Richmond", 60, "95")],
"Richmond": [("Charlottesville", 71, "64"), ("Williamsburg", 51, "64"), ("Durham", 151, "85")],
"Durham": [("Richmond", 151, "85"), ("Raleigh", 29, "40"), ("Greensboro", 54, "40")],
"Raleigh": [("Durham", 29, "40"), ("Wilmington", 129, "40"), ("Richmond", 171, "95")],
"Greensboro": [("Charlotte", 92, "85"), ("Durham", 54, "40"), ("Ashville", 173, "40")],
"Ashville": [("Greensboro", 173, "40"), ("Charlotte", 130, "40"), ("Knoxville", 116, "40"), ("Atlanta", 208, "85")],
"Charlotte": [("Atlanta", 245, "85"), ("Ashville", 130, "40"), ("Greensboro", 92, "85")],
"Jacksonville": [("Atlanta", 346, "75"), ("Tallahassee", 164, "10"), ("Daytona Beach", 86, "95")],
"Daytona Beach": [("Orlando", 56, "4"), ("Miami", 95, "268")],
"Orlando": [("Tampa", 94, "4"), ("Daytona Beach", 56, "4")],
"Tampa": [("Miami", 281, "75"), ("Orlando", 94, "4"), ("Atlanta", 456, "75"), ("Tallahassee", 243, "98")],
"Atlanta": [("Charlotte", 245, "85"), ("Ashville", 208, "85"), ("Chattanooga", 118, "75"), ("Macon", 83, "75"), ("Tampa", 456, "75"), ("Jacksonville", 346, "75"), ("Tallahassee", 273, "27") ],
"Chattanooga": [("Atlanta", 118, "75"), ("Knoxville", 112, "75"), ("Nashville", 134, "24"), ("Birmingham", 148, "59")],
"Knoxville": [("Chattanooga", 112,"75"), ("Lexington", 172, "75"), ("Nashville", 180, "40"), ("Ashville", 116, "40")],
"Nashville": [("Knoxville", 180, "40"), ("Chattanooga", 134, "24"), ("Birmingam", 191, "65"), ("Memphis", 212, "40"), ("Louisville", 176, "65")],
"Louisville": [("Nashville", 176, "65"), ("Cincinnati", 100, "71"), ("Indianapolis", 114, "65"), ("St. Louis", 260, "64"), ("Lexington", 78, "64") ],
"Cincinnati": [("Louisville", 100, "71"), ("Indianapolis,", 112, "74"), ("Columbus", 107, "71"), ("Lexington", 83, "75"), ("Detroit", 263, "75")],
"Columbus": [("Cincinnati", 107, "71"), ("Indianapolis", 176, "70"), ("Cleveland", 143, "71"), ("Pittsburgh", 185, "70")],
"Detroit": [("Cincinnati", 263, "75"), ("Chicago", 283, "94"), ("Mississauga", 218, "401")],
"Cleveland":[("Chicago", 344, "80"), ("Columbus", 143, "71"), ("Youngstown", 75, "80"), ("Buffalo", 194, "90")],
"Youngstown":[("Pittsburgh", 67, "76")],
"Indianapolis": [("Columbus", 175, "70"), ("Cincinnati", 112, "74"), ("St. Louis", 242, "70"), ("Chicago", 183, "65"), ("Louisville", 114, "65"), ("Mississauga", 498, "401")], 
 "Pittsburg": [("Columbus", 185, "70"), ("Youngstown", 67, "76"), ("Philadelphia", 304, "76"), ("New York", 391, "76"), ("Bedford", 107, "76")],
"Bedford": [("Pittsburg", 107, "76")], 
#COMEBACK
"Chicago": [("Indianapolis", 182, "65"), ("St. Louis", 297, "55"), ("Milwaukee", 92, "94"), ("Detroit", 282, "94"), ("Cleveland", 344, "90")],
"New York": [("Philadelphia", 95, "95"), ("Albany", 156, "87"), ("Scranton", 121, "80"), ("Providence,", 95, "181"), ("Pittsburgh", 389, "76")],
"Scranton": [("Syracuse", 130, "81")],
"Philadelphia": [("Washington", 139, "95"), ("Pittsburgh", 305, "76"), ("Baltimore", 101, "95"), ("New York", 95, "95")]
    }
    map_obj = Map(connections)
    starting_city, destination_city = parse_args(map_obj)
    main(starting_city, destination_city, connections)
