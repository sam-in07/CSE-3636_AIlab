# Pandas Example Code:

import pandas as pd

# Step 1: Create a DataFrame
data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22],
    'City': ['New York', 'London', 'Paris']
})

# Step 2: Display the DataFrame
print("DataFrame:")
print(data)

# Step 3: Access a column
print("\nAges:")
print(data['Age'])

# Step 4: Filter rows
print("\nPeople older than 23:")
print(data[data['Age'] > 23])