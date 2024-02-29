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
# @title 2.What is the average battery power for single-sim phones that have a camera or front camera  with a higher resolution than 12 megapixels?
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
# @title Create a pivot table that shows the percentage of phones with Bluetooth per generation,  pivoted around the phone generation and split by “ram” quartiles. (i.e. the rows are the  generation number and the columns are 4 quartiles of ram size).
data['ram_quartile'] = pd.qcut(data['ram'], q=4)
pivot_table = pd.pivot_table(data, values='bluetooth', index='gen', columns='ram_quartile', aggfunc=lambda x: np.mean(x == 'Yes'))
print("Pivot table for Bluetooth percentage per generation and RAM quartiles:", pivot_table)

#5
# @title Create a new Dataframe based on the original that has the following features: [id,  battery_power, ram, talk_time, Bluetooth, cores, sim, memory, price], and contains a random  sampling of half of the medium speed phones.

phones = data[data['speed'] == 'medium'].sample(frac=0.5, random_state=42)
new_data = phones[['id', 'battery_power', 'ram', 'talk_time', 'bluetooth', 'cores', 'sim', 'memory', 'price']]
print('new dataFrame for task 2,5',new_data)

#6
# @title Using this new dataset, what is the maximum total talk time you can achieve if you use 3  phones, and which 3 phones will you use?
selected_phones = new_data.sort_values(by='talk_time', ascending=False).head(3)
talk_time_maximum = selected_phones['talk_time'].sum()
print(" phones with the maximun talk time:")
print(selected_phones)
print("\nMaximum total talk time achievable with these phones:", talk_time_maximum)
=======
print(data.head(100))
