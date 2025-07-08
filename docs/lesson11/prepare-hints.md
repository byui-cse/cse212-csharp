---
layout: default
title: "W11 Final Project Helps"
---

# Final Project Hints & Helps

## Where do I write up my Report?
The ***report.md*** file is in your repository you may need to switch to from the `solution` view to the `files` view in the Explorer tab:

{% include image.html url="solution-files.png" description="Shows switching to the Files view" caption="Select Files to view the markdown files in the solution" %}

## My IPlaylist Interface is not working

The c# solution file defines projects. Each project is a library or an executable, and they might reference each other to use classes defined in other projects. Our solution puts the `Menu`, `IPlaylist`, and `Song` classes in the `Common` project. Some projects may not have references to this `Common` project. To add the reference, right-click on the project, then **Add**, then **Reference...**.

{% include image.html url="add-reference.png" description="Shows adding a reference to Common" caption="Adding a reference to one of your projects to another project" %}

***Note for Spring 2025 Semester***

Spring 2025 project was missing the following references:
* `Playlist2` needs to reference `Common`
* `Playlist2Tests` needs to reference `Playlist2`
* `Playlist3` needs to reference `Common`
* `Playlist3Tests` needs to reference `Playlist3`

Alternately, you can **Sync Fork** your repository to update your local repository.

## Using Markdown Language
The Markdown language is commonly used to develop documentation. The purpose of requiring Markdown for your report is to give you experience using this language. Using a simple editor and the knowledge of a little bit of syntax, you can create documents with headers, bulleted lists, links, bold text, tables and pictures. A common place to see Markdown documents is in GitHub repositories. GitHub automatically interprets the Markdown file and displays as intended.

There are many different tools available to help you write and preview Markdown files. Your editor has built-in support for Markdown. If you create a file with an `md` extension, then you can click on the preview button, and you can see the Markdown and the finished product side by side.

Writing in Markdown requires the memorization of some basic syntax (here is an example of a [cheat sheet](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) you might find useful). Listed below is common syntax you may want to use in your report.

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
