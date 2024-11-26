import math 
def distanceformula(v,a,t):
    d = (v*t) + ((1/2)*a*(2*t))
    print("The Time is ",t,"sec"," and The Distance is ",d,"m")

v = float(input("Give me the Speed of the Vehicle:"))
a = float(input("Give me the Acceleration of the Vehicle:"))
t = int(input("Give me the Time:"))
print("The Speed of the Vehicle is ",v,"m/s"," The Accelaration of the Vehicle is ",a,"m/s^2")

for x in range(t+1):
    distanceformula(v,a,x)


