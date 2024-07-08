# -*- coding: utf-8 -*-
"""Restaurant Business Rankings 2020

Dataset Link-https://www.kaggle.com/datasets/michau96/restaurant-business-rankings-2020
"""

# Importing essential libraries
import pandas as pd
import matplotlib.pyplot as plt
# ignore the warnings
import warnings
warnings.filterwarnings("ignore")

# Defining the file path and creating dataframe
df=pd.read_csv("C:/Users/Admin/Desktop/Python_Visualization Project/archive/Future50.csv")

# Displaying the first few rows of the DataFrame
print(df.head())

# Displaying the last few rows of the DataFrame
print(df.tail())

# Displaying the shape of the data
print(df.shape)

# Describing the dataset
print(df.describe())

# checking for missing values
print(df.isnull().sum())

# checking for duplicate rows
print(df.duplicated().sum())

#showing the information of the data
df.info()

# Sorting the data based on Sales and selecting the top 10 restaurants
top_10_sales = df.sort_values(by='Sales', ascending=False).head(10)

# Creating the line chart
plt.figure(figsize=(12, 8))
plt.plot(top_10_sales['Restaurant'], top_10_sales['Sales'], marker='o', markersize = 15, color='teal', linewidth = 6, linestyle = '-.', markeredgecolor = 'black')
plt.xlabel('Restaurant')
plt.ylabel('Sales')
plt.title('Top 10 Restaurants by Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Counting the occurrences of each value in the 'Franchising' column
franchising_counts = df['Franchising'].value_counts()

# Creating the pie chart
plt.figure(figsize=(8, 8))
plt.pie(franchising_counts, labels=franchising_counts.index, autopct='%1.1f%%', startangle=90, colors = ['cyan', 'magenta'], shadow=True)
plt.title('Is the restaurent a franchise or not?')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.legend()
plt.show()

# Sorting the data based on Unit Volume and selecting the top 10 restaurants
top_10_unit_volume = df.sort_values(by='Unit_Volume', ascending=False).head(10)

# Colors and widths for the bars
colors = ['cyan', 'magenta', 'yellow', 'green', 'blue', 'red', 'orange', 'purple', 'brown', 'pink']
widths = [1 , .9, .8, .7, .6, .5, .4, .3, .2, .1]

# Creating the bar plot
plt.figure(figsize=(12, 8))
bars = plt.bar(top_10_unit_volume['Restaurant'], top_10_unit_volume['Unit_Volume'], color=colors, width=widths, edgecolor = 'black')
plt.xlabel('Restaurant')
plt.ylabel('Unit Volume')
plt.title('Top 10 Restaurants by Unit Volume')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
# Defining custom bins for the 'Units' attribute
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]

# Creating the histogram for 'Units' with specified bins
plt.figure(figsize=(10, 6))
plt.hist(df['Units'], bins=bins,  histtype = 'bar', color='cyan', rwidth = 0.5, edgecolor = 'black')
plt.title('Histogram of Units')
plt.xlabel('Units')
plt.ylabel('Frequency')

plt.show()


# Creating the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(data=df, x='Units', y='Unit_Volume', color='magenta', marker='o')
plt.title('Scatter Plot between Units and Unit Volume')
plt.xlabel('Units')
plt.ylabel('Unit Volume')
plt.grid(True)
plt.show()
#plt.savefig("C:/Users/Admin/Desktop/Python_Visualization Project/test.pdf")
