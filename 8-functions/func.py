def greet_user():
        """Display a simple Greeting"""
        print("Hello")

def count_to10():
    """Count to 10 and print each number"""
    numberx = 0
    while numberx < 10:
        numberx += 1
        print(numberx)

def fav_game(game):
    """Ask for a game and print it"""
    print("\nyour fav game is: " +game)


greet_user()
count_to10()
game2 = input("What is your fav game?")
fav_game(game2)
