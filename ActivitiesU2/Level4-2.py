import matplotlib.pyplot as plt

match = list(range(1, 39))
goals = [
    2, 1, 0, 3, 2, 1, 1, 2, 3, 0, 
    1, 2, 1, 3, 0, 2, 1, 4, 2, 1, 
    3, 0, 2, 1, 2, 3, 1, 0, 2, 3, 
    1, 2, 3, 0, 1, 2, 1, 3
]

plt.plot(match, goals, color="blue", label="Goals per match")
max_goals = max(goals)
idx_max = goals.index(max_goals)
plt.plot(match[idx_max], goals[idx_max], 'ro', markersize=8, label='Best match')

plt.title("Goals per match")
plt.xlabel("Matches")
plt.ylabel("Goals")
plt.legend()
plt.show()
