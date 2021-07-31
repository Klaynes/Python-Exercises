#hangman = [" O", "/|\\", " |", " |", "/ \\"]
#####################Unfinished and pretty useless code, just setting up the github and making sure it is working for forum posts.
import random
import copy


def replacements(guess, word, word_as_dashes, list_of_indexes):
    while guess in word:
    	print(f"while guess in word 1: ***guess:{guess} ***word:{word} ***:{word_as_dashes} ***{list_of_indexes}")

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

def in_word(guess, word):
	if guess in word:
		return 1
	if guess not in word:
		return 0

def ask_player():
	guess = input("Pick a letter: ")
	return guess

def get_word():
	with open("sowpods.txt", "r") as f:
		lines = f.readlines()
		return list(lines[random.randint(1, len(lines))].strip().lower())


word = list(get_word())
print(word)
word_as_dashes = list("_" * len(word))
letters_guessed_right = set()
letters_guessed_wrong = set()
turn = 1
guess = ask_player()
in_word = in_word(guess, word)
if in_word == 1:
	print("if in_word == 1:")
	list_of_indexes = where_in_word(guess, word)
	print("where in word complete")
	if list_of_indexes:
		print("if list of index not empty")
		print(word)
		print(word_as_dashes)
		word_and_word_as_dashes = replacements(guess, word, word_as_dashes, list_of_indexes)
		word = word_and_word_as_dashes[0]
		word_as_dashes = word_and_word_as_dashes[1]
		print("****************************************")
		print(word)
		print("****************************************")
		print(word_as_dashes)		

else:
	wrong_letter()




						
