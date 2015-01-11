# Calculate word frequency

## Description

Write a program that looks for a file called `sample.txt`. This file will contain the text of a book, part of a book, or speech in plain text format. It reads this file and then returns the top 20 words used in the text and the number of times they are used.

## Objectives

### Learning Objectives

After completing this assignment, you should understand:

* Reducing a collection into another form

### Performance Objectives

After completing this assignment, you should be able to:

* Open and read files
* Create a dictionary
* Sort a list

## Details

### Deliverables

* A GitHub repo called approximate-square-root containing at least:
  * This `README.md` file
  * a file called `word_frequency.py`

### Requirements  

* Your program must pass my tests in `word_frequency_test.py`. You should be able to run this with `python word_frequency_test.py`.
* You need a function called `word_frequency` that takes a string and returns a dictionary of all the words used in the string and the number of times they were used.

## Normal Mode

Your program should open `sample.txt` and read in the entirety of its text. You'll need to normalize the text so that words in different cases are still the same word and so it's scrubbed of punctuation. Once you've done that, go through the text and find the number of times each word is used.

After that, find the top 20 words used and output them to the console in reverse order, along with their frequency, like this:

```
peanut 33
racket 31
and 29
common 21
religion 15
fate 14
algorithm 10
the 9
...
```

## Hard Mode

In addition to the requirements from **Normal Mode**:

1. Change your program so that you have to give it the name of the file to read on the command line, like so: `python word_frequency.py sample.txt`.

2. Output the words to the console in a simple text-based histogram format, like so:

```
peanut    #################################
racket    ###############################
and       #############################
common    #####################
religion  ###############
fate      ##############
algorithm ##########
the       #########
...
```

## Additional Resources

* [Project Gutenberg](https://www.gutenberg.org/) - good source of free texts.
* [String type in Python](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str).
* [Regular expression operations](https://docs.python.org/3/library/re.html).
