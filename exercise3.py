from exercise2 import vavg_abs, vavg_copper, vavg_galvanized, total_vavg_abs, total_vavg_copper, total_vavg_galvanized
from exercise1 import rho_abs, rho_copper, rho_galvanized
import math

d_abs = 52.
d_copper = 26.
d_galvanized = 26.6

mu_abs = 0.00001862
mu_copper = 0.00001893
mu_galvanized = 0.00001888

Vcl_abs = vavg_abs[0]
Vcl_copper = vavg_copper[0]
Vcl_galvanized = vavg_galvanized[0]

print('\n\n')
print('center line v')
print(Vcl_abs)
print(Vcl_copper)
print(Vcl_galvanized)
print('\n')

Vavg_abs = total_vavg_abs[1]
Vavg_copper = total_vavg_copper[1]
Vavg_galvanized = total_vavg_galvanized[1]

Q_abs = round(Vavg_abs*(math.pi*(d_abs/2000)**2), 4)
Q_copper = round(Vavg_copper*(math.pi*(d_copper/2000)**2), 4)
Q_galvanized = round(Vavg_galvanized*(math.pi*(d_galvanized/2000)**2), 4)

print('Q')
print(Q_abs)
print(Q_copper)
print(Q_galvanized)
print('\n')

print('Vavg')
print(Vavg_abs)
print(Vavg_copper)
print(Vavg_galvanized)
print('\n')

print('Kv')
print(Vavg_abs/Vcl_abs)
print(Vavg_copper/Vcl_copper)
print(Vavg_galvanized/Vcl_galvanized)
print('\n')

Re_abs = round((rho_abs*Vavg_abs*d_abs/1000)/mu_abs, 2)
Re_copper = round((rho_copper*Vavg_copper*d_copper/1000)/mu_copper, 2)
Re_galvanized = round((rho_galvanized*Vavg_galvanized*d_galvanized/1000)/mu_galvanized, 2)

print('Re')
print(Re_abs)
print(Re_copper)
print(Re_galvanized)
print('\n')