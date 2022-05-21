# Comments (#) 
# Python ignores anything after '#'. We can use this to explain code, document who wrote the core or
# Temporarily disable code (to debug)

# Functions store a set of instructions to be reused over and over again (Saving time and effort)
# Functions can be built in such as 'print()' and 'int()' or self defined

def watch(parameter): #arguments get converted to parameters which allows us to do the same thing with slightly different variables
    print('The arguments added to the function become the parameters. we can see the first below:')
    print(parameter) 
    print('note this function does not return any value so it is a void function')

def addition(a, b):
    print('this function returns a value when called aka a fruitful function')
    temp = a + b
    return temp

# Variables store changing or not changing information. The variables have to start with a letter or '_'.
# Variables can only use letters, numbers or "_".
# When naming them it is important to choose a name that helps you remember what is in there

const_var = "this value does not change"
_variable = addition(1,2)

# Expressions do things with variables, mathematically they follow PEMDAS and from left to right should any issues arise.
# Mathematical expressions are: + - * / % (**) or addition, subtraction, multiplication, division, remainder and power
# these symbols are used because we don't have mathmatical symbols in computer keyboards
# % - remainder means the amount left after division (24/5) the remainder is 4
# Keep mathmatical expressions are simple as possible and split up long expressions where possible

a = 1
b = 2
c = 3

PEMDAS_EG = a - (b*c)**b  #brackets are done first, then power, then subtraction
