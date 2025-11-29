import pandas as pd

data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print(series)


dex = ['a', 'b', 'c', 'd', 'e']
series_with_index = pd.Series(data, index=dex)
print(series_with_index)

print(series[0])
print(series_with_index['b'])

print(series * 2)
print(series_with_index + 5)

print(series[series > 30])
print(series.std())

# Statistical operations on a Series
print(series.mean())  # Calculating the mean of the Series
print(series.std())  # Calculating the standard deviation of the Series


print(series.index)
print(series.values)
print(series.describe())


data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 28, 35],
    'City': ['New York', 'Los Angeles', 'Chicago', 'San Francisco']
}

df = pd.DataFrame(data)

print(df)

# Sample data (replace with your own data source)
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 28, 35],
    'City': ['New York', 'Los Angeles', 'Chicago', 'San Francisco']
}

# Create a Pandas DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Basic statistics
print("\nSummary Statistics:")
print(df.describe())

# Accessing specific columns
print("\nAges:")
print(df['Age'])

# Filtering data
print("\nPeople older than 30:")
print(df[df['Age'] > 30])

# Grouping data
print("\nAverage age by city:")
print(df.groupby('City')['Age'].mean())

# Sorting data
print("\nSorted by age:")
print(df.sort_values('Age'))
