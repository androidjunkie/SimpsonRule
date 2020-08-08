# simpsonsRule.py
# A program which esimates the value of a definite integral or a 
# range of sequential y-values for which x1 < x2 for y(x). 
# Currently only evaluates a set of values, as entering functions and differentiating opens a whole other can of worms
# Zachary Martin, Math 141H Spring 2020

import math

def main():
    print("Welcome to the Simpson's rule calculator. This calculator estimates the value of a set of y-values")
    print('which cannot be evaluated by the usual methods of line of best fit and integration in Excel, for example.')
    yVals, n, a, b = getYVals()
    
    ySum = 0
    for i in yVals:
        ySum += i
    simp = (1/3) * ((b - a)/n) * ySum
        
    print("The value for the Simpson's rule estimation to 4 decimal places is:" , format(simp, ',.4f'), '.', sep='')


# gets the y vals 'yVals' for the summation to be completed in main()
def getYVals():
    yVals = [] 
    
    while(True): # This loop prompts the user to choose a function or a set of y values
        valOrfunc = input('Enter f for a function or v for a set of y-values')
        if(valOrfunc.upper() == 'F'):
            function = True
            break
        elif(valOrfunc.upper() == 'V'):
            function = False
            break
        else:
            print('Incorrect value entered. Please retry.')
            
    if(function): # This loop approximates the integral of a function using simpson's rule
        print('Function not currently supported, sorry.')

        a, b = getBounds()
        string = 'Please enter your error as a decimal: '
        error = input(string)
        error = convertToNum(error, string)
        # Sympy stuff 4th derivative somewhere here. Calculates fourth derivative of f(x) for error calculation
        # error calculation using 4th derivative a la sympy
        deltax = (b-a)/n
        function, base = mathFunction()
        # then we need to evaluate the function with eval() and change the value of x for each time
        x = a
        for i in range(n):
            yVals.append(eval(function))
            x += deltax
            
            
        
        
    # todo: figure out a way of getting a function from a user and computing the error of it
    # using derivatives.
    # todo: if figured out, then add conditional statements for choosing value-based simpson's rule
    # or function-based simpson's rule
    else: # This loop approximates the area under a discontinous bunch of data points.
        print('\nHead\'s up: In order to properly use Simpson\'s rule, you must have an even number of data points, or an odd number of delta x\'s.\n\n')
        print('This version of the calculator assumes that each data point is seperated evenly along the independent variable line.')
        i = 0
        coeffs = 1
        while(True): # This loop handles the 1,4,2...2,4,1 rule for the coefficients of the y-values in simpson's rule summation.
            valOrQuit = input('Enter y-value number ' + str(i+1) + ' or q to finish: ')
                
            if(valOrQuit.upper() != 'Q'):
                valOrQuit = convertToNum(valOrQuit)
                lastNum = valOrQuit
                if(i%2 == 0 and i!=0):
                    coeffs = 2
                    i += 1
                elif((i+1)%2 == 0):
                    coeffs = 4
                    i += 1
                else:
                    i+=1
                yVals.append(coeffs*valOrQuit)
            else:
                coeffs = 1
                yVals[-1] = coeffs*lastNum
                a, b = getBounds()
                break
            
    return yVals, i, a, b

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

def getBounds():
    msg1 = 'Please enter the lower bound of the interval: '
    a = input(msg1)
    a = convertToNum(a, msg1)
    
    msg2 = 'Please enter the upper bound of the interval: '
    b = input(msg2)
    b = convertToNum(b, msg2)
    
    return a,b
            
            
# This function converts an input to a number or else returns an error 
# message and retries the input.
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
'''
def k4(function):
    
def derivative(function):
    # this function ESTIMATES the derivative using the definition of a derivative. It's somewhat janky, but close enough for our purposes
    deriv = 'not yet deriv'
'''
        

main()
