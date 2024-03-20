import math

d_abs = 52.
d_orifice = 38.1
rho_abs = 1.155

beta = d_orifice/d_abs

Q_abs = 0.0319

dP_orifice = (98.9/1000)*1000*9.81

Cd = Q_abs/((math.pi*(d_orifice/1000)**2/4)*((2*dP_orifice)/(rho_abs*(1-beta**4)))**0.5)

# x = (math.pi*(d_orifice/1000)**2/4)

print(Cd)