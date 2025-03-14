import pandas as pd

df= pd.read_csv(r"C:\Users\Abraham\Desktop\DOINGS\AB_NYC_2019.csv")

#Basic information about the data set

print("\n data_info:")
print(df.info())

print("\n data heading")
print(df.head)

#check for missing values
print("\nmissing values")
print(df.isnull().sum())

#checking for duplicate
print("\nduplicate valeues")
print(df.duplicated().sum())



import numpy as np

# Handling missing values
df = df.assign(
    name=df['name'].fillna('Unknown'),
    host_name=df['host_name'].fillna('Unknown'),
    reviews_per_month=df['reviews_per_month'].fillna(0),
    last_review=pd.to_datetime(df['last_review']).fillna(pd.Timestamp("2000-01-01"))
)


# Outlier Detection
# Checking for outliers using IQR method for price and minimum_nights
Q1 = df[['price', 'minimum_nights']].quantile(0.25)
Q3 = df[['price', 'minimum_nights']].quantile(0.75)
IQR = Q3 - Q1

# Defining outlier bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identifying outliers
outliers_price = df[(df['price'] < lower_bound['price']) | (df['price'] > upper_bound['price'])]
outliers_nights = df[(df['minimum_nights'] < lower_bound['minimum_nights']) | (df['minimum_nights'] > upper_bound['minimum_nights'])]

# Count of outliers
outliers_price_count = outliers_price.shape[0]
outliers_nights_count = outliers_nights.shape[0]

print("\noutliers price count")
print(outliers_price_count)

print("\noutlier_nights_count")
print(outliers_nights_count)

# Capping outliers in 'price' and 'minimum_nights' based on IQR bounds

# Define the upper limit for capping
price_cap = upper_bound['price']
nights_cap = upper_bound['minimum_nights']

# Apply capping
df['price'] = np.where(df['price'] > price_cap, price_cap, df['price'])
df['minimum_nights'] = np.where(df['minimum_nights'] > nights_cap, nights_cap, df['minimum_nights'])

# Verify if outliers are capped
new_outliers_price = df[(df['price'] > price_cap)]
new_outliers_nights = df[(df['minimum_nights'] > nights_cap)]

# Count of remaining outliers
new_outliers_price_count = new_outliers_price.shape[0]
new_outliers_nights_count = new_outliers_nights.shape[0]

print("\nnew outlier_price_count")
print(new_outliers_price_count)

print("\nnew_outliers_night_count")
print(new_outliers_nights_count)
