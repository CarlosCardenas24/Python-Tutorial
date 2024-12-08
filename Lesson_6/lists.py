users = ['Carlos', 'Lola', 'Nala']

data = ['Carlos', 42, True]

emptylist = []

print("Carlos" in emptylist)

print(users[0])
print(users[-2])

print(users.index('Nala'))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

users.append('Jasmin')
print(users)

users += ['Tiger']
print(users)

users.extend(['Odin', 'Selene'])
print(users)

# users.extend(data)
# print(users)

users.insert(0, 'Camerina')
print(users)

users[2:2] = ['Riku', 'Spawn']
print(users)

users[1:3] = ['Armando', 'Juan']
print(users)

users.remove('Camerina')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

users[1:2] = ['carlos']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, "Neir", True])
print(mylist)

# Tuples

mytuple = tuple(('Carlos', 42, True))

anothertuple = (1, 4, 2, 8, 2, 2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Neir')
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))