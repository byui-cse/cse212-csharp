---
layout: default
title: "W04 Prepare: Reading"
---

# W04 Prepare: Reading
## Table of Contents
* [Queues](#queues)
	* [Grocery Store Queue](#grocery-story-queue)
	* [Web Server Queue](#web-server-queue)
	* [Reader/Writer Queue](#readerwriter-queue)
	* [Queues in C#](#queues-in-c)
* [Finding Defects Using Testing](#finding-defects-using-testing)
	* [Testing Code from Requirements](#testing-code-from-requirements)
	* [Running Test Cases](#running-test-cases)
* [Key Terms](#key-terms)

## Queues
During the last lesson, we learned about the stack. The Stack was "Last In, First Out" (LIFO). The **queue** is characterized as "First In, First Out" (FIFO) and can also be implemented using a variety of data structures including a `List`.

### Grocery Story Queue

In the example below, we can see a line at a busy grocery store used to represent a queue. The person next in line for the cashier is called the **front** and the person at the end of the line is called the **back**. When the person at the front is removed from the queue we call this a **dequeue** operation. When a new person joins the queue at the back, we call this an **enqueue** operation. Note that someone cannot cheat and enter the line in the middle of the queue. 

<!--- Image x here  -->
{% include image.html url="queue.jpg"
description="Shows a line at a grocery store with the next person be dequeued from the front and a new person being enqueued into the back."
caption="Grocery Store Line Queue"
%}

Queues are used when we need to process a collection of requests in a fair and orderly way. Consider the following two common queues used in software: the **Web Server Queue** and the **Reader/Writer Queue**. 

### Web Server Queue
A web server receives numerous HTTP (Hypertext Transfer Protocol) requests for web pages from clients throughout the world. Each request requires the web server to send back information. The amount of time it takes to send that information makes it difficult to respond timely to all requests. This would be similar to a customer service desk that had only one phone. If the customer service agent is helping someone else, then no one would pick up your call. To solve the problem, a queue is used to pick up all the phone calls and transfer you to the customer service agent when they are ready for the next person.

<!--- Image x here  -->
{% include image.html url="web_server.jpg"
description="Shows 3 laptop computers sending requests through the Internet Cloud to a server.  The server enqueues the requests into a Web Server Queue (which currently has 4 requests with space for 5).  The server dequeues requests from the queue when it is ready.  The response is sent to back to the laptop through the Internet Cloud."
caption="Web Server Queue"
%}
The web server does the same thing. When a request is sent, it is put into a queue until the web server can process the request. In this way, all requests are received and none of them are lost. Queues frequently have a self-imposed maximum size. If a queue is full, then the software may need to send an error message back to the client.


### Reader/Writer Queue
Frequently, we have the need to run different software components concurrently (e.g. looks like they are running at the same time). Each component is called a **process** or a thread (additional information about threads in C# can be found [here](https://www.c-sharpcorner.com/article/introduction-to-multithreading-in-C-Sharp/)). Each process will likely have their own set of variables that are maintained. Frequently, there is need to have shared data between the processes. The diagram below shows a variable which is being shared by multiple processes.

<!--- Image x here  -->
{% include image.html url="reader_writer.jpg"
description="Shows 3 processes trying to read a shared variable and 3 processes trying to write to a shared variable."
caption="Reader/Writer Problem"
%}

Processes P1 through P6 are all trying to use the variable at the same time. Processes P1, P2, and P3 are reading the variable and processes P4, P5, and P6 are writing to the variable. The concurrent reading is not a problem. However, if everyone tries to both read and write at the same time, new and modified values may be missed or overwritten. One solution is to protect the code that is writing to the shared data so that only one process can change the variable at a time. A queue is used to ensure order and integrity. When a process wants to write, it is enqueued. When a process is dequeued, it is then allowed to modify the shared variable. When the process is done, then the next process is dequeued.

### Queues in C#

Queues are an abstraction that you can represent in many ways. You might create your own queue using an fixed array or a list (dynamic array). There is also a built-in data type in the `Collections` library which provides a `Queue` for optimal performance.

| Common Queue Operation | Description | C# Code  | Performance |
|------------------------|-------------|--------------|-------------|
| enqueue(value)   | Adds "value" to the back of the queue    | `myQueue.Enqueue(value)` | O(1) |
| dequeue()        | Removes items from the queue | `var value = myQueue.Dequeue()` | O(1) |
| size()           | Number of elements in the queue  | myQueue.Count    | O(1) |
| empty()          | Returns true if the length of the queue is zero.  | `if (myQueue.Count == 0)`  | O(1) |

Because a queue is just an abstraction, you can implement your own queue using a List object. In that case, performance my be worse as it requires O(n) to add or remove from the front of your List - causing either the Enqueue or Dequeue operation to take longer than O(1).

Here's an example of creating a new built-in queue for characters:

```csharp
var q = new Queue<char>();
q.Enqueue('A');
char ch = q.Dequeue(); // retrieves the 'A'
```

## Finding Defects Using Testing

The best time to find a **defect** is while you are *"in-phase."* This means that before you deliver your software to the customer you want to identify as many errors as possible. It is much more expensive to fix errors if the software has already been delivered to the customer. The two most common methods for finding defects are:

* Code Review
* Testing


### Testing Code From Requirements
Even the best code reviewers may not be able to analyze all the different scenarios that the software will execute within. **Testing** is a process of demonstrating that specific inputs will result in expected outputs. The selection of inputs can be done systematically. We do not need to test all input combination. Often times we will write code to test your code. Consider a program that was supposed to determine if a year was a leap year. The **requirements** of a program would include the following:

* Every 4 years shall be a leap year.
* Every 100 years shall not be a leap year.
* Every 400 years shall be a leap year.

Based on these requirements, we can write some **test cases**. Notice that we are not writing test cases based on what the code does. Each test case includes an **expected result**. If there is an error in the code, we may incorrectly write the test case based on the faulty code. Using the requirements above, we may write the following tests:

* Test 1
	* **Scenario:** Year 1996 (multiple of 4 but not multiple of 100 or 400)
	* **Expected Result:** True
* Test 2
	* **Scenario:** Year 1900 (multiple of 4, multiple of 100, not multiple of 400)
	* **Expected Result:** False
* Test 3
	* **Scenario:** Year 2000 (multiple of 4, multiple of 100, multiple of 400)
	* **Expected Result:** True
* Test 4
	* **Scenario:** Year 2003 (not multiple of 4, 100, or 400)
	* **Expected Result:** False

### Running Test Cases

Notice that each test has a detailed scenario and expected result based on the requirements. If we were given a function called `IsLeapYear(int year)` we could write inline test code as follows:

```csharp
var result = isLeapYear(1996);
Console.WriteLine(result);
result = isLeapYear(1900);
Console.WriteLine(result);
result = isLeapYear(2000);
Console.WriteLine(result);
result = isLeapYear(2003);
Console.WriteLine(result);
```

If anything fails when we run the test code, then we must look manually at the output, then track down where in the code that the test failed.

Instead of printing out the results, test code in C# can use the `Trace.Assert` function. If the `Trace.Assert` function fails, then the program will exit and tell you which test (e.g. assert statement) failed. For example:

```csharp
Trace.Assert(IsLeapYear(1996), "1996 should have been a leap year"); // true
Trace.Assert(!IsLeapYear(1900), "1900 should not have been a leap year"); // false
Trace.Assert(IsLeapYear(2000), "2000 should have been a leap year"); // true
Trace.Assert(!IsLeapYear(2003), "2003 should not have been a leap year"); // false
```

For more complicated programs, a single test scenario may require you to call multiple functions to properly set up the scenario. For example, if we were testing the enqueue and dequeue functions of a queue class, we might enqueue three numbers and then dequeue the three numbers to ensure that they came out in the correct order. The test code may look like the following:


<!--  Python
```python
# Test 1
# Scenario: Ensure that after adding 3 items to the queue, they can be 
#           removed in the proper order
# Expected Result: 100, 200, 300
print("Test 1")
queue = Queue()
queue.enqueue(100)
queue.enqueue(200)
queue.enqueue(300)
result = queue.dequeue()
print(result)
result = queue.dequeue()
print(result)
result = queue.dequeue()
print(result)
```
-->

<!--  C# version -->
```csharp
// Test 1
// Scenario: Ensure that after adding 3 items to the queue, they can be removed in the proper order
// Expected Result: 100, 200, 300
Console.WriteLine("Test 1");
var queue = new Queue<int>();
queue.Enqueue(100);
queue.Enqueue(200);
queue.Enqueue(300);
var result = queue.Dequeue();
Trace.Assert(result == 100);
result = queue.Dequeue();
Trace.Assert(result == 200);
result = queue.Dequeue();
Trace.Assert(result == 300);
```

In addition to finding defects, testing also has the benefit of helping the programmer better understand the requirements of the software. Whether you or another engineer wrote the code, the process of writing test scenarios will increase your understanding of what the software should do.

Testing like this is also critical in the software life-cycle where code needs to constantly be improved.  In the **Continuous Integration / Continuous Deployment (aka: CI/CD [See HERE](https://en.wikipedia.org/wiki/Continuous_integration))** model of development, operating software or apps can be updated for audiences of millions of users, sometimes many times a day.  For this model to work, a key part of the release process has to include rigorous testing that not only checks the functionality of the new features, but also assures regression testing to make sure the new 'fix' hasn't broken something along the way.  These tests are automated with assert statements, most-often programmatically generated to get maximum coverage of the code.

## Key Terms

<dl>
<dt>back</dt>
<dd>Refers to the location in the queue where an enqueue occurs. The last item put in the queue is found in the back.</dd>
<dt>defect</dt>
<dd>This is an error in code.</dd>
<dt>dequeue</dt>
<dd>The operation to remove an item from the queue. The item is removed from the front of the queue.</dd>
<dt>enqueue</dt>
<dd>The operation to add an item to the queue. The item is added to the back of the queue.</dd>
<dt>expected result</dt>
<dd>The result that you expect to receive when you run a test case. The expected result is based on your understanding of the software requirements.</dd>
<dt>front</dt>
<dd>Refers to the location in the queue where a dequeue occurs. The first item put in the queue is found in the front. If you use a dynamic array (List) this is index 0.</dd>
<dt>process</dt>
<dd>The place where software runs. A process has code that is executed and memory used for variables in that code. Multiple processes can run at the same time. Processes can share memory.</dd>
<dt>queue</dt>
<dd>A data structure that follows a First In, First Out (FIFO) rule. The queue is used both to maintain order in data and to remember data when there is not time to process it.</dd>
<dt>requirements</dt>
<dd>Written description of what software should do.</dd>
<dt>test cases</dt>
<dd>Scenarios that are written to test that code behaves per the requirements. A test case will usually have test code unless the procedure is for the user to interact with the software. An expected result is written for each test case.</dd>
<dt>testing</dt>
<dd>An activity to demonstrate that the code correctly implements the requirements.</dd>
</dl>
