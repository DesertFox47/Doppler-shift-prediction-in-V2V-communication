from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pickle
import glob
import os
from sklearn import preprocessing
from sklearn import utils
from sklearn.metrics import accuracy_score

all_files = glob.glob(os.path.join("./traindataset", "*.csv"))
li = []
for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)
frame = pd.concat(li, axis=0, ignore_index=True)

data = frame.values
X = data[:,0:5]
y = data[:,6]
#["V1", "V2", "x_acc", "y_acc", "z_acc", "angle_degrees", "observed_frequency", "gain", "observed_frequency_t5", "gain_t5", "angle_degrees_t5"]

lab_enc = preprocessing.LabelEncoder()
encoded = lab_enc.fit_transform(y)
print(utils.multiclass.type_of_target(y.astype('int')))
y=y.astype('int')

X_train, X_test, y_train, y_test = train_test_split(
             X, y, test_size = 0.2, random_state=42)


k = 197
knn_classifier = KNeighborsClassifier(n_neighbors=k)

# Fit the classifier to the training data
knn_classifier.fit(X_train, y_train)

##Make predictions on the test data
y_pred = knn_classifier.predict(X_test)
print(y_pred[0])
print(y_test[0])

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')


neighbors = np.arange(1, 100)
train_accuracy = np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))
for i, k in enumerate(neighbors):
    knn_classifier = KNeighborsClassifier(n_neighbors=k)
    knn_classifier.fit(X_train, y_train)
    train_accuracy[i] = knn_classifier.score(X_train, y_train)
    test_accuracy[i] = knn_classifier.score(X_test, y_test)
plt.plot(neighbors, test_accuracy, label = 'Testing dataset Accuracy')
plt.plot(neighbors, train_accuracy, label = 'Training dataset Accuracy')
plt.legend()
plt.xlabel('n_neighbors')
plt.ylabel('Accuracy')
plt.show()









