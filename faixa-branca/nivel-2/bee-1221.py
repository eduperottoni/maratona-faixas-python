test_cases = int(input())
prime_numbers = []

for test in range(test_cases):
    number = int(input())
    factors = 0

for n in range(number,0,-1):
    if n % 2 != 0:
        if number % n == 0:
            factors += 1
if factors == 1:
    print('Prime')
else:
    print('Not Prime')
