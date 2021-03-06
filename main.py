import random

full_options = {"R": "Rock", "P": "Paper", "S": "Scissors"}
options = ["R","P","S"]

print("Welcome to Rock, Paper, Scissors!")
print("R = Rock, P = Paper, S = Scissors")

while True:
	while True:
		selected = input("Choose your weapon: R, P, S: ").upper()
		if selected in options:
			break
		else:
			print("You must choose R, P, or S")
			continue

	computer_choice = random.choice(options)
	print("Player ({}) : CPU ({})".format(full_options[selected],full_options[computer_choice]))
	if selected == computer_choice:
		print("It's a tie!")
		continue
	elif selected == "R" and computer_choice == "S":
		print("Player win!")
	elif selected == "S" and computer_choice == "P":
		print("Player win!")
	elif selected == "P" and computer_choice == "R":
		print("Player win!")
	else:
		print("CPU win!")
	play_again = input("Want to play again? (Y= YES, N= NO):")
	if play_again.lower() != "y":
		break

