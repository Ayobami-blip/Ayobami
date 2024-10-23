from random import randint

answer = randint(0, 50)
count = 0

while count < 3:
    guess = input('Guess a number between 0 and 50: ')
    try:
        if int(guess) == count:
            print('You got the answer right')
            break
        else:
            if count == 2:
                print('You Loose')
            else:
                print('Wrong try again')
            count += 1
            print(f"You have guessed {count} times")
    except ValueError:
        print('Pls enter number only')
print('Game over')