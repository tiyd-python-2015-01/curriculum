# Blackjack

## Description

Implement the game of Blackjack.

## Objectives

### Learning Objectives

After completing this assignment, you should understand:

* how to track state by using objects

### Performance Objectives

After completing this assignment, you should be able to:

* Build an interactive game
* Test an object-oriented program

## Details

### Deliverables

* A Git repo called blackjack containing at least:
  * `README.rst` file explaining how to run your project
  * a `requirements.txt` file
  * a full suite of tests for your project

### Requirements  

* Passing unit tests
* No PEP8 or Pyflakes warnings or errors

## Normal Mode

The rules of Blackjack: https://en.wikipedia.org/wiki/Blackjack. See the additional resources for more.

Create a game of Blackjack that one person plays on the command line against a computer dealer.

* The game should start the player with $100 and bets are $10.
* The only valid moves are hit and stand.
* Allow the player to keep playing as long as they have money.
* The dealer uses one deck and reshuffles after each round.

## Hard Mode

In addition to the requirements from **Normal Mode**:

* The dealer uses a shoe of six decks. With a shoe, the dealer uses something called a _cut card_. A plastic card is inserted somewhere near the bottom of the shoe. Once it is hit, the shoe is reshuffled at the end of the round. You can simulate this by reshuffling after there are 26 or less cards left in the shoe.
* The player can choose how much they want to bet before each round.
* Add doubling-down.
* Add surrender (early surrender as opposed to late surrender.)
* Add [insurance](https://en.wikipedia.org/wiki/Blackjack#Insurance).
* Add splitting hands.

## Nightmare Mode

In addition to the requirements from **Hard Mode**:

* Add the ability to choose rulesets, like:
  * No surrender/early surrender/late surrender.
  * Dealer hits soft 17 vs dealer stands of soft 17.
  * Number of decks used in the shoe.

Each choice should be able to be made separately.

## Notes

This is again an assignment with a text-based interface, which can be very hard to test. You will do best at this assignment by building all the logic for each piece and testing it well before then adding the interface on top of it.

## Additional Resources

* Other Blackjack rule summaries:
  * http://www.pagat.com/banking/blackjack.html
  * http://wizardofodds.com/games/blackjack/basics/#toc-Rules
