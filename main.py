import random

full_options = {"R": "Rock", "P": "Paper", "S": "Scissors"}
options = ["R","P","S"]
cpu_count = 0
player_count = 0

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
	elif selected == "R" and computer_choice == "S":
		print("Player win!")
		player_count += 1
	elif selected == "S" and computer_choice == "P":
		print("Player win!")
		player_count += 1
	elif selected == "P" and computer_choice == "R":
		print("Player win!")
		player_count += 1
	else:
		print("CPU win!")
		cpu_count += 1
	print("SCORE: Player ({}) - CPU ({})".format(player_count, cpu_count))
	play_again = input("Want to play again? (Y= YES, N= NO):")
	if play_again.lower() != "y":
		break
print("Final Score: Player ({}) - CPU ({})".format(player_count, cpu_count))
print("Thanks for playing! Bye!")
