---
layout: default
title: "CSE 212 Rider Helps"
---

# CSE 212 Rider Helps
## Table of Contents
* [What is Rider?](#what-is-rider)
* [Obtaining a Student License](#obtaining-a-student-license)
* [Rider Setup](#development-environment)
  * [Using JetBrains Toolbox (preferred)](#net-core---c)
  * [Standalone Install](#vs-code-or-jetbrains-rider)
* [Using Rider](#downloading-course-files)
  * [Opening Files With a Single Click](#preparing-for-the-final-project)
  * [Why Doesn't the **Run** Button Work?](#preparing-for-the-final-project)
  * [Using Version Control]()
  * [It's Broke... How Do I Reset It?]()

## What is Rider?

JetBrains Rider is a cross-platform Integrated Development Environment (IDE) that will speed up development and give you experience that will prepare you for coding in the workplace. Using this tool will give you *many* advantages over Visual Studio Code (which you probably have used in the past). Rider supplies better coding helps, a working **Run** button, help with debugging errors, and is used across the industry to increase productivity in .NET development.

## Obtaining a Student License

You will need to activate a [student license](https://www.jetbrains.com/community/education/#students){:target="_blank"} which involves creating an account and supplying your BYU-Idaho email address.

1. Apply for a student license: [https://www.jetbrains.com/community/education/#students](https://www.jetbrains.com/community/education/#students)

{% include image.html url="jetbrains-student-apply-link.png" description="Shows the apply button" caption="Click <u>Apply now</u>" %}

{% include image.html url="jetbrains-student-email.png" description="Use your BYU-Idaho Email Address" caption="Fill out the form" %}

You will receive an email asking you to verify and log in with your JetBrains account. You will need to create an account. This account does not have to be your BYU-Idaho email address, as the student license verification will tie the student email with the account regardless.

Next, you open Rider and select the option to activate your license via the JetBrains Account. It will use your default browser to log in to your JetBrains account. After logging in, your license will be shown in Rider, and you can click Activate to begin using Rider.

{% include image.html url="jetbrains-student-activate.png" description="Activate license via JetBrains account" caption="Activate your license via your JetBrains Account" %}


2. 

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
