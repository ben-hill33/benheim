# DSA review

## [Whiteboard interview advice](https://hackernoon.com/the-best-whiteboard-interview-advice-i-ever-received-3ebbfa72e4a)

When given a problem to solve, don't just approach the whiteboard and attempt to solve it, even if you think you understand the problem, you should take these steps before moving forward:
- _Restate the question_
  - It's important to restate the question because, if you think you understand the question and how to solve the problem, restating the question might bring up something you didn't think about
  - You might also see that you didn't actually understand the question
  - A good example if the question was fizz buzz:
    - "So I'd like to restate the problem to you to make sure I understand what you're looking for. 
    - The sole parameter for my function will be an integer. 
    - The sole output of my function will be an incrementing array, starting from the number 1 and ending at the input number
    - If a number is a multiple of 3, the output will insteada be 'fizz'. 
    - If a number is a multiple of 5, the output will instead be 'buzz'.
    - However, if the output is a multiple of both 3 and 5, the output will instead be 'fizzbuzz'. 
    - Is my understanding correct?"
  - The interviewer should give you affirmation or perhaps your understanding was incorrect and they'll help you understand
  - There's no situation where restating the problem will hurt you
    - It shows you can articulate a problem _and gives you time to think it through while you discuss_.
  - It will also help you quite your nerves if you're feeling some anxiety
- _Ask about edge cases_
  - Think about the inputs and expected output and think about potential edge cases to the problem
  - _Ask about them_
  - In many cases, the interviewer hasn't even thought about edge cases and will make something up.
- _Ask about test cases_
  - Ask your interviewer if there's any test cases the function should pass. 
  - Your interviewer might be _expecting_ you to ask this question
  - It's also possible they're _not expecting_ it and will show you're thinking about testing
- _Write pseudo code and ask if it makes sense_
  - You don't actually want to start writing code in an actual language
  - There's constraints like remembering idiosyncrasies of the language rather than trying to come up with the correct logic
  - Ask the interviewer if your pseudo code makes sense
    - They may be the type that doesn't want to give you hints, or
    - They might be interested in how you think and want to discuss your pseudo code with you.
  - The worst case is the interviewer will tell you to continue without offering feedback
  - The best case is te interviewer might point out logical flaws in your pseudo code that will give you some serious benefit when transitioning to actual code
  - _Bonus_: if your pseudocode looks good but you end up having difficulty translating it to actual doe, you have earned a lot of points by now
  - Example pseudocode for fizzbuzz:
```
const = fizzBuzz(n) {
 // If n is not a number or not an integer greater 
 // than zero, return null
 
 // create empty array to store output
 
 // Loop through numbers from 1 to n
 
  // If number modulo 3 is zero, add ‘fizz’ 
  // to output array
  // Else If number modulo 5 is zero, 
  // add ‘buzz’ to output array
  // Else If number modulo 3 is zero and 
  // number modulo 5 is zero, add ‘fizzbuzz’ 
  // to array
  // Else add the number to the array
 
 // return output array
}
```

At this point you might realize that you'd never get to the third 'else-if' statement.
- Alternatively, when you confirm your pseudocode with the interviewer, they might offer that for free.
- In that case you can rewrite your pseudocode to make sure you check the third condition first:
```
function fizzBuzz(n) {
 // If n is not a number or not an integer greater 
 // than zero, return null
 
 // create empty array to store output
 
 // Loop through numbers from 1 to n
  // If number modulo 3 is zero and 
  // number modulo 5 is zero, add ‘fizzbuzz’ 
  // to array
 
  // Else If number modulo 3 is zero, add ‘fizz’ 
  // to output array
  // Else If number modulo 5 is zero, 
  // add ‘buzz’ to output array
  // Else add the number to the array
 
 // return output array
}
```

- _Write the actual code and ask if it looks good_
- _Stuck? Ask for help!_
  - It's not illegal to ask for help, just phrase it conversationally,
  - "I'm a little stuck, do you have any tips to get me moving in the right direction?"
    - The answer might be no, but it might also be yes, so it's worth a shot


## [7 tips to ace a programming interview](https://blog.usejournal.com/6-tips-to-ace-a-whiteboard-programming-interview-f06c1b378bc6)

- _Take a few minutes_
  - What the advice from the previous article above overlooks is that it's difficult to really think critically about a problem while you're talking
  - When the interviewer gives you a problem, it's ok to repeat the question, then say something like, _"Got it. If it's ok with you, I'm just going to take a minute to think about the problem, then I'll start talking"_
- _Write down the steps of the solution_
  - You don't need to be verbose, just keep the steps in order and somewhat readable
    - _start at middle of array_
    - _keep variables tracking left and right boundaries of search area_
    - _if value equal to searchval, return true_
    - _if left and right boundaries are adjacent, return false_
    - _if value bigger than searchval, go halfway towards left boundary, move the right boundary along with us_
    - _if value smaller than searchval, go halfway towards right boundary, and move th left boundary along with us_
- _Write pseudocode first_
- _Don't sweat the small stuff_
  - Interviews aren't about how well you remembered semi colons
  - They're about demonstrating depth and breadth of knowledge
    - personality strengths
    - and problem solving abilites
  - If you make a mistake, it's ok, pick up your ruck and move on
  - If you can't remember the name of a particular method, name the method yourself of something that achieves the same functionality and tell your interviewer that you know it's not called that, but you can't remember off the top of your head what it is
- _Sit down, be humble_
  - Remember that the coding interview isn't just to assess whether you're an elite programmer. Make sure to
    - Clearly and effectively express your ideas and solutions
    - Treat the interviewer with respect
    - Accept criticism with humility
    - Humility with criticism will show that you can collaborate with others to come up with solutions
    - Empathetically communicate 
    - Be honest (especially about yourself)
  - If your interviewer gives you criticism, take it gratefully, don't say snarky comments about how you could've done it that way or get angry or raise your voice.
    - The interviewer has their opinion, and they didn't have to share it, they could've just written it down silently and rejected you as a candidate later
    - They've given you a chance to correct your course because they think you're worth it and have given you an opportunity to demonstrate how you accept feedback from your peers
- _Come prepared_
  - Knowing you've done all you can to prepare keeps you calm, cool, and collected during the interview and afterwards.
  - Regardless of the outcome, _you know_ that you did your best, which will make you proud of yourself, which will motivate you to move forward to the next goal
- _Review your work_


[Table of Contents](../index.md)
