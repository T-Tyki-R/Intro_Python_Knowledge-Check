# Check to see if integer is even or odd
def evenOrOdd(number):
    return "Even" if number % 2 == 0 else "Odd"

print(evenOrOdd(2))
print(evenOrOdd(3))

# Convert integers to strings
def number_to_string(num):
    return str(num)
print(number_to_string(123))

# Remove all whitespaces from strings
def no_space(x):
    return x.replace(" ", "")

print(no_space("Hello World"))
print(no_space("Python Programming"))

# Count how many times each vowels pops up in a string
def get_count(sentence):
    vowels = "aeiouAEIOU"
    count = 0
    for i in sentence:
       if i in vowels:
           count += 1
    return count

print(get_count("Hello World"))