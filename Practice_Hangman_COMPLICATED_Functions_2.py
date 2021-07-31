import random
import copy
missed = 0

# Sent here when the wrong letter is guessed
def wrong_letter():
	# The list containing the elements of the 'hanged man'
	hangman = [" O", "/|\\", " |", " |", "/ \\"]
	# prints out the hangman list to the index relative to the 'missed' variable
	for i in range(missed):
		print(hangman[i])

# Does all of the replacing dashes w/ characters and characters w/ dashes. Called after 'where_in_word' does its thing
def replacements(guess, word, word_as_dashes, list_of_indexes):
	# While the guessed letter is still in the word...
    while guess in word:
    	# Using the list of indexes given to it by 'where_in_word', pop 1 element out at a time and use as index
    	index_to_change = list_of_indexes.pop()
    	# Change the letter in the word to a _ so it can move on to the next occurance of the letter if multiple exist
    	word[index_to_change] = "_"
    	# Change a _ in the word shown to players to keep them aware of the correct guesses so far
    	word_as_dashes[index_to_change] = guess
    # return the word (it now has _'s where a letter used to be) and word_as_dashes (it's _'s are now letter(s)) 	
    return [word, word_as_dashes]

# Finds where in the word the correct letters appear
def where_in_word(guess, word):
	# Create an empty list to eventually hold the indexes of the letters guessed correctly for that turn
    list_of_indexes = []
    # So as not to change 'word' permanently during this search, deepcopy is used b/c 'word' needs to be sent to
    # replacements exactly the same as it was when it entered here.
    temp_word = copy.deepcopy(word)
    # while the guess is still in the 'word'. (they will be replaced with _'s in this copy so that .index can find the next
    # occurance of that letter if there are multiple occurances)
    while guess in temp_word:
    	# Finds the index # of the 1st occurance of the guessed letter.
        index_number = temp_word.index(guess)
        # Start adding the index(es) to the list of index. These will be needed by the 'replacements' function
        list_of_indexes.append(index_number)
        # Replace the letter with a _ after it's index has been logged
        temp_word[index_number] = "_"
        # When it has caught all occurances of the guessed letter, it can move on.
        if guess not in temp_word:
        	# Return the list_of_indexes we created
            return list_of_indexes
            break

# Ask player for a letter
def ask_player():
	guess = input("Pick a letter: ")
	return guess

# Pull a random word from the file
def get_word():
	with open("sowpods.txt", "r") as f:
		lines = f.readlines()
		return list(lines[random.randint(0, len(lines)-1)].strip().lower())
# Start the main portion of the active program and set flag to use when the game is won or lost
game_on = True
word = list(get_word())
# Prints out the word for testing purposes. Delete if this were not just an exercise.
print(word)
# Creates a row or list of _'s that the player player can see to know what the word evolves into 
word_as_dashes = list("_" * len(word))
# Show player that evolving word as they guess correct letters
print(word_as_dashes)
# A set to place the letters that have already been guessed.
letters_guessed = set()
while game_on == True:
	# Number of turns left
	left = 5 - missed
	# If no _'s are left in 'word_as_dashed' then they have all been guessed correctly. Game won.
	if "_" not in word_as_dashes:
		print("Thats it! You saved him!")
		break
	print(f"You have {left} guesses left!")		
	guess = ask_player()
	if guess in letters_guessed:
		print("You already used that letter!")
		missed -= 1
	# If you have guessed correctly
	if guess in word:
		# Add guess to list of letters already guessed
		letters_guessed.add(guess)
		# Find where in the word those letters exist
		list_of_indexes = where_in_word(guess, word)
		if list_of_indexes:
			# Retrieve the tuple containing the 2 variables returned by the 'replacements' function
			word_and_word_as_dashes = replacements(guess, word, word_as_dashes, list_of_indexes)
			# Assign the 2 variables using their index position within the tuple
			word = word_and_word_as_dashes[0]
			word_as_dashes = word_and_word_as_dashes[1]
		# Print out 'word_as_dashes' so player can see their progress
		print(word_as_dashes)		
	# Bad times for mr. guy.
	else:
		missed += 1
		if missed == 5:
			print("You lose! Poor guy!")
			game_on = False
		letters_guessed.add(guess)
		wrong_letter()
				