"""@author: Manju Panthangi"""

import random

playerScore = 0
print(
    'Welcome to the game "ROCK PAPER SCISSOR".\n The rules of the game are as follows:-\n1-User have to enter their option\n2-If you win you get 10 points and if you loose 5 point will be deducted')


def rockpaperscissors():
    global playerScore
    game = ['rock', 'paper', 'scissor']
    ComputersChoice = random.choice(game)
    # print(s)
    PlayersChoice = input('Enter your choice among "rock","paper","scissor"\n').lower()
    print('computer generated:', ComputersChoice)
    if (PlayersChoice == 'scissor' and ComputersChoice == 'paper'):
        print('You won 10 points\n')
        playerScore = playerScore + 10
    elif (PlayersChoice == 'paper' and ComputersChoice == 'rock'):
        print('You won 10 points\n')
        playerScore = playerScore + 10
    elif (PlayersChoice == 'rock' and ComputersChoice == 'scissor'):
        print('You won 10 points\n')
        playerScore = playerScore + 10
    elif (PlayersChoice == ComputersChoice):
        print('Both are same i.e no one wins\n')
    else:
        print('You lost 5 point\n')
        playerScore = playerScore - 5


while (True):

    t = int(input('Do you want to play?\nChoose an option\n1:YES\n2:NO\n'))
    if (t == 1):
        rockpaperscissors()
    elif (t == 2):
        print('Your score is=', playerScore)
        exit()
    else:
        print('invalid input')
