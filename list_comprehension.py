"SYNTAX: new_list = [expression for item in list if condition == True]"
numbers = [1, 2, 3, 4, 5]

doubled_numbers = [num * 2 for num in numbers]
# print(doubled_numbers)

list_range = [i for i in range(11) if i % 2 == 0]
# print(list_range)

"FOR LOOP vs LIST COMPREHENSION"
# For Loop to square each element
square_numbers = []
for num in numbers:
    square_numbers.append(num ** 2)
# print(square_numbers)

# List Comprehension
squared_numbers = [num ** 2 for num in numbers]
# print(squared_numbers)

"CONDITIONALS IN LIST COMPREHENSION"
# Filter out even numbers from a list
even_numbers = [num for num in range(1, 10) if num % 2 == 0]
# print(even_numbers)

"LIST COMPREHENSION IN STRINGS"
word = "Python"
vowels = "aeiou"
vowels_in_python = [vowel for vowel in word if vowel in vowels]
print(vowels_in_python[0])

