#!/usr/bin/env python
# coding: utf-8

# # test page

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


x = np.array([i for i in range(10)])
y = np.array([i**2 for i in range(10)])

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()


# ```{admonition} 確率密度関数と分布関数
# :class: seealso
# 
# \begin{gather*}
# F(x) = \int_{-\infty}^x f(t)dt \\
# P(a\leq X\leq b) = F(b)-F(a) = \int_{a}^b f(t)dt
# \end{gather*}
# 
# ```
