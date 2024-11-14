import matplotlib.pyplot as plt
import numpy as np
import random



"""
I think the code is not working because the image is being incorrectly usedand turned into an array

the other reason could be the fact that the "robot" that we are using to move through the maze is not moving through the middle with a certain amount, to make it work the "robot" needs to move from the 
of each "block" each block is 10 units by 10 units from what i understand so the robot needs to move in units of 5 either up or down
in order for this to work the start point needs to be the exact mid point of its block and the end point the same thing
"""


# Load the image
maze_img = plt.imread(r'C:\Users\temma\DSA2\Submission\maze-2.png')

# Check the shape and confirm it has an alpha channel
print("Shape:", maze_img.shape)
print("Data Type:", maze_img.dtype)
print("Unique values in original image:", np.unique(maze_img))

# Convert to grayscale by averaging only the RGB channels, ignore the alpha channel
maze_gray = np.mean(maze_img[..., :3], axis=2)

# Apply threshold to create a binary maze
threshold = 0.5
maze_binary = maze_gray < threshold  # True for wall, False for path
maze_array = maze_binary.astype(int)  # Convert to integer array (1 for walls, 0 for paths)

# Display the resulting binary array
print("Unique values in binary maze:", np.unique(maze_array))

print(maze_array)

# Display the maze using the 'binary' colormap for clear black-and-white visualization
plt.imshow(maze_array, cmap='binary')

#plt.axis('off')
plt.show()


#define the starting point and exit for the maze
start = (95, 5) # startin point is top left


print("This is the start: ",start)
print("Starting Point Value:", maze_array[start])


exit_point = (115.5,204.5) # exit is at the bottom
print("This is the exit: ", exit_point)
print("exit Point Value:", maze_array[exit_point])

#define the directions (up down left right)
directions = [(-5, 0), (5, 0), (0, -5), (0, 5)]

# the function below will check if the cell is within the maze boundaries and is a path (not a wall)

def is_valid_move(maze, pos):
    x, y = pos
    return 0 <= x < maze.shape[0] and 0 <= y <maze.shape[1] and maze[x, y] == 0

# this is the Backtracking Algorithm
def backtracking_maze_solver(maze, start, exit_point):
    stack = [ start ]
    visited = set()
    visited.add(start)

    while stack:
        current = stack[-1]

        #check if the current postion is the exit

        if current == exit_point:
            return stack # this will return the path to the exit
        
        #this will try all 4 directions to find an unvisited path
        found_path = False

        for direction in directions:
            next_move = (current[0] + direction[0], current[1] + direction[1])


            if is_valid_move(maze, next_move) and next_move not in  visited:
                stack.append(next_move)
                visited.add(next_move)
                found_path = True
                break # this will make the move to the next cell
        if not found_path:
            stack.pop() # this will backtrack if no path is found from the current postion

    return None    


# Las Vegas Algorithm

def las_vegas_maze_solver(maze, start, exit_point, max_steps= 400):
    current = start
    visited = set()
    visited.add(current)
    steps = 0

    while steps < max_steps:
        #check if the curreent postion is the exit
        if current == exit_point:
            return visited # return the visited path if successful
        
        # collect the possible moves
        possible_moves = [(current[0] + direction[0], current[1] + direction[1])
                          for direction in directions if is_valid_move(maze, (current[0] + direction[0], current[1] + direction[1]))]
        
        # if there is are possible moves, randomly choose one

        if possible_moves:
            current = random.choice(possible_moves)
            visited.add(current)
        else:
            #if there are no possible moves, randoml;y backtrack within the visited cells
            current = random.choice(list(visited))

        steps += 1
    return None # return none if edxit is not found within the max_steps


# visualise the soolution path in the maze

def visualise_path(maze, path, title= "Maze Solution"):
    maze_copy = maze.copy()
    for (x, y) in path:
        maze_copy[x, y] = 0.5 # this marks the path as gray
    plt.imshow(maze, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()


#run both algorithms and display the solution



backtracking_path = backtracking_maze_solver(maze_array, start, exit_point)
if backtracking_path:
    visualise_path(maze_array,backtracking_path, title="Backtracking Solution")
else:
    print("No solution found with backtracking")

las_vegas_path = las_vegas_maze_solver(maze_array, start, exit_point)
if las_vegas_path:
    visualise_path(maze_array, las_vegas_path, title = "Las Vegas Solution")
else:
    print("No solution found with Las Vegas within the step limit")






            











