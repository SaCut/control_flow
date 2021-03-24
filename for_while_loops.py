# for loops

shopping_list = ["bread", "eggs", "milk", "orange"]
shopping_dictionary = {
	"bread": 1,
	"eggs": 12,
	"milk": 1,
	"orange": 10
}

# # the non-loop way
# print(shopping_list[0])
# print(shopping_list[1])
# print(shopping_list[2])
# print(shopping_list[3])

# # with for loop
# for i in shopping_list:
# 	print(i)

# # a foor loop can iterate through any list of elements
# for i in "string":
# 	print(i)

# for i in shopping_dictionary:
# 	print(i)

# for i in shopping_dictionary.values():
# 	print(i)

# # break will stop the loop
# for i in shopping_list:
# 	if i == "milk":
# 		print("found the milk")
# 		break
# 	else:
# 		print("not milk")

food_bill = {
	1: {"name": "James", "bill": "£1"},
	2: {"name": "Bond", "bill": "£2"},
	3: {"name": "Shah", "bill": "£3"}
}

# for i in food_bill.values():
# 	print(i)

# exercise
# print the name and the bill amount for each person
for i in food_bill.values():
	print("name:", i["name"] + ",", "bill:", i["bill"])
