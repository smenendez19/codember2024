code = "528934712834"
moves = "URDURUDRUDLLLLUUDDUDUDUDLLRRRR"

code = list(map(int, code))


def left(code, i):
    if i == 0:
        return code, len(code) - 1
    return code, i - 1


def right(code, i):
    if i == len(code) - 1:
        return code, 0
    return code, i + 1


def up(code, i):
    if code[i] > 8:
        code[i] = 0
        return code, i
    code[i] = code[i] + 1
    return code, i


def down(code, i):
    if code[i] < 1:
        code[i] = 9
        return code, i
    code[i] = code[i] - 1
    return code, i


i = 0

moves_commands = {"U": up, "D": down, "L": left, "R": right}

print(code, moves)

for move in moves:
    code, i = moves_commands[move](code, i)

print("".join(list(map(str, code))))
