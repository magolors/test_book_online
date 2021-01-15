#!/usr/bin/env python
# coding: utf-8

# # test page

# In[11]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[12]:


x = np.array([i for i in range(10)])
y = np.array([i**2 for i in range(10)])

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()


# ```{note}
# This is an example of directives.
# ```
