#!pip install numpy
#pip install matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#from google.colab import drive
#mobile_price_csv= "/content/mobile_price_1.csv"

#Task 1

#1
# @title Loading the data into a Pandas Dataframe.
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
print(data)


#6
# @title 6. Change the memory column to hold the memory in GB instead of MB.