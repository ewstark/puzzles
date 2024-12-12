import argparse

verbose = False
current_day = 7

def read_puzzle_input (filename):
    equations = []  # contains tuple (target, [values]) for each equation
    with open(filename, "rt") as f:
        input_lines = [l.strip() for l in f.readlines()]
        for line in input_lines:
            fields = line.split(' ')
            target = int(fields[0][:-1])
            values = [int(i) for i in fields[1:]]
            equations.append((target, values))
    return equations

def seeker (target, running, values):
    if len(values) == 1:
        if running + values[0] == target: return True
        if running * values[0] == target: return True
        if int(str(running)+str(values[0])) == target: return True
        return False
    if seeker(target, running + values[0], values[1:]): return True
    if seeker(target, running * values[0], values[1:]): return True
    if seeker(target, int(str(running)+str(values[0])), values[1:]): return True
    return False

def test_validation (target, values):
    global verbose
    if verbose: print(f"Checking: {target} : {', '.join([str(_) for _ in values])}", end=' - ')
    if seeker(target, values[0], values[1:]):
        if verbose: print("GOOD")
        return target
    if verbose: print("bad")
    return 0

if __name__ == "__main__":
    default_filename = f"day{current_day}.input.txt"
    parser = argparse.ArgumentParser(description=f"AoC 2024, day{current_day}")
    parser.add_argument("filename", type=str, nargs='?', default=default_filename, help="input file")
    parser.add_argument("-v", "--verbose", action="store_true", help="enable verbose debug output")
    args = parser.parse_args()
    verbose = args.verbose

    equations = read_puzzle_input(args.filename)
    total_calibration = 0

    if verbose:
        print(f"{len(equations)} input equations:")
        for e in equations:
            print(f"   {e[0]} : {' ? '.join([str(_) for _ in e[1]])}")
        print()

    for e in equations:
        total_calibration += test_validation(e[0], e[1])

    print(f"Result = {total_calibration}")

# submitted 438027111276610 = correct

# --- Part Two ---
# The engineers seem concerned; the total calibration result you gave them is nowhere close to being within safety
# tolerances. Just then, you spot your mistake: some well-hidden elephants are holding a third type of operator.
# 
# The concatenation operator (||) combines the digits from its left and right inputs into a single number. For example,
# 12 || 345 would become 12345. All operators are still evaluated left-to-right.
# 
# Now, apart from the three equations that could be made true using only addition and multiplication, the above example
# has three more equations that can be made true by inserting operators:
#     156: 15 6 can be made true through a single concatenation: 15 || 6 = 156.
#     7290: 6 8 6 15 can be made true using 6 * 8 || 6 * 15.
#     192: 17 8 14 can be made true using 17 || 8 + 14.
# 
# Adding up all six test values (the three that could be made before using only + and * plus the new three that can now
# be made by also using ||) produces the new total calibration result of 11387.
# 
# Using your new knowledge of elephant hiding spots, determine which equations could possibly be true. What is their
# total calibration result?
