# Functions

The function gives software the ability to organize and reuse software code. Imagine you are in a car factory. If you were the only one in the factory, it would take a very long time to build a single car. However, if you have multiple people in the factory, the work could get done more efficiently. One of the reasons we have efficiency is because we can organize the building of the car better with several hands to help. However, if we put 1000 people in the car factory but didn't get them responsibilities, we would probably not be very successful. The people in the factory are like functions in code. The functions are added to organize the effort but each function must have a specific task to complete. If we are wise, we will give tasks to each function that are commonly repeated in our software. 

Thinking of our favorite game again, you can think of common things which are done all the time which are likely written as their own functions:

- Update the location of the space ship
- Fire the photon torpedoes
- Check to see if we have been hit
- Draw the planets, moons, and asteroids around us
- Calculate the health of our ship
- Save the state of our game so we can play again later

## Functions are Methods

In C#, we typically call functions methods and can only be defined within a class. A method definition can be broken down into the following parts:

* Method Signature
    * Access level
    * Optional modifiers
    * Name
    * Parameters
    * Return type
* Method Body


We can see all five parts in the example below which converts degrees in fahrenheit to degrees in celsius:

```csharp
public static double ConvertTemp(double degF) {
    var degC = (degF - 32) * (5/9);
    return degC;
}
```

The access level is `public` so that it can be accessed from outside the class. `static` allows the function to be called without creating an instance of the class in which the function resides. `double` refers to the type of data returned from the function.The name of the function is `ConvertTemp`. The function parameters is `degF`. The function body is the code with the curly braces `{ }`. The function return is in the function body with the keyword `return` that provides the value of `degC` as a result. 

When you write a function, you have to think about the inputs it needs, the outputs it will provide, and how it will perform the task. Inputs are listed in the function parameters. It is possible that a function will not need any information because it will obtain all the information it needs from within the function or the class. If there are no parameters, then the parenthesis are still provided but are kept empty. If there is more than one parameter, then commas are used to separate the parameters. C# can have an optional parameter using an `=` sign after the name of the parameter with the default value if the parameter is not supplied. The code below shows several examples of parameters:

```csharp
public void SayHello() {  // No Parameters
}

public int AddNumbers(List<int> numbers) {  // One parameter ... a list
}

public static double CalcDensity(double mass, double volume) {  // Two parameters ... two numbers
}

private void DrawShip(int x, int y, bool forceField = false) { // Three parameters
}                                          // The x and y are required
                                           // The forceField is optional. If it
                                           // is not specified, then it will be 
                                           // assumed to be false
```

Outputs of a function are provided by a `return` statement. If there is no output, the declared return type is `void` and you can omit a `return` statement. A function can only return a single output, so if you want to return multiple values, you'll need to encapsulate them in another class. Here are some examples:

```csharp
public void SayHello() {
    Console.WriteLine("Hello");
    // No outputs
}

public static double CalcDensity(double mass, double volume) {
    var density = mass / volume;
    return density;  // Return one output
}

public static User GetUser() {
    Console.Write("Username: ");
    var username = Console.ReadLine();
    Console.Write("Password: ");
    var password = Console.ReadLine();
    return new User(username, password);  // Return two outputs in an object of type User
}
```

A function does not run (or execute) until it has been called. When you call a function, you connect inputs and outputs to that function. Be careful not to assume that parameter and variables in a function are the same as variables outside of the function just because their names are the same. When you pass values to the function, those are called arguments. The arguments are supplied in the order declared in the parameters in the method signature and will fill up from left to right. Here are some examples of calling functions:

```csharp
private static double CalcDensity(double mass, double volume) {
    var density = mass / volume;
    return density;  // Return one output
}

private static User GetUser() {
    Console.Write("Username: ");
    var username = Console.ReadLine();
    Console.Write("Password: ");
    var password = Console.ReadLine();
    return new User(username, password);  // Return two outputs in an object of type User
}

// Entry point for the program
public static void Main() {
    Console.Write("Enter the mass: ");
    double myMass = double.ParseDouble(Console.ReadLine());
    Console.Write("Enter the volume: ");
    double myVolume = double.ParseDouble(Console.ReadLine());

    // Call the function and use the '=' sign to store the result
    double myDensity = CalcDensity(my_mass, my_volume)

    // Use a class to save all of the outputs. 
    User user = GetUser()
}
```

## Organizing Functions

In larger software, you will need several functions and they will likely need to call each other. Before you write a bunch of functions, you should plan what functions you will need and how they will be called. One way represent this is with a calling tree. The following diagram is meant to represent a weather observation tool:

![weather_design](weather_design.jpg)

Notice that each line represents a function calling a function. In C#, the program execution begins at a function called `Main` which must be a `public static` function. Each line shows the inputs and outputs. With this information, we can write what is called stub code. Stub code includes all the parts of a function except the detailed implementation of the function body. The goal with stub code is to obtain code that both matches your plan (i.e. your design) and code that also runs (doesn't do the weather stuff yet but it does run). The next step after stub code is implementing each function one at a time. Here is the stub code for the design above:

```csharp
// Starting place for the program
public static void Main() {
    var tempList = new List<double>();
    var pressureList = new List<double>();
    var humidityList = new List<double>();
    // These calls should be done when the user wants them
    // The lists above need to be updated when new sensor data is received
    WeatherData data = ReadSensors();
    DisplayWeather(data.Temp, data.Pressure, data.Humidity);
    DisplayHistory(tempList, pressureList, humidityList);
}

private static WeatherData ReadSensors() {
    var temp = ReadTemp();
    var pressure = ReadPressure();
    var humidity = ReadHumidity();
    return new WeatherData(temp, pressure, humidity);
}

private static double ReadTemp() {
    // Read from actual sensor
    var temp = 0;
    return temp;
}

private static double ReadPressure() {
    // Read from actual sensor
    var pressure = 0;
    return pressure;
}

private static double ReadHumidity() {
    // Read from actual sensor
    var humidity = 0;
    return humidity;
}

public static void DisplayWeather(double temp, double pressure, double humidity) {
    // Only do the conversion if needed
    var convertedTemp = ConvertTemp(temp, metric=true);
}

public static void DisplayHistory(List<double> tempList, List<double> pressureList, List<double> humidityList) {
    // Need to call ConvertTemp on all the temp's in the list if needed
    DrawGraph(tempList);
    DrawGraph(pressureList);
    DrawGraph(humidityList);
}

private static double ConvertTemp(temp, metric=False) {
    // Do conversion calculation
    var calc_temp = 0;
    return calc_temp;
}

public static void DrawGraph(List<double> valuesList) {
    // Draw a graph
}
```

In the stub code, there is still plenty of work to be done to fully implement the solution. When C# begins the application, it will call the `Main()` function for you.

## Example: Electronic Purchase

When making a purchase, there are several things that must be determined:

- What is the tax?
- What is the shipping cost?
- Are there any coupons?

We will write a separate function to handle of each of these questions. The table below works out all of the inputs and outputs of each of these functions:

| Function      | Inputs                                            | Outputs        |
| ------------- | ------------------------------------------------- | -------------- |
| calc_tax      | subtotal, country_tax_rate, local_tax_rate        | total_tax      |
| calc_shipping | total_weight, distance, expedited (True or False) | total_shipping |
| calc_coupons  | subtotal, coupon_code                             | total_savings  |

Here is the implementation for these three functions:

```csharp
/// <summary>Use the tax rates to determine the total tax.</summary>
public double CalcTax(double subtotal, double countryTaxRate, double localTaxRate) {
    var countryTax = subtotal * countryTaxRate;
    var localTax = subtotal * localTaxRate;
    var totalTax = countryTax + localTax;
    return totalTax;
}

/// <summary>
/// Minimum shipping cost is $5.
/// For every pound over 20 pounds, there is a 25 cent per pound cost.
/// If the distance is greater than 1000 miles, there is a 50% additional shipping charge
/// For expedited shipping, there is a $20 extra charge.
/// </summary>
public double CalcShipping(double totalWeight, double distance, bool expedited) {
    double shipping = 5;
    if (totalWeight > 20)
        shipping += (totalWeight - 20) * 0.25;
    if (distance > 1000)
        shipping *= 1.5;
    if (expedited)
        shipping += 20;
    return shipping;
}

/// <summary>
/// CODE      RULES
/// ------    -------------------
/// SAVE50    50% if spending more than $20
/// SAVE10    10% with no minimum spending
/// </summary>
public double CalcCoupons(double subtotal, string couponCode) {
    if (couponCode == "SAVE50") {
        if (subtotal >= 20)
            return subtotal * 0.5;
        else
            return 0;
    }
    else if (couponCode == "SAVE10") {
        return subtotal * 0.1;
    }
    else {
        return 0;
    }
}
```

To call these functions, we will create a function called `CalcFinalPrice` which will provide all the needed inputs of which `expedited` and `couponCode` will be optional. The decision to make these optional was because we envision that possibility that the user won't know about these things so we will provide some default values. Some sample test cases are shown below as well.

```csharp
public double CalcFinalPrice(double subtotal, double countryTaxRate, double localTaxRate, 
                             double totalWeight, double distance, bool expedited=false, 
                             string couponCode="") {
    var tax = CalcTax(subtotal, countryTaxRate, localTaxRate);
    var shipping = CalcShipping(totalWeight, distance, expedited);
    var savings = CalcCoupons(subtotal, couponCode);
    return subtotal + tax + shipping - savings;
}

...
public static void Main() {
    var cart = new Cart();
    var price = cart.CalcFinalPrice(100, 0.06, 0.001, 30, 125, couponCode: "SAVE50");
    Console.WriteLine("${:.2f}".format(price));

    price = cart.CalcFinalPrice(100, 0.06, 0.001, 30, 125, expedited: true);
    Console.WriteLine("${:.2f}".format(price));

    price = cart.CalcFinalPrice(100, 0.06, 0.001, 30, 125);
    Console.WriteLine("${:.2f}".format(price));

    price = cart.CalcFinalPrice(100, 0.06, 0.001, 30, 2000);
    Console.WriteLine("${:.2f}".format(price));
}
```

The result of running these tests is:

```
$63.60
$133.60
$113.60
$117.35
```

##  Problem to Solve: Robot

A robot wants to move around on the following grid:

![robot_grid](robot_grid.jpeg)

When the robot starts, the robot will be at position (5, 5) and have 100 units of fuel. Create a separate function to do each of the following:

- `MoveUp` - Change the coordinate position and reduce fuel by 5. Display an error message if there is not enough fuel.
- `MoveDown` - Change the coordinate position and reduce fuel by 5. Display an error message if there is not enough fuel.
- `MoveLeft` - Change the coordinate position and reduce fuel by 5. Display an error message if there is not enough fuel.
- `MoveRight` - Change the coordinate position and reduce fuel by 5. Display an error message if there is not enough fuel.
- `FireLaser` - Reduce fuel by 10 and display "Pew Pew". Display an error message if there is not enough fuel.

Notice that all of these described above must be done within the functions. You do not need to worry about leaving the boundaries of the grid shown above. You will also need to write code to prompt the user for a command to move or to fire the laser. The appropriate function should be called based on the user choice. Think about the inputs and outputs required for each function before writing the code.

An example execution of the program is shown below:

```
Robot at (5,5) with 100 units fuel
l)eft r)ight u)p d)own f)ire q)uit
> l

Robot at (4,5) with 95 units fuel
l)eft r)ight u)p d)own f)ire q)uit
> l

Robot at (3,5) with 90 units fuel
l)eft r)ight u)p d)own f)ire q)uit
> l

Robot at (2,5) with 85 units fuel
l)eft r)ight u)p d)own f)ire q)uit
> r

Robot at (3,5) with 80 units fuel
l)eft r)ight u)p d)own f)ire q)uit
> u

Robot at (3,6) with 75 units fuel
l)eft r)ight u)p d)own f)ire q)uit
> u

Robot at (3,7) with 70 units fuel
l)eft r)ight u)p d)own f)ire q)uit
> u

Robot at (3,8) with 65 units fuel
l)eft r)ight u)p d)own f)ire q)uit
> d

Robot at (3,7) with 60 units fuel
l)eft r)ight u)p d)own f)ire q)uit
> d

Robot at (3,6) with 55 units fuel
l)eft r)ight u)p d)own f)ire q)uit
> f
Pew Pew!

Robot at (3,6) with 45 units fuel
l)eft r)ight u)p d)own f)ire q)uit
> f
Pew Pew!

Robot at (3,6) with 35 units fuel
l)eft r)ight u)p d)own f)ire q)uit
> f
Pew Pew!

Robot at (3,6) with 25 units fuel
l)eft r)ight u)p d)own f)ire q)uit
> f
Pew Pew!

Robot at (3,6) with 15 units fuel
l)eft r)ight u)p d)own f)ire q)uit
> f
Pew Pew!

Robot at (3,6) with 5 units fuel
l)eft r)ight u)p d)own f)ire q)uit
> f
Not enough fuel!

Robot at (3,6) with 5 units fuel
l)eft r)ight u)p d)own f)ire q)uit
> u

Robot at (3,7) with 0 units fuel
l)eft r)ight u)p d)own f)ire q)uit
> u
Not enough fuel!

Robot at (3,7) with 0 units fuel
l)eft r)ight u)p d)own f)ire q)uit
> q
```

You can check your code with the solution here: [Solution](functions-problem-solution)

[Back to Welcome Page](0-welcome.md)