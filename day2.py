'''CREATING PLOTS IN PANDAS'''
import pandas as pd
import matplotlib.pyplot as plt

air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)
print(air_quality)

# With a DataFrame, pandas creates by default one line plot for each of the columns with numeric data.
air_quality.plot()
plt.show()

# selecting particular columns
air_quality["station_london"].plot()
plt.show()

# In this code, alpha=0.5 means that the data points in the scatter plot will be semi-transparent.
air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
plt.show()

air_quality.plot(kind="box")
plt.show()

# each column in a separate subplot
axs = air_quality.plot.area(figsize=(12, 4), subplots=True)
plt.show()
