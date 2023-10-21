import pandas

# creating a dataframe with name data
data = pandas.read_csv("data/mutual_funds_data.csv")

# printing the data (by default pandas print first and last 5 rows of the dataframe)
print(data)

# if you want to see first N rows of the dataframe use .head() method with the required no of rows.
print(data.head(10))

"""if you want to see the data type of each column in dataframe use 
.dtypes (the .dtypes is an attribute and not a method so it does not need to be used with brackets)
Attributes represents characteristics of a dataframe while methods actually do something to the 
dataframe"""
print(data.dtypes)
"""The data types in this DataFrame are integers (int64), floats (float64) and strings (object)."""

# converting csv data to excel
data.to_excel("MF_data.xlsx",index=False)

# info() method provide technical information about a dataframe.
data.info()

# head/tail(similar to head)/info are methods and .dtypes is an attribute


# SELECTING SUBSET OF A DATAFRAME
# To select a single column, use square brackets [] with the column name of the column of interest.
print(data["fund_manager"])
# In a Dataframe each column is called as "series".
# A pandas Series is 1-dimensional and only the number of rows is returned.
# .shape is also an attribute
print(data["fund_manager"].shape)

# for selecting multiple columns use double squared brackets [[]]
print(data[["alpha","beta","sharpe"]])

# specific rows in dataframe. ex. here i want to select beta lower than 1.
high_rating = data[data["rating"] > 3]
print(high_rating)
# remember while sorting using multiple conditions put each condition in a separate set of brackets.
# plus we can not use or , and we have use their symbols
fund = data[(data["rating"] > 3) & (data["fund_age_yr"]>5)]
print(fund)

# The notna() conditional function returns a True for each row the values are not a Null value.
filtered_data = data.notna()
print(filtered_data)

# selecting specific rows and columns from a daraframe.
# When selecitng both rows and columns
# The loc/iloc operators are required in front of the selection brackets []
# i want name of funds whose 5 year return is greater than 15
dataframe = data.loc[data["returns_5yr"] > 15, "scheme_name"]
print(dataframe)