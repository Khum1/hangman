
guess = input('Enter a letter: ')

while len(guess) != 1 or guess.isalpha() == False:
    print("Invalid letter. Please enter a single alphabetical character.")
    guess = input('Enter a letter: ')
