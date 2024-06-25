---
layout: default
title: "W10 Prepare: Reading"
---

# W10 Prepare: Reading
## Table of Contents
* [Final Project Description](#final-project-description)
    * [Project Requirements](#project-requirements)
    * [Guidance](#guidance)
    * [Using Markdown Language](#using-markdown-language)
    * [Creating Example Problems](#creating-example-problems)
    * [Milestone Submissions](#milestone-submissions)
    * [Grading Rubric](#grading-rubric)
    * [Working Independently](#working-independently)

## Final Project Description
The information below is the complete description for the final project you will complete during the remainder of the semester. You may want to bookmark or print this page out for easier reference.

### Project Requirements
To prove that you understand the material from this course, you will be required to create a **Data Structure Tutorial**. The tutorial must meet the following requirements:

1. The tutorial must cover three different data structures as follows:
    1. Select one of the following: stack, queue
    2. Select one of the following: set, linked list
    3. You must include the following: tree
2. Each of the three data structure training modules must include the following:
    1. Detailed and organized coverage of the topic with documentation including (but not limited to) example C# code, diagrams, and tables. You should assume that the student using your tutorial will already know how to program in C#. **This should be written in your own words. Remember, you are the teacher now.**
    2. A complete example of a problem solved using the data structure. The problem should be **created by you** and not be a copy of an existing problem.
    3. A second problem (again created by you) which is given to the student of your tutorial to solve on their own. You need to provide a link to the solution.
    4. Your tutorial must use the C# programming language.
3. You must write the tutorial using Markdown language. You should create at least the following files:

| Filename      | Purpose                                                                                                                                                                                                                                                                                   |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0-welcome.md  | Provide an introduction to the student as well as links to three modules. It is important that you provide your name, class, section, and email address on this page.                                                                                                                     |
| 1-topic.md    | Provide the tutorial for the first data structure topic. You should include a link back to the welcome page.                                                                                                                                                                              |
| 2-topic.md    | Provide the tutorial for the second data structure topic. You should include a link back to the welcome page.                                                                                                                                                                             |
| 3-topic.md    | Provide the tutorial for the third data structure topic. You should include a link back to the welcome page.                                                                                                                                                                              |
| Picture Files | If you want a picture (e.g., jpg, bmp, gif, png) to be included in your tutorial, then you need to make sure the files are included in your tutorial submittal. If you copy an image from the internet, make sure that you can legally copy it and be sure to provide source information. |
| C# Files      | You will likely want to include C# files for the student to see the solution to the second problem.                                                                                                                                                                                       |
| Other Files   | If you have any other file that needs to be displayed or accessed by your tutorial, make sure they are included in your submittal.                                                                                                                                                        |

### Guidance
When you write each of the data structure modules, you will want to consider the following questions (this is not an exhaustive list):
* What is the purpose of the data structure?
* What is the performance of the data structure (you will need to talk about big O notation)?
* What kind of problems can be solved using the data structure?
* How would the data structure be used in C# (in some cases you will need to discuss recursion)?
* What kind of errors are common when using the data structure?
* ...

This list of questions is not an exhaustive list but will be helpful to get you started.

To help you visualize what this project requires, a complete [C# Fundamentals Tutorial](https://github.com/byui-cse/cse212-csharp/blob/master/CSharpFundamentals/0-welcome.md) example written in Markdown has been provided. This example covers three fundamental topics in C# programming: decisions, loops, and functions. Please note that your tutorial will not be on these basic C# topics. Your tutorial will be on data structures as described in project requirements shown in the previous section. The structure of this example tutorial follows the project requirements for structure, technical depth, and sample problems.

### Using Markdown Language
The Markdown language is commonly used to develop documentation. The purpose of requiring Markdown for your tutorial is to give you experience using this language. Using a simple editor and the knowledge of a little bit of syntax, you can create documents with headers, bulleted lists, links, bold text, tables and pictures. A common place to see Markdown documents is in GitHub repositories. The link above for the example tutorial was shown to you in GitHub. GitHub automatically interprets the Markdown file and displays as intended.

There are many different tools available to help you write and preview Markdown files. Visual Studio Code has built-in support for Markdown. If you create a file with an `md` extension, then you can click on the preview button, and you can see the Markdown and the finished product side by side.

{% include image.html url="visual_studio_code.jpg" description="Shows the 0-welcome.md file from the example loaded into Visual Studio Code with the preview enabled." caption="Markdown in Visual Studio Code" %}

Writing in Markdown requires the memorization of some basic syntax (here is an example of a [cheat sheet](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) you might find useful). Listed below is syntax that was used in the example tutorial.

``````markdown
	
# Title

When you put a hash sign in front, you get a header.

If you want sub-headings, use more than one hash:

# Header
## Section
### Sub-Section

To make a bulleted list, use a single star in front:
* Item 1
* Item 2
* Item 3

To make an ordered list, use numbers:
1. Item 1
2. Item 2
3. Item 3

To highlight some code in your sentence use the 
back-tick (left leaning apostrophe) around the code 
like this `x = 42`

If you have a block of code you want to show, use three back-ticks
before and after the code.  If you put the name of the programming 
language after the fourth back-ticks, then it will highlight the 
syntax for you:

 ```csharp
int x = 3
int y = 7
int z = x * y
Console.WriteLine(z)
```

To put text in italics, use a single star:  *i am italics*
To put text in bold, use two stars: **i am bold**

To create a link use the format: 
[Text to Display](filename or link)

To display a picture use the format: 
![Alternate Text to Display](filename or link)

To display a table, use hyphens and pipes (vertical bars):

| header 1 |   header 2 |   header 3   |
|:---------|-----------:|:------------:|
| left     |      right |   centered   |
| value 12 |   value 22 |   value 32   |
| value 13 |   value 23 |   value 33   |
``````

### Creating Example Problems

One of the requirements for each data structure is an example problem and an exercise for the student. The idea with these example problems is for you to show how to **use** the data structure to solve a problem, not how to build the data structure. The problem should be designed to take advantage of the strengths of the data structure. Your instructor may give you a scenario that your examples and problems must fit with. Example: _You are working for a company that is developing a music app. All of your examples and student problems should be features of the music app which use the various data structures._ Check with your instructor if there are restrictions for your example and problem.

Here is my process for building a problem:

1. Identify the strengths of the data structure
    * Example: Queue is good at keeping things in order
2. Come up with how this applies in your given application
    * Example: My vacation planning app needs to keep requests from various customers in order
3. Put those 2 things together
    * Example: Use a queue to keep track of requests

The example problem should be a problem where you describe the problem or the requirements and then show the student how to get to the answer. Having C# code chunks in the markdown file is good enough for the example - especially if you include blocks of text in between the code to help the student understand why that data structure helps.

The problem for the student should include some description of the problem scenario and the requirements for completing it. You may give the student a starting project, but it is not required to give them starting code. You must include a link to your solution which should be working code.

The template repository has 3 projects already created for you for each data structure (`ds1-example`, `ds1-problem`, `ds1-solution`, etc.). The ___example___ project is for you to drop your code in and is more for you than for me. It lets you make sure your code is the right syntax to include in the markdown files. The ___problem___ project is for you to have a place to put starting code for your student problem - you don't have to use it, but it's here if you want it. The ___solution___ project should be used to store your solution code so that you can give the student a link to that folder. You don't have to use any of these projects if you don't want to, these are mostly there for convenience for you. 

#### How to Start Your Own Project in C#

So far in our course, we have not required you to create a new C# project. Each of your student problems' solutions should be in a separate C# project. You create a project in C# by using a terminal to navigate to the solution folder and then run `dotnet new console` to create a new application.

{% include image.html url="create_code_solution.jpg" description="Shows the terminal creating a new C sharp console application." caption="Create a New C# Project" %}

You can then open the created solution file to begin editing your problem solution.

{% include image.html url="explore_code_solution.jpg" description="Shows the project folder after creating a new C sharp project." caption="Folder Containing the C# Project" %}

### Milestone Submissions
You will have three milestone submissions during the remainder of the semester in which you will receive a grade and feedback from your teacher:

* Outline - You will submit an outline of your tutorial. An example outline will be provided in the assignment description.
* Draft Submission 1 - You will submit one of your completed data structure topic markdown files for review.
* Draft Submission 2 - You will submit another one of your completed data structure topic markdown files for review.

### Grading Rubric
The final project will be graded as follows:

###### Each data structure page will be evaluated for audience:

|  Anyone | Programmers | CSE 212 Students | Professors | Rocket Scientists | Nobody |
|--------:|------------:|-----------------:|-----------:|------------------:|-------:|
| 100 pts |      93 pts |           83 pts |     71 pts |            60 pts |  0 pts |

###### Each example and problem demonstrate understanding of when to use this data structure

|         |    Yes | Yes, but code doesn't work |       No | No Effort |
|---------|-------:|---------------------------:|---------:|----------:|
| Example | 50 pts |                   41.5 pts | 35.5 pts |     0 pts |
| Problem | 50 pts |                   41.5 pts | 35.5 pts |     0 pts |

###### Number of errors in the entire tutorial

|        |   0 | 1-3 | 4-6 | 7+ |
|--------|----:|----:|----:|---:|
| Points | 100 |  88 |  75 | 60 |

##### Points Breakdown

| Area               | Criteria        |        Points |
|--------------------|-----------------|--------------:|
| Data Structure 1   | Audience        |   **100 pts** |
|                    | Example Problem |    **50 pts** |
|                    | Student Problem |    **50 pts** |
| Data Structure 2   | Audience        |   **100 pts** |
|                    | Example Problem |    **50 pts** |
|                    | Student Problem |    **50 pts** |
| Data Structure 3   | Audience        |   **100 pts** |
|                    | Example Problem |    **50 pts** |
|                    | Student Problem |    **50 pts** |
| Errors in Tutorial |                 |   **100 pts** |
|                    |  ***Total***    | ***700 pts*** |

### Working Independently
This final project **must be completed individually** to ensure you are meeting all course outcomes. You should not complete this project within a group. If you obtain help from a tutor, the tutor should help you understand principles but should not help you design or write your project. It is an honor code violation to obtain text or example problems for your project from others including using the internet (i.e. sites that allow students to share their solutions).