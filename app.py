# write 'hello world' to the console
print('hello world')
# Write  variables names option with the values (Rock, Scissors and Paper) 
# then a input names user from the consol that can be this variables again
# An a variable names computer with a random choice batwing option
# if user its not one of the option return option invalid 
# the cane of returns depend of the wine of the game
# La Rock gana a las tijeras.
# Las Scissors ganan al papel.
# El Paper gana a la piedra.
# if user its one of the option return the option that the computer choose and the result of the game
# if the computer and the user choose the same option the result its a draw
# if the user wins return 'You win'
# if the computer wins return 'You lose'
# if the user choose invalid option return 'Invalid option'

import random
options = ['Rock', 'Scissors', 'Paper']
user = input('Enter your option: ')
computer = random.choice(options)
if user not in options:
    print('Invalid option')
elif user == computer:
    print(f'Computer: {computer}')
    print('Draw')
elif user == 'Rock' and computer == 'Scissors':
    print(f'Computer: {computer}')
    print('You win')
elif user == 'Scissors' and computer == 'Paper':
    print(f'Computer: {computer}')
    print('You win')
elif user == 'Paper' and computer == 'Rock':
    print(f'Computer: {computer}')
    print('You win')
else:
    print(f'Computer: {computer}')
    print('You lose')

# add a question if you want to play again
# and if the answer is yes repeat the game
# and if the answer is no finish the game
# and count the number of games that the user wins
# and print the number of games that the user wins
games = 0
wins = 0
while True:
    options = ['Rock', 'Scissors', 'Paper']
    user = input('Enter your option: ')
    computer = random.choice(options)
    if user not in options:
        print('Invalid option')
    elif user == computer:
        print(f'Computer: {computer}')
        print('Draw')
    elif user == 'Rock' and computer == 'Scissors':
        print(f'Computer: {computer}')
        print('You win')
        wins += 1
    elif user == 'Scissors' and computer == 'Paper':
        print(f'Computer: {computer}')
        print('You win')
        wins += 1
    elif user == 'Paper' and computer == 'Rock':
        print(f'Computer: {computer}')
        print('You win')
        wins += 1
    else:
        print(f'Computer: {computer}')
        print('You lose')
    games += 1
    play_again = input('Do you want to play again? (yes/no): ')
    if play_again == 'no':
        break
print(f'You win {wins} of {games} games')
