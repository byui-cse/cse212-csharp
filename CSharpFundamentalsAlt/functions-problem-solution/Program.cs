using functions_problem_solution;
    // Start with a robot at (5,5) with fuel of 100.  Provide a menu
    // for the user to move the robot around.

var robot = new Robot();
var robotFuel = 100;

var choice = "";
while (choice != "q") {
    Console.WriteLine($"Robot at ({robot.X},{robot.Y}) with {robotFuel} units fuel");
    Console.WriteLine("l)eft r)ight u)p d)own f)ire q)uit");
    Console.Write("> ");
    choice = Console.ReadLine();

    // Call the appropriate function.  The current robot information
    // is sent to the function and the updated information is returned
    // and saved.
    if (choice == "l")
        robotFuel = robot.MoveLeft(robotFuel);
    else if (choice == "r")
        robotFuel = robot.MoveRight(robotFuel);
    else if (choice == "u")
        robotFuel = robot.MoveUp(robotFuel);
    else if (choice == "d")
        robotFuel = robot.MoveDown(robotFuel);
    else if (choice == "f")
        robotFuel = robot.FireLaser(robotFuel);
    Console.WriteLine();
}
