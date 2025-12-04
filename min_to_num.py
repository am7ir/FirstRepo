'''
This program compute your legal age
Amirr
'''

def get_min(x,y):
    '''
    Docstring for get_min
    این تایع بین دو عدد کوپکترین را پیدا می کند و بر می گرداند
    :param x: عدد اول
    :param y: عدد دوم
    '''
    mn = x
    if y< x:
        mn = y
    return y

a = float(input("num 1 : " ))
b = float(input("num 2 : "))
mn = get_min(a,b)
print (mn)
