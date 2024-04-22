---
layout: default
title: "CSE 212 Rider Helps"
---

# CSE 212 Rider Helps
## Table of Contents
* [What is Rider?](#what-is-rider)
* [Obtaining a Student License](#obtaining-a-student-license)
* [Rider Setup](#rider-setup)
  * [Using JetBrains Toolbox (preferred)](#using-jetbrains-toolbox-preferred)
  * [Standalone Install](#rider-as-a-stand-alone-application)
* [Using Rider](#using-rider)
  * [Opening Files With a Single Click](#opening-files-with-a-single-click)
  * [Why Doesn't the **Run** Button Work?](#why-doesnt-the-_run_-button-work)
  * [Using Version Control](#using-version-control)
  * [It's Broke... How Do I Reset It?](#its-broke-how-do-i-reset-it)
  * [Navigating Assignments with TODOs](#navigating-assignments-with-todos)

## What is Rider?

JetBrains Rider is a cross-platform Integrated Development Environment (IDE) that will speed up development and give you experience that will prepare you for coding in the workplace. Using this tool will give you *many* advantages over Visual Studio Code (which you probably have used in the past). Rider supplies better coding helps, a working **Run** button, help with debugging errors, and is used across the industry to increase productivity in .NET development.

## Obtaining a Student License

You will need to activate a [student license](https://www.jetbrains.com/community/education/#students){:target="_blank"} which involves creating an account and supplying your BYU-Idaho email address.

Apply for a student license: [https://www.jetbrains.com/community/education/#students](https://www.jetbrains.com/community/education/#students)

{% include image.html url="jetbrains-student-apply-link.png" description="Shows the apply button" caption="Click <u>Apply now</u>" %}

{% include image.html url="jetbrains-student-email.png" description="Use your BYU-Idaho Email Address" caption="Fill out the form" %}

You will receive an email asking you to verify and log in with your JetBrains account. You will need to create an account. This account does not have to be your BYU-Idaho email address, as the student license verification will tie the student email with the account regardless.

Next, you open Rider and select the option to activate your license via the JetBrains Account. It will use your default browser to log in to your JetBrains account. After logging in, your license will be shown in Rider, and you can click Activate to begin using Rider.

{% include image.html url="jetbrains-student-activate.png" description="Activate license via JetBrains account" caption="Activate your license via your JetBrains Account" %}

## Rider Setup

Before you install Rider, make sure you have your [student license](#obtaining-a-student-license). There are 2 ways to install Rider, using the JetBrains Toolbox (which allows you to install all JetBrains products), and simply installing Rider as a stand-alone application.

### Using JetBrains Toolbox (preferred)

Follow the instructions provided on [JetBrains Toolbox app website](https://www.jetbrains.com/toolbox-app/){:target="_blank"} to install the JetBrains Toolbox. Once the Toolbox is running, click its icon in your notification section of your operating system and look for Rider on the list of available tools, and click the `Install` button. The toolbox will let you know when there are updates to your installed tools.

### Rider as a Stand-Alone Application

Follow the instructions provided on the [Rider download page](https://www.jetbrains.com/rider/download/){:target="_blank"}. Once downloaded, follow the prompts to install Rider. The first time Rider starts up, it will prompt you for color theme, additional plugins, and keyboard mappings. If you've only ever used VS Code, you should pick the VS Code (not Visual Studio) keyboard mappings as it will behave more like VS Code. Most students should not install any additional plugins as Rider comes ready to use.

> If Rider does not start properly, check the [system requirements](https://www.jetbrains.com/dotnet/download/system-requirements/#section-rider) to make sure your system can run it.

## Using Rider

By default, Rider is ready to use for .NET development. Under this section are a few things that can help make your life easier or can help when something doesn't go right.

### Opening Files With a Single Click

To make Rider feel more like VS Code and easier to use, click the 3 dots where your file list shows up, and make sure `Open Files with Single Click` is checked.

{% include image.html url="jetbrains-one-click-options.png" description="Go into the Explorer Options" caption="Click <u>⋮</u>" %}

{% include image.html url="jetbrains-one-click-enable.png" description="Check the Single Click option" caption="Click <u>Open Files with Single Click</u>" %}

### Why Doesn't the _Run_ Button Work?

Most likely, the _Run_ button doesn't work because you only opened the folder in Rider and didn't open the project file. I'll show you how to avoid and fix this.

#### Avoiding the Gray `Run` Button

The easiest way to avoid getting the gray `Run` button in the first place is to open the project when you first open Rider. Using GitHub Desktop, when you select `Open in Rider`, Rider will prompt you with something like the following prompt:

{% include image.html url="jetbrains-run-button-avoid-error.png" description="Open repository message" caption="Click <u>OK</u> - Do NOT 'Just open the directory'" %}

#### Fixing the Gray `Run` Button

Use your Folder Explorer on Windows or Finder on Mac to find the folder that you've opened and then make sure to open the __.csproj file:

{% include image.html url="jetbrains-run-button-fix.png" description="Open the project using the .csproj file" caption="Open the ___.csproj file using Rider" %}

If this still opens the folder without the `Run` button, see [Reset Rider help](#its-broke-how-do-i-reset-it)

### Using Version Control

Make sure and use the `Commit and Push` option. If you just used commit, you can use tools like GitHub Desktop to push all changes that you've committed. Also, you can use the Git -> Push menu option.

### It's Broke... How Do I Reset It?

All of Rider's settings for a given project are stored in the same directory as the project. Notice how when I show hidden files, there's 3 extra files in my folder:

{% include image.html url="jetbrains-rider-folder.png" description="Finder window of a project file" caption="Showing hidden files using macOS Finder" %}

 How to see hidden files: [Windows](https://www.google.com/search?q=show+hidden+files+windows+explorer) / [macOS](https://www.google.com/search?q=show+hidden+files+mac+finder)

In order to reset Rider's view of a project, do the following:

1. Make sure the project is closed in Rider
2. Remove the project from the recent list of projects
3. Using Finder or Explorer (or a terminal) delete the __.idea__ folder
4. Open the project again, and Rider should prompt you to open the project file and not the directory, make sure you follow the advice to [avoid this in the future](#avoiding-the-gray-run-button)

{% include image.html url="jetbrains-rider-reset.png" description="Finder window of a project file without the hidden folder .idea" caption="Remove the .idea folder" %}

### Navigating Assignments with TODOs

For almost all of your teach one another assignments and prove assignments, you will be cloning a repository, making changes, and then committing and pushing changes to that repository. You will then submit a link to your repository in canvas as the submission. For cloning, committing, and pushing changes we *strongly* encourage you to use [GitHub Desktop](https://desktop.github.com/){:target="_blank"} over any other tools. I've seen other tools lose track of changes, miss files, or experience authentication issues.

