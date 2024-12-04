import argparse
import re

verbose = False
current_day = 4

puzzle_data = []
width = 0
height = 0
search_word = ['X', 'M', 'A', 'S']

def read_puzzle_input (filename):
    puzz_in = []
    with open(filename, "rt") as f:
        if (verbose): print(f"reading from '{filename}'")
        input_lines = [l.strip() for l in f.readlines() if len(l.strip()) > 0]
        for line in input_lines:
            if (verbose): print(f">> '{line}'")
            puzz_in.append([c for c in line])
    return puzz_in

# returns True if the search_word is found in the puzzle starting at [x,y] and proceeding [dx,dy]
def check_word (y, x, dy, dx):
    global puzzle_data, width, height, search_word
    word_len = len(search_word)
    for c in search_word:
        if y < 0 or y >= height or x < 0 or x >= width:
            return False
        if c != puzzle_data[y][x]:
            return False
        x += dx
        y += dy
    return True

def count_words (y, x):
    global puzzle_data, width, height, search_word
    found_words = 0;
    if check_word(y, x,  0, -1):
        found_words += 1
        print("left ", end='')
    if check_word(y, x,  0,  1):
        found_words += 1
        print("right ", end='')
    if check_word(y, x, -1, -1):
        found_words += 1
        print("UL ", end='')
    if check_word(y, x, -1,  0):
        found_words += 1
        print("up ", end='')
    if check_word(y, x, -1,  1):
        found_words += 1
        print("UR ", end='')
    if check_word(y, x,  1, -1):
        found_words += 1
        print("DL ", end='')
    if check_word(y, x,  1,  0):
        found_words += 1
        print("down ", end='')
    if check_word(y, x,  1,  1):
        found_words += 1
        print("DR ", end='')
    return found_words

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
    for y in range(height):
        for x in range(width):
            if puzzle_data[y][x] == search_word[0]:
                found_words = count_words(y, x)
                if found_words > 0:
                    print(f"Found {found_words} at [{x}, {y}]")
                    final_result += found_words
    print(f"Result = {final_result}")

# submitted 2401 = correct

# --- Day 4: Ceres Search ---
# "Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button
# on it. After a brief flash, you recognize the interior of the Ceres monitoring station!
# 
# As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to
# know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.
# 
# This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping
# other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need
# to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:
#    ..X...
#    .SAMX.
#    .A..A.
#    XMAS.S
#    .X....
#
# The actual word search will be full of letters instead. For example:
#    MMMSXXMASM
#    MSAMXMSMSA
#    AMXSXMAAMM
#    MSAMASMSMX
#    XMASAMXAMM
#    XXAMMXXAMA
#    SMSMSASXSS
#    SAXAMASAAA
#    MAMMMXMMMM
#    MXMXAXMASX
# 
# In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters 
# not involved in any XMAS have been replaced with .:
#    ....XXMAS.
#    .SAMXMS...
#    ...S..A...
#    ..A.A.MS.X
#    XMASAMX.MM
#    X.....XA.A
#    S.S.S.S.SS
#    .A.A.A.A.A
#    ..M.M.M.MM
#    .X.X.XMASX
# 
# Take a look at the little Elf's word search. How many times does XMAS appear?
