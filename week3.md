# Week 3

## Day 1

*Question of the day:* How would you find the odds of rolling 21 or higher on 6 dice using a computer?

### Goals

* Stochastic programming
* Randomness

### Exercise

Compute the value of pi only using randomness.

Imagine you have a 1 meter by 1 meter square. This square has a circle inscribed in it so that the diameter of the circle is 1 meter.

If you generate random points in the square, you should be able to tell if the points are inside or outside the circle.

### Assignment

[Random art](assignments/random-art)

## Day 2

*Question of the day:* Given the following lifespans, taken from a much larger population, what percentage of people would you expect to live to be older than 99?

Data: [52, 61, 67, 75, 79, 92, 94, 97, 100, 100]

### Goals

* Plotting
* Simple statistics
* Basic statistical inquiry

### Exercise

Take these weights of domestic house cats:

```py
weights = [11.3, 8.06, 9.96, 9.76, 10.09, 9.93, 9.76, 11.47, 8.09, 11.38, 8.47, 9.44, 10.52, 8.02, 9.46, 8.44, 8.95, 9.26, 10.62, 8.76]
```

Plot a histogram of these weights. Find the mean and standard deviation of this sample of cat weights.

### Assignment

[Plotting randomness in a notebook](assignments/charting)


## Day 3

*Question of the day:* No question today.

### Goals

* Creating simulations
* Monte Carlo simulations

### Plan

Live code a simulation of Roombas.

* Room to be vacuumed is 15x20 feet.
* Each turn, the Roomba moves 1 foot (or until it hits a wall). Whatever space the Roomba is on is cleaned.
* Assume the Roomba can remember only one thing: the number of degrees it last rotated.
* Our default Roomba will move in a straight line until it hits a wall, then will rotate 90-270 degrees.

### Exercise

No exercise today.

### Assignment

[Some Pig](assignments/some-pig)

## Day 4

*Question of the day:*

### Goals

* NumPy

### Exercise

You run a department store. During lunch hours, you get your biggest volume of
customers, with an average of 100.

Most customers take 2 to 3 minutes (70% of customers), but 30% of customers
are high-maintenance and take 7-10 minutes. (Look at `numpy.fromfunction` for
  an idea on how to handle this.)

If you want to make sure you can handle the average workload, how many cashiers
do you need? If you want to be able to handle 1 standard deviation above the
average work load, how many then?

### Assignment

[Traffic simulation](assignments/traffic-simulation)
