---
layout: default
title: "W04 Teach: Group Practice"
---

# W04 Teach: Group Practice

## Instructions

These problems should be completed and discussed as a group. Answers are provided below.

All the files for this assignment will be found in the GitHub classroom ***teach-04*** repository.

#### Step 1: [Accept your assignment repository](teach-classroom){:target="_blank"}

### Problem 1 - Simple Queue
1. Download the repository and load the `teach-04.sln` in your code editor. (Note: Do not read through the code first. Instead, proceed with the instructions below). 
2. The SimpleQueue class implements a traditional FIFO queue that has an enqueue and dequeue function. Here are the detailed requirements (which can not be changed): 
   1. The enqueue method shall put a new item in the back of the queue
   2. The dequeue method shall remove an item from the front of the queue
   3. If the queue is empty, then the dequeue method shall throw an IndexOutOfRangeException
3. The code contains three test cases already implemented for you. Run the code and determine if a test has failed. If the test case fails, then you know that there is one or more errors in the function related to the test. If your build crashes, you can see which lines of code the error occurred on.
4. Find the errors and fix the code. All your test cases should pass when the code is fixed. There are two major errors in the code you were given.
5. When you are done, examine the tests in the `TestSimpleQueueSolution.cs` file and take a look at the `SimpleQueueSolution.cs` file and discuss it together.

### Problem 2 - Customer Service Queue
1. The CustomerService class maintains a queue of records that include the name, account ID, and the problem. Here are the detailed requirements (which can not be changed):
   1. The user shall specify the maximum size of the Customer Service Queue when it is created. If the size is invalid (less than or equal to 0) then the size shall default to 10.
   2. The AddNewCustomer method shall enqueue a new customer into the queue.
   3. If the queue is full when trying to add a customer, then an `InvalidOperationException` should be thrown.
   4. The ServeCustomer function shall dequeue the next customer from the queue and return the `Customer` object.
   5. If the queue is empty when trying to serve a customer, then `null` value should be returned.
2. Write test cases based on the requirements above and then implement the tests. Ensure that your tests cover all the requirements listed above.
3. Run your test cases. If the test case fails, then look in the related code for the errors and fix them. All your test cases should pass when the code is fixed. There are three major errors in the code you were given.
4. When you are done, examine the tests in the `TestCustomerServiceSolution.cs` file and take a look at the `CustomerServiceSolution.cs` file and discuss it together.

