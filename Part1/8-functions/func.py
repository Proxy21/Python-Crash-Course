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

def add_two_numbers(number1, number2):
    """return number1 and 2 added"""
    number3 = number1 + number2
    return number3


greet_user()
count_to10()
game2 = input("What is your fav game?")
fav_game(game2)
nu = add_two_numbers(5,3)
print(nu)
