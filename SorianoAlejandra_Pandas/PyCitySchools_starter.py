#!/usr/bin/env python
# coding: utf-8

# # PyCity Schools Analysis
# 
# * As a whole, schools with higher budgets, did not yield better test results. By contrast, schools with higher spending per student actually (\$645-675) underperformed compared to schools with smaller budgets (<\$585 per student).
# 
# * As a whole, smaller and medium sized schools dramatically out-performed large sized schools on passing math performances (89-91% passing vs 67%).
# 
# * As a whole, charter schools out-performed the public district schools across all metrics. However, more analysis will be required to glean if the effect is due to school practices or the fact that charter schools tend to serve smaller student populations per school. 
# ---

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[2]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
school_data = "Resources/schools_complete.csv"
student_data = "Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas Data Frames
school_data = pd.read_csv(school_data)
student_data = pd.read_csv(student_data)

# Combine the data into a single dataset
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])


# ## District Summary
# 
# * Calculate the total number of schools
# 
# * Calculate the total number of students
# 
# * Calculate the total budget
# 
# * Calculate the average math score 
# 
# * Calculate the average reading score
# 
# * Calculate the overall passing rate (overall average score), i.e. (avg. math score + avg. reading score)/2
# 
# * Calculate the percentage of students with a passing math score (70 or greater)
# 
# * Calculate the percentage of students with a passing reading score (70 or greater)
# 
# * Create a dataframe to hold the above results
# 
# * Optional: give the displayed data cleaner formatting

# In[3]:


total_schools = school_data["School ID"].count()
total_schools


# In[4]:


total_students = student_data["Student ID"].count()
total_students


# In[5]:


total_budget = school_data["budget"].sum()
total_budget


# In[6]:


average_math = student_data["math_score"].mean()
average_math


# In[7]:


average_reading = student_data["reading_score"].mean()
average_reading


# In[8]:


average_score = (average_reading + average_math) /2
average_score


# In[9]:


passing_math = student_data.loc[student_data["math_score"] >= 70, [
    "math_score"]]
passing_math.head()


# In[10]:


passing_reading = student_data.loc[student_data["reading_score"] >= 70, [
    "reading_score"]]
passing_reading.head()


# In[11]:


percentage_math= ((passing_math["math_score"].count())/total_students)*100
percentage_math


# In[12]:


percentage_reading= ((passing_reading["reading_score"].count())/total_students)*100
percentage_reading


# In[13]:


stats_df = pd.DataFrame({
    "Total Schools": [total_schools],
    "Total Students": [total_students],
    "Total Budget $": [total_budget],
    "Average Math Score":[average_math],
    "Average Reading Score": [average_reading],
    "% Passing Math": [percentage_math],
    "% Passing Reading": [percentage_reading],
    "% Overall Passing Rate": [average_score]
})
stats_df


# In[11]:





# ## School Summary

# * Create an overview table that summarizes key metrics about each school, including:
#   * School Name
#   * School Type
#   * Total Students
#   * Total School Budget
#   * Per Student Budget
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)
#   
# * Create a dataframe to hold the above results

# ## Top Performing Schools (By Passing Rate)

# * Sort and display the top five schools in overall passing rate

# In[52]:


perstudent = (school_data["budget"])/(school_data["size"])
school_data["Per Student Budget"] = perstudent
school_data.head()


# In[15]:


average_grades = student_data[["school_name", "reading_score", "math_score"]]
average_grades.head()


# In[47]:


school_group = average_grades.groupby(["school_name"])
average_school = school_group.mean()
average_school.head()


# In[46]:


student_70_math = ((student_data["math_score"] >= 70).groupby(student_data.school_name).sum())
student_70_math


# In[48]:


student_70_reading = ((student_data["reading_score"] >= 70).groupby(student_data.school_name).sum())
student_70_reading


# In[ ]:





# In[13]:





# ## Bottom Performing Schools (By Passing Rate)

# * Sort and display the five worst-performing schools

# In[14]:





# ## Math Scores by Grade

# * Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.
# 
#   * Create a pandas series for each grade. Hint: use a conditional statement.
#   
#   * Group each series by school
#   
#   * Combine the series into a dataframe
#   
#   * Optional: give the displayed data cleaner formatting

# In[66]:





# In[15]:





# ## Reading Score by Grade 

# * Perform the same operations as above for reading scores

# In[16]:





# ## Scores by School Spending

# * Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)

# In[17]:


# Sample bins. Feel free to create your own bins.
spending_bins = [0, 585, 615, 645, 675]
group_names = ["<$585", "$585-615", "$615-645", "$645-675"]


# In[18]:





# ## Scores by School Size

# * Perform the same operations as above, based on school size.

# In[ ]:


# Sample bins. Feel free to create your own bins.
size_bins = [0, 1000, 2000, 5000]
group_names = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]


# In[19]:





# ## Scores by School Type

# * Perform the same operations as above, based on school type.

# In[20]:





# In[ ]:




