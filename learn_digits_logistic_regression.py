# -*- coding: utf-8 -*-
"""
Learns a model for classifying images of handwritten digits.
The specific dataset is hosted at UCI Machine Learning Repository 
Created on Thu Mar  6 13:36:38 2014

@author: pruvolo
"""

import matplotlib.pyplot as plt
import numpy
from sklearn.datasets import *
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression

data = load_digits()
print data.DESCR
n_trials = 1
train_percentages = range(5,95,5)
test_accuracies = numpy.zeros(len(train_percentages))

for (i,train_percent) in enumerate(train_percentages):
	test_accuracy = numpy.zeros(n_trials)
	for n in range(n_trials):
		X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, train_size=train_percent/100.0)
		model = LogisticRegression()
		model.fit(X_train, y_train)
		test_accuracy[n] = model.score(X_test, y_test)
	test_accuracies[i] = test_accuracy.mean()

fig = plt.figure()
plt.plot(train_percentages, test_accuracies)
plt.xlabel('Percentage of Data Used for Training')
plt.ylabel('Accuracy on Test Set')
plt.show()
