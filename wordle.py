
# 1. Pick a random word from a list of words (ideally a super large list/dictionary)
# 2. Prompt the user for a 5-letter word and validate
#     a. lowercase the input word
#     b. Make sure there are only letters.
#     c. Make sure the guessed_word is only 5 characters long.
#     d. Enhancement - Make sure the guessed_word is a valid word.
# 3. Compare the guessed_word with the secret_word.
#     a. If the guessed_word equals the secret_word then they win! Game Over!
#     b. else If the letter is in the same spot in both guessed_word and the secred_word then color it Green.
#     c. else If the letter from guessed_word is in secred_word then color it Yellow.
#     d. else color it normal (black/white).
#     e. Print the colored word (and eventually previous guesses)
# 4. If the guess wasn't correct then we let the guess again and decrease their remaining attempts.