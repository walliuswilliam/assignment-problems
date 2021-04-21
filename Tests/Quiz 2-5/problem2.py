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

def dummy_is_complete(x):
  if x == 'complete':
    return 1
  else:
    return 0

def dummy_is_none(x):
  if x == 'none':
    return 1
  else:
    return 0

df['testprep=complete'] = df['test preparation course'].apply(dummy_is_complete)
df['testprep=none'] = df['test preparation course'].apply(dummy_is_none)
 
for edu_type in df['parental level of education'].unique():
  dummy_variable_name = 'ParentEducation={}'.format(edu_type)
  dummy_variable_values = df['parental level of education'].apply(lambda entry: int(entry == edu_type))
  df[dummy_variable_name] = dummy_variable_values

del df['parental level of education']
del df['test preparation course']


df_train = df[:997]
df_test = df[997:]

arr_train = np.array(df_train)
arr_test = np.array(df_test)

y_train = arr_train[:,0]
y_test = arr_test[:,0]

x_train = arr_train[:,1:]
x_test = arr_test[:,1:]

regressor = LogisticRegression(max_iter=1000)
regressor.fit(x_train, y_train)

coef_dict = {}
feature_columns = df_train.columns[1:]
feature_coefficients = regressor.coef_

for i in range(len(feature_columns)):
  column = feature_columns[i]
  coefficient = feature_coefficients[0][i]
  coef_dict[column] = coefficient

y_test_predictions = regressor.predict(x_test)
y_train_predictions = regressor.predict(x_train)

def convert_regressor_output_to_survival_value(output):
  if output < 0.5:
    return 0
  else:
    return 1

y_test_predictions = [convert_regressor_output_to_survival_value(output) for output in y_test_predictions]
y_train_predictions = [convert_regressor_output_to_survival_value(output) for output in y_train_predictions]

def get_accuracy(predictions, actual):
  num_correct = 0
  num_incorrect = 0
  for i in range(len(predictions)):
    if predictions[i] == actual[i]:
      num_correct += 1
    else:
      num_incorrect += 1
  return num_correct / (num_correct + num_incorrect)


print('\nfeatures:', features_to_use)
print('\ntraining accuracy:', get_accuracy(y_train_predictions, y_train))
print('testing accuracy:', get_accuracy(y_test_predictions, y_test), '\n')

coef_dict['constant'] = regressor.intercept_[0]
print('coefficients', {a:round(b,4) for a,b in coef_dict.items()})