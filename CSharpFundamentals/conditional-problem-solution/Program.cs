// Prompt the user for information

Console.Write("Please enter the age of your child: ");
var age = int.Parse(Console.ReadLine()!);
Console.Write("Please enter the number of children in your family: ");
var children = int.Parse(Console.ReadLine()!);
Console.Write("Please enter the family annual income: $");
var income = int.Parse(Console.ReadLine()!);

if (age < 8 || age > 16) {
    // No calculations if they can't attend
    Console.WriteLine("N/A - They can't attend");
}
else {
    double basePrice;
    double discount;

    // Determine their base price
    // Note that we already know the age is 8-16
    if (age <= 10) {
        basePrice = 1000;
    }
    else if (age <= 12) {
        basePrice = 1500;
    }
    else {
        basePrice = 2000;
    }

    // Determine discount based on income and 
    // children in the family
    if (income < 25000) {
        if (children == 1) {
            discount = 0.70;
        }
        else if (children == 2) {
            discount = 0.80;
        }
        else {
            discount = 0.90;
        }
    }
    else if (income < 50000) {
        if (children == 1) {
            discount = 0.40;
        }
        else if (children == 2) {
            discount = 0.50;
        }
        else {
            discount = 0.60;
        }
    }
    else if (income < 75000) {
        if (children == 1) {
            discount = 0.10;
        }
        else if (children == 2) {
            discount = 0.20;
        }
        else {
            discount = 0.30;
        }
    }
    else {
        // Family size does not matter for 
        // the higher income bracket
        discount = 0;
    }

    // Calculate the updated price and display it.
    var price = basePrice * (1 - discount);
    Console.WriteLine($"Price for child is: ${price}");
}