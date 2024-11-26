import math 
a = float(input("Give me the value of a:"))
b = float(input("Give me the value of b:"))
c = float(input("Give me the value of c:"))
d = (2*b)-(4*a*c)
if a == 0:
    x4 = -c/b
    print("The X is ",x4)    
if b == 0:
    x5 = math.sqrt(c/a)  
    print("The X is ",x5)  
if c == 0:
    x6 = (-b-b)/(2*a)
    x7 = 0
    print("The First X is ",x6," and The Second is ",x7)
else:    
    if d == 0:
        x3 = -b/(2*a)
        print("The X is ",x3)
    elif d < 0:
        complexsolution = math.sqrt(-d)
        print("The First Complex Solution is ", -b ,"+ i * ", complexsolution , " / ", 2*a )
        print("The Second1 Complex Solution is ", -b ,"- i * ", complexsolution , " / ", 2*a )
    else:
        d2 = math.sqrt(d)
        x1 = ((-b) + (d2/2*a))
        x2 = ((-b) - (d2/2*a))
        print("The First X is ",x1," and The Second X is ",x2)         


