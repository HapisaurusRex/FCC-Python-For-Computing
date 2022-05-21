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

def condition_example(x, nest):
    if x>0:
        print('Since the value entered is greater than 0 the question asked is answered and it can print this statement')
        if (nest > 1):
            print('we can see that if the nest question is answered correctly, this will show')
    elif x <= 0:
        print('this will print if the value is less than or equal to 0')
        if (nest > 1):
            print('since this conditional is based on the condition before it being met, this outputs a different message at the same level of indentation')
    else:
        print('this code never runs unless something goes wrong, this can be used as a catch all if the if statements dont catch every possible answer to the question')
        #an else statement is manditory, infact if no ifs are met the code just skips the code block entirely

def danger_zone():
    try:
        print('this code is run if the code works without error')
    except:
        print('this code runs if the code nested under the try statement fails to run without error')

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

# Conditional statements ask questions and then run code based on the answer, the questions have to be asked in a specific way which use boolean operators.
# These are: < , <=, ==, >=, >, != or less than, less than or equal to, equal to, greater than or equal to, grater than, and not equal 
# Condiitonal statements can ask a question within a question (called nested statement) and can continue asking questions forever if desired
# Programmers use indents (4 spaces     ) to indicate the scope of the statement (where one statement begins while nested in another statement)
# indents are reduced  if the code segment has ended

# there are several ways to make decisions using these statements

print('one way')
print('if this condition is met, do this, if not met the code block doesnt run')
condition_example(1,0)

print('two way')
print('if this condition is not met, do something else')
condition_example(0,0)

print('multi-way')
print('this variation of two way has multiple ifs to check and')
condition_example(a,0)
# BE cautions with multi way condtional statements as if statements are checked in order, so if x<2 , x<20, and x<10 are listed in that order
# x<10 is never run because everything under 20 satifies the condition before it and that is run instead'

print('try/except')
print('this asks whether the code in the try section works and if it doesnt it runs the code under the except statement instead')
danger_zone()