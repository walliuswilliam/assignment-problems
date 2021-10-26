import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

unnormalized = pd.read_csv('Tests/flower.csv')


print('Mean sepal length:', unnormalized['SepalLengthCm'].mean(), '\n')
print('Mean sepal width:', unnormalized['SepalWidthCm'].mean(), '\n')
print('Mean petal length:', unnormalized['PetalLengthCm'].mean(), '\n')
print('Mean petal width:', unnormalized['PetalWidthCm'].mean(), '\n')


min_max = unnormalized[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']].copy()
df = unnormalized[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']].copy()

for column in min_max:
  if column != 'Survived':
    min_max[column] = (min_max[column]-min(df[column]))/(max(df[column])-min(df[column]))

min_max = min_max.sample(frac=1).reset_index(drop=True)

min_max['Species'] = unnormalized['Species'].copy()
half = int(len(min_max)/2)
training = min_max[:half]
testing = min_max[half:]

train_arr = training[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']].to_numpy()
test_arr = testing[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']].to_numpy()

k_list = []
accuracies = []
for k in range(1, 75):
  accuracy = 0

  x = train_arr
  y = training['Species'].to_numpy().tolist()

  knn = KNeighborsClassifier(n_neighbors=k)
  knn.fit(x, y)
  prediction = knn.predict(test_arr)

  for prediction_index in range(len(prediction)):
    if prediction[prediction_index] == y[prediction_index]:
      accuracy += 1
  accuracies.append(accuracy/75)
  k_list.append(k)


high_k = max(accuracies)
k_index = accuracies.index(high_k)
print('best k', k_list[k_index], '\ntesting accuracy:', high_k)
