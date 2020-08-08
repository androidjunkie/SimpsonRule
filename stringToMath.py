# an attempt at interpreting inputted strings using string slicing/arguments
# and using them to manipulate the math inside of a python function... 
# This function will be utilized for the simpsonsRule.py program's approximation of the area under a curve 
# using Simpson's rule... we'll see how far this goes
# Zach Martin, March 2020

import math

def main():
    functionString, base = mathFunction()
    print('The evaluation of the inputted expression is: ' +str(eval(functionString)) + '.')

# notes:
# only allows independent variable of x. Limited in scope of math operators.
# todo: print the syntax rules
# todo: handle cases of e^(u)
# todo: broaden scope to fourth derivative using sympy

def mathFunction():
    string1 = """Syntax rules:
    This program accepts the standard multiplication, division, addition, and subtraction operators eg * / + -.
    The ONLY independent variable allowed MUST be denoted "x". (Note: currently, as a calculator, this point is moot anyways)
    Natural logarithms are written as "ln" and logarithms with any other base are written as "log." 
    The base for those logarithms will be asked after the input is given. DO NOT input the base until prompted.
    Natural exponents are written as e^(power) and must always include parentheses (eg e^(x) ). 
    Roots must be written as fractional powers (eg square root of 5 is written 5^(1/2) )
    Trigonometric and hyperbolic functions aren't supported.
    """
    print(string1)
    while(True):
        mathStr = input('Please enter your math string using the syntax rules: ')
        evalStr = ''
        maybeLog = ''
        numLogs = 0
        for i in mathStr:
            try:
                float(i)
                evalStr += i
            except ValueError:
                if(i=='x'):
                    evalStr += i
                elif(i in {'(', ')', '*', '+', '-', '/', '.', ','}): # the sequence allows for multiple comparisons of i. 
                                                           # In this case, all of the operators in the sequence are naturally evaluated by python. 
                    evalStr += i
                elif(i=='^'):
                    evalStr += '**'
                elif(i in {'l', 'n', 'o', 'g', 'e'}):
                    maybeLog += i
                    if(maybeLog == 'ln'):
                        evalStr += 'math.log'
                        maybeLog = ''
                        continue                # is this continue necessary???
                    elif(maybeLog == 'log'):
                        evalStr += '(1/math.log(base))*math.log' # uses log rules to rewrite the log in terms of ln. Easier to deal with in math module, less input.
                        numLogs += 1
                        base = input('Please enter the base of logarithm number ' + str(numLogs) + ': ')
                        base = convertToNum(base)
                        maybeLog = ''
                        continue
                    elif(maybeLog =='e^'):
                        evalStr += 'math.exp'
                        maybeLog = ''
                        continue
                else:
                    print('Input error. This calculator doesn\'t know what to do with your value or operator "' + i + '." Please re-enter your math string.')
                    break
        break
    return evalStr, base
    
def convertToNum(val, msg = 'Please re-enter value: '):
    errMsg = 'Incorrect value entered! '
    while(True):
        try:
            val = int(val)
            break
        except ValueError:
            try:
                val = float(val)
                break
            except ValueError:
                val = input(errMsg + msg)
    return val
    
main()
