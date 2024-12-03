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

mul_re = re.compile("mul\\(\\d{1,3}\\,\\d{1,3}\\)|do\\(\\)|don\\'t\\(\\)")

muls_enabled = True

def extract_muls (line_text):
    global mul_re, muls_enabled
    line_result = 0
    search_result = mul_re.findall(line_text)
    for r in search_result:
        if r[0] == 'm':  # mul
            vals = [int(v) for v in r[4:-1].split(',')]
            if muls_enabled:
                if verbose: print(f"adding {vals} = {vals[0] * vals[1]}")
                line_result += vals[0] * vals[1]
            else:
                if verbose: print(f"skipping {vals}")
        elif r[2] == 'n':  # don't
            muls_enabled = False
        else:  # do
            muls_enabled = True
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

# submitted 98826679 = too high
# Corrected code to retain enable/disable state across input lines
# submitted 88802350 = correct

# --- Part Two ---
# As you scan through the corrupted memory, you notice that some of the conditional statements are also still intact.
# If you handle some of the uncorrupted conditional statements in the program, you might be able to get an even more
# accurate result.
#
# There are two new instructions you'll need to handle:
#
# The do() instruction enables future mul instructions.
# The don't() instruction disables future mul instructions.
# Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.
#
# For example:
#    xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
#
# This corrupted memory is similar to the example from before, but this time the mul(5,5) and mul(11,8) instructions are
# disabled because there is a don't() instruction before them. The other mul instructions function normally, including
# the one at the end that gets re-enabled by a do() instruction.
#
# This time, the sum of the results is 48 (2*4 + 8*5).
#
# Handle the new instructions; what do you get if you add up all of the results of just the enabled multiplications?
