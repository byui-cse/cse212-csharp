// See https://aka.ms/new-console-template for more information
/*
---------  CSE212 -----------
This file is not intended to have useable code.  It has been created to generate and check 
syntax for code snippets used in the course material (prepare.md)
*/

/* EXAMPLE 1:
python version
```
(PYTHON VERSION)
def find_bob(name_list):
	for name in name_list:
		if name == "Bob":
			return True
	return False
```

---------------------------
*/

bool FindBob(string[] nameList) {
    foreach (var name in nameList) {
        if (name == "Bob"){
            return true;
        }
    }
    return false;
}

/* EXAMPLE 2: */

void MultipleLoops(int n) {
    for (int i = 1; i < n; i++) {
        Console.WriteLine(i);
            for (int j = 1; j < n; j++) {
                Console.WriteLine(i*i);
        }
    }
}

void MultiplicationTable(int n) {
    for (int i = 1; i < n; i++) {
            for (int j = 1; j < n; j++) {
                Console.WriteLine((i+1)* (j+i));
        }
    }
}



void ShortMultiplicationTable(int n) {
    for (int i = 1; i < n; i++) {
            for (int j = 1; j < 3; j++) {
                Console.WriteLine((i+1)* (j+i));
        }
    }
}


void LotsOfLoops(int n) {
    int total = 0;
    for (int i = 1; i < n; i++) {
        for (int j = 1; j < n; j++) {
            for (int k = 1; k < n; k++) {
                total += (i*j*k);
            }
        }
    }
    Console.WriteLine(total);
}

/* Using built-in Stopwatch to measure performance */
var watch = new System.Diagnostics.Stopwatch();
watch.Start();
for (int i = 0; i < 1000; i++)
{
    Console.Write(i);
}
watch.Stop();  // sdf
Console.WriteLine($"Execution Time: {watch.ElapsedMilliseconds} ms");
/************************************/



int LotsOfLoopsWithInstrumentation(int n) {
    int total = 0;
    int count = 0; // Variable just to instrument 
    for (int i = 1; i < n; i++) {
        for (int j = 1; j < n; j++) {
            for (int k = 1; k < n; k++) {
                total += (i*j*k);
                count++;  //Count the number of times in the inner-most loop
            }
        }
    }
    Console.WriteLine(total);   // output from useful work
    return count;               // instrumentation
}
int work = LotsOfLoopsWithInstrumentation(1000);
Console.WriteLine("Innermost count is: %i",work);   // output from useful work







Console.WriteLine("find_bob is: ",FindBob({"jim","bob"}));

LotsOfLoops(6);
MultipleLoops([1,2,3]);
MultiplicationTable([1,2,3]);
ShortMultiplicationTable([1,2,3]);
