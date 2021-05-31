test_scores = [12, 99, 65, 85, 42]
test_names = ["Andy", "Martin", "Zahara", "Vuyo", "Ziyaad"]

import numpy as np
import matplotlib.pyplot as plt

np.array(test_scores)
np.array(test_names)
plt.bar(test_names, test_scores, color="blue")
plt.ylabel("Marks(%)")
plt.xlabel("Names")
plt.title("Python marks for five students")
plt.show()
