#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import libraries (operating system)
import os 
import csv


# In[3]:


#read_csv specific to pandas
#assumes variable without quotes
file_name = os.path.join("Resources", "election_data.csv")


# In[8]:


#helps not store a previous value.. always starts at 0 instantiating
total_votes = 0 
candidate_list = []
votes_each = {}


with open(file_name) as election_data:
    line_reader = csv.reader(election_data)
#take out header, next tells it to skip index 0 
    header = next(line_reader)
    #row is a changing variable
    for row in line_reader:
        #print(row)
        total_votes = total_votes + 1
        # total_votes += 1 ; does the same thing
        candidates = row[2]
        if candidates not in candidate_list: 
            #add candidate in candidate_list
            candidate_list.append(candidates)
            votes_each[candidates] = 0 
        #tab out from forloop so that it adds vote even if they were already added once
        votes_each[candidates] = votes_each[candidates] + 1
        
#name is a new variable
for name in votes_each:
    votes_each[name] = (votes_each[name] / total_votes)*100
    
max_vote = max(votes_each, key=votes_each.get)
        
        
print(total_votes) #indent at declaration of variable or after
print(candidate_list)   
print(votes_each)
print(max_vote)


# In[ ]:




