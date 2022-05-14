#!/usr/bin/env python
# coding: utf-8

# In[28]:


url='https://nam11.safelinks.protection.outlook.com/?url=https%3A%2F%2Fconvertio.co%2F&data=04%7C01%7CKeshav.Kunal%40everestgrp.com%7Cfe4eba709d1947af1b7408d9f62e1561%7C29656626bbab4437ba66213753425fd1%7C0%7C0%7C637811503447524991%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000&sdata=lo%2Bz4TkN%2BeZRuW1KMWt6Oi581gB758e%2FW61m47byW0Y%3D&reserved=0'                
path = "G:\\Driver\\chromedriver.exe"

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path=path)
driver.implicitly_wait(0.5)
driver.maximize_window()

driver.get(url) #url
           
#to identify element
s = driver.find_element(By.XPATH, "//input[@type='file']")
           
#file path specified with send_keys
s.send_keys("G:\\Final_Code\\data.csv")


# In[ ]:




