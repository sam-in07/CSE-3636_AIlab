import matplotlib.pyplot as plt

# Step 1: Define data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]  # Pattern: y = 2 * x

# Step 2: Create the plot
plt.plot(x, y)

# Step 3: Add labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot")

# Step 4: Show the plot
plt.show()