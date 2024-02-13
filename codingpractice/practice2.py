from functools import reduce

# lambda, map, filter, and reduce are functions that are primarily applicable to iterable data types such as lists, tuples, and sets. They are designed to work with sequences of data

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)


listofli = list(map(lambda x: (x*2), li))
print(listofli)


ages = [13, 90, 17, 59, 21, 60, 5]

adults = list(filter(lambda x: (x < 18), ages))
print(adults)

age = (13, 90, 34, 28, 49, 57, 37, 59, 50, 46, 90, 100)

adult = tuple(filter(lambda x: x < 18, age))

print(adult)

# reduce function
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x + y, numbers)
print(f"Reduce Method:  {product}")

lis = [1, 3, 5, 6, 2, ]
print("The maximum element of the list is : ", end="")
print(reduce(lambda a, b: a if a > b else b, lis))
