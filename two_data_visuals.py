import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# %matplotlib inline

test_scores = [100, 85, 60, 50, 100]
test_names = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]

np.array(test_scores)
np.array(test_names)

plt.figure(figsize=(20, 8))

plt.subplot(121)

plt.bar(test_names, test_scores, color="orange")
plt.ylabel("Energy Level(%)")
plt.xlabel("Days of the week(1-5)")
plt.title("Abdul-Malik's Energy level for the week")

cities = ['East London', 'Cape Town', 'Kimberley', 'Durban']
rainfall = [140,  200, 120, 157]
x_pos = [i for i, _ in enumerate(cities)] #labels on the x-axis
#labeling and visuals
plt.subplot(122)
plt.bar(x_pos, rainfall, color='green')
plt.xlabel("cities")
plt.ylabel("Rainfall in (mm)")
plt.title("Rainfall for the 4 main cities in SA")
plt.xticks(x_pos, cities)


plt.show()
