cont_testes = 0
while True:
    cont_testes += 1
    loops = int(input())

    if loops == 0:
        break
    else:
        print(f'Teste {cont_testes}')
        sum_piggy0 = 0
        sum_piggy1 = 0
        for loop in range(loops):
            p0, p1 = [int(x) for x in input().split()]
            sum_piggy0 += p0
            sum_piggy1 += p1
            print(sum_piggy0 - sum_piggy1)
        print('')
