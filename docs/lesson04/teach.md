---
layout: default
title: "W02 Teach: Group Practice"
---

# W01 Teach: Group Practice

## Instructions

These problems should be completed and discussed as a group. Answers are provided below.

### I. PROBLEM 1 - SIMPLE QUEUE
  1. Download the following code and load into your code editor: [file here]() (Note: Do not read through the code first. Instead, proceed with the instructions below). 
   
  2. The Simple_Queue class implements a traditional FIFO queue that has an enqueue and dequeue function. Here are the detailed requirements (which can not be changed): 
     1. The enqueue function shall put a new item in the back of the queue
   
     2. The dequeue function shall remove an item from the front of the queue

     3. If the queue is empty, then the dequeue function shall raise an IndexError exception
   
  3. The code contains three test cases already implemented for you. Run the code and determine if a test has failed. If the test case fails, then you know that there is one or more errors in the function related to the test. If your build crashes, you can see which lines of code the error occurred on.
   
  4. Find the errors and fix the code. All your test cases should pass when the code is fixed. There are two major errors in the code you were given.
   
  5. When you are done, take a look at the [solution]() and discuss it together.

### II. PROBLEM 2 - CUSTOMER SERVICE QUEUE
  1. Download the following code and load into your code editor: [file here]() (Note: Do not read through the code first. Instead, proceed with the instructions below).
   
  2. The Customer_Service class maintains a queue of records that include the name, account ID, and the problem. Here are the detailed requirements (which can not be changed):
   
     1. The user shall specify the maximum size of the Customer Service Queue when it is created. If the size is invalid (less than or equal to 0) then the size shall default to 10.
   
     2. The add_new_customer function shall enqueue a new customer into the queue.
   
     3. If the queue is full when trying to add a customer, then an error message will be displayed.
   
     4. The serve_customer function shall dequeue the next customer from the queue and display the details.
   
     5. If the queue is empty when trying to serve a customer, then an error message will be displayed.
   
  3. Write test cases based on the requirements above and then implement the tests. Ensure that your tests cover all of the requirements listed above.

  4. Run your test cases. If the test case fails, then look in the related code for the errors and fix them. All your test cases should pass when the code is fixed. There are three major errors in the code oyu were given.
   
  5. When you are done, take a look at the [Solution]() and discuee it together.

