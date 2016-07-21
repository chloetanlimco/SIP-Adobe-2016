number = 79

guess = input("Guess my favorite number. ")

while number != int(guess):
	if number > int(guess):
		print("Your guess was too low.")
		guess = input("Try again. ")
	else:
		print("Your guess was too high.")
		guess = input("Try again. ")

if number == int(guess):
	print("You guessed it right!")

print("Game Over.")