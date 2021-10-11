import pandas as pd
import numpy as np
df_iris_data=pd.read_csv('C:/Users/akshansh/Desktop/noddy/IRIS.csv')
df_iris_data.columns # or row

import matplotlib.pyplot as plt # liberary for bar Chart

plt.hist(df_iris_data,bins = 5,color = 'red')
plt.bar(df_iris_data.sepal_length,df_iris_data)
#box plot - to find the outlier
plt.boxplot(df_iris_data,vert = False)

#scater plot
x = [1,5,6,7,8,9,10,50,25]
y = [2,3,4,5,6,10,5,4,10]

plt.plot(x,y,".--g") #fmt = [marker][line][color]
plt.plot(x,y,"v:r") 

#multiple line
x = np.array([0,2,6,8])
y1 = np.array([4,7,8,1])
y2 =np.array([6,9,10,2])
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y1,x,y2)

#labels and titles
plt.plot(x,y1,x,y2)
plt.xlabel("stunumber")
plt.ylabel("height")
plt.title('height chart')
plt.grid(axis = 'x',color ='r',lw ='.5') 

#subplots

#column wise splitting
#plot1
plt.subplot(1,2,1) # 1 row and 2 columns 1 first graph
plt.plot(y1)
#plot 2
plt.subplot(1,2,2)
plt.plot(y2)

plt.subplot(2,1,1) # 1 row and 2 columns 1 first graph
plt.plot(y1)

#plot 2
plt.subplot(2,1,2)
plt.plot(y2)
plt.xlabel("stunumber")











