#!pip install numpy
#pip install matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#from google.colab import drive
#mobile_price_csv= "/content/mobile_price_1.csv"

#Task 1

#1
# @title 1. Loading the data into a Pandas Dataframe.
mobile_price_csv= "mobile_price_1.csv"
data = pd.read_csv(mobile_price_csv)

#2
#*2. Which of the categorical features are nominal and which are ordinal? *
#Nominal features: Bluetooth, SIM, WiFi, Screen
#Ordinal features: Generation, Cores, Speed

#3
# @title 3. Add a column that holds the total screen resolution for each device. Name it resolution.
data['resolution'] = data['px_height'] * data['px_width']

#4
# @title 4. Add a column that holds the DPI (dots per inch) of the screen width and name it DPI_w.
data['DPI_w'] = data['px_width'] / ( data['sc_w'] * 0.393701)
data['DPI_w']= data['DPI_w'].replace([np.inf, -np.inf , np.nan], 0) #replace the inf and nan value with 0


#5
# @title 5. Add a column that holds the ratio battery_power/talk_time and name it call_ratio.Do not leave NaN/Infinite values.
data['call_ratio'] = data['battery_power']/data['talk_time']
data['call_ratio']= data['call_ratio'].replace([np.inf, -np.inf , np.nan], 0)



#6
# @title 6. Change the memory column to hold the memory in GB instead of MB.
data['memory'] = data['memory'] / 1024

#7
# @title 7. Include the output of the `describe()` function of the dataframe.
data.describe()

#8
# @title 8. Convert the following features into categorical series in the Dataframe: speed,screen,cores
data['speed'] = data['speed'].astype('category')
data['screen'] = data['screen'].astype('category')
data['cores'] = data['cores'].astype('category')


#Task 2

#1
# @title 1. How many phones do not have a camera at all (front or back)?
phone_with_nan_Value = data[(data['f_camera'].isna()) & (data['camera'].isna())]
print("Number of phones do not have a camera at all:", len(phone_with_nan_Value))

#2
# @title 1. How many phones do not have a camera at all (front or back)?
# Filter the DataFrame based of who have single sim and have a camera with more than 12 pixel
filter = data[(data['sim'] == 'Single') & ((data['camera'] > 12) | (data['f_camera'] > 12))]
battery_power_AVG = filter['battery_power'].mean()
print("Average battery power of phones whos have a single sim and have a camera with more than 12 pixel", battery_power_AVG)

#3
# @title  3.What is the ID and price of the most expensive phone that has no wifi, a touch screen and  weighs more than 145 grams?

filter= data[(data['wifi'] == 'none') & (data['screen'] == 'Touch') & (data['mobile_wt'] > 145)]


if len(filter) > 0:

    most_expensive= filter.loc[filter['price'].idxmax()]
    id = most_expensive['id']
    price = most_expensive['price']

    print("ID :", id ,'Price :',price)
else:
    print("No phone  that has no wifi, a touch screen and  weighs more than 145 grams")

#4
# @title