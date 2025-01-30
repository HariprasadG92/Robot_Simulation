class Robot:
    def __init__(self, robot_id):
        self.robot_id = robot_id
        self.position = (0, 0)  # Starting at the top-left corner of the grid

    def move(self, command, occupied_positions):
        x, y = self.position
        moves = {
            "L1": (-2, -1), "L2": (-2, 1), "L3": (-1, -2), "L4": (-1, 2),
            "L5": (1, -2), "L6": (1, 2), "L7": (2, -1), "L8": (2, 1)
        }

        if command in moves:
            dx, dy = moves[command]
            new_x, new_y = x + dx, y + dy

            if (new_x, new_y) not in occupied_positions and new_x >= 0 and new_y >= 0:
                self.position = (new_x, new_y)
                print(f"Robot {self.robot_id} moved to {self.position}.")
            else:
                print(f"Move blocked. Robot {self.robot_id} remains at {self.position}.")
        else:
            print("Invalid move command.")

class RobotManager:
    def __init__(self):
        self.robots = {}

    def add_robot(self, robot_id):
        if robot_id in self.robots:
            print(f"Robot with ID {robot_id} already exists.")
        else:
            self.robots[robot_id] = Robot(robot_id)
            print(f"Robot with ID {robot_id} added.")

    def move_robot(self, robot_id, command):
        if robot_id not in self.robots:
            print(f"Robot with ID {robot_id} does not exist.")
        else:
            occupied_positions = {robot.position for robot in self.robots.values() if robot.robot_id != robot_id}
            self.robots[robot_id].move(command, occupied_positions)

    def display_robots(self):
        if not self.robots:
            print("No robots available.")
        else:
            print("Current robots:")
            for robot_id, robot in self.robots.items():
                print(f"Robot ID: {robot_id}, Position: {robot.position}")

    def display_robot_position(self, robot_id):
        if robot_id not in self.robots:
            print(f"Robot with ID {robot_id} does not exist.")
        else:
            position = self.robots[robot_id].position
            print(f"Robot {robot_id} is at position {position}.")

# Main program
def main():
    robot_manager = RobotManager()
    while True:
        print("\nOptions:")
        print("1. Add a new robot")
        print("2. Move a robot")
        print("3. Display all robots")
        print("4. Display a robot's position")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            robot_id = input("Enter a unique robot ID: ")
            robot_manager.add_robot(robot_id)
        elif choice == '2':
            robot_id = input("Enter the robot ID to move: ")
            command = input("Enter the movement command (L1-L8 for horse moves): ").upper()
            robot_manager.move_robot(robot_id, command)
        elif choice == '3':
            robot_manager.display_robots()
        elif choice == '4':
            robot_id = input("Enter the robot ID: ")
            robot_manager.display_robot_position(robot_id)
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
