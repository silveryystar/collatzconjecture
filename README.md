# Collatz Conjecture Graphing Tool
A tool that plots iterations per integer number in the Collatz Conjecture, a currently unsolved mathematical question.

# Setup
1. Install Python at https://www.python.org/downloads/.
2. Download repository.
3. Open Terminal in repository folder.
4. Enter ```pip install matplotlib```. 
5. Enter ```python main.py```.

# Usage
Run *main.py* via ```python main.py``` in Terminal.
```Maximum number:``` will print.
Enter the maximum integer value for the code to iterate.

After, assuming arbitrary integers are wholly divisible by the entered integer and equal integers in range 1 to 100, percents will print indicating program's progress.
For low *n*, such that *n* < 10^6, the program usually takes less than a minute to run.
For high *n*, such as *n* > 10^6, the program can take significantly longer to run.

After completing, a plot will open in a new tab, showing patterns in the Collatz Conjecture.

# Example
Suppose the user wants to plot 1 ≤ *n* ≤ **1000000** (10^6).
Run *main.py* via ```python main.py``` in Terminal.
When ```Maximum number:``` prints, enter ```1000000```.

After, the program will iterate over each integer, logging the number of iterations until reaching 1 for each number.
As the program runs, it will indicate its progress via printing percents.

After the program iterates over all values between 1 and **1000000**, the plot will open.
To save the plot, click the "save the figure" icon, the rightmost option located at the bottom left of the figure.
For this example, the plot is *Figure_0.png* in the repository.

# Errors
1. ```Invalid input. Enter an integer.```
Solution: Enter an integer value greater than or equal to 1.
2. ```MemoryError```
Solution: Allocate more random-access memory (RAM) to Python, decrease maximum *n*, or slice points.

# Contact
For help, improvements, etc., feel free to contact **silveryystar** on Discord.