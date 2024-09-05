def find_path(maze, x, y, exit_x, exit_y):
    # If out of bounds or a wall, return False. This is a base case that checks to see if the position (x,y) is outside the maze or a wall. 
    if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]) or maze[x][y] != 0:
        return False
    
    # If we have reached the exit, return True and mark it. Second base case thats checks for the exit and marks it
    if x == exit_x and y == exit_y:
        maze[x][y] = '*'  # Mark exit as part of the path
        return True
    
    # Mark the current cell as part of the path. this changes the cell into a * marking that it's part of the path
    maze[x][y] = '*'
    
    # Try all four directions: down, up, right, left. This checks for four different directions of the maze returning true if a path has been found 
    if (find_path(maze, x + 1, y, exit_x, exit_y) or  # Move down
        find_path(maze, x - 1, y, exit_x, exit_y) or  # Move up
        find_path(maze, x, y + 1, exit_x, exit_y) or  # Move right
        find_path(maze, x, y - 1, exit_x, exit_y)):   # Move left
        return True
    
    # If none of the directions work, backtrack. This marks that if none of the recursive calls finds a valid path, it will unmark the cell and return false
    maze[x][y] = 0
    return False
    
# just for organization purposes to print out the maze properly
def print_maze(maze):
    for row in maze:
        print(" ".join(map(str, row)))

# Maze: 0 = open, 1 = wall
maze = [
    [1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 0]
]
#Starting point and exit point of the maze
start_x, start_y = 0, 1
exit_x, exit_y = 4, 4

if find_path(maze, start_x, start_y, exit_x, exit_y):
    print("Path found:")
else:
    print("Path not found:")

print_maze(maze)
