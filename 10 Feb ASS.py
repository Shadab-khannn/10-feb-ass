#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Q1. Which function is used to open a file? What are the different modes of opening a file? Explain each mode
of file opening.


# ANS - 

# You can Open files using the Open With () Method. The Open() function in python accepts two arguments. The first
# one is the file name along with the complete path and the second one is the file open mode.

# r = Open a file for Reading.
# W = Open a file for writing. 
# x = Open a file for exclusive.
# a = Open a file for appending at the end of the file without truncating it.
# b = Open in binary mode.
# 

# In[ ]:





# In[ ]:


get_ipython().run_line_magic('pinfo', 'file')


# ANS- 

# The close() method closes an open file. You should always close your files, in some cases, due to buffering, changes,
# made to a file may not show until you close the file.

# It is important to close files in python. Because files are limited resources managed by the operating system, making sure files
# are closed after use will protect against hard-to-debug issues like running out of files handles or experiencing corrupted data.

# In[ ]:





# In[ ]:


Q3. Write a python program to create a text file. Write ‘I want to become a Data Scientist’ in that file. Then
close the file. Open this file and read the content of the file.


# ANS- 

# In[28]:


f = open("test.txt", "w")


# In[29]:


for i in range(7):
    f.write("I Want to become a Data Scientist")


# In[30]:


f.close()


# In[33]:


f = open("test.txt" , "r")


# In[34]:


f.read()


# In[ ]:





# In[ ]:





# In[ ]:


Q4. Explain the following with python code: read(), readline() and readlines().


# ANS - 

# read() : This function reads the entire file and returns a string.
# readline() : This function readlines from that files and returns as a string. it fetch the line n , if it is been called nth time.
# readlines() : This function return a list where each element is single line of that file.

# In[ ]:





# In[ ]:


Q5. Explain why with statement is used with open(). What is the advantage of using with statement and
get_ipython().run_line_magic('pinfo', 'together')


# ANS - 

# The with statement works with the open() function to open a file. Unlike open() where you have to close the file with the close()
# method, the with statement closes the file for you without you telling it to. This is because the with statement calls 2 built-in
# methods behind the scene - __enter()__ and __exit()__.
# No need to explicitly close the opened file , ""with statement"" takes care of that. when with the block ends, it will automatically close 
# the file. so , it reduces the number of lines of code and reduces the chances of bug.

# In[ ]:





# In[ ]:


Q6. Explain the write() and writelines() functions. Give a suitable example.


# ANS - 

# Write() function:
#                   The write() function will write the content in the file without adding any extra characters.
#         The write() function is written in to the opened file. The string may include numbers , special characters , or
#         symbols. While writing data to a file , we must know that the write function does not add a new line characters (/n)
#         to the end of the string. The write() function returns none.

# In[36]:


data = open("test.txt" , "a")


# In[37]:


data.write("welcome to data science course")


# In[38]:


f.close()


# In[39]:


data = open("test.txt" , "r")


# In[40]:


print(data.read())


# In[ ]:





# Writelines() function:
#                       This function writes the content of a list to a file.
#         The writelines() function is written in to opened file. similar to the write()function, the writelines()function
#         does not add a newline characters(\n) to the end of the string.

# In[41]:


file1 = open("employees.txt" , "w")


# In[42]:


lst = []
for i in range (3):
    name = input("enter the name of the employee: ")
    lst.append(name + " \n ")
file1.writelines(lst)
file1.close()
print ("data is written in to the file. ")
    


# In[ ]:





# In[ ]:




