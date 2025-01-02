namespace functions_problem_solution;

public class Robot {
    public int X { get; set; } = 5;
    public int Y { get; set; } = 5;

    /// <summary>
    /// Move y up by 1 and fuel down by 5 (if there is enough fuel)
    /// </summary>
    /// <param name="fuel">amount of fuel in the tank</param>
    /// <returns>The updated fuel</returns>
    public int MoveUp(int fuel) {
        if (fuel >= 5) {
            Y += 1;
            fuel -= 5;
        }
        else {
            Console.WriteLine("Not enough fuel!");
        }

        return fuel;
    }

    /// <summary>
    /// Move y down by 1 and fuel down by 5 (if there is enough fuel)
    /// </summary>
    /// <param name="fuel">amount of fuel in the tank</param>
    /// <returns>The updated fuel</returns>
    public int MoveDown(int fuel) {
        if (fuel >= 5) {
            Y -= 1;
            fuel -= 5;
        }
        else {
            Console.WriteLine("Not enough fuel!");
        }

        return fuel;
    }

    /// <summary>
    /// Move x down by 1 and fuel down by 5 (if there is enough fuel)
    /// </summary>
    /// <param name="fuel">amount of fuel in the tank</param>
    /// <returns>The updated fuel</returns>
    public int MoveLeft(int fuel) {
        if (fuel >= 5) {
            X -= 1;
            fuel -= 5;
        }
        else {
            Console.WriteLine("Not enough fuel!");
        }

        return fuel;
    }

    /// <summary>
    /// Move x up by 1 and fuel down by 5 (if there is enough fuel)
    /// </summary>
    /// <param name="fuel">amount of fuel in the tank</param>
    /// <returns>The updated fuel</returns>
    public int MoveRight(int fuel) {
        if (fuel >= 5) {
            X += 1;
            fuel -= 5;
        }
        else {
            Console.WriteLine("Not enough fuel!");
        }

        return fuel;
    }

    /// <summary>
    /// Move fuel down by 10 and display the firing message (if there is enough fuel)
    /// </summary>
    /// <param name="fuel">amount of fuel in the tank</param>
    /// <returns>The updated fuel</returns>
    public int FireLaser(int fuel) {
        if (fuel >= 10) {
            fuel -= 10;
            Console.WriteLine("Pew Pew!");
        }
        else {
            Console.WriteLine("Not enough fuel!");
        }

        return fuel;
    }
}