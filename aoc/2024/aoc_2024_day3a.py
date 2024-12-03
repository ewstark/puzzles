import argparse
import re

verbose = False
current_day = 3

def read_puzzle_input (filename):
    puzz_in = []
    with open(filename, "rt") as f:
        if (verbose): print(f"reading from '{filename}'")
        input_lines = [l.strip() for l in f.readlines() if len(l.strip()) > 0]
        for line in input_lines:
            if (verbose): print(f">> '{line}'")
            puzz_in.append(line)
    return puzz_in

# regex search string = "mul\(\d{1,3}\,\d{1,3}\)"
mul_re = re.compile("mul\(\d{1,3}\,\d{1,3}\)")

def extract_muls (line_text):
    global mul_re
    line_result = 0
    search_result = mul_re.findall(line_text)
    for r in search_result:
        vals = [int(v) for v in r[4:-1].split(',')]
        if verbose: print(f"{r} = {vals}")
        line_result += vals[0] * vals[1]
    return line_result


if __name__ == "__main__":
    default_filename = f"day{current_day}.input.txt"
    parser = argparse.ArgumentParser(description=f"AoC 2024, day{current_day}")
    parser.add_argument("filename", type=str, nargs='?', default=default_filename, help="input file")
    parser.add_argument("-v", "--verbose", action="store_true", help="enable verbose debug output")
    args = parser.parse_args()
    verbose = args.verbose
    puzzle_data = read_puzzle_input(args.filename)
    final_result = 0

    for line_number, line_text in enumerate(puzzle_data):
        line_result = extract_muls(line_text)
        print(f"line {line_number} result = {line_result}")
        final_result += line_result

    print(f"Result = {final_result}")

# submitted 174336360 = correct

# --- Day 3: Mull It Over ---
# "Our computers are having issues, so I have no idea if we have any Chief Historians in stock! You're welcome to check
# the warehouse, though," says the mildly flustered shopkeeper at the North Pole Toboggan Rental Shop. The Historians
# head out to take a look.
#
# The shopkeeper turns to you. "Any chance you can see why our computers are having issues again?"
#
# The computer appears to be trying to run a program, but its memory (your puzzle input) is corrupted. All of the
# instructions have been jumbled up!
#
# It seems like the goal of the program is just to multiply some numbers. It does that with instructions like mul(X,Y),
# where X and Y are each 1-3 digit numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024.
# Similarly, mul(123,4) would multiply 123 by 4.
#
# However, because the program's memory has been corrupted, there are also many invalid characters that should be
# ignored, even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.
#
# For example, consider the following section of corrupted memory:
#    xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
#     ********                    ********                *****************
#
# Only the four highlighted sections are real mul instructions. Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).
#
# Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?