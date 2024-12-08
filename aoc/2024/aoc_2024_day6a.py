import argparse

verbose = False
current_day = 6

def read_puzzle_input (filename):
    maze = []
    x = 0
    y = 0
    with open(filename, "rt") as f:
        input_lines = [l.strip() for l in f.readlines()]
        for idx, line in enumerate(input_lines):
            if '^' in line:
                x = line.index('^')
                y = idx
                line = line[:x] + 'X' + line[x+1:]
            maze.append([c for c in line])
    return maze, (x,y)

def next_pos (x, y, dir):
    if dir == 'N':
        y -= 1
    elif dir == 'S':
        y += 1
    elif dir == 'E':
        x += 1
    else:  # dir == 'W'
        x -= 1
    return (x, y)

def turn_right (dir):
    if dir == 'N':
        return 'E'
    elif dir == 'S':
        return 'W'
    elif dir == 'E':
        return 'S'
    # else:  # dir == 'W'
    return 'N'
    
def move_guard (maze, guard_pos):
    visits = set()
    dir = 'N'
    x, y = guard_pos
    visits.add((x, y))
    maze_width = len(maze[0])
    maze_height = len(maze)
    if verbose: print(f"width={maze_width} height={maze_height}")
    while (x > 0) and (x < maze_width) and (y > 0) and (y < maze_height):
        next_x, next_y = next_pos(x, y, dir)
        if (next_x >= 0) and (next_x < maze_width) and (next_y >= 0) and (next_y < maze_height):
            cell_type = maze[next_y][next_x]
            if cell_type == '#':
                dir = turn_right(dir)
            else:
                x = next_x
                y = next_y
                visits.add((x, y))
                maze[y][x] = 'X'
        else:
            # done
            break
    return visits

if __name__ == "__main__":
    default_filename = f"day{current_day}.input.txt"
    parser = argparse.ArgumentParser(description=f"AoC 2024, day{current_day}")
    parser.add_argument("filename", type=str, nargs='?', default=default_filename, help="input file")
    parser.add_argument("-v", "--verbose", action="store_true", help="enable verbose debug output")
    args = parser.parse_args()
    verbose = args.verbose

    maze, guard_pos = read_puzzle_input(args.filename)

    if verbose:
        print(f"input maze: (guard at {guard_pos})")
        for line in maze:
            print(''.join(line))
        print()

    visits = move_guard(maze, guard_pos)

    if verbose:
        print("completed maze:")
        for line in maze:
            print(''.join(line))
        print()

    print(f"Result = {len(visits)}")

# submitted 4882 = too low
# submitted 4883 = correct (corrected code to properly add last position)

# --- Day 6: Guard Gallivant ---
# The Historians use their fancy device again, this time to whisk you all away to the North Pole prototype suit manufacturing
# lab... in the year 1518! It turns out that having direct access to history is very convenient for a group of historians.
# 
# You still have to be careful of time paradoxes, and so it will be important to avoid anyone from 1518 while The Historians
# search for the Chief. Unfortunately, a single guard is patrolling this part of the lab.
# 
# Maybe you can work out where the guard will go ahead of time so that The Historians can search safely?
# 
# You start by making a map (your puzzle input) of the situation. For example:
#     ....#.....
#     .........#
#     ..........
#     ..#.......
#     .......#..
#     ..........
#     .#..^.....
#     ........#.
#     #.........
#     ......#...
# 
# The map shows the current position of the guard with ^ (to indicate the guard is currently facing up from the perspective of
# the map). Any obstructions - crates, desks, alchemical reactors, etc. - are shown as #.
# 
# Lab guards in 1518 follow a very strict patrol protocol which involves repeatedly following these steps:
#   * If there is something directly in front of you, turn right 90 degrees.
#   * Otherwise, take a step forward.
# 
# Following the above protocol, the guard moves up several times until she reaches an obstacle (in this case, a pile of failed
# suit prototypes):
#     ....#.....
#     ....^....#
#     ..........
#     ..#.......
#     .......#..
#     ..........
#     .#........
#     ........#.
#     #.........
#     ......#...
# 
# Because there is now an obstacle in front of the guard, she turns right before continuing straight in her new facing direction:
#     ....#.....
#     ........>#
#     ..........
#     ..#.......
#     .......#..
#     ..........
#     .#........
#     ........#.
#     #.........
#     ......#...
# 
# Reaching another obstacle (a spool of several very long polymers), she turns right again and continues downward:
#     ....#.....
#     .........#
#     ..........
#     ..#.......
#     .......#..
#     ..........
#     .#......v.
#     ........#.
#     #.........
#     ......#...
# 
# This process continues for a while, but the guard eventually leaves the mapped area (after walking past a tank of universal solvent):
#     ....#.....
#     .........#
#     ..........
#     ..#.......
#     .......#..
#     ..........
#     .#........
#     ........#.
#     #.........
#     ......#v..
# 
# By predicting the guard's route, you can determine which specific positions in the lab will be in the patrol path. Including the guard's starting position, the positions visited by the guard before leaving the area are marked with an X:
#     ....#.....
#     ....XXXXX#
#     ....X...X.
#     ..#.X...X.
#     ..XXXXX#X.
#     ..X.X.X.X.
#     .#XXXXXXX.
#     .XXXXXXX#.
#     #XXXXXXX..
#     ......#X..
# 
# In this example, the guard will visit 41 distinct positions on your map.
# 
# Predict the path of the guard. How many distinct positions will the guard visit before leaving the mapped area?