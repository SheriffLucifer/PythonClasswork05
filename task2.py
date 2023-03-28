n = int(input('Введите любое целое число: '))

def primeNumber(n):
    result = True
    for i in range(2, n):
        if n % i == 0:
            result = False
    return result

def getNumber(n):
    if primeNumber(n) == False:
        for i in range(2, n):
            if n % i == 0 and primeNumber(i) == True:
                print(i, end = ' ')
                getNumber(n // i)
                break
    else:
        print(n)

getNumber(n)