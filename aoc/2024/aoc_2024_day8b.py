import argparse

verbose = False
current_day = 8

def read_puzzle_input (filename):
    antennas = []  # 2d array, rows of [char]
    freqs = {}     # maps frequency letters to map locations as [tuples (x,y)]
    with open(filename, "rt") as f:
        input_lines = [l.strip() for l in f.readlines()]
        for y, line in enumerate(input_lines):
            antennas.append([_ for _ in line])
            for x, c in enumerate(line):
                if c != '.':
                    if c in freqs:
                        freqs[c].append((x,y))
                    else:
                        freqs[c] = [(x,y)]
    return (antennas, freqs)

if __name__ == "__main__":
    default_filename = f"day{current_day}.input.txt"
    parser = argparse.ArgumentParser(description=f"AoC 2024, day{current_day}")
    parser.add_argument("filename", type=str, nargs='?', default=default_filename, help="input file")
    parser.add_argument("-v", "--verbose", action="store_true", help="enable verbose debug output")
    args = parser.parse_args()
    verbose = args.verbose

    antennas, freqs = read_puzzle_input(args.filename)
    map_width = len(antennas[0])
    map_height = len(antennas)
    unique_locations = 0
    all_towers = set() # tuples (x,y) of input tower locations

    if verbose:
        print(f"input antennas ({map_width}x{map_height})")
        for e in antennas:
            print(f"   {''.join(e)}")
        print(f"frequency locations ({len(freqs)})")
        for f in freqs:
            print(f"   {f}: {freqs[f]}")
            for tower_loc in freqs[f]:
                all_towers.add(tower_loc)
        print()
        print(f"All towers: {all_towers}")

    antinodes = set()
    
    for f in freqs:
        if len(freqs[f]) > 1:
            for start_idx in range(len(freqs[f])-1):
                for n in freqs[f][start_idx+1:]:
                    antinodes.add((n[0], n[1]))
                    antinodes.add((freqs[f][start_idx][0], freqs[f][start_idx][1]))
                    dx = n[0] - freqs[f][start_idx][0]
                    dy = n[1] - freqs[f][start_idx][1]
                    x1 = n[0] + dx
                    y1 = n[1] + dy
                    while x1 >= 0 and x1 < map_width and y1 >= 0 and y1 < map_height:
                        antinodes.add((x1, y1))
                        x1 += dx
                        y1 += dy
                    x2 = freqs[f][start_idx][0] - dx
                    y2 = freqs[f][start_idx][1] - dy
                    while x2 >= 0 and x2 < map_width and y2 >= 0 and y2 < map_height:
                        antinodes.add((x2, y2))
                        x2 -= dx
                        y2 -= dy

    print("antinodes:")
    for y in range(map_height):
        print("   ", end='')
        for x in range(map_width):
            if (x,y) in antinodes:
                unique_locations += 1
                if (x,y) in all_towers:
                    print(antennas[y][x], end='')
                else:
                    print("#", end='')
            else:
                print(".", end='')
        print()
    print()

    print(f"Result = {unique_locations}")

# submitted 1285 = correct

# --- Part Two ---
# Watching over your shoulder as you work, one of The Historians asks if you took the effects of resonant harmonics
# into your calculations.
# 
# Whoops!
# 
# After updating your model, it turns out that an antinode occurs at any grid position exactly in line with at least
# two antennas of the same frequency, regardless of distance. This means that some of the new antinodes will occur at
# the position of each antenna (unless that antenna is the only one of its frequency).
# 
# So, these three T-frequency antennas now create many antinodes:
#     T....#....
#     ...T......
#     .T....#...
#     .........#
#     ..#.......
#     ..........
#     ...#......
#     ..........
#     ....#.....
#     ..........
# 
# In fact, the three T-frequency antennas are all exactly in line with two antennas, so they are all also antinodes!
# This brings the total number of antinodes in the above example to 9.
# 
# The original example now has 34 antinodes, including the antinodes that appear on every antenna:
#     ##....#....#
#     .#.#....0...
#     ..#.#0....#.
#     ..##...0....
#     ....0....#..
#     .#...#A....#
#     ...#..#.....
#     #....#.#....
#     ..#.....A...
#     ....#....A..
#     .#........#.
#     ...#......##
# 
# Calculate the impact of the signal using this updated model. How many unique locations within the bounds of the 
# map contain an antinode?
