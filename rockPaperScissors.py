# Rock Paper Scissors
from random import randrange

print("Welcome to Rock, Paper, Scissors")
game_chars = {1: {"Rock": "Its a tie", "Paper": "You lost", "Scissors": "You win"},
              2: {"Paper": "Its a tie", "Scissors": "You lost", "Rock": "You win"},
              3: {"Scissors": "Its a tie", "Rock": "You lost", "Paper": "You win"}}
print(f"\nGame rules:\n")
for x in game_chars:

    print(f"{list(game_chars[x].keys())[0]}({x}) --V/S-- {list(game_chars[x].keys())[2]}-------->"
          f"{list(game_chars[x].keys())[0]} Wins!")


game_value = True
username = str(input("\nPlease Enter Your Name: ")).capitalize()

game = input(f"\nHello {username} Do you wanna play? Y/N\n").capitalize()

for x in game_chars:
    print(f"For --{list(game_chars[x].keys())[0]}-- Press {x}")
if game == "Y":
    while game_value is True:

        jonny_number = False
        player_input = input("Choose your player: \n")
        while jonny_number is False:
            if player_input.isdigit():
                player_input = int(player_input)
                if player_input in range(1, 4):
                    jonny_number = True
                else:
                    player_input = input("Wrong Key. Enter a valid choice:\n")
            else:
                player_input = input("Wrong Key. Enter a valid choice:\n")
                continue

        print("Computer Turn...\n")
        pc_number = randrange(1, 4)
        pc_number = list(game_chars[pc_number].keys())[0]
        print(f"Your choice is: {list(game_chars[player_input].keys())[0]}\nComputer Choice is: {pc_number}")
        print(list(game_chars[player_input].keys())[0], "V//S", pc_number)
        print(f"{game_chars[player_input][pc_number]} , {username}\n")
        if list(game_chars[player_input].keys())[0] == pc_number:
            continue
        else:
            continue_game = input("Play again? Y/N\n").capitalize()
            if continue_game == "Y":
                game_value is True
            else:
                print("\nAdios")
                exit()

else:
    print("\nAdios amigo")
    exit()
