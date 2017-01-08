#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl 
### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import tree

clf=tree.DecisionTreeClassifier(min_samples_split=40)
t0=time()
clf=clf.fit(features_test, labels_test)
print "training time:",round(time()-t0,4),"s"
t1=time()
pred=clf.predict(features_test)
print "Prediction Time:", round(time()-t1,4),"s"
plt.plot(pred)
from sklearn.metrics import accuracy_score
print accuracy_score(pred, labels_test)
print len(features_train[0])
plt.show()



#########################################################


