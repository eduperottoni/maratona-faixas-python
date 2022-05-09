container = [cont_width, cont_length, cont_height] = [int(x) for x in input().split()]
ship = [ship_width, ship_length, ship_height] = [int(x) for x in input().split()]

measures = []
for index, measure in enumerate(container):
    measures.append(ship[index]//measure)

cont = 1
for measure in measures: cont *= measure

print(cont)
