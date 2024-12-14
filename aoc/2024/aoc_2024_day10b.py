import argparse

verbose = False
current_day = 10

def read_puzzle_input (filename):
    topo_map = []  # 2D array of ints
    with open(filename, "rt") as f:
        input_lines = [l.strip() for l in f.readlines()]
        for line in input_lines:
            topo_map.append([int(c) for c in line])
    return topo_map


def climb_trail (peaks, x, y):
    global topo_map, height, width
    current_height = topo_map[y][x]
    if current_height == 9:
        peaks.append((x,y))
    else:
        next_height = current_height + 1
        if y > 0 and topo_map[y-1][x] == next_height:
            climb_trail(peaks, x, y-1)
        if y < (height-1) and topo_map[y+1][x] == next_height:
            climb_trail(peaks, x, y+1)
        if x > 0 and topo_map[y][x-1] == next_height:
            climb_trail(peaks, x-1, y)
        if x < (width-1) and topo_map[y][x+1] == next_height:
            climb_trail(peaks, x+1, y)

def count_peaks (x, y):
    global topo_map, height, width
    peaks = []
    climb_trail(peaks, x, y)
    return len(peaks)

if __name__ == "__main__":
    default_filename = f"day{current_day}.input.txt"
    parser = argparse.ArgumentParser(description=f"AoC 2024, day{current_day}")
    parser.add_argument("filename", type=str, nargs='?', default=default_filename, help="input file")
    parser.add_argument("-v", "--verbose", action="store_true", help="enable verbose debug output")
    args = parser.parse_args()
    verbose = args.verbose

    topo_map = read_puzzle_input(args.filename)
    trailhead_sum = 0
    trailheads = set()
    height = len(topo_map)
    width = len(topo_map[0])

    if verbose: print(f"input topo_map ({width}x{height}:")
    for y,row in enumerate(topo_map):
        if verbose: print(f"{''.join([str(n) for n in row])}")
        for x,n in enumerate(row):
            if n == 0:
                trailheads.add((x,y))

    for x,y in trailheads:
        peaks = count_peaks(x, y)
        print(f"found {peaks} peaks starting at trailhead ({x}, {y})")
        trailhead_sum += peaks

    print(f"Result = {trailhead_sum}")

# submitted 1062 = correct

# --- Part Two ---
# The reindeer spends a few minutes reviewing your hiking trail map before realizing something, disappearing for a few minutes,
# and finally returning with yet another slightly-charred piece of paper.
# 
# The paper describes a second way to measure a trailhead called its rating. A trailhead's rating is the number of distinct
# hiking trails which begin at that trailhead. For example:
#   .....0.
#   ..4321.
#   ..5..2.
#   ..6543.
#   ..7..4.
#   ..8765.
#   ..9....

# The above map has a single trailhead; its rating is 3 because there are exactly three distinct hiking trails which begin at
# that position:
#   .....0.   .....0.   .....0.
#   ..4321.   .....1.   .....1.
#   ..5....   .....2.   .....2.
#   ..6....   ..6543.   .....3.
#   ..7....   ..7....   .....4.
#   ..8....   ..8....   ..8765.
#   ..9....   ..9....   ..9....
# 
# Here is a map containing a single trailhead with rating 13:
#   ..90..9
#   ...1.98
#   ...2..7
#   6543456
#   765.987
#   876....
#   987....
# 
# This map contains a single trailhead with rating 227 (because there are 121 distinct hiking trails that lead to the 9 on the
# right edge and 106 that lead to the 9 on the bottom edge):
#   012345
#   123456
#   234567
#   345678
#   4.6789
#   56789.
# 
# Here's the larger example from before:
#   89010123
#   78121874
#   87430965
#   96549874
#   45678903
#   32019012
#   01329801
#   10456732
# 
# Considering its trailheads in reading order, they have ratings of 20, 24, 10, 4, 1, 4, 5, 8, and 5. The sum of all trailhead
# ratings in this larger example topographic map is 81.
# 
# You're not sure how, but the reindeer seems to have crafted some tiny flags out of toothpicks and bits of paper and is using
# them to mark trailheads on your topographic map. What is the sum of the ratings of all trailheads?
