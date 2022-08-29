---
layout: default
title: "W02 Teach: Group Practice"
---

# W02 Teach: Group Practice

## Instructions

 These problems should be completed and discussed as a group. Answers are provided below.

### I. PROBLEM 1 - ANALYZE CODE

In this section, you will be asked several questions related to performance using big O notation. You will be asked to compare your answers to the actual solutions at the end of this section. You should watch the clock to make sure you don't spend more than half of your hour on this section before going to the next section.

  1. Open up the following code and determine the big O notation for each of the four methods: [file here.]()
   
  2. Using the LINQ syntax, we can sum an array of number as follows: 
      * var numbers = new [] {1, 2, 3, 4, 5, 6};
      * Console.Out.WriteLine(numbers.sum());
      * var average = numbers.Average();
      * Console.Out.WriteLine(average);

     What is the big O notation for this code? You will need to think about how the built-in methods are implemented.
   
  3. Using either a graphing calculator or a graphing website (e.g. desmos.com), plot the following graphs:
     * y = x^2 to represent O(n^2)
      * y = log(x) to represent O(log n)
       * y = x to represent O(n)
  
      Using the graph, put the big O notations in order (best performance first and worst performance last) for when n is large.

  4. When you are done, take a look at the [solution]() and discuss it together.

## II. Problem 2 - PREDICT, MEASURE, AND COMPARE CODE

  1. Download the following code and load into your code editor: [file here]() (NOTE: Do not run the code until you're asked to below)
   
  2. This file contains three different methods called Algorithm1, Algorithm2, and Algorithm3. Predict the performance of each method using big O notation.
   
  3. Run the code and observe the outputs. Here is what the columns in the table represent:
   
      * n - The size of the data given to the methods in this test
   
      * alg1_count - The number of loop iterations (i.e. work) done by Algorithm1
       
      * alg2_count - The number of loop iterations (i.e. work) done by Algorithm2
       
      * alg3_count - The number of loop iterations (i.e. work) done by Algorithm3
       
      * alg1_time - The time in milliseconds it took to complete Algorithm1
     
      * alg2_time - The time in milliseconds it took to complete Algorithm2
       
      * alg3_time - The time in milliseconds it took to complete algorithm3
      
     While the alg#_count value should be the same in every execution, the Time will vary every time it is executed on the same or different computers. For the timing numbers, the code ran the test 10 times and took the average. This was done since there are some operating system conditions that could affect timing in some cases.

  4. Discuss the fllowing together: 
      
      * Do that actual results agree wiht the big O predictions made earlier? If not, what do oyu think the big O should be?
     
      * Which method (Algorithm1, Algorithm2, Algorithm3) has the best performance and which one the worst performance?
       
      * Looking at the results, why do we say that big O only applies when n in "large"?
       
  5. When you are done, take a look at the [solution]() and discuss it together.  


