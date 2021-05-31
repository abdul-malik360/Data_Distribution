test_scores = [100, 85, 60, 50, 100]
test_names = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]

import numpy as np
import matplotlib.pyplot as plt

np.array(test_scores)
np.array(test_names)
plt.figure(figsize=(20, 8))
plt.bar(test_names, test_scores, color="orange")
plt.ylabel("Energy Level(%)", fontsize=18)
plt.xlabel("Days of the week(1-5)", fontsize=18)
plt.title("Abdul-Malik's Energy level for the week", fontsize=22)
plt.show()
