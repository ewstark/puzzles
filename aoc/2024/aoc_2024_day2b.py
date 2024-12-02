import argparse

verbose = False
current_day = 2

def read_puzzle_input(filename):
    puzz_in = []
    with open(filename, "rt") as f:
        if (verbose): print(f"reading from '{filename}'")
        input_lines = [l.strip() for l in f.readlines() if len(l.strip()) > 0]
        for line in input_lines:
            if (verbose): print(f">> '{line}'")
            vals = line.split(' ')
            puzz_in.append([int(i) for i in vals])
    return puzz_in

def check_line(line):
    if check_permutation(line):
        return True
    for n in range(len(line)):
        l = line[:]
        del l[n]
        if check_permutation(l):
            return True
    return False

def check_permutation(line):
    mode = "none"
    if verbose: print(f"checking {l} ", end='')
    prev = line[0]
    for n in line[1:]:
        diff = n - prev
        if abs(diff) < 1 or abs(diff) > 3:
            if verbose: print(f"diff = {diff}, fail")
            return False
        if mode == "none":
            if n > prev:
                if verbose: print("inc ", end='')
                mode = "inc"
            else:
                if verbose: print("dec ", end='')
                mode = "dec"
        elif mode == "inc":
            if n < prev:
                if verbose: print("n < prev, fail")
                return False
        elif mode == "dec":
            if n > prev:
                if verbose: print("n > prev, fail")
                return False
        else:
            assert(False)
        prev = n
    if verbose: print("pass")
    return True

if __name__ == "__main__":
    default_filename = f"day{current_day}.input.txt"
    parser = argparse.ArgumentParser(description=f"AoC 2024, day{current_day}")
    parser.add_argument("filename", type=str, nargs='?', default=default_filename, help="input file")
    parser.add_argument("-v", "--verbose", action="store_true", help="enable verbose debug output")
    args = parser.parse_args()
    verbose = args.verbose
    puzzle_data = read_puzzle_input(args.filename)
    safe_lines = 0
    if verbose:
        print("Input:")
        for l in puzzle_data:
            print(f"{l}")

    for l in puzzle_data:
        is_safe = check_line(l)
        if is_safe:
            safe_lines += 1
            print(f"{l} is safe")
        else:
            print(f"{l} is UNSAFE")

    print(f"Safe lines = {safe_lines}")

# submitted 520 = correct

# --- Day 2: Red-Nosed Reports ---
# --- Part Two ---
# The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the
# Problem Dampener.
# 
# The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level
# in what would otherwise be a safe report. It's like the bad level never happened!
# 
# Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, 
# the report instead counts as safe.
# 
# More of the above example's reports are now safe:
#    7 6 4 2 1: Safe without removing any level.
#    1 2 7 8 9: Unsafe regardless of which level is removed.
#    9 7 6 2 1: Unsafe regardless of which level is removed.
#    1 3 2 4 5: Safe by removing the second level, 3.
#    8 6 4 4 1: Safe by removing the third level, 4.
#    1 3 6 7 9: Safe without removing any level.
# 
# Thanks to the Problem Dampener, 4 reports are actually safe!
# 
# Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports.
# How many reports are now safe?
