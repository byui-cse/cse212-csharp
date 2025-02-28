---
layout: default
title: "W03 Prepare: Reading"
---

# W03 Prepare: Reading
## Table of Contents
* [Stacks](#stacks)
    * [Stack of Pancakes](#stack-of-pancakes)
    * [The "Undo" Option and the Stack](#the-undo-option-and-the-stack)
    * [Software and the Function Stack](#software-and-the-function-stack)
    * [Stacks in C#](#stacks-in-c)
* [Understanding Code Using Reviews](#understanding-code-using-reviews)
    * [Code Reviews](#code-reviews)
    * [Read code "cover-to-cover"](#read-code-cover-to-cover)
    * ["Execute" the Code Manually](#execute-the-code-manually)
    * [Analyze the use of Data Structures](#analyze-the-use-of-data-structures)
* [Key Terms](#key-terms)

---
## Stacks
---

A **stack** is a data structure that is characterized by the order in which items are added and removed. Often called "Last In, First Out" (LIFO), the stack can be used to accomplish various tasks and can be implemented using a C# list.

### Stack of Pancakes
If you were going to make pancakes for your family or friends, you probably would have a plate ready to stack the hot pancakes on as they finished cooking. Each time we put a pancake onto the stack, we call this a **push** operation. In our culinary example, we might say that each new pancake goes onto the top of the stack. However, since we are going to implement our stacks in C#, we will say that the pancake is actually added to the **back**. When we take a pancake off to eat, we call this a **pop** operation. Notice that we push and pop from the back of the stack. Removing from the middle of the stack is not generally allowed (especially at the dinner table). Notice that the pancake at the **front** is the very first pancake that was cooked. If the pancakes are made faster than they are eaten, then this first pancake would get cold. A LIFO (Last In, First Out) structure like the stack can result in data not being used for a long time. This might not work well for a rotating stock system in a grocery store, but the real benefit of the stack is the ability to remember where we have been.


<!--- Image x here   orig size was: 750 x 507-->
{% include image.html url="pancake_stack.jpg"
description="Shows a stack of pancakes where no pancakes are pushed to the back and pancakes are popped from the back to be eaten."
caption="Stack of Pancakes"
%}



### The "Undo" Option and the Stack

One of the most common stacks that people use on a computer is related to the Undo option in word processors and editors. When we type something on the keyboard, the item is both displayed to the screen and also added to a stack. If we type the phrase `"The rain in Spain stays mainly in the plain"`, we would expect the following commands to be pushed onto the stack:
`Type "The", Type "rain", Type "in"`, and so forth. The last item to be pushed would be `Type "plain"`. If we press the Undo button, the software will pop the stack and receive: `Type "plain"`. The software will then do the opposite of this which would result in the word `"plain"` being removed from the screen.

{% include image.html url="undo_stack.jpg"
description="Shows a computer screen and history stack with the initial text of The rain in Spain stays mainly in the plain. Changes to the screen and stack are shown as described in the text of this section."
caption="Stack used to Undo Text"
%}


Since the stack is maintaining a history of what was typed, we can guarantee that pressing the Undo button will revert changes in the right order. If we popped five additional times, we would have `"The rain in"` remaining on the screen. If we type `"Idaho stays mainly in Rexburg"`, we would see five new pushes to the stack. The original first three commands to display `"The rain in"` still remains at the front of the stack. If the Undo button is pressed enough times, then these initial words would eventually be removed.

Stacks are useful when we need to maintain history and perform an operation (eg. Undo function in an editor) backwards.

### Software and the Function Stack

Even if we didn't know what a stack was before today, we have actually been using stacks in all software we have written. When we call a function in our code, we are telling the computer two things:

* Which function we want to call
* Which function to go back to when we are done

The first of these is clear in our code. If we are currently in function A, then we expect to call function B. However, how do we tell the computer that we want to return to function A when function B is finished. This can be even more complicated by the fact that function B may need to call functions C, D, and E before it can finish. The computer accomplishes this by using a function stack. When a function is called, it is pushed to the stack. The current function running is always on the back of the stack. When the function finishes, it is popped off the stack. The result is that the function to return to is the one that is on the back of the stack.


<!--- Image x here   orig size was: 750 x 507-->
{% include image.html url="function_stack.jpg"
description="Shows a structure chart of function A calling function B, function B called functions C and D (in order), and function D calling function E. Shows the function stack (front to back) when B is running (A, B), when C is running (A, B, C), when C finishes (A, B), when D is running (A, B, D), when E is running (A, B, D, E) and when B finishes. (A)"
caption="Function Stack in Programming"
%}

In addition to keeping track of the function name that is running, the stack also allows us to see where in the function we were when a function was originally called as well as the memory that we were using in our function. Stacks work well for remembering where we've been and the circumstances we were in during that previous time.

When using C# or other programming languages, we will often see error messages that look like the following. Notice that the information is showing which functions have called which functions up until the point of error. This display of information comes directly from the function call stack (often abbreviated to just ___call stack___). Here's an example of a call stack trace from an error during runtime:

{% include image.html url="exception_function_stack.png"
description="Shows the call stack from a C# program running in Rider when the program died because of an array error."
caption="C# Exception showing Function Stack"
%}

Many code editors also include a debugger. Debuggers can be used to pause execution of software so that we can see what is occurring within our code step-by-step. Part of the debugger capability is the display of the call stack when the software is paused (due to a breakpoint or an exception).

{% include image.html url="debugger_call_stack.png"
description="Shows the call stack from a C# program running in Rider when a breakpoint was reached and paused the software."
caption="Debugger showing Function Stack"
%}

<!-- Python Version
### Stacks in Python

In Python, a stack can be represented using a list. To push an item to the back of the stack, the append function can be used on the list. To pop items from the back of the stack, the pop function can be used. The pop function will also delete it from the list. The size can be determined by using the len function on the list. The performance of the stack using a Python list is based on the performance of the dynamic array.


| **Common Stack Operation** | **Description**                                      | **Python Code**        | **Performance**                                                      |
|------------------------|----------------------------------------------------------|------------------------|----------------------------------------------------------------------|
| push(value)            | Adds "value" to the back of the stack.                   | my_stack.append(value) | ***O(1)*** - Performance of adding to the end of a dynamic array     |
| pop()                  | Removes and returns the item from the back of the stack. | value = my_stack.pop() | ***O(1)*** - Performance of removing from the end of a dynamic array |
| size()                 | Return the size of the stack.                            | length = len(my_stack) | ***O(1)*** - Performance of returning the size of the dynamic array  |
| empty()                | Returns true if the length of the stack is zero.         | if len(my_stack) == 0: | ***O(1)*** - Performance of checking the size of the dynamic array   |
-->




<!-- C-Sharp Version -->
### Stacks in C#
In C#, a stack can be represented using an array of various data types. Because stack is a common data structure, the framework comes with a built-in `Stack` class. (See [documentation](https://docs.microsoft.com/en-us/dotnet/api/system.collections.stack?view=net-6.0)).  These methods are shown in the table below, along with the big O performance of them.

| Common Stack Operation | Description | C# Code  | Performance  |
|------------------------|-------------|----------|--------------|
| push(value) | Adds "value" to the back of the stack. | `myStack.Push(value)` | O(1) |
| pop()       | Removes and returns the item from the back of the stack. | `var value = myStack.Pop()` | O(1) |
| size()      | Return the size of the stack. | `var length = myStack.Count` | O(1) |
| empty()     | Returns true if the length of the stack is zero.         | `if (myStack.Count == 0)` | O(1) |

## Understanding Code Using Reviews

### Code Reviews

We have frequently been asked to write code for either school or work. However, how often have we been asked to complete the companion activity of reading code? We have likely looked at code from websites and books, but there is a significant difference between looking at code and reading code. When we read code, we are attempting to understand the code like we would a book. If we open a book and read a few random pages, we might get a high level summary of what the book is about. However, to fully understand the book, we would need to not only read the book cover to cover, but we would also need to become acquainted personally with the diverse set of characters, follow a potentially winding plot, and discover the underlying messages woven in the story from the author. This type of reading takes effort. Reading code for understanding takes an equal amount of effort.

There are multiple reasons why we might be asked to read code in our teams:

* A team member has written some code and has asked other engineers to review the code for correctness against the design and for compliance against company standards.
* A team member is asked to modify some code that was written by a former employee with or without the aid of a well documented design.
* A team member needs to integrate their software with an external library which included several code examples that demonstrate how to properly use the library.

When we read code others have written, we refer to this activity as a **review**. A review should follow a methodical process. Many companies will include a review checklist for engineers to use to ensure that they both understand the code and that they have checked all the coding standards. When you review code, there are several strategies that you can use including the following:

* Read code "cover to cover"
* "Execute" the code manually
* Analyze the use of data structures

Each of these methods will be discussed below. When working with these methods, we should try to employ principles learned from the scientific method. The scientific method requires us to form a hypothesis about what we think the code should be doing. As we read through the code, we will test our hypothesis and look at the results. If we are incorrect, then we can correct our misconceptions and form a new hypothesis. This iterative process is necessary to fully understand code. There are no shortcuts. We can be tempted to search for the answer online or in a book. While this may produce a faster answer, we will have not obtained full understanding of the code.

In this process, it is possible that we might find defects in the code that we were given. Code reviews are a common tool for increasing software quality. Performing these steps will require us to keep a good notebook to record our hypothesis, experiments, and conclusions. A good reviewer will always have a pen and paper ready to complete their task.

### Read Code "Cover to Cover"

Unlike a book, code does not begin on page one. We need to find where the code begins and follow it as it calls functions, runs loops, and branches in different directions with decision statements. If the code has multiple functions, the creation of a **structure chart** (also called a calling tree) will be helpful. The structure chart will use boxes to represent functions and arrows to represent functions calling functions. Frequently drawn with the starting function at the top and working downwards, these diagrams can help us navigate through the code. On the arrows, we may frequently write the inputs and outputs related to each function. This will help us better understand the data in the code and which functions are responsible for creating, modifying, and using that data.

{% include image.html url="structure_chart.jpg"
description="Shows a structure chart where the main function calls the readAccessRecords function and the searchAccessRecords function. The readAccessRecords function receives an accessFile input and produces accessRecords and recordCount as an output. The searchAccessRecords function receives the accessREcords, numRecords, startTime, and entTime while producing no output. The searchAccessRecords function also call the displayAccessRecord function providing accessRecord as an input with no outputs."
caption="Structure Chart"
%}

If the code contains classes, then creating a **UML** (Unified Modelling Language) class diagram to show the classes (with member data and member functions) and the relationships between the classes will help us to visualize the software and enable us to read different sections of the code based on their dependencies to others. For example, in the diagram below, we can see that the Order HAS-A (object composition shown with the filled in diamond) list of Products and that each Product IS-A either a PerishableProduct or an ElectronicProduct (inheritance shown with the open triangle). With this drawn, we would probably start with understanding the Product base class first since it has no dependency on other objects. Second, we would review the different types of Products. Finally, we would review the Order class which contains the list of the Product objects that we already understand.

{% include image.html url="uml_diagram.jpg"
description="Shows the classes and their relationships shown in the text above. The Order class has an integer order_id and a list of Product objects called products. The Order class has an init function, an add_product function that takes a product object as an input, and a display function. The Product class has a string name and a float price with an init function and a display function. The ElectronicProduct has a string url_download and both an init and download function. The PerishableProduct has an expiry datetime object and both an init and donate function."
caption="UML Class Diagram"
%}

When we are looking at a single function, it can be useful to diagram the behavior of the function. Simple **flow charts** can quickly give us a better perspective of the loops and decisions in our code. In the flow chart, use diamonds to represent decisions, boxes to represent actions, and arrows to show flow.

{% include image.html url="flow_chart.jpg"
description="Shows the flow of random number guessing game. After getting the seed from the user and seeding the generator, a random number is selected and the guess counter is reset. A loop begins with the user being prompted for a guess. The guess counter will be updated and then the guess is compared with the actual number. Either the phrase higher, lower, or congratulations will be displayed. If the correct answer was guessed, the guess count is also displayed. The user is prompted to play the game again. If they want to play again, then the process above repeats starting with the selection of a random number and the resetting of the guess counter. Otherwise, the software says goodbye and the program ends."
caption="Flow Chart"
%}

### "Execute" the Code Manually

It is not always practical to run code that we are given. If we can, then running the code with inputs that we generate can be helpful to understand the software. However, the goal in this process is to understand the software without running the code on the computer. Instead, we are going to run the software in our minds and on paper.

If we created diagrams in the previous step from our reading of the code "cover to cover," then we can run the code from the diagrams. This is an incomplete approach but is very helpful in gaining more understanding of what the software will perform.

To execute code manually in our minds and on paper, we must start at the beginning (or if we are looking at one piece of the software, perhaps start at the beginning of one of the functions). If inputs are provided at the beginning (or at any other place along the way), we will have to develop useful inputs to see what will happen. For example, consider the following code:

```csharp
public static string DoSomething(string text) {
    var newText = "";
    foreach (var letter in text) {
        if (letter != ' ') {
            var newLetter = (char)(letter + 1);
            newText += newLetter;
        }
        else {
            newText += letter;
        }
    }

    return newText;
}
```

The method needs a string for an input, and so we will propose something like "Hello". We will then step through each line of code and record in our notebook the value of each variable. If we come across a code function that we don't understand
(e.g. the `(char)` type casting), then go online to read about those. Each `char` is stored as an [ASCII](https://www.asciitable.com/) numeric code that represents a character. As soon as we add to a character `letter + 1`, it becomes an integer, so the `(char)` tells C# that it needs to consider whatever number the integer is as a `char` data type. When we finish evaluating our code, we get `Ifmmp` which appears to be a form of simple childhood encryption in which each letter in the original text is changed by one letter higher in the alphabet. When we ran the program, we noticed that you had to check if the letter was a space. It would be good to try to the test again with spaces. If we tried "Hello World", we end up with `Ifmmp Xpsme`. Not only does the function perform the encoding, but it also preserves the spaces.

| text  | letter | letter + 1 | newLetter | newText |
|-------|--------|------------|-----------|----------|
| Hello | H      | 73         | I         | I        |
|       | e      | 102        | f         | If       |
|       | l      | 109        | m         | Ifm      |
|       | l      | 109        | m         | Ifmm     |
|       | o      | 112        | p         | Ifmmp    |

This type of simple analysis by evaluating the variables, step-by-step, is often valuable to understand what the code is doing.

### Analyze the use of Data Structures

When code contains a data structure like a list or a stack (and others that we will learn during the course), we should consider why the data structure was used. Data structures are used both for storing information but also to use the information in different ways. Looking at the readings above, a stack is used if we want to remember where we have been and potentially go reverse or backwards. Knowing this capability, you can form a hypothesis about what the code is doing if you see a stack being used in the code. During the activities this week, you will be reading code that uses stacks. How the stack is being used will help you better understand the purpose and behavior of the code.

## Key Terms
<dl>
<dt>back</dt>
<dd>Refers to the location in a stack where a push and pop occurs. The last item put into the stack is found in the back.</dd>
<dt>flow charts</dt>
<dd>A diagram that models the behavior of a program, algorithm, or function. Actions are shown in boxes, decisions shown in diamonds, and arrows are used to show execution flow.</dd>
<dt>front</dt>
<dd>Refers to the location in a stack where the first item added to the stack can be found. Traditionally, this is index 0 of a dynamic array.</dd>
<dt>pop</dt>
<dd>The operation to remove the last item pushed to the stack. The item from the back of the stack is removed and returned.</dd>
<dt>push</dt>
<dd>The operation to add a new item onto the stack. The item is placed at the back of the stack.</dd>
<dt>review</dt>
<dd>A formal process of ensuring code is written correctly. Code is usually reviewed against the design and coding standards. Frequently, checklists are used to help the reviewer.</dd>
<dt>stack</dt>
<dd>A data structure that follows a Last In, First Out (LIFO) rule. The stack is used to reverse data or remember previous data including previous results.</dd>
<dt>structure chart</dt>
<dd>A diagram showing which functions call which functions. Frequently, the arrows used to show function calls also include parameters that are passed between the functions.</dd>
<dt>UML</dt>
<dd>Unified Modeling Language. A formal modelling language to represent object-oriented designs. UML includes many types of diagrams including class diagrams, activity diagrams, and state diagrams.</dd>
</dl>
