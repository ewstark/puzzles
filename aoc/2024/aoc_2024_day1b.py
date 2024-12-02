import argparse

verbose = False
current_day = 1

def read_puzzle_input(filename):
    l1 = []
    l2 = []
    with open(filename, "rt") as f:
        if (verbose): print(f"reading from '{filename}'")
        input_lines = [l.strip() for l in f.readlines() if len(l.strip()) > 0]
        for line in input_lines:
            vals = [int(i) for i in line.split('   ')]
            if (verbose): print(f"{vals}")
            l1.append(vals[0])
            l2.append(vals[1])
    return (l1, l2)

def render_puzzle(puzzle_input):
    for line in puzzle_input:
        print(line)

def counted_list(as_list):
    as_dict = {}
    for n in set(as_list):
        as_dict[n] = as_list.count(n)
    return as_dict

if __name__ == "__main__":
    default_filename = f"day{current_day}.input.txt"
    parser = argparse.ArgumentParser(description=f"AoC 2024, day{current_day}")
    parser.add_argument("filename", type=str, nargs='?', default=default_filename, help="input file")
    parser.add_argument("-v", "--verbose", action="store_true", help="enable verbose output")
    args = parser.parse_args()
    verbose = args.verbose
    puzzle_data = read_puzzle_input(args.filename)
    if verbose: print(f"Input = {puzzle_data}")

    d1 = counted_list(puzzle_data[0])
    d2 = counted_list(puzzle_data[1])
    if verbose:
        print(f"d1: {d1}")
        print(f"d2: {d2}")
    running_score = 0
    for d in d1:
        if verbose: print(f"Looking for {d}... ", end='')
        if d in d2:
            factor = d * d1[d] * d2[d]
            if verbose: print(f"found, d1[d]={d1[d]} d2[d]={d2[d]} = {factor}")
            running_score += factor
        else:
            if verbose: print("not found")
    print(f"Total = {running_score}")

# submitted 26674158 = correct
# 
# --- Part Two ---
# Your analysis only confirmed what everyone feared: the two lists of location IDs are indeed very different.
# 
# Or are they?
# 
# The Historians can't agree on which group made the mistakes or how to read most of the Chief's handwriting, but in 
# the commotion you notice an interesting detail: a lot of location IDs appear in both lists! Maybe the other numbers
# aren't location IDs at all but rather misinterpreted handwriting.
# 
# This time, you'll need to figure out exactly how often each number from the left list appears in the right list.
# Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of
# times that number appears in the right list.
# 
# Here are the same example lists again:
#    3   4
#    4   3
#    2   5
#    1   3
#    3   9
#    3   3
#
# For these example lists, here is the process of finding the similarity score:
#    * The first number in the left list is 3. It appears in the right list three times, so the similarity score increases by 3 * 3 = 9.
#    * The second number in the left list is 4. It appears in the right list once, so the similarity score increases by 4 * 1 = 4.
#    * The third number in the left list is 2. It does not appear in the right list, so the similarity score does not increase (2 * 0 = 0).
#    * The fourth number, 1, also does not appear in the right list.
#    * The fifth number, 3, appears in the right list three times; the similarity score increases by 9.
#    * The last number, 3, appears in the right list three times; the similarity score again increases by 9.

# So, for these example lists, the similarity score at the end of this process is 31 (9 + 4 + 0 + 0 + 9 + 9).
# 
# Once again consider your left and right lists. What is their similarity score?
