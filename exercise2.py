from exercise1 import v_abs, v_copper, v_galvanized
import matplotlib.pyplot as plt

vavg_abs = list()
vavg_copper = list()
vavg_galvanized = list()

r_abs = [0, 0.5, 1, 1.5, 2, 6, 10, 14, 18, 22, 26]
r_copper = [0, 0.5, 1, 1.5, 2, 4, 6, 8, 10, 12, 13]
r_galvanized = [0, 0.5, 1, 1.5, 2, 4, 6, 8, 10, 12, 13]

for i in range(len(v_abs) // 2):
    vavg_abs.append((v_abs[i] + v_abs[-i])/2)
    vavg_copper.append((v_copper[i] + v_copper[-i])/2)
    vavg_galvanized.append((v_galvanized[i] + v_galvanized[-i])/2)


vavg_abs.append(v_abs[10])
vavg_abs.reverse()
vavg_copper.append(v_copper[10])
vavg_copper.reverse()
vavg_galvanized.append(v_galvanized[10])
vavg_galvanized.reverse()

total_vavg_abs = 0
total_vavg_copper = 0
total_vavg_galvanized = 0

for i in range(len(vavg_abs) - 1):
    total_vavg_abs += ((r_abs[i+1]/1000)**2 - (r_abs[i]/1000)**2)*((vavg_abs[i+1]+vavg_abs[i])/2)
    total_vavg_copper += ((r_copper[i+1]/1000)**2 - (r_copper[i]/1000)**2)*((vavg_copper[i+1]+vavg_copper[i])/2)
    total_vavg_galvanized += ((r_galvanized[i+1]/1000)**2 - (r_galvanized[i]/1000)**2)*((vavg_galvanized[i+1]+vavg_galvanized[i])/2)

total_vavg_abs /= (r_abs[-1]/1000)**2
total_vavg_abs = [total_vavg_abs] * 11
total_vavg_copper  /= (r_copper[-1]/1000)**2
total_vavg_copper = [total_vavg_copper] * 11
total_vavg_galvanized  /= (r_galvanized[-1]/1000)**2
total_vavg_galvanized = [total_vavg_galvanized] * 11

print('\n\n')
print(total_vavg_galvanized)
print('\n\n')

plt.style.use('seaborn-v0_8')

fig, (ax1, ax2, ax3) = plt.subplots(3)
fig.set_size_inches(14,8)
fig.tight_layout(pad=5.0)

l1,= ax1.plot(r_abs, vavg_abs)
l2,= ax1.plot(r_abs, total_vavg_abs, linestyle='dashed')
ax1.ticklabel_format(useOffset=False, style='plain')
ax1.set_xticks(r_abs, r_abs, rotation=-90)
ax1.set_title('Average Radial and Average Total Speed of ABS Pipe')
ax1.set_xlabel('Radial Distance [mm]')
ax1.set_ylabel('Speed [m/s]')

ax1.legend([l1, l2], ['V_avg ABS', 'Total V_avg ABS'])

l1,= ax2.plot(r_copper, vavg_copper)
l2,= ax2.plot(r_copper, total_vavg_copper, linestyle='dashed')
ax2.ticklabel_format(useOffset=False, style='plain')
ax2.set_xticks(r_copper, r_copper, rotation=-90)
ax2.set_title('Average Radial and Average Total Speed of Copper Pipe')
ax2.set_xlabel('Radial Distance [mm]')
ax2.set_ylabel('Speed [m/s]')

ax2.legend([l1, l2], ['V_avg Copper', 'Total V_avg Copper'])

l1,= ax3.plot(r_galvanized, vavg_galvanized)
l2,= ax3.plot(r_galvanized, total_vavg_galvanized, linestyle='dashed')
ax3.ticklabel_format(useOffset=False, style='plain')
ax3.set_xticks(r_galvanized, r_galvanized, rotation=-90)
ax3.set_title('Average Radial and Average Total Speed of Galvanized Pipe')
ax3.set_xlabel('Radial Distance [mm]')
ax3.set_ylabel('Speed [m/s]')

ax3.legend([l1, l2], ['V_avg Galvanized', 'Total V_avg Galvanized'])

# plt.show()
fig.savefig('ex2.svg')