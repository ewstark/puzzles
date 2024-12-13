import argparse

verbose = False
current_day = 9

def read_puzzle_input (filename):
    file_map = []  # array of int(0-9)
    with open(filename, "rt") as f:
        input_lines = [l.strip() for l in f.readlines()]
        for line in input_lines:
            for c in line:
                file_map.append(int(c))
    return file_map

def render_file_map (file_map):
    global verbose
    disk = []
    current_id = 0
    as_file = True
    for n in file_map:
        if as_file:
            disk.extend([current_id for _ in range(n)])
            current_id += 1
        else: # space
            disk.extend([-1 for _ in range(n)])
        as_file = not as_file
    if verbose: print(f"top ID = {current_id-1}")
    return disk

def show_disk (disk):
    print(f">", end='')
    for n in disk:
        if n < 0:
            print(".", end='')
        else:
            print(f"{n % 10}", end='')
    print()


if __name__ == "__main__":
    default_filename = f"day{current_day}.input.txt"
    parser = argparse.ArgumentParser(description=f"AoC 2024, day{current_day}")
    parser.add_argument("filename", type=str, nargs='?', default=default_filename, help="input file")
    parser.add_argument("-v", "--verbose", action="store_true", help="enable verbose debug output")
    args = parser.parse_args()
    verbose = args.verbose

    file_map = read_puzzle_input(args.filename)

    if verbose:
        print(f"input file_map: {''.join([str(n) for n in file_map])}")

    disk = render_file_map(file_map)

    if verbose: show_disk(disk)
    next_file = len(disk) - 1
    next_space = 0
    while True:
        while disk[next_space] != -1 and next_space < next_file:
            next_space += 1
        while disk[next_file] == -1 and next_space < next_file:
            next_file -= 1
        if next_space < next_file:
            disk[next_space] = disk[next_file]
            disk[next_file] = -1
            next_space += 1
            next_file -= 1
            if verbose: show_disk(disk)
        else:
            break

    final_result = 0
    for idx, n in enumerate(disk):
        if n < 0:
            break
        final_result += idx * n

    print(f"Result = {final_result}")

# submitted 6337367222422 = correct

# --- Day 9: Disk Fragmenter ---
# Another push of the button leaves you in the familiar hallways of some friendly amphipods! Good thing you each somehow got
# your own personal mini submarine. The Historians jet away in search of the Chief, mostly by driving directly into walls.
# 
# While The Historians quickly figure out how to pilot these things, you notice an amphipod in the corner struggling with his
# computer. He's trying to make more contiguous free space by compacting all of the files, but his program isn't working; you
# offer to help.
# 
# He shows you the disk map (your puzzle input) he's already generated. For example:
#     2333133121414131402
# 
# The disk map uses a dense format to represent the layout of files and free space on the disk. The digits alternate between
# indicating the length of a file and the length of free space.
# 
# So, a disk map like 12345 would represent a one-block file, two blocks of free space, a three-block file, four blocks of
# free space, and then a five-block file. A disk map like 90909 would represent three nine-block files in a row (with no free
# space between them).
# 
# Each file on disk also has an ID number based on the order of the files as they appear before they are rearranged, starting
# with ID 0. So, the disk map 12345 has three files: a one-block file with ID 0, a three-block file with ID 1, and a five-block
# file with ID 2. Using one character for each block where digits are the file ID and . is free space, the disk map 12345
# represents these individual blocks:
#     0..111....22222
# 
# The first example above, 2333133121414131402, represents these individual blocks:
#     00...111...2...333.44.5555.6666.777.888899
# 
# The amphipod would like to move file blocks one at a time from the end of the disk to the leftmost free space block (until
# there are no gaps remaining between file blocks). For the disk map 12345, the process looks like this:
#     0..111....22222
#     02.111....2222.
#     022111....222..
#     0221112...22...
#     02211122..2....
#     022111222......
# 
# The first example requires a few more steps:
#     00...111...2...333.44.5555.6666.777.888899
#     009..111...2...333.44.5555.6666.777.88889.
#     0099.111...2...333.44.5555.6666.777.8888..
#     00998111...2...333.44.5555.6666.777.888...
#     009981118..2...333.44.5555.6666.777.88....
#     0099811188.2...333.44.5555.6666.777.8.....
#     009981118882...333.44.5555.6666.777.......
#     0099811188827..333.44.5555.6666.77........
#     00998111888277.333.44.5555.6666.7.........
#     009981118882777333.44.5555.6666...........
#     009981118882777333644.5555.666............
#     00998111888277733364465555.66.............
#     0099811188827773336446555566..............
# 
# The final step of this file-compacting process is to update the filesystem checksum. To calculate the checksum, add up
# the result of multiplying each of these blocks' position with the file ID number it contains. The leftmost block is in
# position 0. If a block contains free space, skip it instead.
# 
# Continuing the first example, the first few blocks' position multiplied by its file ID number are 0 * 0 = 0, 1 * 0 = 0, 
# 2 * 9 = 18, 3 * 9 = 27, 4 * 8 = 32, and so on. In this example, the checksum is the sum of these, 1928.
# 
# Compact the amphipod's hard drive using the process he requested. What is the resulting filesystem checksum? (Be careful
# copy/pasting the input for this puzzle; it is a single, very long line.)
