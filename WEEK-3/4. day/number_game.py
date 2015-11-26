import random
def get_int():
    number=int(input ("Enter an integer: "))
    return number

number_to_guess = random.randint(0, 10)
number_of_guesses=5

while number_of_guesses > 0:
    try:
        guess = get_int()
    except ValueError:
        print("Your entered a wrong value")
    else:
        if guess == number_to_guess:
            print("You won.")
            break
        elif guess > number_to_guess:
            print ("Your number is too high.")
            number_of_guesses-=1
            print("You have %d more life." % number_of_guesses)
        elif guess < number_to_guess:
            print ("Your number is too small.")
            number_of_guesses-=1
            print("You have %d more life." % number_of_guesses)

if number_of_guesses == 0:
    print("You lost. The correct answer %d." % number_to_guess)
