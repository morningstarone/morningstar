# Statistics:
#  grp of methods to collect analyse and present and interpret data

# Variables:
# quantitative variables:
#   variable that can be measured numerically. Data collected on quantitative variable are called quantitative data
#   variable that can assume 
# Nominal variables:
#   variables that have values that have no logical ordering
# ordinal variables:
#   have values with logical order, but the relative distances b/w values aren't clear
# Interval & ratio scales:
#   continuous variables have values with a logical order, and the relative distances b/w values are meaningful.
#   Continuous variables can be either 'ratio' level or 'interval' level. Ratio measures have a true 0 point.

# Data is categorised into:
#   descriptive statistics:
#       collect, classify, represent, predict data
#       centre of tendency:
#           Mean, mode, median, outlier
#       Level of dispersion:
#           variance
#           std
#           range
#           skewness
#           quartiles

# Skewness:
#   Skp=Mean-Mode/std  -3<=skp<=3

import numpy as np

arr12=np.array([[2,3,4,5],[9,7,0,5]])
# print(arr)
# print(np.ndim(arr))
# print(np.shape(arr))
# print(np.reshape(arr,[4,2]))
# print(arr[0])

# np.arange(1,11).reshape(5,2)

# np.linspace(1,10,5)

# def create_arr():
#     arr=np.array([[2,3,4,5],[9,7,0,5]])
#     print(dimension(arr))
#     print(arr.mean())
#     arr1=np.append(arr,[[78,98,23,9],[345,56,89,12876]],axis=0)
#     print(arr1)
# def dimension(arr):
#     return arr.T

# create_arr()

from numpy import random
import pandas as pd
x=random.randint(100)
print(x)

x=random.randint(100,size=(5))
print(x)

df=pd.DataFrame(np.random.randint(0,100,size=(365,5)))
print(df)

arr=np.random.randint(0,50,size=(365,5))
arr1=np.mean(arr,axis=0)
print(arr1)
arr2=np.max(arr,axis=0)
print(arr2)

arr3=np.min(arr,axis=0)
print(arr3)

arr4=np.std(arr,axis=0)
print(arr4)

l=[]
arr5=(np.max(arr,axis=1)-np.min(arr,axis=1))
print(np.max(arr5))
print(np.where((arr5==np.max(arr5))))
print(arr5.shape)

days_above_30_NY = np.sum(arr[:, 0] > 30)
print(days_above_30_NY)

current_streak = 0
max_streak = 0

for temp in arr[:, 1]:
    if temp < 20:
        current_streak += 1
    else:
        if current_streak > max_streak:
            max_streak = current_streak
        current_streak = 0


if current_streak > max_streak:
    max_streak = current_streak

print("\nLongest streak of days with temperature below 20°C in Los Angeles:", max_streak)

print(max(np.mean(arr[:,3]),np.mean(arr[:,2])))

print(np.corrcoef(arr[:,4],arr[:,1])[0,1])

print(np.mean(arr[:31,0]))

print(np.mean(arr[31:59,0]))

print(np.mean(arr[59:90,0]))

print(np.mean(arr[90:120,0]))

print(np.mean(arr[120:151,0]))

print(np.mean(arr[151:181,0]))

print(np.mean(arr[181:212,0]))
print(np.mean(arr[212:243,0]))
print(np.mean(arr[243:273,0]))
print(np.mean(arr[273:304,0]))
print(np.mean(arr[304:334,0]))
print(np.mean(arr[334:365,0]))


arr_m=np.array([np.mean(arr[:31,4]),np.mean(arr[31:59,4]),np.mean(arr[59:90,4]),np.mean(arr[90:120,4]),
np.mean(arr[120:151,4]),
np.mean(arr[151:181,4]),
np.mean(arr[181:212,4]),
np.mean(arr[212:243,4]),
np.mean(arr[243:273,4]),
np.mean(arr[273:304,4]),
np.mean(arr[304:334,4]),
np.mean(arr[334:365,4])])
print(arr_m.shape)
print('max value for phoenix:',np.where(arr_m==np.max(arr_m)))



import numpy as np

def normalize_temperature_data(arr):

    mean_temperatures = np.mean(arr, axis=0)
    std_dev_temperatures = np.std(arr, axis=0)
    
    normalized_data = (arr - mean_temperatures) / std_dev_temperatures
    
    return normalized_data


normalized_data = normalize_temperature_data(arr)

print("Normalized temperature data:")
print(normalized_data)
def miss(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j]=='Nan':
                print('null value')
print(miss(arr))
       