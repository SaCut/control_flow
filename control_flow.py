# control flow

# conditional statements are used to control the flow of a program

# age = 15

# # if the user is above the age of fifteen, allow them to buy tickets
# if age >= 15:
# 	print("Thank you, please proceeed to your purchase")
# # otherwise, if the age is below 15, don't allow the purchase
# elif age < 15:
# 	print("You're not a man, youre three kids in a trenchcoat!")
# # if neither is true, display an error message
# else:
# 	print("Oops, something went wrong, please try again later")

# for loops and while loops

# Exercise -
# As a user I would like to sell tickets according the age of the user
# and category of the movie -
# age = 12a, PG, U, 15 and 18
# user input to let us know the age to decide whether to sell the ticket or not
# casting implemented
# display the age back to the user with appropriate message

user_age = input("How old are you? ")
user_age = int(user_age)

free_purchase = "Thank you, please proceed to the purchase."
too_young = "Sorry, you're not old enough to purchase this ticket."
error_message = "We're sorry, something went wrong. Please try again later."

movie = "PG"

if movie == "18":
	if user_age >= 18:
		print(free_purchase)
	elif user_age < 18:
		print(too_young)
	else:
		print(error_message)
if movie == "15":
	if user_age >= 15:
		print(free_purchase)
	elif user_age < 15:
		print(too_young)
	else:
		print(error_message)
if movie == "12":
	if user_age >= 12:
		print(free_purchase)
	elif user_age < 12:
		print(too_young)
	else:
		print(error_message)
if movie == "U":
	print(free_purchase)
else:
	print(error_message)