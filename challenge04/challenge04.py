import json
import os
import sys

network_file = open(os.path.join(os.path.dirname(sys.argv[0]), "network.txt"), "r")

list_nodes = network_file.read()
nodes = json.loads(list_nodes)

groups = []

for pair in nodes:
    exists = False
    for group in groups:
        if pair[0] in group and pair[1] not in group:
            group.add(pair[1])
            exists = True
            break
        if pair[0] not in group and pair[1] in group:
            group.add(pair[0])
            exists = True
            break
        if pair[0] in group and pair[1] in group:
            exists = True
            break

    if not exists:
        groups.append(set(pair))

merged_groups = []

for i in range(0, len(groups)):
    for j in range(i + 1, len(groups)):
        if groups[i].intersection(groups[j]):
            groups[i] = groups[i].union(groups[j])
            groups[j] = set()

saved_groups = []

for group in groups:
    if len(group) == 2:
        saved_groups.append(group)


saved_nodes = []

for group in saved_groups:
    saved_nodes += list(group)

sorted_nodes = sorted(saved_nodes)

print(",".join(list(map(str, sorted_nodes))))
