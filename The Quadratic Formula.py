import math 
a = float(input("Give me the value of a:"))
b = float(input("Give me the value of b:"))
c = float(input("Give me the value of c:"))
d = (2*b)-(4*a*c)
if d == 0:
    x3 = -b/(2*a)
    print("The X is ",x3)
if d < 0:
    print("Its Imposible")
if d > 0:
    d2 = math.sqrt(d)
    x1 = ((-b) + (d2/2*a))
    x2 = ((-b) - (d2/2*a))
    print("The First X is ",x1," and The Second X is ",x2) 
        
