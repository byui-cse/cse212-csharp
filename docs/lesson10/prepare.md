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
    1. Detailed and organized coverage of the topic with documentation including (but not limited to) example Python code, diagrams, and tables. You should assume that the student using your tutorial will already know how to program in Python. **This should be written in your own words. Remember, you are the teacher now.**
    2. A complete example of a problem solved using the data structure. The problem should be **created by you** and not be a copy of an existing problem.
    3. A second problem (again created by you) which is given to the student of your tutorial to solve on their own. You need to provide a link to the solution.
    4. Your tutorial must use the Python programming language.
3. You must write the tutorial using Markdown language. You should create at least the following files:

| Filename         |  Purpose                                                          |
|------------------|-------------------------------------------------------------------|
| 0-welcome.md     | Provide an introduction to the student as well as links to three modules. It is important that you provide your name, class, section, and email address on this page. |
| 1-topic.md       | Provide the tutorial for the first data structure topic. You should include a link back to the welcome page. |
| 2-topic.md       | Provide the tutorial for the second data structure topic. You should include a link back to the welcome page. |
| 3-topic.md       | Provide the tutorial for the third data structure topic. You should include a link back to the welcome page. |
| Picture Files       | If you want a picture (e.g., jpg, bmp, gif, png) to be included in your tutorial, then you need to make sure the files are included in your tutorial submittal. If you copy an image from the internet, make sure that you can legally copy it and be sure to provide source information. |
| Python Files       | You will likely want to include Python files for the student to see the solution to the second problem. |
| Other Files       | If you have any other file that needs to be displayed or accessed by your tutorial, make sure they are included in your submittal. |

### Guidance
When you write each of the data structure modules, you will want to consider the following questions (this is not an exhaustive list):
* What is the purpose of the data structure?
* What is the performance of the data structure (you will need to talk about big O notation)?
* What kind of problems can be solved using the data structure?
* How would the data structure be used in Python (in some cases you will need to discuss recursion)?
* What kind of errors are common when using the data structure?
* ...

This list of questions is not an exhaustive list but will be helpful to get you started.

To help you visualize what this project requires, a complete [Python Fundamentals Tutorial](https://github.com/byui-cse/cse212-course/blob/master/python_fundamentals/0-welcome.md) example written in Markdown has been provided. This example covers three fundamental topics in Python programming: decisions, loops, and functions. Please note that your tutorial will not be on these basic Python topics. Your tutorial will be on data structures as described in project requirements shown in the previous section. The structure of this example tutorial follows the project requirements for structure, technical depth, and sample problems.

### Using Markdown Language
The Markdown language is commonly used to develop documentation. The purpose of requiring Markdown for your tutorial is to give you experience using this language. Using a simple editor and the knowledge of a little bit of syntax, you can create documents with headers, bulleted lists, links, bold text, tables and pictures. A common place to see Markdown documents is in GitHub repositories. The link above for the example tutorial was shown to you in GitHub. GitHub automatically interprets the Markdown file and displays as intended.

There are many different tools available to help you write and preview Markdown files. Visual Studio Code has built-in support for Markdown. If you create a file with an `md` extension, then you can click on the preview button and you can see the Markdown and the finished product side by side.

{% include figure.html url="visual_studio_code.jpg" description="Shows the 0-welcome.md file from the example loaded into Visual Studio Code with the preview enabled." caption="Markdown in Visual Studio Code" %}

Writing in Markdown requires the memorization of some basic syntax (here is an example of a [cheat sheet](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) you might find useful). Listed below is syntax that was used in the example tutorial.

```markdown
	
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

 ```python
x = 3
y = 7
z = x * y
print(z)
\`\`\`

To put text in italics, use a single star:  *i am italics*
To put text in bold, use two stars: **i am bold**

To create a link use the format: 
[Text to Display](filename or link)

To display a picture use the format: 
![Alternate Text to Display](filename or link)

To display a table, use hyphens and pipes (vertical bars):

header 1 | header 2 | header 3
-------- | -------- | --------
value 11 | value 21 | value 31
value 12 | value 22 | value 32
value 13 | value 23 | value 33
```
		
### Milestone Submissions
You will have three milestone submissions during the remainder of the semester in which you will receive a grade and feedback from your teacher:

Outline - You will submit an outline of your tutorial. An example outline will be provided in the assignment description.

Draft Submission 1 - You will submit one of your completed data structure topic markdown files for review.

Draft Submission 2 - You will submit another one of your completed data structure topic markdown files for review.

### Grading Rubric
The final project will be graded as follows, with only five possible numeric grades (there is no scale):

Grade	Description
100% (A)	Demonstrated creativity while providing an engaging tutorial. All requirements have been satisified and there were no significant technical errors. This tutorial would be very helpful for most students to learn data structures. You should consider adding new sections to discuss additional data structures to prepare for future interviews.
89% (B+)	Most requirements have been implemented OR there were some significant technical errors. This tutorial would be helpful for some students to learn data structures but may cause some confusion if material is not updated. You should address the issues in the tutorial to prepare for future interviews.
75% (C)	Only some requirements have been implemented OR there are numerous technical errors. This tutorial would not be helpful for most students to learn data structures. You should consider spending time after the course to review your course notes and rework the tutorial so you are prepared for future interviews.
60% (D-)	Only some requirements have been implemented and there are numerous technical errors. This tutorial is not ready for other students to learn data structures. You should consider either retaking the course or spending time after the course to reattempt the tutorial. These actions are important to prepare you for future intreviews.
0% (F)	Project was not submitted or shows no effort to attempt.

### Working Independently
This final project must be completed individually to ensure you are meeting all course outcomes. You should not complete this project within a group. If you obtain help from a tutor, the tutor should help you understand principles but should not help you design or write your project. It is an honor code violation to obtain text or example problems for your project from others including using the internet (i.e. sites that allow students to share their solutions).