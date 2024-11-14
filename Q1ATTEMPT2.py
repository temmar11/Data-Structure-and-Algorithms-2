from PIL import Image
import numpy as np
import random
import matplotlib.pyplot as plt


# Load and preprocess the maze image
def load_maze(image_path, threshold=128, sample_rate=10):
    maze_image = Image.open(image_path).convert('L')  # Convert to grayscale
    binary_maze = np.array(maze_image) > threshold  # Threshold for binary conversion
    binary_maze = binary_maze.astype(int)  # Convert boolean to int (1 for path, 0 for wall)
    sampled_maze = binary_maze[::sample_rate, ::sample_rate]  # Sample every `sample_rate` pixel
    return sampled_maze

# Function to display the maze as a single array
def display_maze(maze):
    print("Sampled Binary Maze Array:")
    print(maze.tolist())  # Convert the entire maze to a list of lists for cleaner display

# Define the Backtracking approach with debug output
def backtracking_solve(maze, start, end):
    path = []
    visited = set()
    
    def backtrack(x, y):
        if (x, y) == end:
            return True
        if (x, y) in visited or not (0 <= x < maze.shape[0] and 0 <= y < maze.shape[1]) or maze[x][y] == 0:
            return False

        visited.add((x, y))
        path.append((x, y))
        
        # Debug output to trace path
        print(f"Visiting: ({x}, {y}), Path so far: {path}")

        # Define direction order: down, right, up, left
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        for dx, dy in directions:
            if backtrack(x + dx, y + dy):
                return True
        
        # Backtracking
        path.pop()
        return False

    if backtrack(start[0], start[1]):
        print("Path found using Backtracking:")
        print(path)
    else:
        print("No path found using Backtracking.")
    
    return path

# Define the Las Vegas approach with debug output
def las_vegas_solve(maze, start, end, max_steps=400):
    x, y = start
    steps = 0
    path = [(x, y)]
    visited = set(path)
    
    while steps < max_steps:
        if (x, y) == end:
            print("Path found using Las Vegas approach:")
            print(path)
            return path
        
        # Debug output to trace path
        print(f"Current position: ({x}, {y}), Steps: {steps}, Path length: {len(path)}")
        
        # Randomly choose a direction
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        random.shuffle(directions)
        
        moved = False
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < maze.shape[0] and 0 <= ny < maze.shape[1] and maze[nx][ny] == 1 and (nx, ny) not in visited:
                x, y = nx, ny
                path.append((x, y))
                visited.add((x, y))
                moved = True
                break
        
        if not moved:
            break
        
        steps += 1
    
    if (x, y) == end:
        print("Path found using Las Vegas approach:")
        
    else:
        print("No path found within", max_steps, "steps using Las Vegas approach.")
        
    
    print(path)
    return path

# Main function to solve the maze with start/end validation
def solve_maze(image_path, start, end, method="backtracking"):
    maze = load_maze(image_path)
    display_maze(maze)  # Display the maze as a single multidimensional array

    # Ensure start and end points are paths
    if maze[start[0], start[1]] == 0:
        print("Invalid start point; it is a wall.")
        return
    if maze[end[0], end[1]] == 0:
        print("Invalid end point; it is a wall.")
        return

    if method == "backtracking":
        return backtracking_solve(maze, start, end)
    elif method == "las_vegas":
        return las_vegas_solve(maze, start, end)
    else:
        print("Invalid method specified.")


# Visualization function for the maze path
def visualize_path(maze, path, start, end):
    # Create a plot of the maze
    plt.figure(figsize=(8, 8))
    plt.imshow(maze, cmap="binary")  # Display maze (0=black for walls, 1=white for paths)

    # Mark visited path squares
    for (x, y) in path:
        plt.plot(y, x, 's', color='blue', markersize=5)  # Small squares for path

    # Mark start and end points
    plt.plot(start[1], start[0], 'go', markersize=10, label="Start")  # Start point as green
    plt.plot(end[1], end[0], 'ro', markersize=10, label="End")        # End point as red

    plt.legend()
    plt.title("Maze Path Visualization")
    plt.axis('off')  # Turn off the axes for a cleaner look
    plt.show()

# Example usage
image_path = r'C:\Users\temma\DSA2\Submission\maze-2.png'
start = (9, 1)  # Specify the starting point
end = (11, 19)  # Specify the ending point


method = "backtracking" 
#method = "las_vegas"
##BEcauae LV is not working every time i try it there might be a way to repeat it auto unit i can find a path
solve_maze(image_path, start, end, method)

path = solve_maze(image_path, start, end, method)
if path:  # If a path is returned, visualize it
    visualize_path(load_maze(image_path), path, start, end)