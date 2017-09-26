import random
import copy
from collections import deque
import sokobanmaze

# TODO: make actual algorithm for generation
def gen_rand_maze(nx, ny):
    maze = [['#'] + [' '] + ['#'] * (nx - 2)]
    for y in range(1, ny - 1):
        row = ['#']
        for x in range(1, nx - 1):
            row.append(random.sample([' '] * 3 + ['#'] * 6 + ['@'] * 3, 1)[0])
        row.append('#')
        maze.append(row)
    maze[ny - 2][nx - 2] = 'h'
    maze.append(['#'] * nx)
    return sokobanmaze.SokobanMaze(maze)

# Checks if maze is solvable
def BFS(maze):
    root = copy.deepcopy(maze)
    visited = [root]
    queue = deque([root])
    while (queue):
        node = queue.popleft()
        if (node.is_solved()):
            return True
        else:
            up = copy.deepcopy(node)
            up.move_h(0, 1)

            down = copy.deepcopy(node)
            down.move_h(0, -1)

            right = copy.deepcopy(node)
            right.move_h(1, 0)

            left = copy.deepcopy(node)
            left.move_h(-1, 0)

            for m in [up, down, right, left]:
                if m not in visited:
                    visited.append(m)
                    queue.append(m)
    return False

def get_maze(nx, ny):
    maze = gen_rand_maze(nx, ny)
    i = 1
    print(i)
    solvable = BFS(maze)
    while (not solvable):
        i += 1
        if (i % 1000 == 1):
            print(i)
        maze = gen_rand_maze(nx, ny)
        solvable = BFS(maze)
    print(maze.get_boulder_count())
    return maze
