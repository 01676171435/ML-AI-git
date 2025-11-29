from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import pandas as pd

# Replace 'your_dataset.csv' with the actual path to your CSV file
dataset = pd.read_csv('your_dataset.csv')
dataset.columns = ['yearsExperience', 'Salary']

# Features and target variable
x = dataset[['yearsExperience']]
y = dataset[['Salary']]

# Split the dataset into training and test sets
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=1/3, random_state=0)

# Create a LinearRegression model and fit it to the training data
regressor = LinearRegression()
regressor.fit(x_train, y_train)
