import random

def guess():
    ''' This function guesses the randomly generated number '''
    randomNumber = random.randint(0, 21)
    cnt = 0 

    while True:
        cnt += 1 
        number = int(input('Enter the number between 0 to 20: '))
        if number < randomNumber:
            print('Too small')
        elif number > randomNumber:
            print('Too large')
        else:
            print('You have got it in', cnt, 'tries')
            break

if __name__ == '__main__':
    guess()