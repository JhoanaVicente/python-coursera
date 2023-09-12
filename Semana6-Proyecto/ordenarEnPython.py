numbers = [4, 6, 2, 7,1]
numbers.sort()
print(numbers)

names = ["Carlos", "Ray", "Alex", "Kelly"]
print(names)
print(sorted(names))
print(names)
# Sorted returns a new list, while sort returns the same list reorganized.

# Ordena elementos de una lista basados en el valor de retorno de una función.
print(sorted(names, key=len))
