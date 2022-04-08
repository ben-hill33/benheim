# Timing our code

Suppose we want to write a function that calculates the sum of all numbers from one up to (and including) some number _n_

In my implementation example I have two functions that do the same thing. Which one is better?
**What does better mean?**
- Is it faster?
- Less memory-intensive?
- More readable?

**The problem with Time**
- Different machines will record different times
- The _same_ machine will record different times
- For fast algorithms, speed measurements may not be precise enough

**If not time, then what?**
- Rather than counting seconds, which are so variable,
- Count the _number_ of simple operations the computer has to perform

**Counting Operations**
```
function addUpTo(n) {
  let total = 0;
  for (let i = 1; i <= n; i++) {
    total += i;
  }
  return total;
}
```
As _n_ grows, there's more assignments that happen

In this function, that does the same as the above:
```
function addUpTo(n) {
  return n * (n + 1) / 2;
}
```
There are three operations happening: multiplication, addition, and division. This will make time drastically less complex as the sum gets larger. This function's runtime would be O(1) as the complexity doesn't really increase all that much as it grows.

**Simplifying Big O Expressions**
When determining the time complexity of an algorithm, there helpful rules to abide by:
- Constants don't matter
  - O(2n) = O(n)
  - O(500) = O(1) - Constant
  - O(13n2) = O(n2)
- Smaller terms don't matter either

**Big O Shorthands**
- Arithmetic operations are constant
- Variable assignments are constant
- Accessing elements in an array (by index or key) is constant
- In a loop, the complexity is the length of the loop times the complexity of whatever happens inside of the loop




  
