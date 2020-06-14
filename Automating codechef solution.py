#!/usr/bin/env python
# coding: utf-8

# In[59]:


from selenium import webdriver


# In[60]:


browser=webdriver.Chrome(r"C:\Users\Dhruv\chromedriver.exe")


# In[61]:


browser.get("https:\\codechef.com\\")


# In[62]:


user_element=browser.find_element_by_id("edit-name")


# In[63]:


user_element.send_keys("dhruvchadha10")


# In[64]:


user_password=browser.find_element_by_id("edit-pass")


# In[65]:


from getpass import getpass


# In[66]:


user_password.send_keys(getpass("enter the password"))


# In[67]:


browser.find_element_by_id("edit-submit").click()


# In[73]:


browser.get("https:\\codechef.com\\submit\\TEST")


# In[74]:


browser.find_element_by_id("edit-submit").click()


# In[75]:


with open("main.cpp","r") as f:
    code=f.read()


# In[76]:


browser.find_element_by_id("edit_area_toggle_checkbox_edit-program").click()


# In[77]:


code_element=browser.find_element_by_id("edit-program")


# In[78]:


code_element.send_keys(code)


# In[79]:


browser.find_element_by_xpath('//*[@id="edit-language"]/option[10]').click()


# In[80]:


browser.find_element_by_id("edit-submit-1").click()


# In[ ]:




