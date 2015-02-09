# Classify Iris data using Bayes methods

## Description

Train a Naive Bayes classifier to classify examples from the
classic [Iris flower data set](https://en.wikipedia.org/wiki/Iris_flower_data_set).

## Objectives

### Learning Objectives

After completing this assignment, you should understand:

* Simple Bayesian analysis
* The importance of separating training and test data

### Performance Objectives

After completing this assignment, you should be able to:

* Create a Bayesian classifier
* Train your classifier
* Test your classifier

## Details

### Deliverables

* A Git repo called iris-bayes containing at least:
  * `README.md` file explaining how to run your project
  * a `requirements.txt` file

### Requirements  

* No PEP8 or Pyflakes warnings or errors

## Normal Mode

Load the Iris data set into Python. (`sklearn.datasets.iris` has it, as well as [a CSV for Pandas](https://raw.githubusercontent.com/pydata/pandas/master/doc/data/iris.data).)

Subsample the data so that you have a training data set and a test data set.

Use the [Gaussian Naive Bayes](http://scikit-learn.org/stable/modules/naive_bayes.html#gaussian-naive-bayes) algorithm to classify the Iris data. After training it on your training data, test it on your test data. You should have 80% or higher success.

## Hard Mode

In addition to the requirements from **Normal Mode**:

Go to the [Scikit-Learn users' manual](http://scikit-learn.org/stable/user_guide.html) and read about support vector machines and nearest neighbors. Try both methods on the Iris data and see if you have better or worse results.
