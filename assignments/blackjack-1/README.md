# Blackjack, Part I

## Description

Plan how to create a game of blackjack.

## Objectives

### Learning Objectives

After completing this assignment, you should understand:

* Object-oriented design.

### Performance Objectives

After completing this assignment, you should be able to:

* Design a system using responsibilities and collaborators.
* Turn your design into objects.

## Details

### Deliverables

* A Git repo called blackjack containing at least:
  * a `README.md` file explaining your design.
  * a `lib/blackjack` directory with a file for each of your classes, with
    their responsibilities and collaborators described in a comment
  * a completed Card and Deck class
  * tests for Cards and Decks

### Requirements  

* Passing unit tests
* No PEP8 or Pyflakes warnings or errors

## Normal Mode

Read through [the rules of blackjack](https://en.wikipedia.org/wiki/Blackjack)
carefully. After reading through them, write out the steps to run the game in
outline format. (See the additional resources for more on the rules of
blackjack.)

After that, go through your steps and find all the actors -- that is, nouns
that take actions. Create class-responsibility-collaborator (CRC) cards for
each and then create empty classes for each of them with the responsibilities
and collaborators at the top as a comment. Here is an example that you might
find in `lib/blackjack/card.py`:

```py
class Card:
    """A playing card.

    Responsibilities:

    * Has a rank and a suit.
    * Has a point value. Aces point values depend on the Hand.

    Collaborators:

    * Collected into a Deck.
    * Collected into a Hand for each player and a Hand for the dealer.
    """  
```

Lastly, implement the `Card` and `Deck` classes.

## Additional Resources

* Other Blackjack rule summaries:
  * http://www.pagat.com/banking/blackjack.html
  * http://wizardofodds.com/games/blackjack/basics/#toc-Rules
* [Portland Pattern Repository page on CRC cards](http://c2.com/cgi/wiki?CrcCard)
* [A Brief Tour of Responsibility-Driven Design](http://www.wirfs-brock.com/PDFs/A_Brief-Tour-of-RDD.pdf)
