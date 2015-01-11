# Approximate a square root

## Description

Write a program that asks the user for a positive number and then outputs the approximated square root of the number. Use Newton's method to find the square root, with epsilon = 0.01.

## Objectives

### Learning Objectives

After completing this assignment, you should understand:

* How variables work
* How `while` works
* The concept of successive approximation

### Performance Objectives

After completing this assignment, you should be able to:

* Write a Python script
* Ask for input
* Print output

## Details

### Deliverables

* A GitHub repo called approximate-square-root containing at least:
  * This `README.md` file
  * a file called `square_root.py`

### Requirements  

Here is an example of the program running correctly:

```
$ python square_root.py
Enter a positive number: 4
The square root of 4 is 2.0.

$ python square_root.py
Enter a positive number: 20
The square root of 20 is 4.472137791286727.
```

Your program will be tested with the script `test.sh`. To run this script, run `brew install roundup` first.

## Normal Mode

Newton's method of successive approximations says that whenever we have a guess `y` for the value of the square root of a number `x`, we can get a better guess (one closer to the actual square root) by averaging `y` with `x/y`. If we do this over and over, we should be able to get a very accurate guess.

You have to write a script that asks the user for a positive number and then compute the square root with a maximum error of 0.1. You then print out your answer to the user.

## Hard Mode

In each iteration of your loop, print out the current number of iterations and the current guess.

## Extra Hard Mode

Look up [complex numbers in Python](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex). Allow negative numbers as input into your program.

## Additional Resources

* Read more about [the Babylonian/Newton's method of approximating square roots](https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method).
* [Numeric types in Python](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex).

## Credit

This assignment is adapted from [SICP](https://mitpress.mit.edu/sicp/chapter1/node9.html) by Abelson and Sussman.
