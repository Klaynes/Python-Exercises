import random
import copy
missed = 0


def wrong_letter():
	hangman = [" O", "/|\\", " |", " |", "/ \\"]
	for i in range(missed):
		print(hangman[i])

def replacements(guess, word, word_as_dashes, list_of_indexes):
    while guess in word:
    	index_to_change = list_of_indexes.pop()
    	word[index_to_change] = "_"
    	word_as_dashes[index_to_change] = guess

    return [word, word_as_dashes]

def where_in_word(guess, word):
    list_of_indexes = []
    temp_word = copy.deepcopy(word)
    while guess in temp_word:
        index_number = temp_word.index(guess)
        list_of_indexes.append(index_number)
        temp_word[index_number] = "_"
        if guess not in temp_word:
            return list_of_indexes
            break

def ask_player():
	guess = input("Pick a letter: ")
	return guess

def get_word():
	with open("sowpods.txt", "r") as f:
		lines = f.readlines()
		return list(lines[random.randint(0, len(lines)-1)].strip().lower())
game_on = True
word = list(get_word())
print(word)
word_as_dashes = list("_" * len(word))
letters_guessed = set()

while game_on == True:
	if "_" not in word_as_dashes:
		print("Thats it! You saved him!")
		break		
	guess = ask_player()
	if guess in letters_guessed:
		print("You already used that letter!")
	if guess in word:   #	in_word = in_word(guess, word)
		letters_guessed.add(guess)
		list_of_indexes = where_in_word(guess, word)
		if list_of_indexes:
			word_and_word_as_dashes = replacements(guess, word, word_as_dashes, list_of_indexes)
			word = word_and_word_as_dashes[0]
			word_as_dashes = word_and_word_as_dashes[1]
		print(word_as_dashes)		
		
	else:
		missed += 1
		if missed == 5:
			print("You lose! Poor guy!")
			game_on = False
		letters_guessed.add(guess)
		wrong_letter()
				