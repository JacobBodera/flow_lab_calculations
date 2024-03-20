import matplotlib.pyplot as plt
from exercise2 import vavg_abs, vavg_copper, vavg_galvanized
from exercise3 import Vcl_abs, Vcl_copper, Vcl_galvanized

r_abs = [0, 0.5, 1, 1.5, 2, 6, 10, 14, 18, 22, 26]
r_copper = [0, 0.5, 1, 1.5, 2, 4, 6, 8, 10, 12, 13]
r_galvanized = [0, 0.5, 1, 1.5, 2, 4, 6, 8, 10, 12, 13]

nodimV_abs = list()
nodimV_copper = list()
nodimV_galvanized = list()

for i in range(len(vavg_abs)):
    nodimV_abs.append(vavg_abs[i]/Vcl_abs)
    nodimV_copper.append(vavg_copper[i]/Vcl_copper)
    nodimV_galvanized.append(vavg_galvanized[i]/Vcl_galvanized)

laminar_abs = list()
laminar_copper = list()
laminar_galavanized = list()

for i in range(len(r_abs)):
    laminar_abs.append(1-(r_abs[i]**2/r_abs[-1]**2))
    laminar_copper.append(1-(r_copper[i]**2/r_copper[-1]**2))
    laminar_galavanized.append(1-(r_galvanized[i]**2/r_galvanized[-1]**2))    

plt.style.use('seaborn-v0_8')

fig, (ax1) = plt.subplots(1)
fig.set_size_inches(14,8)
fig.tight_layout(pad=5.0)

l1,= ax1.plot(r_abs, nodimV_abs, color='red')
l2,= ax1.plot(r_abs, laminar_abs, color='red', linestyle='dashed', markersize=0.5)
l3,= ax1.plot(r_abs, nodimV_copper, color='orange')
l4,= ax1.plot(r_abs, laminar_copper, color='orange', linestyle='dashed')
l5,= ax1.plot(r_abs, nodimV_galvanized, color='blue')
l6,= ax1.plot(r_abs, laminar_galavanized, color='blue', linestyle='dotted')
ax1.ticklabel_format(useOffset=False, style='plain')
ax1.set_xticks(r_abs, r_abs, rotation=-90)
ax1.set_title('Non-Dimensional Smoothed Speed Profiles for Different Pipes Versus Radial Distance')
ax1.set_xlabel('Radial Distance [mm]')
ax1.set_ylabel('Smoothed Speed [-]')

ax1.legend([l1, l2, l3, l4, l5, l6], ['Actual ABS', 'Laminar ABS', 'Actual Copper', 'Laminar Copper', 'Actual Galvanized', 'Laminar Galvanized'])

plt.show()