import pandas as pd

df = pd.read_csv(r'G:\Programing\all code\ML-AI\weather.csv')
print(type(df))
print(df)

print(df.head())
print(df.tail())
print(df.describe())
print(df.shape)
print(df.dtypes)

df.columns = ['outlok', 'temperature', 'humidity', 'windy', 'play']

t = df['temperature']
print(type(t))
print(t)

sum = 0
for value in t:
    sum += value
print(sum)

df1 = df[['temperature', 'humidity']]
print(df1)

df3 = df.iloc[0:10, [1, 2]]
print(df3)

df4 = df.iloc[1::2, [0, 1, 3]]
print(df4)

df5 = df.loc[1:len(df)-1:2, ['temperature', 'windy']]
print(df5)

df4 = df.iloc[1::2, [0, 1, 3]]
print(df4)

df4 = df.loc[1:len(df)-1:2, ['outlook', 'temperature', 'windy']]
print(df4)

# all statistical measures over temperature column
temperature = df[['temperature']]

print("Mean: ", temperature.mean())
print("Standard Deviation: ", temperature.std())
print("Variance: ", temperature.var())
print("Lower Quartile: ", temperature.quantile(0.25))
print("Median: ", temperature.quantile(0.5))
print("Median: ", temperature.median())
print("Upper Quartile: ", temperature.quantile(0.75))
print("Skewness: ", temperature.skew())
print("Kurtosis: ", temperature.kurt())
print("Min: ", temperature.min())
print("Max: ", temperature.max())


df.hist(column=['temperature'], bins=3)
df.hist(column=['humidity'], bins=3)


humidity = df[['humidity']]
print("Mean: ", humidity.mean())
print("Standard Deviation: ", humidity.std())
print("Variance: ", humidity.var())
print("Lower Quartile: ", humidity.quantile(0.25))
print("Median: ", humidity.quantile(0.5))
print("Median: ", humidity.median())
print("Upper Quartile: ", humidity.quantile(0.75))
print("Skewness: ", humidity.skew())
print("Kurtosis: ", humidity.kurt())
print("Min: ", humidity.min())
print("Max: ", humidity.max())
