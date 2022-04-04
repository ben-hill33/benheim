# Game of Greed

## [Random Module](https://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python)
The random module provides access to functions that support many operations, like generating random numbers. 

### Random functions
- **randint** - import random -> `print random.randint(0, 5) `
  - This will output either 1, 2, 3, 4 or 5
- **random** - random.random() * 100
  - Outputs random number between 0 and 100
- **choice** - generate random value from the sequence 
  - `random.choice( ['red', 'black', 'green'] )`
  - `myList = [2, 109, False, 10, "Lorem", 482, "Ipsum"]
random.choice(myList)`
- **shuffle** - shuffles the elements in list in place, so they are in a random order
  - `from random import shuffle
x = [[i] for i in range(10)]
shuffle(x)`
- **randrange** - Generate a randomly selected element from range(start, stop, step)

- More on [random, python docs](https://docs.python.org/3/library/random.html)
- [Generating Random Data in Python](https://realpython.com/python-random/)


## [What is Risk Analysis in Software Testing and how to perform it?](https://www.edureka.co/blog/risk-analysis-in-software-testing/)
The probably of any unwanted incident is defined as Risk. In software testing, risk analysis is the process of identifying the risks in applications or software that you built and prioritizing them to test. 

### Why use Risk Analysis?
Using risk analysis at the beginning of a project highlights the potential problem areas. Here is a list of possible risks you could encounter:
1. Use of new hardware
2. Use of new technology
3. Use of new automation tool
4. The sequence of code
5. Availability of test resources for the application

Unavoidable risks:
1. Time allocated for testing
2. Defect leakage due to the complexity or size of the application
3. Urgency from the clients to deliver the project
4. Incomplete requirements

In such cases, use:
- Conduct risk assessment review meeting
- Use maximum resources to work on high-risk areas
- Create a risk assessment database for future use
- Identify and notice the risk magnitude indicators: high, medium, low
  - High: the effect of the risk would be very high and non-tolerable
  - Medium: Tolerable but not desirable. Limited risk
  - Low: Tolerable. Little or no external exposure or no financial loss

## Lecture notes

Welcome to Game of Greed
(y)es to play or (n)o to decline
> y
Starting round one
Rolling 6 dice...
*** 1 1 3 3 6 6 ***
Enter dice to keep, or (q)uit:
> 113366
YOu have 1500 unbanked points and 0 dice remaining
(r)oll again, (b)ank your points or (q)uit:
*** random output of numbers as above ***

[counter method](https://pymotw.com/3/collections/counter.html)

[Table of Contents](../index.md)
