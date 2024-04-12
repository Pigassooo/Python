import matplotlib
import pandas as pd
from matplotlib import pyplot as plt


matplotlib.use('TkAgg')  # 或者尝试其他后端，如 'Qt5Agg'

data = pd.read_csv('data/data5.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

ax2.plot(ages, py_salaries, label='Python')
ax2.plot(ages, js_salaries, label='JavaScript')

ax1.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

ax1.legend()
ax1.set_title('Median Salary (USD) by Age')
ax1.set_xlabel('Ages')
ax1.set_ylabel('Median Salary (USD)')

ax2.legend()
ax2.set_title('Median Salary (USD) by Age')
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()

fig1.savefig('Pics/07.fig1.png',dpi=300)
fig2.savefig('Pics/07.fig2.png',dpi=300)