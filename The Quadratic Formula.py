import math 
a = float(input("Give me the value of a:"))
b = float(input("Give me the value of b:"))
c = float(input("Give me the value of c:"))
d = (2*b)-(4*a*c)
if d == 0:
    print(-b/(2*a))
if d < 0:
    print("Its Imposible")
if d > 0:
    x1 = ((-b) + (math.sqrt(d)))/2*a
    x2 = ((-b) - (math.sqrt(d)))/2*a
    print("The First X is ",x1," and The Second X is ",x2) 
        
