print("This is a crash course to learn AI and ML")

name = "Bengal Tiger"
age = 23
print("%s is %d years old." % (name, age))

name = input("Enter your name: ")

age = int(input("Enter your age: "))
print(f'{name} is {age} years old')

x = [3, "hello", 1.2]
print("x[0]: ", x[0])
print("x[1]: ", x[1])
print("x[-1]: ", x[-1])  # the last item
print("x[-2]: ", x[-2])  # the second to last item

# Indexing beyond length
print(x[:100])
print(len(x[:100]))

# Slicing
print("x[:]: ", x[:])  # all indices
print("x[1:]: ", x[1:])  # index 1 to the end of the list
print("x[1:2]: ", x[1:2])  # index 1 to index 2 (not including index 2)
print("x[:-1]: ", x[:-1])  # index 0 to last index (not including last index)


# Creating a list
my_list = [1, 2, 3, "apple", "banana"]

# Accessing elements
print(my_list[0])  # Output: 1
print(my_list[3])  # Output: "apple"

# Modifying elements
my_list[1] = 5
print(my_list)  # Output: [1, 5, 3, "apple", "banana"]

# Adding elements
my_list.append("orange")
print(my_list)  # Output: [1, 5, 3, "apple", "banana", "orange"]

# Removing elements
my_list.remove("apple")
print(my_list)  # Output: [1, 5, 3, "banana", "orange"]

# Slicing
sub_list = my_list[1:4]
print(sub_list)  # Output: [5, 3, "banana"]

# Iterating over a list
for item in my_list:
    print(item)

# Checking if an element is in a list
if "banana" in my_list:
    print("Banana is in the list")

# Length of a list
print(len(my_list))  # Output: 5
# Indexing


# String operations
hello = "Hello"
world = "World"

helloworld = hello + " " + world
print(helloworld)

# String formatting
name = "Alice"
age = 30
formatted_string = f"{name} is {age} years old."
print(formatted_string)
print(type(formatted_string))

# String operations again
text = "Hello, world!"

# Length of the string
print(len(text))  # Output: 13

# Convert to uppercase
uppercase_text = text.upper()
print(uppercase_text)  # Output: HELLO, WORLD!

# Convert to lowercase
lowercase_text = text.lower()
print(lowercase_text)  # Output: hello, world!

# Check if the string starts with a specific substring
starts_with_hello = text.startswith("Hello")
print(starts_with_hello)  # Output: True

# Check if the string ends with a specific substring
ends_with_world = text.endswith("world!")
print(ends_with_world)  # Output: True

# Find the index of a substring
index_of_comma = text.find(",")
print(index_of_comma)  # Output: 5

# Replace a substring with another
new_text = text.replace("world", "Python")
print(new_text)  # Output: Hello, Python!

# Split the string into a list of substrings
words = text.split(" ")
print(words)  # Output: ['Hello,', 'world!']

# Join a list of substrings into a string
joined_text = "-".join(words)
print(joined_text)  # Output: Hello,-world!

# Strip whitespace from the beginning and end of the string
stripped_text = text.strip()
print(stripped_text)  # Output: Hello, world!


# Creating a tuple
my_tuple = (1, 2, 3, "apple", "banana")

# Accessing elements
print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: "apple"

# Tuples are immutable, so you cannot modify elements
# my_tuple[1] = 5  # This will raise an error

# Slicing
sub_tuple = my_tuple[1:4]
print(sub_tuple)  # Output: (2, 3, "apple")

# Iterating over a tuple
for item in my_tuple:
    print(item)

# Checking if an element is in a tuple
if "banana" in my_tuple:
    print("Banana is in the tuple")

# Length of a tuple
print(len(my_tuple))  # Output: 5

# Tuples are immutable, meaning their elements cannot be changed once created.
# This includes deleting elements.

# If you need to remove elements, you can convert the tuple to a list,
# modify the list, and then convert it back to a tuple.

my_tuple = (1, 2, 3, "apple", "banana")

# Convert tuple to list
my_list = list(my_tuple)

# Remove element from list
my_list.remove("apple")

# Convert list back to tuple
new_tuple = tuple(my_list)

print(new_tuple)  # Output: (1, 2, 3, "banana")


# Creating a set
my_set = {1, 2, 3, "apple", "banana"}

# Adding elements
my_set.add("orange")
print(my_set)  # Output: {1, 2, 3, "apple", "banana", "orange"}

# Removing elements
my_set.remove("apple")
print(my_set)  # Output: {1, 2, 3, "banana", "orange"}

# Iterating over a set
for item in my_set:
    print(item)

# Checking if an element is in a set
if "banana" in my_set:
    print("Banana is in the set")

# Length of a set
print(len(my_set))  # Output: 5


# Creating a dictionary to store student information
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "grades": {"math": 90, "science": 85, "english": 92}
}

# Accessing values in the dictionary
print("Student Name:", student["name"])
print("Student Age:", student["age"])
print("Student Major:", student["major"])

# Accessing values within the nested "grades" dictionary
print("Math Grade:", student["grades"]["math"])
print("Science Grade:", student["grades"]["science"])

# Modifying values in the dictionary
student["age"] = 21
student["grades"]["english"] = 95

# Adding a new key-value pair to the dictionary
student["city"] = "New York"

# Iterating through the dictionary and printing key-value pairs
print("\nStudent Information:")
for key, value in student.items():
    print(f"{key}: {value}")

# Checking if a key exists in the dictionary
if "address" in student:
    print("Student Address:", student["address"])
else:
    print("Address information not available.")

# Removing a key-value pair from the dictionary
del student["city"]

# Printing the updated dictionary
print("\nUpdated Student Information:")
for key, value in student.items():
    print(f"{key}: {value}")
