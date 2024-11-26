import math 
m = float(input("Give me the Mass of the body:"))
h = float(input("Give me the Height that the body fell:"))
d = h*9.81*m
mi = d
x = 1
while h > x:
    x = x + 1 
    hd = h - x 
    d = m*9.81*hd
    k = mi - d 
    v = math.sqrt((k*2)/2)
    print("The Dyn En is ", "%.2f" % d," in ","%.2f" % hd,"m The Kin En is ","%.2f" % k," and the Speed is ","%.2f" % v,"m/s The M En is ","%.2f" % mi,) 
    
   

    
