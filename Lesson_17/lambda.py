squared = lambda num : num * num
# def squared(num): return num * num

print(squared(2))

addTwo = lambda num : num + 2
# def addTwo(num): return num + 2

print(addTwo(12))

sum_total = lambda a, b : a + b
# def sum(a, b): return a + b

print(sum_total(21, 62))

########################

def funcBuilder(x):
    return lambda num : num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

##########################

lambda num : num * num

numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num : num * num, numbers)
print(list(squared_nums))

##########################

lambda num : num % 2 != 0

odd_nums = filter(lambda num : num % 2 != 0, numbers)
print(list(odd_nums))

##########################

from functools import reduce

lambda acc, curr: acc + curr

numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)
print(total)

print(sum(numbers, 10))

lambda acc, curr: acc + len(curr)

names = ["Carlos Cardenas", "Lola Idontknow", "Nala Something Random"]

char_count= reduce(lambda acc, curr: acc + len(curr), names, 0)
print(char_count)