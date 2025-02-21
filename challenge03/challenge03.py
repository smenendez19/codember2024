import os
import sys

movements_file = open(os.path.join(os.path.dirname(sys.argv[0]), "trace.txt"), "r")

movements_list = movements_file.read().split("\n")

result_final = 0

for movements in movements_list:
    instructions = list(map(int, movements.split(" ")))
    i = 0
    result = 0
    print(instructions)
    while i < len(instructions) and i > -1:
        prev_i = i
        i += instructions[prev_i]
        if instructions[prev_i] >= 0:
            instructions[prev_i] += 1
        else:
            instructions[prev_i] -= 1
        result += 1

    print(instructions, result)
    result_final += result

print("Final:", result_final)
