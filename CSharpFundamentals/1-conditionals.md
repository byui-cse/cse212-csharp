# Conditionals

Software would be very boring if we didn't have the ability to make choices. Imagine you had a game app on your phone that didn't allow you to make any choices:

- You wouldn't be able to set an avatar if you select one when the game starts
- You wouldn't be able to move if you swipe left or right
- You wouldn't be able to change to a new level if you completed all the tasks
- You wouldn't be able to start the game over if you lose
- You wouldn't be able to fire your weapon if you pull the trigger (and likewise, neither would your enemies)
- In reality, the game would always run the exact same way regardless of what you tried to do 

A conditional in C# is written using the `if` statement. In the example below, a message is displayed if the temperature is below freezing (using units of Fahrenheit):

```csharp
if (temp <= 32.0) {
	Console.WriteLine("Watch for ice!");
}
```

In C#, we use the curly braces `{ }` to indicate the block of code. In this case, the block of code that displays the message will only occur the the condition is true. The condition `temp <= 32.0` is called a boolean expression. A boolean expression will also result in a true or a false. If the boolean expression is true, then code in the block will run.

Instead of a block of code, you may have a single statement following the `if` statement, but in order to have more than one line, you must use the curly braces. In general, it is good practice to use curly braces to prevent inadvertent errors.

```csharp
if (temp <= 32.0)
	Console.WriteLine("Watch for ice!");
```

## Boolean Expressions

A boolean expressions will use one or more of the following boolean operators:

- `==`  :  Equal To (Don't confuse this with a single `=` sign which is used for assigning a value to a variable)
- `>` : Greater than
- `>=` : Greater than or equal to
- `<` : Less than
- `<=` : Less than or equal to
- `!=` : Not equal to

Here are some examples of Boolean Expressions:

```csharp
if (name == "Bob") {
	Console.WriteLine("We found Bob!");
}

if (pressure > 100) {
	Console.WriteLine("Danger! High Pressure Alert!");
}
	
if (choice != "quit") {
	Console.WriteLine("Let's keep playing");
}
```

We can make compound boolean expressions by combining one or more boolean expressions together using these boolean operators:

- `&&` (and): Test to see if both boolean expressions are True
- `||` (or): Test to see if at least one of the two boolean expression are True
- `!` (not): Test to see if a boolean expression is false (note this one only deals with one boolean expression)

We can make compound boolean expressions as complicated as they need to be. We can use parentheses to help create the right scenarios. Here are some examples:

```csharp
if (temp > 50 && wind < 20) {
	Console.WriteLine("Lets go hiking!")
}

if (pressure < 20 || (pressure < 30 and leak_detected == true)) {
	Console.WriteLine("Someone quickly close the valve!");
}

// We can rewrite the previous example without the == because leak_detected
// is already a boolean. Here is how we do that:

if (pressure < 20 || (pressure < 30 && leak_detected)) {
	Console.WriteLine("Someone quickly close the valve!");
}
	
if ((!alive) && (points > 30) && (name != "Bob")) {
	Console.WriteLine("Since you did well (and you are not Bob), you get to play again!");
}
```

## Multiple Conditions

When we allow the software to make decisions, there might be more than one decision that should be made. Specifying multiple conditions in C# uses the `else if` and `else` keywords. The "else if" and represents an additional condition. The `else` keyword represents all other possible conditions. Here is a complete example to consider:

```csharp
if (temp <= 32.0)
	Console.WriteLine("Watch for ice!");
else if (temp <= 50.0)
	Console.WriteLine("Might want to bring a jacket!");
else if (temp <= 80.0)
	Console.WriteLine("What a beautiful day!");
else
	Console.WriteLine("Its warm out there ... look for some shade!");
```

When this code runs, if will first consider the `temp <= 32.0` condition. If its true, then it will run the code within the block but then skip all the other conditions. If the first condition was false, then it will consider the second condition `temp <= 50`. Notice that in this second condition, we can assume that the temperature is already greater than 32.0 because the first condition failed. If none of the first 3 conditions result in a true (perhaps the temperature is balmy 90 degrees), then the `else` condition will result in true. Notice that we never put a boolean condition next to the keyword `else`.

Sometimes programmers think they always need to put an `else if` and an `else` when they write an `if` statement. This is not true. You should think about all the scenarios you want to check for and use the `else if` and `else` as needed. If we wrote the same code above  but without `else if` and `else`, we would have to write more complicated boolean expressions. It is better to use `else if` and `else` to simplify the code and ensure the result we want.

## Ternary Operations

One handy way of creating an if/else statement is to put both conditions in a single statement. The single statement encapsulates the condition, the value if the condition is true, and the value if the condition is false.

```csharp
var name = preferredName != null ? preferredName + " " + lastName : firstName + " " + lastName;
```

In this example, the condition is `preferredName != null`. If there is a preferred name set, the it will use `preferredName + " " + lastName`, otherwise it will use `firstName + " " + lastName`.

## Example : Geometry Calculator

In the example below, we will write a simple Geometry Calculator. Before we write the code, we should first think about what we want the software to do. Writing a list of requirements is an important step in writing software. The requirements can help us ensure that we using conditionals correctly. 

Geometry Calculator Requirements:

- Allow the user to select the shape they want to calculate the area for
- Ask the user for the size information of the shape they selected
- Ensure that size lengths are all valid (greater than zero)
- Display the results

```csharp
Console.WriteLine("Welcome to the Geometry Calculator");
Console.WriteLine("Please select a shape:");
Console.WriteLine("1) Square");
Console.WriteLine("2) Triangle");
Console.WriteLine("3) Circle");
Console.Write("> ");
var choice = int.Parse(Console.ReadLine()!);
if (choice == 1) {
    Console.Write("Side length of the square: ");
    var side = float.Parse(Console.ReadLine()!);
    if (side > 0) {
        var area = side * side;
        Console.WriteLine($"The area is {area}");
    }
    else {
        Console.WriteLine("Invalid side length!");
    }
}
else if (choice == 2) {
    Console.Write("Length of the triangle base: ");
    var length = float.Parse(Console.ReadLine()!);
    Console.Write("Length of the triangle height: ");
    var height = float.Parse(Console.ReadLine()!);
    if (length > 0 && height > 0) {
        var area = 0.5 * length * height;
        Console.WriteLine($"The area is {area}");
    }
    else {
        Console.WriteLine("One of the lengths was invalid!");
    }
}
else if (choice == 3) {
    Console.Write("Radius of the circle: ");
    var radius = float.Parse(Console.ReadLine()!);
    if (radius > 0) {
        var area = Math.PI * radius * radius;
        Console.WriteLine($"The area is {area}");
    }
    else {
        Console.WriteLine("Invalid radius length!");
    }
}
else {
    Console.WriteLine("Invalid Menu Selection");
}
```

Note the use of `else if` to provide conditions for different choices and `else` for the special condition of an invalid choice. Within each conditional block, different prompts, variables, expressions, and conditionals are used.

## Problem to Solve : Summer Camp Cost

Write a program that will determine the cost for a child to attend a summer camp based on various factors described below:

The base cost of attending summer camp is determined by the age of the child:

|   Age   |      Cost      |
| :-----: | :------------: |
| Under 8 | Can not attend |
|  8-10   |     $1000      |
|  11-12  |     $1500      |
|  13-16  |     $2000      |
| Over 16 | Can not attend |

The base cost is reduced based on the number of children (of any age) in the family and the family income:

| Family Income        | 1 Child in Family | 2 Children in Family | 3+ Children in Family |
| -------------------- | ----------------- | -------------------- | --------------------- |
| Under 25K per Year   | - 70%             | - 80%                | - 90%                 |
| Under 50K per Year   | - 40%             | - 50%                | - 60%                 |
| Under 75K per Year   | - 10%             | - 20%                | - 30%                 |
| 75K or More per Year | No Reduction      | No Reduction         | No Reduction          |

You can test your program with the following scenarios:

- Test 1: 10 year old, 2 children in the family, family income 45K per year will cost: $500 (50% off)
- Test 2: 14 year old, 3 children in the family, family income 70K per year will cost: $1400 (30% off)
- Test 3: 12 year old, 1 child in the family, family income 80K per year will cost: $1500 (0% off)
- Test 4: 18 year old, 3 children in the family, family income 23K per year will cost: N/A - They can't attend

You can check your code with the solution here: [Solution](conditional-problem-solution)



[Back to Welcome Page](0-welcome.md)



