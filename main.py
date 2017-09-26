from mazegenerator import get_maze
import copy
import pickle

def play_maze(maze):
    maze_copy = copy.deepcopy(maze)
    print("Use asdw keys + enter to navigate trough the maze")
    maze.printer()
    c = raw_input()
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
            # TODO: support downloading good mazes from memory
            print("name maze")
            name = raw_input()
            pickle.dump(maze_copy, open('mazes/' + name + '.p', 'wp'))
        maze.printer()
        c = raw_input()

def main():
    # sokoban
    maze = get_maze(10, 5)
    play_maze(maze)

if __name__ == "__main__":
    main()
