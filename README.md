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
- `for` loop syntax is:
```python
for item in iterable_element:
	some_code
```

##### exercises
- We used loops to iterate through a shopping list:
```python
shopping_list = ["bread", "eggs", "milk", "orange"]

# the non-loop way
print(shopping_list[0])
print(shopping_list[1])
print(shopping_list[2])
print(shopping_list[3])

# with for loop
for item in shopping_list:
	print(item)
```

- We used `break` to interrupt a for loop:
```python
for item in shopping_list:
	if item == "milk":
		print("found the milk")
		break
	else:
		print("not milk")
```


- We iterated through a dictionary:
```python
food_bill = {
	1: {"name": "James", "bill": "£1"},
	2: {"name": "Bond", "bill": "£2"},
	3: {"name": "Shah", "bill": "£3"}
}

# print the name and the bill amount for each person
for person in food_bill.values():
	print(f'name: {person["name"]}, bill: {person["bill"]}')
```

#### While loops
- `while` loops iterate until a boolean condition is met, the condition being dependent on some value that is changed inside the loop.
- `while` loops are used instead of `for` when the cone needs to be iterated over not a set amount of times, but until a certain condition is met
- `while` syntax is:
```python
while condition_is_true:
	some_code
	# the execution stops when the condition becomes false
```

