#!/usr/bin/env python
# coding: utf-8

# # Directives
# 
# ```{attention}
# attention
# ```
# 
# ```{caution}
# caution
# ```
# 
# ```{danger}
# danger
# ```
# 
# ```{error}
# error
# ```
# 
# ```{hint}
# hint
# ```
# 
# ```{important}
# important
# ```
# 
# ```{note}
# note
# ```
# 
# ```{seealso}
# seealso
# ```
# 
# ```{tip}
# tip
# ```
# 
# ```{warning}
# warning
# ```
# 
# ```{admonition} tip
# :class: tip
# admonoition
# ```
# 
# ```{code-block} python
# A = list(map(int, input().split()))
# print(A)
# ```
# 
# ```{code-block} cpp
# int main(int argc, char *argv[]) {
#     return 0;
# }
# ```

# In[1]:


a = 3
b = 4
print(a*b)


# In[2]:


get_ipython().system('jupyter-book create --help')


# In[3]:


get_ipython().system('jupyter-book create --help')


# ````md
# ```{directivename} arg1 arg2
# :key1: metadata1
# :key2: metadata2
# My directive content.
# ```
# ````
# 
# 
# 
# {fa}`check,text-success mr-1` This is an example of Roles (check mark & success color).
# 
# {fa}`check,text-info mr-1` This is an example of Roles (check mark & info color).
