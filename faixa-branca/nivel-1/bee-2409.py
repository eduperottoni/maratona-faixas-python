measures = [int(x) for x in input().split()]
door = [height, width] = [int(x) for x in input().split()]

measures_ordered = sorted(measures)
door_ordered = sorted(door)

cont_pass = 0
for measure in measures_ordered:
    for index, dimension in enumerate(door_ordered):
        if measure <= dimension:
            cont_pass += 1
            door_ordered[index] = 0
            break

if cont_pass >= 2: print('S')
else: print('N')
