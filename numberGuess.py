import random 

guessCount = 0

print("Hello, this is a game where you guess what number I am thinking of.")

number = random.randint(1,10)
print("I am thinking of a number between 1 and 10 can you guess it? You have 5 guesses so use them wisely!")

while guessCount < 5:
    print("Guess my number!")
    guess = input()
    guess = int(guess)

    guessCount = guessCount + 1

    if guess < number:
        print("this guess is too low")

    if guess > number:
    	print("this guess is too high")

    if guess == number:
    	print("Correct!")
    	break

if guess != number:
		number = str(number)
		print("No the right number was: " + number)

