class Robot:
    def __init__(self, robot_id):
        self.robot_id = robot_id
        self.position = (0, 0)  # Starting at the top-left corner of the grid

    def move(self, command, occupied_positions):
        direction = command[0]
        steps = int(command[1:])
        x, y = self.position

        if direction == 'N':  # Move north (up)
            for _ in range(steps):
                if (x - 1, y) in occupied_positions:
                    break
                x = max(0, x - 1)
        elif direction == 'E':  # Move east (right)
            for _ in range(steps):
                if (x, y + 1) in occupied_positions:
                    break
                y += 1
        elif direction == 'S':  # Move south (down)
            for _ in range(steps):
                if (x + 1, y) in occupied_positions:
                    break
                x += 1
        elif direction == 'W':  # Move west (left)
            for _ in range(steps):
                if (x, y - 1) in occupied_positions:
                    break
                y = max(0, y - 1)

        self.position = (x, y)
        print(f"Robot {self.robot_id} moved to {self.position}.")

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
            command = input("Enter the movement command (e.g., N4, E3): ").upper()
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
