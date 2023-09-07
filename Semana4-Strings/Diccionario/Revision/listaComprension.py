# Include a calculation with a for loop in a range with 2 parameters (lower, upper+1).
def list_years(start, end):
    return [year for year in range(start, end+1)]

# Call the years() function with two parameters.
print(list_years(1972, 1975))
# Should print [1972, 1973, 1974, 1975]



# Use a list comprehension [ ] with a for loop and an if condition.   
def odd_numbers(x, y):
    return [n for n in range(x, y) if n % 2 != 0]

# Call the years() function with two parameters.
print(odd_numbers(5, 15))
# Should print [5, 7, 9, 11, 13]
