import sys
sys.path.insert(1, '../')

import lib.tilt as tilt

def load_maze(width, height):
    # create a blank grid
    grid = {}
    for x in range(width):
        for y in range(height):
            nodes = [(0, (i,j)) for i,j in [(x,y-1),(x,y+1),(x-1,y),(x+1,y)]
                          if 0 <= i < width and 0 <= j < height ]
            grid[(x, y)] = nodes

    # traverse every node via breadth first search
    current = next(iter(grid))
    visited = {key: False for key in grid}
    stack = [current]
    visited[current] = True
    path = []
    while len(stack) > 0:
        path.append(current)
        unvisited = [n for _, n in grid[current] if not visited[n]]
        if len(unvisited) == 0:
            current = stack.pop()
        else:
            stack.append(current)
            # randomly choose the next node to add variety to the maze
            current = random.choice(unvisited)
            visited[current] = True

    # remove the unused exits into other nodes (like placing walls between nodes)
    graph = {key: [] for key in grid}
    for i in range(len(path)-1):
        graph[path[i]].append((random.randint(0, MAX_WEIGHT), path[i+1]))
    
    return graph

maze = load_maze(10, 10)
ax, ay, _ = tilt.get_tilt_data()

