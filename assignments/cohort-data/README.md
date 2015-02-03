# Analyze cohort data

## Description

Analyze the difficulty metrics for the cohort Rails and Python courses.

## Objectives

### Learning Objectives

After completing this assignment, you should understand:

* Telling stories with data

### Performance Objectives

After completing this assignment, you should be able to:

* Clean data
* Merge data

## Details

### Deliverables

* A Git repo called cohort-data containing at least:
  * `README.md` file explaining how to run your project
  * a `requirements.txt` file
  * a suite of tests for your project

### Requirements  

* Passing unit tests
* No PEP8 or Pyflakes warnings or errors

## Normal Mode

Using Pandas, load the `cohort_3_python.csv` and `cohort_3_rails.xlsx` files.
You will need to merge them together at some point in this process.

Calculate and chart:

* Mean difficulty for lectures per day, per class
* Mean difficulty for lectures per week, per class
* Mean difficulty for homework per day, per class
* Mean difficulty for homework per week, per class
* Mean difficulty for lectures and homework per week day. Is there a trend, like Mondays are easier?
* Choose a sample student from each class and graph their data. What's their story? Are they getting better over time?
