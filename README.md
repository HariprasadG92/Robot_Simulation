# Robot Movement Simulation

## Project Overview
This project simulates a system where multiple robots can move within a grid-based terrain. Each robot starts at the top-left corner of the grid and can move in specified directions based on user inputs. The program ensures that no two robots occupy the same cell at any time, and robots stay within the grid boundaries. The project is designed with simplicity and user interaction in mind.

## Problem Statement
The goal of the project is to:
1. **Create multiple robots**, each identified by a unique ID.
2. **Move robots on a grid** based on user-provided commands (e.g., `N4` to move north by 4 steps).
3. **Prevent collisions** by ensuring no two robots occupy the same position.
4. **Display robot positions**, either all at once or individually.

## How the Program Works

### 1. Core Classes
#### a. **Robot Class**
This class represents an individual robot.
- **Attributes:**
  - `robot_id`: A unique identifier for the robot.
  - `position`: The robot's current position on the grid, starting at `(0, 0)`.
- **Methods:**
  - `move(command, occupied_positions)`: Moves the robot based on the input command, ensuring it does not collide with other robots or move out of bounds.

#### b. **RobotManager Class**
This class manages multiple robots.
- **Attributes:**
  - `robots`: A dictionary mapping robot IDs to `Robot` instances.
- **Methods:**
  - `add_robot(robot_id)`: Adds a new robot with a unique ID.
  - `move_robot(robot_id, command)`: Moves the specified robot according to the command.
  - `display_robots()`: Displays all robots and their positions.
  - `display_robot_position(robot_id)`: Displays the position of a specific robot.

### 2. Features
#### a. **Add Robots**
- Users can add robots by providing a unique ID.
- If the ID already exists, the program notifies the user.

#### b. **Move Robots**
- Robots can move in four directions:
  - `N`: North (up)
  - `E`: East (right)
  - `S`: South (down)
  - `W`: West (left)
- The movement command specifies the direction and number of steps, e.g., `N4`.
- The robot stops moving if it encounters a collision or reaches the grid boundary.

#### c. **Prevent Collisions**
- Before moving, the program checks if the destination cell is occupied by another robot.
- If a collision is detected, the robot stops in the previous cell.

#### d. **Display Robot Positions**
- Users can view all robots and their positions.
- Alternatively, they can query the position of a specific robot.

### 3. User Interaction
The program runs in a loop, presenting the following options:
1. Add a new robot.
2. Move a robot by providing its ID and movement command.
3. Display all robots and their positions.
4. Display the position of a specific robot.
5. Exit the program.

## Code Explanation
Here is how the program works step-by-step:

### 1. Adding Robots
The `add_robot` method in the `RobotManager` class creates a new `Robot` instance if the ID is unique. If the ID already exists, it informs the user.
```python
robot_manager.add_robot(robot_id)
```

### 2. Moving Robots
The `move_robot` method updates a robot's position based on the input command. It prevents collisions and ensures the robot remains within the grid.
```python
robot_manager.move_robot(robot_id, command)
```

### 3. Displaying Positions
The `display_robots` and `display_robot_position` methods provide information about the positions of all robots or a specific robot.
```python
robot_manager.display_robots()
robot_manager.display_robot_position(robot_id)
```

### 4. Handling Collisions
Before moving a robot, the program calculates all occupied positions and ensures the robot does not move into an occupied cell.
```python
occupied_positions = {robot.position for robot in self.robots.values() if robot.robot_id != robot_id}
```

## Example Output
### Adding Robots
```plaintext
Options:
1. Add a new robot
2. Move a robot
3. Display all robots
4. Display a robot's position
5. Exit
Enter your choice: 1
Enter a unique robot ID: R1
Robot with ID R1 added.
```

### Moving a Robot
```plaintext
Enter the robot ID to move: R1
Enter the movement command (e.g., N4, E3): N3
Robot R1 moved to (0, 0).
```

### Displaying All Robots
```plaintext
Current robots:
Robot ID: R1, Position: (0, 0)
Robot ID: R2, Position: (1, 1)
```
