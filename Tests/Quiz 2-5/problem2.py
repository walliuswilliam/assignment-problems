import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
import sys


df = pd.read_csv('Tests/Quiz 2-5/StudentsPerformance.csv')

print('last 3 math scores', df['math score'][997:], '\n')

print('mean math scores', df['math score'].mean(), '\n')

df_completed = df[df['test preparation course'] == 'completed'].copy()
df_incomplete = df[df['test preparation course'] == 'none'].copy()

print('mean completed math scores', df_completed['math score'].mean(), '\n')
print('mean incomplete math scores', df_incomplete['math score'].mean(), '\n')

print('categories of p.l.e.', df['parental level of education'].unique(), '\n')


dummy_cols = ['test preparation course', 'parental level of education']
keep_cols = ['math score'] + dummy_cols
df = df[keep_cols]

for colname in dummy_cols:
  unique_values = df[colname].unique()
  for unique_value in unique_values:
    dummy_colname = '{}={}'.format(colname, unique_value)
    df[dummy_colname] = df[colname].apply(lambda x: int(x==unique_value) )
  del df[colname]

all_data_array = np.array(df)

train_array = all_data_array[:-3, :]
test_array = all_data_array[-3:, :]

x_train = train_array[:, 1:]
x_test = test_array[:, 1:]

y_train = train_array[:, 0]
y_test = test_array[:, 0]

regressor = LinearRegression()
regressor.fit(x_train, y_train)
predictions = regressor.predict(x_test)

print('actual values: {}'.format(y_test))
print('predictions  : {}'.format(predictions))
