nodes = [
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    31,
    32,
    33,
    34,
    35,
    36,
    37,
    38,
    39,
    40,
    41,
    42,
    43,
    44,
    45,
    46,
    47,
    48,
    49,
    50,
    71,
    72,
    73,
    74,
    75,
    76,
    77,
    78,
    79,
    80,
    81,
    82,
    83,
    84,
    85,
    86,
    87,
    88,
    155,
    156,
    157,
    158,
    175,
    176,
    177,
    178,
    179,
    180,
    181,
    182,
    183,
    184,
    195,
    196,
]


def check_prime_number(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


prime_nodes = []

for node in nodes:
    if not check_prime_number(node):
        continue
    else:
        sum_node = sum([int(i) for i in str(node)])
        print(node, sum_node)
        if check_prime_number(sum_node):
            prime_nodes.append(node)

print(f"{len(prime_nodes)}-{prime_nodes[2]}")
