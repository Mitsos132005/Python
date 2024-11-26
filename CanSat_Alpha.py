import math

Pt = float(input('Total pressure input (hPa)'))
#Total Pressure Variable

Ps = float(input('Static pressure input (hPa)'))
#Static Pressure Variable

T = float(input('Temperature input (Celsius)'))
# Air Temperature Variable

RH = float(input('Relative Humidity input [0,1]'))
# Relative Humidity Variable

######################################################################################################################

Rd = 287.058 #Specific gas constant for dry air
Rv = 461.495 #Specific gas constant for water vapor

A=math.pow(10,7.5*T /(T + 237.3))
Psat = 6.1078 * A
#Saturation Vapor Pressure (Vapor Pressure at 100% RH) 

Pv = Psat * RH
# Vapor Pressure

Pd = Pt - Pv
#Dry Air Pressure

Tkelvin = T + 273.15

ρ = ((Pd / (Rd * Tkelvin)) + (Pv / (Rv * Tkelvin)))*100
#Air density

print('                 ')
print('With the following Conditions:')
print('Total Pressure is equal to',Pt,'hPa')
print('Temperature is equal to',T,'°C')
print(RH*100,'% Relative Humidity')
print('                 ')
print('Air Density is equal to',ρ,'kg/m³')
print('                 ')



######################################################################################################################

Pdynamic = Pt-Ps

VelocitySquared = pow(Pdynamic,2)/ρ

Velocity= math.sqrt(VelocitySquared)


print('                 ')
print('With the following Conditions:')
print('Dynamic Pressure is equal to',Pdynamic,'hPa')
print('Air Density is equal to',ρ,'kg/m³')
print('                 ')
print('Velocity is equal to',Velocity,'m/s')



