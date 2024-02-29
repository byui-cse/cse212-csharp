---
layout: default
title: "W06 Prove: Individual Assignment"
---

# W06 Prove: Individual Assignment
## Instructions
This assignment **must be completed individually** to ensure you are meeting all course outcomes. You should not complete this assignment within a group. If you obtain help from a tutor, the tutor should help you understand principles but should not help you answer these problems. It is an honor code violation to obtain answers for these problems from others including using the internet (i.e. sites that allow students to share their solutions).

As you solve the problems, remember to use the principles learned in the first five lessons of the course:
* Problem Solving Strategy: understand the problem, plan and design the solution, implement the solution, and evaluate the solution.
* Evaluate Performance of Alternative Solutions: use big O to determine the best solution.
* Understanding Code Using Reviews: analyze any code you have been given.
* Finding Defects Using Tests: write tests to determine if your solution is working.
* Articulating Answers for Technical Questions: imagine that you were asked one of these questions during an interview. Remember to ensure that you fully understand the problem and work through different scenarios manually. Consider how the data structure you are using will help you solve the problem. A notebook or a whiteboard can be very useful in this process.

All of the files for this assignment will be found in the GitHub classroom ***prove-06*** repository. You will commit changes to your own repository for your submission for this assignment.

#### Step 1: [Accept your assignment repository](prove-classroom){:target="_blank"}

### Problem 1 - Translator Class
Implement the `AddWord` and `Translate` functions in the Translator class using a dictionary. The `AddWord` function should allow the user to add word translations (e.g. english to german). The `Translate` function should return the translation of a word. If the translation is not available for a word, then "???" should be returned instead. You will need to call `AddWord` multiple times to build a translation dictionary for testing. You should assume that there is only one translation for every word (and vice versa).

### Problem 2 - Degree Summary
Finish implementing the `SummarizeDegrees` function in the `MapsTester` class which reads a file and creates a dictionary containing a summary of all the degrees (education) that people earned as reported in the file. The degree can be found in column 4 of the file. Your code should automatically determine the degree names. You should use the following file for testing: `census.txt`.

### Problem 3 - Anagrams
Finish implementing the `IsAnagram` function to determine if two words are anagrams. Two words are an anagram if they use the same letters and the same number of letters. For example, "CAT" and "ACT" are anagrams but "DOG" and "GOOD" are not because "GOOD" has two O's. You must use a dictionary to solve this problem. It is important to note the following assumptions:
* When determining if two words are anagrams, you should ignore any spaces.
* You should ignore letter case. For example, 'Ab' and 'Ba' should be considered anagrams.

Reminder: You can access a letter by index in a string by using the `myString[3]` notation.

### Problem 4 - Maze
Implement the `MoveLeft`, `MoveRight`, `MoveUp`, and `MoveDown` functions in the Maze class. The code provides a sample Maze in the form of a dictionary where the key represents the (x,y) coordinate in the maze and the value contains the valid movements in the format (left, right, up, down). The valid movements are set to `true` and `false`. To test your code, will have to manually move around the maze using the dictionary maze shown in the code. The dictionary maze can be represented graphically as follows (note that it is assumed there is a wall going around the entire maze which means that you cannot leave the outside boundaries of the maze):

{% include image.html url="maze.jpg" description="A maze that has 6 rows (y=1 to y=6) and 6 columns (x=1 to x=6).  Walls are drawn in the following blocks: (3,1) (3,2) (4,2) (6,2) (1,3) (3,3) (6,4) (2,5) (4,5) (6,5) (2,6) (4,6)." caption="Maze Visualization" %}

### Problem 5 - Earthquake JSON Data
Finish implementing the `EarthquakeDailySummary` function to display all the earthquake locations ('place' attribute) and magnitudes ('mag' attribute) for the current day from the United States Geological Service (USGS) website. The [USGS Website](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php) provides details about how to interpret the data that you will receive from their server. The data uses JSON (JavaScript Object Notation) format. In C#, JSON data can be deserialized into an object. Objects are essentially a map, where the keys are the property names and the values are the property values. The difference between objects and dictionaries is that objects are defined at compile time, where dictionaries can be added to dynamically throughout the program execution. Examine the data that you will be deserializing and use it to populate the `FeatureCollection` object with the right properties.

Your output should be formatted to display the data like this, however the places and magnitudes of the earthquakes will be different as this data changes every day.

```
=========== PROBLEM 5 TESTS ===========
1km NE of Pahala, Hawaii - Mag 2.36
58km NW of Kandrian, Papua New Guinea - Mag 4.5
16km NNW of Truckee, California - Mag 0.7
9km S of Idyllwild, CA - Mag 0.25
14km SW of Searles Valley, CA - Mag 0.36
4km SW of Volcano, Hawaii - Mag 1.99
...
```

## Submission
You need to submit the following for this assignment:
* Make sure all of your changes are committed and pushed to the `main` branch of your **prove-06-[username]** repository
* Submit a link to your repository in I-Learn
