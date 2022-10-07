from milestone_1 import word, word_list

guess_1 = input('Enter a letter: ')

while len(guess_1) != 1 or guess_1.isalpha() == False:
    print("Invalid letter. Please enter a single alphabetical character.")
    guess_1 = input('Enter a letter: ')

chosen_word = (word(word_list))

