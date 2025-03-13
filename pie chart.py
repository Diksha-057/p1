#Pie Chart
import matplotlib.pyplot as plt
import numpy as np
y=np.array([1,2,3,4,5,])
cars=['ertiga','Creta','Thar','Nexon','Swift']
plt.title("Pie chart")
plt.pie(y, labels=cars,startangle=90,autopct="%d")
plt.legend(cars)
plt.show()
