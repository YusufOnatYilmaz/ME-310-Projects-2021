import matplotlib.pyplot as plt
# Plotting in order to show the O(n) calculation process.
plt.plot([3, 5, 6, 10, 15,17,20, 25,30,35,40,45,50],[4, 10,13, 25, 40,46, 55,70,85,100,115,130,145])
plt.ylabel("Floating Point Operations")
plt.xlabel("N values")
plt.title("N vs Floating Point Operations")
plt.show()