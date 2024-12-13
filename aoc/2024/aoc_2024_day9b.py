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
    file_sizes = {} # file_id : size (0..9)
    current_id = 0
    as_file = True
    for n in file_map:
        if as_file:
            file_sizes[current_id] = n
            disk.extend([current_id for _ in range(n)])
            current_id += 1
        else: # space
            disk.extend([-1 for _ in range(n)])
        as_file = not as_file
    max_id = current_id - 1
    print(f"top ID = {max_id}")
    return disk, file_sizes, max_id

def show_disk (disk):
    print(f">", end='')
    for n in disk:
        if n < 0:
            print(".", end='')
        else:
            print(f"{n % 10}", end='')
    print()

def clear_file (disk, file_id):
    for i, n in enumerate(disk):
        if n == file_id:
            disk[i] = -1

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

    disk, file_sizes, max_id = render_file_map(file_map)

    if verbose: show_disk(disk)

    for file_id in range(max_id, 0, -1):
        if file_id % 100 == 0: print(f"{file_id}")
        seek_size = file_sizes[file_id]
        # if verbose: print(f"seeking space for file {file_id} with size {seek_size}")
        if seek_size == 0:
            print(f"ignoring file {file_id} with zero size")
        else:
            next_space = 0
            done = False
            old_file_start = disk.index(file_id)
            while next_space < old_file_start and not done:
                # find the next space...
                while next_space < old_file_start and disk[next_space] != -1:
                    next_space += 1
                # find how wide it is (where next file starts)
                next_file = next_space + 1
                while next_file < old_file_start and disk[next_file] == -1:
                    next_file += 1
                width = next_file - next_space
                # see if fits in this space
                if width >= seek_size and next_space < old_file_start:
                    # move
                    # clear old locations
                    clear_file(disk, file_id)
                    # add new locations
                    for i in range(seek_size):
                        disk[next_space+i] = file_id
                    if verbose:
                        print(f"moved {file_id} of size {seek_size} to {next_space}")
                        # show_disk(disk)
                    done = True
                else:
                    next_space = next_file + 1
            if verbose and not done:
                print(f"unable to move {file_id} of size {seek_size}")
                # show_disk(disk)

    final_result = 0
    for idx, n in enumerate(disk):
        if n > 0: final_result += idx * n

    print(f"Result = {final_result}")

# submitted 6361380647183 = correct  (took almost a minute to run)

# --- Part Two ---
# Upon completion, two things immediately become clear. First, the disk definitely has a lot more contiguous free space,
# just like the amphipod hoped. Second, the computer is running much more slowly! Maybe introducing all of that file 
# system fragmentation was a bad idea?
# 
# The eager amphipod already has a new plan: rather than move individual blocks, he'd like to try compacting the files on
# his disk by moving whole files instead.
# 
# This time, attempt to move whole files to the leftmost span of free space blocks that could fit the file. Attempt to
# move each file exactly once in order of decreasing file ID number starting with the file with the highest file ID number.
# If there is no span of free space to the left of a file that is large enough to fit the file, the file does not move.
# 
# The first example from above now proceeds differently:
#     00...111...2...333.44.5555.6666.777.888899
#     0099.111...2...333.44.5555.6666.777.8888..
#     0099.1117772...333.44.5555.6666.....8888..
#     0099.111777244.333....5555.6666.....8888..
#     00992111777.44.333....5555.6666.....8888..
# 
# The process of updating the filesystem checksum is the same; now, this example's checksum would be 2858.
# 
# Start over, now compacting the amphipod's hard drive using this new method instead. What is the resulting filesystem checksum?
