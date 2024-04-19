---
layout: default
title: "W01 Welcome"
---

# W01 Welcome
## Table of Contents
* [About CSE 212](#about-cse-212)
* [Course Reading](#course-reading)
* [Development Environment](#development-environment)
    * [.NET Core - C#](#net-core---c)
    * [VS Code or JetBrains Rider](#vs-code-or-jetbrains-rider)
    * [GitHub Desktop](#github-desktop)
    * [GitHub Classroom](#github-classroom)
* [Downloading Course Files](#downloading-course-files)
* [Preparing for the Final Project](#preparing-for-the-final-project)

## About CSE 212
Welcome to CSE 212 - Programming with Data Structures. This course is intended for students who have studied programming including functions and classes whether in C# or Python. As you progress towards a career as a software engineer, this course will prepare you to effectively use data structures and increase your programming skills. The successful CSE 212 student will develop the following skills:

* Problem Solver: Apply a systematic approach to writing code to solve problems involving data structures.
* Evaluator: Evaluate the performance of alternative solutions for code containing data structures using big O notation.
* Reviewer: Predict the purpose and behavior of existing code containing data structures.
* Tester: Discover defects using testing in code containing data structures.
* Conversant: Articulate the answers to technical questions involving data structures.
* Self-Reliant: Solve problems using data structures independently.

Data structures are containers that hold information. There are different data structures which are suited for different purposes. In this course, you will study the following data structures: dynamic array, stack, queue, set, map, linked list, and tree. You will also learn about big O performance and recursion.

The course is divided into three phases:

* Phase 1 - Prepare (Lessons 1-5)
    * You will learn programming skills and techniques and apply them to data structures.
    * You will complete practice problems with other students and discuss the solutions together.
    * Your individual assignments will be similar to the practice problems.
* Phase 2 - Teach (Lessons 6-9)
    * You will learn complex data structures and rely on your skills discovered in the Prepare phase.
    * You will have a set of problems to individually solve each week.
    * You will meet with other students for a set amount of time each week to collaborate on these problems (without sharing code).
* Phase 3 - Prove (Lessons 10-14)
    * You will demonstrate what you learned in the Prepare and Teach phases by completing a final individual project.
    * Class time will be given to work on your final project.

This course is designed to provide opportunities for you to learn with your peers while at the same time demonstrating your personal mastery of the material. You should only collaborate with other students as directed in the assignments. When working with TA's, tutors, and other individuals outside of class, you should not seek or receive direct help in answering a problem that you were expected to answer on your own. You should seek help to learn course material and then demonstrate your understanding on your own.

Many programming problems in this course have solutions that with some effort could be found online. You should resist the temptation to use online solutions in favor of solving the problems on your own. For this purpose, many of the assignments will require written responses in addition to C# code. When you interview with potential employers, you will not have the luxury of a web search engine to help you answer the question. You will need to be prepared to articulate your answers clearly to others. The successful CSE 212 student will gain this skill.

This course requires that you already know how to write software in some programming language. We will do all of our assignments in C#, and we will cover syntax for those new to C#. If you'd like a review of C#, you should look at the [W3Schools C# Tutorials](https://www.w3schools.com/cs/index.php){:target="_blank"}. Focus should be given to the following modules: variables, data types, strings, methods, loops, and classes.

## Course Reading
Each lesson will have reading in I-Learn. During the Prepare phase of the course, the reading will include material for a new data structure and new programming skill. During the Teach phase of the course, only a new data structure will be presented. No new material will be presented during the Prove phase except for the details of the final project.

Each of the readings will include an overview of the topic including several examples. The application of the topic to C# and the performance implications will also be discussed. Key terms will be highlighted when first used in each of the readings. Definitions for these key terms is summarized in the last section of each reading.

In addition to the reading provided, there is plenty of documentation on the internet and in libraries, including the BYU-Idaho online databases. You may want to visit the [Safari Books Online](http://go.oreilly.com/byu-idaho) database supported by the BYU-Idaho library and search for various books on the subject of data structures.

## Development Environment
The development environment for this course will be using C#. Although initially developed by Microsoft, it has become standard across the computer industry for cross-platform development. Your development environment must be functional to successfully submit assignments during the first lesson. We will use [.NET Core](#net-core---c), [Rider or VS Code](#vs-code-or-jetbrains-rider), [GitHub Desktop](#github-desktop), and [GitHub Classroom](#github-classroom). Please install these tools on your laptops as we will require them the first week of class.

### .NET Core - C#
We will be using the platform independent version of C# called [.NET Core](https://dotnet.microsoft.com/en-us/download){:target="_blank"}. Please download the version for your operating system and install it so that you're ready for class to begin.

### VS Code or JetBrains Rider
JetBrains Rider is a cross-platform Integrated Development Environment (IDE) that will speed up development and give you experience that will prepare you for coding in the workplace. Using this tool will give you *many* advantages over Visual Studio Code (which you probably have used in the past). If you live in an area of the world with limited Internet bandwidth, you may use Visual Studio Code to work on the assignments; however, it is highly encouraged to use JetBrains Rider if you can. Rider supplies better coding helps, a working **run** button, and help with debugging errors.

#### Running with VS Code
In order to run code using VS Code, you will need to use the terminal and the command `dotnet run` in the folder containing your project in order to produce results. 

#### Setting up JetBrains Rider
You will need to activate a [student license](https://www.jetbrains.com/community/education/#students){:target="_blank"} which involves creating an account and supplying your BYU-Idaho email address. You will need to download [JetBrains Rider](https://www.jetbrains.com/rider/){:target="_blank"} or the [JetBrains Toolbox](https://www.jetbrains.com/lp/toolbox/){:target="_blank"} (which then allows you to install Rider).

For additional help, see this [Jetbrains Rider help](../help/rider)

### GitHub Desktop
For almost all of your teach one another assignments and prove assignments, you will be cloning a repository, making changes, and then committing and pushing changes to that repository. You will then submit a link to your repository in canvas as the submission. For cloning, committing, and pushing changes we *strongly* encourage you to use [GitHub Desktop](https://desktop.github.com/){:target="_blank"} over any other tools. I've seen other tools lose track of changes, miss files, or experience authentication issues.

### GitHub Classroom
We will use GitHub Classroom to manage access to assignments and repositories so that teachers and TAs have access to your submissions. You will need to have a [GitHub account](https://github.com/){:target="_blank"}. There is nothing to install, simply click on the links in iLearn to create your repositories for your assignments using GitHub Classroom.

## Downloading Course Files
In the Teach activities and Prove assignments, you will frequently be asked to download documents and files. The instructions will be a page like this one, but the code will be a link to GitHub Classroom for you to "Accept the Assignment". This will create your own personal GitHub repository with a copy of the starting files. It is expected that you make the appropriate changes to the files and then commit and push those changes back to that same repository.

Every file that you download contains the following warning: "It is a violation of BYU-Idaho Honor Code to post or share this code with others or to post it online. Storage into a personal and private repository (e.g. private GitHub repository, unshared Google Drive folder) is acceptable." It is very important that you follow these rules for all material in the course.

The Prove assignments will include a Response Document that you must use to provide your responses to questions. When you submit your assignment, you will need to submit the completed Response Document along with any required code files.

## Preparing for the Final Project
Starting in Week 10, the course will be devoted to working on your final project. The [Week 10 Prepare](../lesson10/prepare) contains the full description of the project. You will be asked to create a detailed tutorial about some of the data structures you have learned during the course. To prepare for the project, you are encouraged to begin taking weekly notes about each data structure with special attention to the following:
* What is the purpose of this data structure and when is it used?
* What is the performance of this data structure (you learn about performance in Week 2)?
* How does the data structure work and how do you use it with C#?
* What are some common errors you may encounter while using the data structure?
* The reading and the assignments contain several problem that require the use of data structures. Can you write additional problems on your own to solve?
