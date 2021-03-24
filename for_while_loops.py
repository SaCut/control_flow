# for loops

# shopping_list = ["bread", "eggs", "milk", "orange"]
# shopping_dictionary = {
# 	"bread": 1,
# 	"eggs": 12,
# 	"milk": 1,
# 	"orange": 10
# }

# # the non-loop way
# print(shopping_list[0])
# print(shopping_list[1])
# print(shopping_list[2])
# print(shopping_list[3])

# # with for loop
# for item in shopping_list:
# 	print(item)

# # a foor loop can iterate through any list of elements
# for letter in "string":
# 	print(letter)

# for item in shopping_dictionary:
# 	print(item)

# for i in shopping_dictionary.values():
# 	print(i)

# # break will stop the loop
# for item in shopping_list:
# 	if item == "milk":
# 		print("found the milk")
# 		break
# 	else:
# 		print("not milk")

# food_bill = {
# 	1: {"name": "James", "bill": "£1"},
# 	2: {"name": "Bond", "bill": "£2"},
# 	3: {"name": "Shah", "bill": "£3"}
# }

# for i in food_bill.values():
# 	print(i)

# # exercise
# # print the name and the bill amount for each person
# for person in food_bill.values():
# 	print(f"name: {person['name']}, bill: {person['bill']}")

# # nested loop
# for person in food_bill.values():
# 	for name, bill in person.items():
# 		print(f"{name}'s bill amount is {bill}")


# while loops
num = 0

while num < 10:
	print(f"it's working! --> {num}")
	if num == 4:
		break # stops the while loop if the condition is met
	num += 1
