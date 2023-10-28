#%%
import pandas as pd

# Create a sample Series with lists of integers
data = pd.Series([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original Series:")
print(data)

# Define a function to check the length and data type of each row
def check_row(row):
    return len(row) == len(data[0]) and all(isinstance(x, type(data[0][0])) for x in row)

# Apply the function to each element in the Series using apply()
matches = data.apply(check_row)

# Check if all the rows satisfy the criteria using all()
result = matches.all()

# Display the result
print("\nResult:", result)



#%%
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie'],
    'gender': ['female', 'male', 'male', 'female', 'male', 'male'],
    'age': [25, 30, 35, 40, 45, 50],
    'score': [80, 90, 75, 85, 95, 70]
})

# Group the DataFrame by 'name' column and sum the 'score' column
grouped = df.groupby('name').agg({'score': 'sum'})

print(grouped)