# Classifing spam

## Description

Use the Spambase dataset to classify spam. This data is already parsed down from email to features.

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

* A Git repo called spambase containing at least:
  * `README.md` file explaining how to run your project
  * a `requirements.txt` file

### Requirements  

* No PEP8 or Pyflakes warnings or errors

## Normal Mode

Go to the UCI Machine Learning repository and [download the Spambase dataset](https://archive.ics.uci.edu/ml/datasets/Spambase). Make sure you [read the documentation for the data](https://archive.ics.uci.edu/ml/machine-learning-databases/spambase/spambase.DOCUMENTATION). This explains what the attributes are in the data file.

Subsample the data set so 60% is training data and 40% is test data. You can subsample however you like, including splitting the original file. Just make sure that you have a representative data set. (The original is about 60% not-spam and 40% spam.)

Then write code to classify the data into spam and not-spam, training with your training data and testing on your test data. Try multiple classifiers to see which gives you the highest success.
