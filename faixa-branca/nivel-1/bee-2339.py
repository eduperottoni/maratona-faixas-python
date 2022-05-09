competitors, papers, per_comp = [int(x) for x in input().split()]

if competitors*per_comp <= papers:
    print('S')
else:
    print('N') 