# Beginner Projects

A list of projects for beginners.

## Table of Contents
- [Getting Started](#getting-started)
- [Project List](#project-list)
- [Projects](#projects)
- [Solutions](#solutions)
- [Contributing](#contributing)
- [Credits](#credits)

## Getting Started

If you're completely new to programming, you may want to look into a tutorial. Before starting, you should already know the basics of programming such as variables, loops, dictionaries, and how to define functions, as well as how to run programs on your own machine.

Each project idea has a basic goal for you to achieve, as well as subgoals that require a bit more thought, but help make your program more interesting. The overall intent for this repository is to serve as a learning resource for everyone and to help transition learners from a beginning level to an intermediate level. In addition, learners are encouraged to contribute their solutions to this repository and thereby learn the basics of Git.

Almost all projects can be completed in any language, but some were specifically written to be completed with Python.

Remember, if you don't know how to do something, Google is your friend.

## Project List 
*Projects are somewhat ordered by increasing difficulty.*

1. [99 Bottles](#99-bottles)
2. [Magic 8 Ball](#magic-8-ball)
3. [Pythagorean Triples Checker](#pythagorean-triples-checker)
4. [Rock Paper Scissors Game](#rock-paper-scissors-game)
5. [Coin Estimator By Weight](#coin-estimator-by-weight)
6. [Mad Libs Story Maker](#mad-libs-story-maker)
7. [Change Calculator](#change-calculator)
8. [Mean, Median, and Mode](#mean-median-and-mode)
9. [Higher Lower Guessing Game](#higher-lower-guessing-game)
10. [Multiplication Table](#multiplication-table)
11. [Fibonacci Sequence](#fibonacci-sequence)
12. [Base Jumper](#base-jumper)
13. [Hangman Game](#hangman-game)
14. [Menu Calculator](#menu-calculator)
15. [Dice Rolling Simulator](#dice-rolling-simulator)
16. [Count and Fix Green Eggs and Ham](#count-and-fix-green-eggs-and-ham)
17. [What's My Number?](#whats-my-number)
18. [Factors of a Number](#factors-of-a-number)
19. [Countdown Clock](#countdown-clock)
20. [Turn Based Pokemon Style Game](#turn-based-pokemon-style-game)
21. [A Variation of 21](#a-variation-of-21)
22. [Compare Recent reddit Karma](#compare-recent-reddit-karma)
23. [Watch for New TIL Facts](#watch-for-new-til-facts)
24. [Random Wikipedia Article](#random-wikipedia-article)
25. [What's the Weather?](#whats-the-weather)
26. [Sierpinski Triangle](#sierpinski-triangle)
27. [Two Numbers](#two-numbers)
28. [Chickens and Rabbits](#chickens-and-rabbits)

## Projects

### 99 Bottles
Create a program that prints out every line to the song "99 bottles of beer on the wall."
- Do not use a list for all of the numbers, and do not manually type them all in. Use a built in function instead.
- Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
- Remember, when you reach 1 bottle left, the word "bottles" becomes singular.

### Magic 8 Ball
Simulate a magic 8-ball.
- Allow the user to enter their question.
- Display an in progress message(i.e. "thinking").
- Create 20 responses, and show a random response.
- Allow the user to ask another question or quit.

Bonus:
- Add a gui.
- It must have box for users to enter the question.
- It must have at least 4 buttons:
  - ask
  - clear (the text box)
  - play again
  - quit (this must close the window)

### Pythagorean Triples Checker
If you do not know how basic right triangles work, read [this article on Wikipedia](https://en.wikipedia.org/wiki/Pythagorean_theorem).

- Allows the user to input the sides of any triangle in any order.
- Return whether the triangle is a Pythagorean Triple or not.
- Loop the program so the user can use it more than once without having to restart the program.

### Rock Paper Scissors Game
Create a rock-paper-scissors game.
- Ask the player to pick rock, paper or scissors.
- Have the computer chose its move.
- Compare the choices and decide who wins.
- Print the results.

Subgoals:
- Give the player the option to play again.
- Keep a record of the score (e.g. Player: 3 / Computer: 6).

### Coin Estimator By Weight
When some people receive change after shopping, they put it into a container and let it add up over time. Once they fill up the container, they'll roll them up in coin wrappers which can then be traded in at a bank for what they are worth.
- Allow the user to input the total weight of each type of coin they have (pennies, nickels, dimes, and quarters).
- Print out how many of each type of coin wrapper they would need, how many coins they have, and the estimated total value of all their money.

Subgoals:
- Round all numbers printed out to the nearest whole number.
- Allow the user to select whether they want to submit the weight in either grams or pounds.

### Mad Libs Story Maker
Create a Mad Libs style game, where the program asks the user for certain types of words, and then prints out a story with the words that the user inputted.
- The story doesn't have to be too long, but it should have some sort of story line.
- Tip: it's easiest to write out a quick story on a piece of paper or a word document, and then go back through and see which words the user should be able to change.

Subgoals:
- If the user has to put in a name, change the first letter to a capital letter.
- Change the word "a" to "an" when the next word in the sentence begins with a vowel.

### Change Calculator
Imagine that your friend is a cashier, but has a hard time counting back change to customers.
- Create a program that allows him to input a certain amount of change, and then print how many quarters, dimes, nickels, and pennies are needed to make up the amount needed.
- Example: if he inputs 1.47, the program will say that he needs 5 quarters, 2 dimes, 0 nickels, and 2 pennies.

Subgoals:
- Allow him to type in the amount of money given to him and the price of the item. The program should then tell him the amount of each coin he needs like usual.
- Loop the program back to the top so your friend can continue to use the program without having to close and open it every time he needs to count change.

### Mean, Median, and Mode
Create three functions that allow the user to find the mean, median, and mode of a list of numbers. If you have access or know of functions that already complete these tasks, do not use them.

Subgoals:
- In the mean function, give the user a way to select how many decimal places they want the answer to be rounded to.
- If there is an even number of numbers in the list, return both numbers that could be considered the median.
- If there are multiple modes, return all of them.

### Higher Lower Guessing Game
Create a simple game where the computer randomly selects a number between 1 and 100 and the user has to guess what the number is.
- After every guess, the computer should tell the user if the guess is higher or lower than the answer.
- When the user guesses the correct number, print out a congratulatory message.

Subgoals:
- Add an introductory message that explains to the user how to play your game.
- In addition to the congratulatory message at the end of the game, also print out how many guesses were taken before the user arrived at the correct answer.
- Allow the user to decide if they want to play again (without having to restart the program).

### Multiplication Table
Create a program that prints out a multiplication table for the numbers 1 through 9.
- It should include the numbers 1 through 9 on the top and left axes, and it should be relatively easy to find the product of two numbers.
- Do not simply write out every line manually (i.e., don't use `print('7 14 21 28 35 49 56 63')`).

Subgoals:
- As your products get larger, your columns will start to get crooked from the number of characters on each line. Clean up your table by evenly spacing columns so it is very easy to find the product of two numbers.
- Allow the user to choose a number to change the size of the table (so if they type in 12, the table printed out should be a 12x12 multiplication table).

### Fibonacci Sequence
If you do not know about the Fibonacci Sequence, read about it [here](https://en.wikipedia.org/wiki/Fibonacci_number).
- Define a function that allows the user to find the value of the nth term in the sequence.
- To make sure you've written your function correctly, test the first 10 numbers of the sequence.
- You can assume either that the first two terms are 0 and 1 or that they are both 1.

There are two methods you can employ to solve the problem:
1. Solve it using a loop
2. Use recursion

Try implementing a solution using both methods.

### Base Jumper
Create a program that converts an integer to the specified base.
- The program should ask for 3 inputs: the number to convert, the base the number is in, and the base to convert the number to.
- The program should accept a base that is in the range of 2 to 16 inclusive.
- Display the result to the user and ask if they want to exit or convert another number.

Subgoals:
- Do not display leading zeros in the result.
- Validate that the number entered is valid for the specified base.

### Hangman Game
Create a program that selects a random word and then allows the user to guess it in a game of hangman.
- Like the real game, there should be blank spots for each letter in the word, and a part of the body should be added each time the user guesses a letter that is not in the answer.
- You may choose how many wrong turns the user can make until the game ends.

Subgoals:
- If the user loses, print out the word at the end of the game.
- Create a "give up" option.

### Menu Calculator
Imagine you have started up a small restaurant and are trying to make it easier to take and calculate orders. Since your restaurant only sells 9 different items, you assign each one to a number, as shown below.

1. Chicken Strips - $3.50
2. French Fries - $2.50
3. Hamburger - $4.00
4. Hotdog - $3.50
5. Large Drink - $1.75
6. Medium Drink - $1.50
7. Milk Shake - $2.25
8. Salad - $3.75
9. Small Drink - $1.25

To quickly take orders, your program should allow the user to type in a string of numbers and then it should calculate the cost of the order. For example, if one large drink, two small drinks, two hamburgers, one hotdog, and a salad are ordered, the user should type in 5993348, and the program should say that it costs $19.50. Also, make sure that the program loops so the user can take multiple orders without having to restart the program each time.

Subgoals:
- If you decide to, print out the items and prices every time before the user types in an order.
- Once the user has entered an order, print out how many of each item have been ordered, as well as the total price.
- If an item was not ordered at all, then it should not show up.

### Dice Rolling Simulator
By using the random module, Python can do things like pseudo-random number generation.
- Allow the user to input the amount of sides on a dice and how many times it should be rolled.
- Your program should simulate dice rolls and keep track of how many times each number comes up (this does not have to be displayed).
- Finally, print out how many times each number came up.

Subgoals:
- Adjust your program so that if the user does not type in a number when they need to, the program will keep prompting them to type in a real number until they do so.
- Put the program into a loop so that the user can continue to simulate dice rolls without having to restart the entire program.
- In addition to printing out how many times each side appeared, also print out the percentage it appeared. If you can, round the percentage to 4 digits total OR two decimal places.

Bonus:
- Create a program that opens a new window and draws 2 six-sided dice
- Allow the user to quit, or roll again
- Allow the user to select the number of dice to be drawn on screen (1-4)
- Add up the total of the dice and display it

### Count and Fix Green Eggs and Ham
Some of you may remember the Dr. Seuss story "Green Eggs and Ham". For those of you that don't remember it or have never heard of it, [here is the story](http://www.site.uottawa.ca/~lucia/courses/2131-02/A2/trythemsource.txt). However, there is a problem with the story I gave you - every time the word "I" is used, it is lowercase.

Your job is to do the following:
- Copy the story into a regular text file.
- Create a program that reads through the story and makes the letter "i" uppercase any time it should be. (Make sure to change it when it's used in sam-I-am's name too.)
- Have your program make a new file, and have it write out the story correctly.
- Print out how many errors were corrected.
- When you're finished, you should have corrected [this many errors](http://www.site.uottawa.ca/~lucia/courses/2131-02/A2/trythemresult.txt).

### What's My Number?
Between 1 and 1000, there is only 1 number that meets the following criteria:
- The number has two or more digits.
- The number is prime.
- The number does NOT contain a 1 or 7 in it.
- The sum of all of the digits is less than or equal to 10.
- The first two digits add up to be odd.
- The second to last digit is even and greater than 1.
- The last digit is equal to how many digits are in the number.

To find out if you have the correct number, [click here](http://www.wikihow.com/Find-a-Number-That-Meets-Certain-Criteria).

### Factors of a Number
- Define a function that creates a list of all the numbers that are factors of the user's number.
- For example, if the function is called factor, factor(36) should return [1, 2, 3, 4, 6, 9, 12, 18, 36].
- The numbers in your list should be sorted from least to greatest, and 1 and the original number should be included.
- Remember to consider negative numbers as well as 0.

Bonus:
- Have the program print the factors of the user's number in a comma-separated string, without a comma after the last number, and without the brackets of a Python list.
- If the user's number is prime, note it.

### Countdown Clock
Create a program that allows the user to choose a time and date, and then prints out a message at given intervals (such as every second) that tells the user how much longer there is until the selected time.

Subgoals:
- If the selected time has already passed, have the program tell the user to start over.
- If your program asks for the year, month, day, hour, etc. separately, allow the user to be able to type in either the month name or its number.
- TIP: Making use of built in modules such as time and datetime can change this project from a nightmare into a much simpler task.

### Turn Based Pokemon Style Game
Write a simple game that allows the user and the computer to take turns selecting moves to use against each other.
- Both the computer and the player should start out at the same amount of health (such as 100), and should be able to choose between the three moves: