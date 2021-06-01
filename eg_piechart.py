import matplotlib.pyplot as plt
sizes = [25, 20, 45, 10]
labels = ["Cats", "Dogs", "Tigers", "Goats"]
plt.axes().set_aspect("equal")# auto # num # aspect ratio
plt.pie(sizes, labels=labels, autopct="%.2f") # float and percentage value

plt.show()
