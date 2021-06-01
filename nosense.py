test_scores = [100, 85, 60, 50, 100]
test_names = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]

marks = [70, 45, 90, 12, 100]
names = ["Memphis", "Godwin", "Thando", "Thabo", "Abdul-Malik"]
import numpy as np
import matplotlib.pyplot as plt

np.array(test_scores)
np.array(test_names)

np.array(marks)
np.array(names)

plt.figure(figsize=(20, 8))

plt.bar(names, marks)
plt.bar(test_names, test_scores, color="orange")

plt.ylabel("Energy Level(%)", fontsize=18)
plt.xlabel("Days of the week(1-5)", fontsize=18)

plt.title("Abdul-Malik's Energy level for the week", fontsize=22)

plt.show()
