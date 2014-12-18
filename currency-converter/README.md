# Currency converter

## Description

Create a set of functions to convert currency from one denomination to another.

## Objectives

### Learning Objectives

After completing this assignment, you should understand:

* Test-driven development

### Performance Objectives

After completing this assignment, you should be able to:

* Raise exceptions
* Write detailed tests
* Break down programming problems into smaller ones

## Details

### Deliverables

* A Git repo called currency-converter containing at least:
  * `README.md` file explaining how to run your project
  * a `currency` module
  * a `test_currency` set of tests

### Requirements  

* Passing unit tests
* No PEP8 or Pyflakes warnings or errors

## Normal Mode

Use test-driven development to design a function called `convert`. Below is a list of all the things it should do. In order to complete this exercise, follow these directions:

* For each requirement, write a test first, and then make the test pass, do not pass Go, do not collect $200.
* Every time you finish a requirement, commit your code with a message describing the requirement.
* Go through the requirements one-by-one. Do not skip around.

### Steps:

* Create a function called `convert` that takes a dictionary called `rates`, a number called `value`, a string called `from`, and a string called `to`. The dictionary should contain a list of tuples, with each tuple containing a currency code you can convert from, a currency code you can convert to, and a rate.

  ```py
  [("USD", "EUR", 0.74)]
  ```

  This means that each dollar is worth 0.74 euros.

  `value` is the amount of currency, `from` is the current currency code, and `to` is the currency code you wish to convert to.

  Given the above rates, make sure that converting 1 dollar into euros returns the following value: `0.74`.

* Next, test that converting 1 euro into dollars returns `1.35` (or an approximation).
* Next, test that you can convert more than one unit of currency.
* Next, as a sanity check, make sure that if you try to convert 1 dollar into dollars, `1.0` is returned.
* Create a new list of rates with two or more tuples. Make sure you can convert both ways with each rate. For example, with these rates:

  ```py
  [("USD", "EUR", 0.74),
   ("EUR", "JPY", 145.949)]
  ```

  Make sure you can convert from USD to EUR, EUR to USD, EUR to JPY, and JPY to EUR.
* Make sure that if you try to make a conversion you do not know about, a `ValueError` is raised with an appropriate message.

## Hard Mode

In addition to the requirements from **Normal Mode**:

* Test that you can convert between any two rates that you have the ability to, even if you do not have a direct conversion rate for them. For example, with the rates:

  ```py
  [("USD", "EUR", 0.74),
   ("EUR", "JPY", 145.949)]
  ```

  Make sure you can convert from USD to JPY.


## Additional Resources

* [Currency charts](http://www.xe.com/currencycharts/) if you want accurate values.
* The [pytest](http://pytest.org/latest/) testing framework.
* [An Introduction to Test Driven Development](https://www.codeenigma.com/community/blog/introduction-test-driven-development).
* [Test-Driven Development](https://en.wikibooks.org/wiki/Introduction_to_Software_Engineering/Testing/Test-driven_Development) on Wikibooks.
* [Test-Driven Development by Example](http://www.amazon.com/Test-Driven-Development-By-Example/dp/0321146530), the canonical book on this stuff.
