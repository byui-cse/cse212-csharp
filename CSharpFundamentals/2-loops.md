# Loops

When we think about computers, many will think about their vast computing power that allows for billions of operations to be completed in a single second. However, even though the computer can do billions of operations, it does not mean that the software programmer needs to write billions of lines. When we write code, we should think about loops that repeat code dozens or millions of times to achieve the desired result. Consider that favorite game again and where loops might exist:

- Draw a collection of enemy ships on the screen (which in higher levels might be many)
- Compare all the bullets and enemy ships to see if you hit one of them (or if they hit you)
- Displaying all the items you have picked along your journey through the galaxy so that you can select one to use to save the world

Loops are used in three ways in C#. The `for` loop is used when you know how many times you want to do something. The `foreach` loop is used when you want to go through all things in a collection. The `while` loop is used when you don't how many times you to do something. Selecting the correct type of loop will help you simplify your code.

## While Loops

The `while` loop also repeats a block of code but the number of times the loop will run is usually not known. The `while` loop includes a boolean condition to determine if the loop should continue running.

```csharp
var choice = "";
while (choice != "quit") {
    Console.Write("Enter a command: ");
    choice = Console.ReadLine();

    // Do something based on the value of choice
}
```

Notice that this loop will continue to run so long as the user does not type "quit" for the command. This loop might run only 1 time if the user types "quit" for their first command or the loop might run forever if the user never types "quit". It's also possible for a while loop to not run at all. Imagine if choice was already equal to "quit" before we got to the while loop. If this was the case, then we would not enter the while loop. It's important to think about how we will allow entry to the `while` loop. In this case, we choose to set `choice` equal to `""` (empty string, which is a safe value). Since `""` does not equal "quit", we know that we will run the while loop at least one time. 

## For Loops

The `for` loop is typically used to loop a certain number of times. A `while` loop only has a condition to check, but the `for` loop contains 3 parts: 1) declaration, 2) condition, and 3) increment. The different parts are separated by the `;` character.

```csharp
for (int i = 0; i < 100; ++i) {
    Console.WriteLine("Hello!");
}
```

The declaration section contains `int i = 0` and usually starts at `0`, but you can also start at a high number and count down if you want. The condition is basically the same as a while loop. While the variable `i` has a value less than 100, the code will execute whatever block follows. After the block of code runs each time, the third part `++i` will increment the value of `i` by one.

## Foreach Loops (Iterators)

The `foreach` loop is frequently also called an iterator because it will iterate (i.e. visit) each item in a collection. The most basic and common collection in C# is the array. If we had an array of numbers that we wanted to print, we could you use a `for` loop:

```csharp
var numbers = new []{5, 1, 3, 2, 7};
foreach (var number in numbers) {
    Console.WriteLine(number);
}
```

The basic format of the loop can be written as `foreach (var item in collection)`. The `collection` in our example above is the list `numbers`. The `item` variable only exists inside the `foreach` loop block. The block of code will run multiple times with the `number` variable being set to the each value within the `numbers` array. In the example, the list has 5 numbers in it. That means the the loop will run 5 times. The first time it runs, `number` will be equal to 5 and so the number 5 will be displayed. The second time the loop runs, the `number` will be equal to 1 and so the number 1 will be displayed next. This will continue until the loop visits all values in the list.

Loops can be used to perform calculations. Suppose we wanted to add all the numbers in the list together (which by the way can be done without a loop using the `Sum` function, but we want to learn about loops right now):

```csharp
var numbers = new []{5, 1, 3, 2, 7};
var sum_numbers = 0;
foreach (var number in numbers) {
    sum_numbers += number;
}
Console.WriteLine(number);
```

The `+=` operator being used to add up all the numbers will run 5 times for each of the 5 numbers in the list.

Arrays are not the only thing we can loop (or iterate) through:

```csharp
// Loop through each letter in a string
var word = "watermelon"
foreach (letter in word) {
    Console.WriteLine(letter);
}
    
// Loop through each line in a file
foreach (var line in File.ReadLines("book.txt")) {
	Console.WriteLine(line);
}
```

To get out of a loop, we can use the `break` statement. The `break` statement will exit the current loop.

```csharp
// Determine if 'A' is in a word
word = "watermelon"
var word = "watermelon"
foreach (letter in word) {
    if (letter == 'A') {
        Console.WriteLine("Found it!");
        break;
    }
}
```

## Example: Random Number Guessing Game

When we design loops, it can be useful to draw a flow chart of how we want our program to run. Designing software before writing code is a wise first step. A flow chart is a simple design technique where rectangle boxes are used to represents actions and diamonds are used to represent decisions. Arrows are drawn to represent the flow between boxes and diamonds. The following flow chart represents a random number guessing game. 

![guess_design](guess_design.jpeg)

In the flow chart, notice that the arrows are forming cycles or loops. This is an indication that loops should be added to your code. The design may lead you to write the code a very specific way. Its also possible that you can simplify your code by reconsidering and redrawing your flow chart. For the chart above, we have a `while` loop within a `while` loop. The outer `while` loop (the red line in the flow chart) is used to allow the user to play a new game again. The inner `while` loop (the blue line in the flow chart) is used to allow the user to continue guessing the number until they get it right. The boolean conditions for those while loops can be determined by looking at the chart. The red loop continues so long as the user says "YES" to the play again prompt. The blue loop continues so long as the guess does not match. Compare the code below with the design above.

```csharp
Console.WriteLine("Welcome");
var random = new Random();
var playAgain = "y"; // This will allow us into the loop the first time
while (playAgain == "y") {
    var randNum = random.Next(1, 100);
    var numGuesses = 0;
    var guess = -1; // This will allow us into the loop the first time
    while (guess != randNum) {
        Console.Write("Enter a guess: ");
        guess = int.Parse(Console.ReadLine()!);
        numGuesses++;
        if (guess < randNum) {
            Console.WriteLine("Higher!");
        }
        else if (guess > randNum) {
            Console.WriteLine("Lower!");
        }
    }
    Console.WriteLine("Congrats!");
    Console.WriteLine($"It took {numGuesses} guesses.");
    Console.Write("Play again (Y/N)? ");
    playAgain = Console.ReadLine()!.ToLower();
}
Console.WriteLine("Goodbye");

```

## Problem to Solve : Geometric Series Sum

Write a program that will allow the user to estimate the sum of geometric series. A geometric series one where each element in the series is calculated by multiplying the previous value by a constant. For example, here is a geometric series:
$$
1, \frac{1}{2}, \frac{1}{4}, \frac{1}{8}, \frac{1}{16}, \frac{1}{32}
$$
The series begins at 1 (called the initial term) and each number is determined by multiplying the previous number by 0.5 (called the series). You should use a loop to add all of the numbers in the series. You will have to ask the user for three things:

- What is the initial term in the series
- What is the ratio to use to calculate each number in the series
- How many terms in the series to calculate and add together (not including the initial term)

After displaying the answer, you should allow the user to calculate another sum instead of exiting the program. You can ignore cases where the user types in invalid values (e.g. ratio of 0, number of terms in the series <= 0, etc).

The example execution show how a ratio of 0.5 converges the sum towards 2 and how a ratio of 2 does not converge but instead goes towards infinity.

```
Initial Term: 1
Ratio: 0.5
Terms to add: 5
Sum = 1.96875000000000000000

Again (Y/N)? Y
Initial Term: 1
Ratio: 0.5
Terms to add: 20
Sum = 1.99999904632568359375

Again (Y/N)? Y
Initial Term: 1
Ratio: 0.5
Terms to add: 50
Sum = 1.99999999999999911182

Again (Y/N)? Y
Initial Term: 1
Ratio: 2
Terms to add: 5
Sum = 63.00000000000000000000

Again (Y/N)? Y
Initial Term: 1
Ratio: 2
Terms to add: 20
Sum = 2097151.00000000000000000000

Again (Y/N)? Y
Initial Term: 1
Ratio: 2
Terms to add: 50
Sum = 2251799813685247.00000000000000000000

Again (Y/N)? N
```

You can check your code with the solution here: [Solution](loops-problem-solution)



[Back to Welcome Page](0-welcome.md)