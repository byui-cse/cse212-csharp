---
layout: default
title: "W02 Teach: Group Practice"
---

# W02 Teach: Group Practice

## Instructions

These problems should be completed and discussed as a group. Answers are provided below.

All of the files for this assignment will be found in the GitHub classroom ***teach-02*** repository.

#### Step 1: [Accept your assignment repository](teach-classroom){:target="_blank"}

### Problem 1 - Analyze Code

In this section, you will be asked several questions related to performance using big O notation. You will be asked to compare your answers to the actual solutions at the end of this section. You should watch the clock to make sure you don't spend more than half of your hour on this section before going to the next section.

1. Open up the file **FourFunctions.cs** and determine the big O notation for each of the four methods: `CalculateFactorial`, `CalculateStats`, `PrintTriangle`, & `DisplayLettersInNames`
   
2. Using the LINQ syntax, we can sum an array of number as follows: 

    ```csharp
    var numbers = new [] {1, 2, 3, 4, 5, 6};
    Console.Out.WriteLine(numbers.Sum());
    var average = numbers.Average();
    Console.Out.WriteLine(average);
    ```

    What is the big O notation for this code? You will need to think about how the built-in methods are implemented.
   
3. Using either a graphing calculator or a graphing website (e.g. [desmos.com](https://www.desmos.com/calculator){:target="_blank"}), plot the following graphs:
    * y = x^2 to represent O(n^2)
    * y = log(x) to represent O(log n)
    * y = x to represent O(n)
  
    Using the graph, put the big O notations in order (best performance first and worst performance last) for when n is large.

4. When you are done, take a look at the [solution](teach-analyze-solution){:target="_blank"} and discuss it together.

### Problem 2 - Predict, Measure, and Compare Code

1. Open the file **Algorithms.cs** (NOTE: Do not run the code until you're asked to below)
   
2. This file contains three different methods called `Algorithm1`, `Algorithm2`, and `Algorithm3`. Predict the performance of each method using big O notation.
   
3. Run the code and observe the outputs. Here is what the columns in the table represent:
    * n - The size of the data given to the methods in this test
    * alg1-count - The number of loop iterations (i.e. work) done by Algorithm1
    * alg2-count - The number of loop iterations (i.e. work) done by Algorithm2
    * alg3-count - The number of loop iterations (i.e. work) done by Algorithm3
    * alg1-time - The time in milliseconds it took to complete Algorithm1
    * alg2-time - The time in milliseconds it took to complete Algorithm2
    * alg3-time - The time in milliseconds it took to complete algorithm3
      
    While the alg*#*-count value should be the same in every execution, the time will vary each time it is executed on the same or different computers. For the timing numbers, the code ran the test 10 times and took the average. This was done since there are some operating system conditions that could affect timing in some cases.

4. Discuss the following together: 
    1. Do the actual results agree with the big O predictions made earlier? If not, what do you think the big O should be?
    2. Which method (Algorithm1, Algorithm2, Algorithm3) has the best performance and which one the worst performance?
    3. Looking at the results, why do we say that big O only applies when n in "large"?
       
  5. When you are done, take a look at the [solution](teach-algorithms-solution){:target="_blank"} and discuss it together.  
