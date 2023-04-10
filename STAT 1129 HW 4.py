#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
array = np.arange(1, 13)
array = arr1d.reshape(3, 4)
print(array)


# In[6]:


import numpy as np
array = np.arange(1, 13)
array = array.reshape(3, 4)
array *= 2
print("Dimension of the array:", array.ndim)
print("Shape of the array:", array.shape)


# In[8]:


import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        print(arr[i, j], end=' ')
    print() 


# In[9]:


for i in np.nditer(arr):
    print(i, end=' ')


# In[11]:


import numpy as np
import matplotlib.pyplot as plt
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([5, 6, 7, 8, 9, 10])
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


# In[14]:


import matplotlib.pyplot as plt
x = [3, 6, 9, 12]
y = [2, 8, 1, 10]
plt.plot(x, y, marker='o')
plt.plot(x[0], y[0], marker='o', markersize=10, color='blue')  
plt.plot(x[1], y[1], marker='o', markersize=10, color='blue')  
plt.plot(x[2], y[2], marker='o', markersize=10, color='blue') 
plt.plot(x[3], y[3], marker='o', markersize=10, color='blue')  
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Line Plot')
plt.show()


# In[16]:


import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4, 5]
y = [2, 4, 6, 14, 10, 12]
plt.plot(x, y, 'o', markersize=10, color='green')
plt.plot(x, y, '--', color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Line Plot')
plt.show()


# In[21]:


import matplotlib.pyplot as plt
x1 = [0, 4]
y1 = [1, 5]
x2 = [0, 4]
y2 = [5, 9]
x3 = [0, 4]
y3 = [9, 13]
plt.plot(x1, y1, color='blue', linestyle='-')
plt.plot(x2, y2, color='orange', linestyle='-')
plt.plot(x3, y3, color='green', linestyle='-')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Multiple Line Plot')
plt.show()


# In[29]:


import matplotlib.pyplot as plt
marks = {'Andy': 88, 'Amy': 66, 'James': 90, 'Jules': 55, 'Arthur': 77}
names = list(marks.keys())
grades = list(marks.values())
plt.bar(names, grades)
plt.title('Marks Bar Chart')
plt.xlabel('Student')
plt.ylabel('Mark')
plt.show()
plt.pie(grades, labels=names, autopct='%1.1f%%')
plt.title('Marks Pie Chart')
plt.legend()
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
plt.show()


# In[32]:


import matplotlib.pyplot as plt
import numpy as np
fig, axs = plt.subplots(2, 3, figsize=(10, 6))
fig.suptitle('Subplots Example')
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
axs[0, 0].plot(x, y1, label='Sin(x)')
axs[0, 0].plot(x, y2, label='Cos(x)')
axs[0, 0].set_title('Multiple Lines Plot')
axs[0, 0].legend()
names = ['A', 'B', 'C', 'D', 'E']
values = [10, 8, 6, 4, 2]
axs[0, 1].bar(names, values)
axs[0, 1].set_title('Bar Chart')
fruits = ['Apple', 'Banana', 'Cherry', 'Durian']
quantities = [30, 20, 10, 5]
axs[0, 2].pie(quantities, labels=fruits, autopct='%1.1f%%')
axs[0, 2].set_title('Pie Chart')
x = np.random.rand(100)
y = np.random.rand(100)
colors = np.random.rand(100)
sizes = 100 * np.random.rand(100)
axs[1, 0].scatter(x, y, c=colors, s=sizes)
axs[1, 0].set_title('Scatter Plot')
values = np.random.randn(1000)
axs[1, 1].hist(values, bins=20)
axs[1, 1].set_title('Histogram')
x = np.arange(-3, 3, 0.1)
y = np.sin(x)
axs[1, 2].plot(x, y)
axs[1, 2].grid()
axs[1, 2].set_title('Grid')
plt.subplots_adjust(hspace=0.5, wspace=0.5)
plt.show()


# In[ ]:




