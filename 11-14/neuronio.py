import math as m
import random as rd

def S(x,w, b): 
    return (x * w) + b

def sigmoid (S):
    return 1/((1+ m.exp(-S)))

t = 1
x = 0.2

lr = 0.7

w = rd.random()
b = rd.random()

epochs = 1000

for i in range(epochs):

    s = S(x,w,b)
    y = sigmoid(s)

    derVies = (y - t) * y  * ( 1 - y ) * x
    derPeso = (y - t) * y  * ( 1 - y ) 

    w = w - lr * derPeso 
    b = b - lr * derVies

    print(sigmoid(S(x,w,b)))
    pass