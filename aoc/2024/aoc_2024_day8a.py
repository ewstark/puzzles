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
                    dx = n[0] - freqs[f][start_idx][0]
                    dy = n[1] - freqs[f][start_idx][1]
                    x1 = n[0] + dx
                    y1 = n[1] + dy
                    x2 = freqs[f][start_idx][0] - dx
                    y2 = freqs[f][start_idx][1] - dy
                    if x1 >= 0 and x1 < map_width and y1 >= 0 and y1 < map_height:
                        antinodes.add((x1, y1))
                    if x2 >= 0 and x2 < map_width and y2 >= 0 and y2 < map_height:
                        antinodes.add((x2, y2))

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

# submitted 367 = correct

# --- Day 8: Resonant Collinearity ---
# You find yourselves on the roof of a top-secret Easter Bunny installation.
# 
# While The Historians do their thing, you take a look at the familiar huge antenna. Much to your surprise, it
# seems to have been reconfigured to emit a signal that makes people 0.1% more likely to buy Easter Bunny brand
# Imitation Mediocre Chocolate as a Christmas gift! Unthinkable!
# 
# Scanning across the city, you find that there are actually many such antennas. Each antenna is tuned to a specific
# frequency indicated by a single lowercase letter, uppercase letter, or digit. You create a map (your puzzle input)
# of these antennas. For example:
#     ............
#     ........0...
#     .....0......
#     .......0....
#     ....0.......
#     ......A.....
#     ............
#     ............
#     ........A...
#     .........A..
#     ............
#     ............
# The signal only applies its nefarious effect at specific antinodes based on the resonant frequencies of the antennas.
# In particular, an antinode occurs at any point that is perfectly in line with two antennas of the same frequency - but
# only when one of the antennas is twice as far away as the other. This means that for any pair of antennas with the 
# same frequency, there are two antinodes, one on either side of them.
# 
# So, for these two antennas with frequency a, they create the two antinodes marked with #:
#     ..........
#     ...#......
#     ..........
#     ....a.....
#     ..........
#     .....a....
#     ..........
#     ......#...
#     ..........
#     ..........
# 
# Adding a third antenna with the same frequency creates several more antinodes. It would ideally add four antinodes, but
# two are off the right side of the map, so instead it adds only two:
#     ..........
#     ...#......
#     #.........
#     ....a.....
#     ........a.
#     .....a....
#     ..#.......
#     ......#...
#     ..........
#     ..........
# 
# Antennas with different frequencies don't create antinodes; A and a count as different frequencies. However, antinodes
# can occur at locations that contain antennas. In this diagram, the lone antenna with frequency capital A creates no
# antinodes but has a lowercase-a-frequency antinode at its location:
#     ..........
#     ...#......
#     #.........
#     ....a.....
#     ........a.
#     .....a....
#     ..#.......
#     ......A...
#     ..........
#     ..........
# 
# The first example has antennas with two different frequencies, so the antinodes they create look like this, plus an
# antinode overlapping the topmost A-frequency antenna:
#     ......#....#
#     ...#....0...
#     ....#0....#.
#     ..#....0....
#     ....0....#..
#     .#....A.....
#     ...#........
#     #......#....
#     ........A...
#     .........A..
#     ..........#.
#     ..........#.
# 
# Because the topmost A-frequency antenna overlaps with a 0-frequency antinode, there are 14 total unique locations that
# contain an antinode within the bounds of the map.
# 
# Calculate the impact of the signal. How many unique locations within the bounds of the map contain an antinode?
