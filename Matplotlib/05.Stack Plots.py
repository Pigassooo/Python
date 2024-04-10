from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")


minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

labels = ['player 1', 'player 2', 'player 3']
colors = ['#008fd5', '#fc4f30', '#e5ae37']

plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colors)

plt.legend(loc=(0.07,0.05), framealpha=0.7)

plt.title("My Awesome Stack Plot")
plt.tight_layout()
plt.show()
