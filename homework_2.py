import random
import re


def the_game(i, s, l):
    while i != 0:
        b = input(f'Try number {range(l + 1)[l - i + 1]}.  Enter any number from 1 to 99: ')
        i -= 1
        if s == int(b):
            print(f'You are really the lucky men! the secret number is: {s}')
        else:
            if i >= 1:
                if int(b) > s:
                    print(f'He-he! Your choice is not correct, the secret number is smaller than {b}. '
                          f'Try once more again.')
                    the_game(i, s, l)
                else:
                    print(f'He-he! Your choice is not correct, the secret number is bigger than {b}. '
                          f'Try once more again.')
                    the_game(i, s, l)
            else:
                print(f'Sorry, but you didn\'t guess. The secret number was {s}')
        return


print("You need to guess the secret number",
      "You can choose one of three difficulty levels",
      "easy - you will have 12 tries to guess",
      "medium - you will have 9 tries to guess",
      "hard - you will have 6 tries to guess", sep='\n')
game_type = ""
while not re.search(r"[1-3]", game_type):
    game_type = input("So, what is your choice stranger (enter the number of level)? \n1 - easy, 2 - medium, 3 - hard\nMy choice is: ")

level = [12, 9, 6]
cnt = level[int(game_type) - 1]

secret = random.randint(1, 99)
#print(secret)
the_game(cnt, secret, cnt)










