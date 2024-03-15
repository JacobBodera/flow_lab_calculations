import matplotlib.pyplot as plt

rho_water = 1000.
g = 9.81

rho_abs = 1.155
rho_copper = 1.131
rho_galvanized = 1.135

x_vals = [a for a in range(1, 22)]
# ABS pipe data
r_abs = [26, 22, 18, 14, 10, 6, 2, 1.5, 1, 0.5, 0, 0.5, 1, 1.5, 2, 6, 10, 14, 18, 22, 26]
deltaP_abs = [11.7, 12.8, 13.6, 14.5, 15.2, 19, 21.2, 22.8, 24.2, 24.5, 24.5, 23.8, 23.5, 22.3, 20.3, 18.2, 14.6, 13.8, 13, 12.2, 11.5]
# Copper pipe data
r_copper = [13, 12, 10, 8, 6, 4, 2, 1.5, 1, 0.5, 0, 0.5, 1, 1.5, 2, 4, 6, 8, 10, 12, 13]
deltaP_copper = [92.5, 99.6, 109, 115.7, 123.2, 144.5, 160.2, 174.3, 182.7, 185.1, 185.3, 185.4, 186.2, 178.5, 166.5, 149.7, 130.2, 124.2, 116.5, 109, 99.8]
# Galvanized pipe data
r_galvanized = [13, 12, 10, 8, 6, 4, 2, 1.5, 1, 0.5, 0, 0.5, 1, 1.5, 2, 4, 6, 8, 10, 12, 13]
deltaP_galvanized = [64.1, 73.2, 77.8, 85.1, 91.5, 112.2, 128, 139.2, 144.7, 145.4, 146.2, 144.3, 139.1, 133.5, 126.9, 116.5, 98.6, 92.2, 85.6, 76.9, 67.9]

# Velocity profiles
v_abs = list()
v_copper = list()
v_galvanized = list()

# Calculating velocity profile base on radius
for i in range(len(r_abs)):
    # Converting mmH2O to Pa and using Equation 3 to find speed
    deltaP_abs[i] *= rho_water*g/1000
    v_abs.append(((2*deltaP_abs[i])/rho_abs)**0.5)
    deltaP_copper[i] *= rho_water*g/1000
    v_copper.append(((2*deltaP_copper[i])/rho_copper)**0.5)
    deltaP_galvanized[i] *= rho_water*g/1000
    v_galvanized.append(((2*deltaP_galvanized[i])/rho_galvanized)**0.5)

plt.style.use('seaborn-v0_8')

fig, (ax1, ax2, ax3) = plt.subplots(3)
fig.set_size_inches(14,8)
fig.tight_layout(pad=5.0)

ax1.scatter(x_vals, v_abs)
ax1.ticklabel_format(useOffset=False, style='plain')
ax1.set_xticks(x_vals, r_abs, rotation=90)
ax1.set_title('Speed of Airflow Through ABS Pipe at Given Radius')
ax1.set_xlabel('Radius [mm]')
ax1.set_ylabel('Speed [m/s]')

ax2.scatter(x_vals, v_copper)
ax2.ticklabel_format(useOffset=False, style='plain')
ax2.set_xticks(x_vals, r_copper)
ax2.set_title('Speed of Airflow Through Copper Pipe at Given Radius')
ax2.set_xlabel('Radius [mm]')
ax2.set_ylabel('Speed [m/s]')

ax3.scatter(x_vals, v_galvanized)
ax3.ticklabel_format(useOffset=False, style='plain')
ax3.set_xticks(x_vals, r_galvanized)
ax3.set_title('Speed of Airflow Through Galvanized Pipe at Given Radius')
ax3.set_xlabel('Radius [mm]')
ax3.set_ylabel('Speed [m/s]')
    
# plt.show()
fig.savefig('ex1.svg')