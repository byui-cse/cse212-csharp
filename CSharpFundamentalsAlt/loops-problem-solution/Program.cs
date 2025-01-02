var again = "Y"; // Allows entry into the loop
while (again == "Y") {
    // Ask user for information about the series
    Console.Write("Initial Term: ");
    var term = decimal.Parse(Console.ReadLine()!);
    Console.Write("Ratio: ");
    var ratio = decimal.Parse(Console.ReadLine()!);
    Console.Write("Terms to add: ");
    var numTerms = decimal.Parse(Console.ReadLine()!);

    // Start with the initial term and then loop 'num_terms' times
    // to calculate more terms.
    var seriesSum = term;
    for (var i = 0; i < numTerms; ++i) { // Runs 'num_terms" times.  'x' is not used
        // Calculate the new term and add it to the sum
        term *= ratio;
        seriesSum += term;
    }

    // Display result and ask if the user wants to do another calculation
    Console.WriteLine($"Sum = {seriesSum:0.00000000000000000000}");
    Console.WriteLine();
    Console.Write("Again (Y/N)? ");
    again = Console.ReadLine()!.ToUpper();
}