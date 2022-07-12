from helpers.game import play_game


def menu():
    print("Menu: \n[1] Start a new game.")
    print("[2] Exit.")


menu()
option = int(input("Please choose one of the options from the menu: "))

if option == 1:
    print("Game started.")
    play_game()
else:
    print("Exiting game.")
