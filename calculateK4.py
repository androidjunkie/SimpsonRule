# Zach Martin, 16 March 2020
#
# calculation of K4 for the simpson's rule code. I plan to use the
# definition of a derivative with a finitely small value for h,
# as well as golden section searching to estimate a rough value for
# k4, which is the maximum value of the fourth derivative of a function

import math

def k4():
    function = 'x**5'
    a0 = 2
    deriv4 = derivative4(function, a0)
    print('fourth derivative is', deriv4)

    
'''
    # here I will use a value of h sufficiently small to estimate the derivative of the function
def derivative4(function, a):
    h = 0.0001
    b=a
    
    f1 = derivative(function, a)
    print('d1 is', f1)
    
    f2 = derivative(function, (a+h))

    deriv2 = (f2-f1)/h
    print('d2 is', deriv2)
    
    a = a+h
    
    f1 = derivative(function, a)
    f2 = derivative(function, (a+h))
    
    deriv2h = (f2-f1)/h
    
    deriv3 = (deriv2h - deriv2)/h
    print('d3 is', deriv3)
    
    
    a = a+h
    
    f1 = derivative(function, a)
    f2 = derivative(function, (a+h))

    deriv2 = (f2-f1)/h
    
    a = a+h
    
    f1 = derivative(function, a)
    f2 = derivative(function, (a+h))
    
    deriv2h = (f2-f1)/h
    
    deriv3h = (deriv2h - deriv2)/h
    
    deriv4 = (deriv3h-deriv3)/h
    
    print('d4 is', deriv4)
    

    return deriv2

'''
def derivative4(function, a, h=0.00001):
    f1 = derivative3(function, a+h)
    f2 = derivative3(function, a)
    deriv4 = (f1-f2)/h
    print('f1', f1)
    
    print('f2', f2)
    
    
    return deriv4

def derivative3(function, a, h=0.00001):
    f1 = derivative2(function, a+h)
    f2 = derivative2(function, a)
    deriv3 = (f1-f2)/h
    print('deriv3', deriv3)
    
    return deriv3

def derivative2(function, a, h=0.00001):
    f1 = derivative(function, a+h)
    f2 = derivative(function, a)
    deriv2 = (f1-f2)/h
    print('deriv2', deriv2)
    
    return deriv2

def derivative(function, a, h=0.00001):
    x = a + h
    f1 = eval(function)
    x = a
    f2 = eval(function)
    deriv = (f1-f2)/h
    print('deriv1', deriv)
    return deriv


k4()
    
