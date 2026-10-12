p = "Python"
c = "Coding"

# 1. 
print(p[6:])
#  an empty string

# 2. 
print(p[::-1])
#  nohtyP

# 3.
p += c
print(p)
# PythonCoding

# 4. 
p = "Mython"

try:
    p[0] = "P"
except TypeError as error:
    print(type(error).__name__)
# TypeError
# Original list
rgb = ["R", "G", "B"]

# Both variables reference the same list
rgb_copy = rgb
rgb_copy.append("A")

print(rgb_copy)
# ['R', 'G', 'B', 'A']

print(rgb)
# ['R', 'G', 'B', 'A']

print(id(rgb) == id(rgb_copy))
# True

# Create an independent copy
rgb = ["R", "G", "B"]
correct_rgb_copy = rgb[:]
correct_rgb_copy.append("A")

print(correct_rgb_copy)
# ['R', 'G', 'B', 'A']

print(rgb)
# ['R', 'G', 'B']

print(id(rgb) == id(correct_rgb_copy))
# False
# Sample list
numbers = [-3, 5, -1, 7, 0, -8, 10]

count = 0

for number in numbers:
    if number > 0:
        count += 1

print("Count of positive numbers:", count)

def filter_even_numbers(numbers):
    # Create an empty result list
    result = []

    # Check every number
    for number in numbers:
        if number % 2 == 0:
            result.append(number)

    return result


# Test the function
test = [1, 2, 3, 4, 5, 6, 7, 8]

print(filter_even_numbers(test))