import argparse
import re

verbose = False
current_day = 4

puzzle_data = []
width = 0
height = 0

def read_puzzle_input (filename):
    puzz_in = []
    with open(filename, "rt") as f:
        if (verbose): print(f"reading from '{filename}'")
        input_lines = [l.strip() for l in f.readlines() if len(l.strip()) > 0]
        for line in input_lines:
            if (verbose): print(f">> '{line}'")
            puzz_in.append([c for c in line])
    return puzz_in

# returns True if the crossing 'MAS' words found, don't need boundary scan
def check_word (y, x):
    global puzzle_data, verbose
    corners = [puzzle_data[y-1][x-1], puzzle_data[y-1][x+1], puzzle_data[y+1][x+1], puzzle_data[y+1][x-1]]
    if verbose: print(f"[{x},{y}]: {corners}")
    if corners in [['M','M','S','S'], ['S','M','M','S'], ['S','S','M','M'], ['M','S','S','M']]:
        return True
    return False

if __name__ == "__main__":
    default_filename = f"day{current_day}.input.txt"
    parser = argparse.ArgumentParser(description=f"AoC 2024, day{current_day}")
    parser.add_argument("filename", type=str, nargs='?', default=default_filename, help="input file")
    parser.add_argument("-v", "--verbose", action="store_true", help="enable verbose debug output")
    args = parser.parse_args()
    verbose = args.verbose
    puzzle_data = read_puzzle_input(args.filename)
    final_result = 0

    # look for first character to seed searches
    width = len(puzzle_data[0])
    height = len(puzzle_data)
    for y in range(1, height-1):
        for x in range(1, width-1):
            if puzzle_data[y][x] == 'A':
                if check_word(y, x):
                    print(f"Found at [{x}, {y}]")
                    final_result += 1
    print(f"Result = {final_result}")

# submitted 1822 = correct

# --- Part Two ---
# The Elf looks quizzically at you. Did you misunderstand the assignment?
# 
# Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; 
# it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that 
# is like this:
#     M.S
#     .A.
#     M.S
# 
# Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be 
# written forwards or backwards.
# 
# Here's the same example from before, but this time all of the X-MASes have been kept instead:
#     .M.S......
#     ..A..MSMS.
#     .M.S.MAA..
#     ..A.ASMSM.
#     .M.S.M....
#     ..........
#     S.S.S.S.S.
#     .A.A.A.A..
#     M.M.M.M.M.
#     ..........
# 
# In this example, an X-MAS appears 9 times.
# 
# Flip the word search from the instructions back over to the word search side and try again. How many times does
# an X-MAS appear?
