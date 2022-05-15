password = 2002
while True:
    attempt = int(input())
    if password != attempt:
        print('Senha Invalida')
        continue
    else:
        print('Acesso Permitido')
        break