#!/usr/bin/env python
# coding: utf-8

# In[9]:


pip install bardapi


# In[10]:


_BARD_API_KEY='YOUR_API_KEY'


# In[1]:


pip install python-dotenv


# In[7]:


get_ipython().system('pip install --upgrade protobuf')


# In[2]:


get_ipython().system('pip install --upgrade protobuf==3.19.0')


# In[3]:


import os
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"


# In[7]:


from bardapi import Bard
from dotenv import load_dotenv

load_dotenv()

def call_bard(query):
    # Replace 'YOUR_API_KEY' with your actual Bard API key
    bard = Bard(token='YOUR_API_KEY')
    answer = bard.get_answer(query)
    return answer['content']

# Example usage
response = call_bard("What movie would you recommend?")
print(response)


# In[ ]:




