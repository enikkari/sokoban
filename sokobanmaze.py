class SokobanMaze:
    points = 0
    steps = 0
    boulders_moved = 0
    solved = False

    #wall = ['#']
    #space = [' ']
    #boulder = ['@']
    #hero = ['h']

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