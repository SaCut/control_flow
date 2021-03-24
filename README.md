# Control flow
- Control flow is used to exectute a block of code according to specific conditions

#### If statement
- The syntax of an if statement is:
```python
if condition:
	some_code
```
- If the condition is true, the program will execute the code, otherwise it will skip it

#### Elif statement
- If the first condition wasn't met, it's possible to check for another condition with `elif`
- The syntax for elif is:
```python
elif condition:
	some code
```

### Else statement
- The else statement executes some code if none of the conditions previosuly specified are true
- The syntax is:
```python
else:
	some_code
```

### Control Flow loops
- Loops are used to iterate over some given block of code
- There are two kinds of loops in Python, `for` and `while`
- Among others, loops have two methods called 'break' and 'continue'. Break interrupts the loop and tells the interpreter to execute any code that comes after, while continue intterupts the current iteration of the loop to move to the successive one

#### For loops
- `for` loops iterate over a set of values, using a range function (a function that returns a list of elements)

#### While loops
- `while` loops iterate until a boolean condition is met, the condition being dependent on some value that is changed inside the loop.
