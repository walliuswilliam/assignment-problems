import pandas as pd
import numpy as np
import sys

df = pd.read_csv('Tests/Quiz 2-6/company_data.csv')



print('Mean training hours:', df['training_hours'].mean(), '\n')

count = 0
for value in df['target']:
  if value == 1:
    count += 1
percent_change_jobs = count/len(df['target'])
print('Percent of students looking to change jobs:', percent_change_jobs*100, '\n')

print('City with the most students:', df['city'].value_counts().idxmax(), '\n')

print('Number of students in the city:', df['city'].value_counts()[df['city'].value_counts().idxmax()], '\n')

city_numbers = []
for city_id in df['city'].unique():
  split_city = city_id.split('_')
  for i in split_city:
    if i.isdigit():
      city_numbers.append(int(i))

print('Highest city ID', max(city_numbers), '\n')


df = df.replace('<10', '0-10')
df = df.replace('10000+', '10000-999999999')
df = df.replace('10/49', '10-49')

print('Students in companies with less than 10 employees:', df['company_size'].value_counts()['0-10'], '\n')

df = df[df['company_size'].notnull()]

count2 = 0
for value in df['company_size']:
  values = value.split('-')
  values = [int(num) for num in values]
  if values[1] <= 100:
    count2 += 1

print('Students in companies with less than 10 employees:', count2)
