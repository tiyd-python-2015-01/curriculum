# Determine if text is palindromic

## Description

Write a program that asks the user for one or more sentences and then lets the user know if it is a palindrome.

## Objectives

### Learning Objectives

After completing this assignment, you should understand:

* Manipulating strings
* How strings are related to lists
* Recursion

### Performance Objectives

After completing this assignment, you should be able to:

* Strip characters out of strings
* Change the case of strings
* Look at substrings

## Details

### Deliverables

* A [gist](https://gist.github.com) containing one file called `palindrome.py`

### Requirements  

* Your program must pass the test script `test.sh`. To run this script, run `brew install roundup` first.
* Your program must output what it is doing at each step.
* Your program must use a recursive function.

## Normal Mode

You have to write a program that, when run, asks the user to input some text. It can be a phrase, a sentence, or multiple sentences. After it is entered, your program will let the user know if it is a palindrome or not. Use "is a palindrome" and "is not a palindrome" in your output in order for the tests to pass.

Letter casing and punctuation do not matter when testing a palindrome. All of the following are valid palindromes:

* stunt nuts
* Lisa Bonet ate no basil.
* A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal: Panama!
* Doc, note, I dissent. A fast never prevents a fatness. I diet on cod.

## Notes

You may want to use the `re.sub` function to strip out punctuation and spaces. A regular expression you can use to match all space and punctuation is `r'[^A-Za-z]'`.

## Additional Resources

* [Palindrome list](http://www.palindromelist.net/).
* [String type in Python](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str).
* [Regular expression operations](https://docs.python.org/3/library/re.html).
