numbers = input('Введите несколько целых чисел: ').split()
print(numbers)
print(sum(numbers.count(x) - 1 for x in numbers) // 2)

