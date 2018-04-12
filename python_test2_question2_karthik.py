# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 13:57:42 2018

@author: karthik
"""

#The data is read from the file students.csv. 
#The path of the file is C:\Users\User\.spyder-py3

import pandas as pd

data = pd.read_csv('C:\\Users\\user\\.spyder-py3\\students.csv')
print(data)
print()
print('Students according to ascending order of thier height')
print(data.sort_values('Height(in meters)'))
print()
data['BMI'] = data['Weight(in kg)']/(data['Height(in meters)']**2)
print(data)
print()
Health_Status = []
for i in data['BMI']:
    if(i<19):
        Health_Status.append("Under-Weight")
    elif(i<=25 and i>=19):
        Health_Status.append("Healthy-Weight")
    elif(i<=30 and i>25):
        Health_Status.append("Over-Weight")
    elif(i>30):
        Health_Status.append("Obese")
data['Status'] = Health_Status
print(data)
print()
print('Under-Weight', [data.Name[i] for i in range(len(data['Status'])) if data.Status[i] == 'Under-Weight'])
print("Healthy-Weight", [data.Name[i] for i in range(len(data['Status'])) if data.Status[i] == 'Healthy-Weight'])
print("Over-Weight", [data.Name[i] for i in range(len(data['Status'])) if data.Status[i] == 'Over-Weight'])
print("Obese", [data.Name[i] for i in range(len(data['Status'])) if data.Status[i] == 'Obese'])
