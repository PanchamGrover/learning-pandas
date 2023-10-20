import pandas

# creating a dataframe with name data
data = pandas.read_csv("mutual_funds_data.csv")

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

