print("hello world")

# Python as a calculator
1 + 2 # addition
6 * 7 # multiplication
5 - 3 # subtraction
15 / 3 # division
17 / 3 # ???

# Data types
type(17)
type(3)
type(3.0)
type("hello")
type(17/3)
type(17/3.0)

17 / 3.0 # there we go

# Ints
# can an int be negative?
# can you turn a string into a number?
# can you turn a float into an int?
# what happens when you try to turn "hello" into an int?

# Floats
# can a float be negative?
# can you turn a string into a float? an int into a float?
# what happens when you add an int and a float?


# Strings
# what happens when you add two strings?
# what happens when you multiply a string by an int? by a float?
# can you subtract strings?
# what happens when you add a string and an int?

"hello"[1]
"hello"[0]
"hello"[-1]
"hello"[1:-1]
"hello"[-1:1]
len("hello")

# True and False
1 == 1
1 == 2
1 == 1.0
1 == '1'

True and True
True and False
False and False
True or False

(1 == 1) and (1 == 2)
len("hello") == len("world")


# Variables
x = 1
y = 2
z = x + y
print(z)
x = x + 1
print(x)
print(z)


# Functions
def my_function():
  print "hello world"

def inconsistent():
  print "line one"
    print "line two"
  print "line three"

my_function()

def show_word(word):
  print("hello " + str(word))

def multiply(num1, num2):
    print(num1 * num2)

show_word("cat")
show_word("dog")

output = show_word("cat")
print(output)

# write a function for z that updates when x and y change
x = 1
y = 2
# z = x + y
def z(x, y):
    return x + y


# returning output
def greet_word(word):
  return "hello " + word

output = greet_word("dog")
print(output)

def double(number):
  return number * 2

double(2)
double(3.0)
double('hello')
double(double(4))

# List
len([1, 2, 3])

# iteration
myList = [8, 6, 7, 5, 3, 0, 9]
for number in myList:
  print(number)
  print(number * 2)
  print("-----")

for value in myList:
  print(value)


if 5 in myList:
  print("yes")

if 10 in myList:
  print("yes")
else:
  print("no")


def check_in_list(value, collection):
  if value in collection:
    print("yes")
  else:
    print "no"

