from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097, 23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']
explode = [0, 0, 0, 0.1, 0, 0,  0, 0, 0, 0,0, 0, 0, 0,0]
# colors = ['yellowgreen', 'gold', 'lightcoral', 'lightskyblue', 'lightslategray']

plt.pie(slices, labels=labels, autopct='%1.1f%%', explode=explode,wedgeprops={'edgecolor': 'black'})

plt.title("My Awesome Pie Chart")
plt.tight_layout()

plt.savefig('Pics/04.My Awesome Pie Chart.png')
plt.show()




