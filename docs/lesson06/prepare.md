---
layout: default
title: "W06 Prepare: Reading"
---

# W06 Prepare: Reading
## Table of Contents
* [Maps](#maps)
    * [Making the Map from the Set](#making-the-map-from-the-set)
    * [Maps in C#](#maps-in-c)
    * [Complex Dictionary Data](#complex-dictionary-data)
    * [Building Summary Tables](#building-summary-tables)
* [Key Terms](#key-terms)

## Maps

### Making the Map from the Set

The **map** is most commonly viewed as a table. In the map below, the first column contains a unique value called the **key**. The second column contains a **value** (not necessarily unique) called the value. The key forms a set because all the values are unique. A map is created in software by associating a value with each item in the key set. In the picture below, the table shows the key and value pairs. The keys are hashed into what looks like a set. The values are then stored with each key value.

<!--- Image 1-->
{% include image.html url="map.jpg"
description="Shows a table with Color (the key) equal to Green (the value), Quantity equal to 25, Price equal to 1.99, Name equal to Pencil, and ID equal to 3924A-3.  Each key/value pair is then stored in the data structure.  The keys are hashed (index(n) = hash(key) % 10) into a list of size 10.  For demonstration purposes, Quantity has been put in Index 1, the Name has been put in Index 3, the Color has been put in Index 4, then Price has been put in Index 7, and the ID has been put in Index 9.  The values for each key value have been placed in the same location as the Key."
caption="Map of Colored Pencil Properties"
%}

### Maps in C#

The performance of the map is the same for the set. Some programming languages call this a HashTable or a HashMap. In C#, this is called a dictionary. The dictionary (like the set) is an object where you define your key data type and your value data type when you define your dictionary:

```csharp
var dictionary = new Dictionary<string, double>();
```

or

```csharp
var dictionary = new Dictionary<string, double>() { { "key1", 2.1 }, { "key2", 2.3 } };
```

| Common Map Operation | Description | C# Code | Performance   |
|----------------------|-------------|---------|---------------|
| put(key, value) | Adds (or replaces) a row in the map with the specified key and value. | `myMap.Add(key, value)` or `myMap[key] = value`  | O(1) - Performance of hashing the key (assuming good conflict resolution) and assigning the value |
| get(key)        | Gets the value for the specified key.       | `myMap[key]`   | O(1) - Performance of hashing the key (assuming good conflict resolution) and getting the associated value |
| remove(key)     | Removes the row from the map containing the specified key. | `myMap.Remove(key)` | O(1) - Performance of hashing the key (assuming good conflict resolution) and removing the associated value |
| member(key)    | Determines if "key" is in the map. | `myMap.ContainsKey(key)` | O(1) - Performance of hashing the key (assuming good conflict resolution) |
| size()         | Returns the number of items in the map. | `myMap.Count` | O(1) - Performance of returning the size of the map |

### Objects are Maps
Whenever you create a class in any programming language, you are creating a map. Each member variable or property on the class can be considered a key, with the value being stored in that variable. Consider the following code:

```csharp
class PersonDataMapping {
  public string FirstName { get; set; }
  public string LastName { get; set; }
  public double Age { get; set; }
}
```

The `PersonDataMapping` class maps the key of "FirstName" with the first name of the person. The lookup and access time is O(1) because the compiler knows the order and type of the variables and can jump to that part of the memory without caring how much additional data belongs to the `PersonDataMapping` class.

### Complex Map Data

Mapping data using keys and values has been a standard among the Internet almost since the beginning. Consider the following example which is data that was received from a website about the location of the [International Space Station](http://open-notify.org/Open-Notify-API/ISS-Location-Now/). This data is called **JSON** (JavaScript Object Notation) data and is a common data format. JSON data is nothing more than a map of maps.

```json
{
  "timestamp": 1584638006, 
  "message": "success", 
  "iss_position": {
    "longitude": -149.9053,
    "latitude": -35.9225
  }
}
```

If we wanted to create a mapping for this complex data, we can create custom classes to map the data appropriately:

```csharp
class SpaceStation {
    public long Timestamp { get; set; }
    public string Message { get; set; }
    public Location IssPosition { get; set; }
}

class Location {
    public double Longitude { get; set; }
    public double Latitude { get; set; }
}
```

With an instance of the `SpaceStation` class, it is essentially a map where the keys are fixed when the program is built. This does require that you know the format of the data (including all of the value data types) before creating the class.

Once we read, the JSON data from the server, we use a `JsonSerializer.Deserialize()` method to convert the raw JSON data into the class object.

```csharp
var spaceStation = JsonSerializer.Deserialize<SpaceStation>(json);
var lon = spaceStation.IssPosition.Longitude;
var lat = spaceStation.IssPosition.Latitude;
Console.WriteLine($"Space Station at Lon: {lon} Lat: {lat}");
```

Notice how `IssPosition` is a key in the `SpaceStation` object. The value for this is another object `Location`. To get the `Longitude` key, we have to go through the `IssPosition` using the `.` notation twice.

Here is another example of data that was received about the number of people that are in space. 

###### JSON:
```json
{
  "people": [
    { "craft": "ISS", "name": "Andrew Morgan" }, 
    { "craft": "ISS", "name": "Oleg Skripochka" }, 
    { "craft": "ISS", "name": "Jessica Meir" }
  ], 
  "message": "success", 
  "number": 3
}
```
###### C#:
```csharp
class Space {
  public Person[] People { get; set; }
  public string Message { get; set; }
  public int Number { get; set; }
}
class Person {
  public string Craft { get; set; }
  public string Name { get; set; }
}

...

var space = JsonSerializer.Deserialize<Space>(json);
foreach (var person in space.People) {
  Console.WriteLine(person.Name);
}
```

Notice that the "people" key has an array for a value (using the square brackets). To display the "name" of each person, we need to loop through each of the objects in the "people" list and display the value associated with the "name" key.

### Building Summary Tables
A map is often described as a table. If we have a large set of data that we want to summarize, we can build a summary table using a map. The summary table could contain counts, sums, minimums, maximums, or other mathematical aggregations.
	
```csharp
var letters = new[] {'A', 'A', 'B', 'G', 'C', 'G', 'G', 'D', 'B'};
var summaryTable = new Dictionary<char, int>();

foreach (var letter in letters) {
	// If the letter is not in our summary table yet, add it
	if (summaryTable.ContainsKey(letter)) {
		// The key is the letter since we want to summarize how
		// many letters we have.  Since it the first time we 
		// have seen this letter, we will set the value to 1.
		summaryTable[letter] = 1;
  }

	// If the letter is in the table, then update the value
	else {
		// We want to increase the value by 1 since we have 
		// already seen this letter before
		summaryTable[letter] += 1;
  }
}

Console.WriteLine(string.Join(", ", summaryTable));
// [A, 2], [B, 2], [G, 3], [C, 1], [D, 1]
```

## Key Terms
<dl>
  <dt>JSON</dt>
  <dd>JavaScript Object Notation. A format used frequently to share data between software. JSON data uses maps and lists. The syntax of JSON is the same as Python.</dd>
  <dt>key</dt>
  <dd>The keys in the map form a set. Each key is unique. Keys are used to lookup value from the map.</dd>
  <dt>map</dt>
  <dd>A data structure that is based on the set. In addition to storing the unique values in the set, the map also includes a value associated with each key. The map has the same O(1) behavior as the set.</dd>
  <dt>value</dt>
  <dd>The value associated with each key within a map. Frequently, these values are referred to as key-value pairs.</dd>
</dl>
