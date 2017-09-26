import random
import copy
from collections import deque
import pickle

class Maze:
    points = 0
    steps = 0
    boulders_moved = 0
    solved = False

    def __init__(self, maze):
        self.maze = maze
        self.ny = len(maze)
        self.nx = len(maze[0])
        self.hx, self.hy = self.find('h')
        self.steps = 0

    def __eq__(self, other):
        return self.get_map() == other.get_map()

    def is_solved(self):
        return self.solved

    def replace(self, x, y, new):
        self.maze[y][x] = new

    def move(self, x, y, right, up):
        # 1 right -1 left
        # 1 up -1 down
        # return new location
        item = self.maze[y][x]
        if ((x + right == -1 or y - up == -1) and item == 'h'):
            self.solved = True
            self.maze[y][x] = ' '
        elif (self.maze[y - up][x + right] == ' '):
            self.maze[y][x] = ' '
            x = x + right
            y = y - up
            self.maze[y][x] = item
        elif (self.maze[y - up][x + right] == '@' and item == 'h'):
            if (self.move(x + right, y - up, right, up) != (x + right, y - up)):
                self.boulders_moved += 1
                x, y = self.move(x, y, right, up)
        return x, y

    def move_h(self, right, up):
        self.steps += 1
        self.hx, self.hy = self.move(self.hx, self.hy, right, up)


    def find(self, item):
        for y in range(1, self.ny):
            for x in range(1, self.nx):
                if (self.maze[y][x] == item):
                    return x, y

    def get_map(self):
        return self.maze

    def get_h(self):
        return self.hx, self.hy

    def get_n(self):
        return self.nx * self.ny

    def get_boulder_count(self):
        return self.boulders_moved

    def printer(self):
        print
        for row in self.maze:
            print(''.join(row))

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
    return Maze(maze)

# Checks if maxze is solvable
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

def main():
    # sokoban
    wall = ['#']
    space = [' ']
    boulder = ['@']
    hero = ['h']
    m = [wall * 6,
         space * 5 + wall,
         wall + space * 2 + wall + space + wall,
         wall + space + wall * 4,
         wall + space * 2 + wall + space + wall,
         wall + space * 2 + boulder + hero + wall,
         wall * 6]
    maze = get_maze(10, 5)
    maze_copy = copy.deepcopy(maze)
    print("Use asdw keys + enter to navigate trough the maze")
    maze.printer()

    c = raw_input()
    # c = 'q'

    while (c != 'q' and not maze.is_solved()):
        if (c == 'w'):
            maze.move_h(0, 1)
        elif (c == 's'):
            maze.move_h(0, -1)
        elif (c == 'd'):
            maze.move_h(1, 0)
        elif (c == 'a'):
            maze.move_h(-1, 0)
        elif (c == 'save'):
            print("name maze")
            name = raw_input()
            pickle.dump(maze_copy, open('mazes/' + name + '.p', 'wp'))
        maze.printer()
        c = raw_input()

if __name__ == "__main__":
    main()
