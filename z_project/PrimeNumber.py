def checkPrime(number):
    '''This function checks for prime number'''
    isPrime = False
    if number == 2:
        print(number, 'is a Prime Number')
    
    if number > 2:
        for i in range(2, number):
            if number % i == 0:
                print(number, 'is not a Prime Number')
                break
            else:
                isPrime = True

        if isPrime:
            print(number, 'is a Prime Number')

if __name__ == '__main__':
    userInput = int(input("Enter a number to check if it's prime or not:"))
    checkPrime(userInput)
