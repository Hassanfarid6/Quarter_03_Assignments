
words = [
    "apple", "banana", "python", "rocket", "guitar", "orange", "flower", "silver", "planet", "tiger",
    "elephant", "pineapple", "avengers", "sunshine", "umbrella", "dinosaur", "hospital", "football", "backpack", "mountain",
    "watermelon", "chocolate", "blueberry", "butterfly", "kangaroo", "adventure", "motorcycle", "television", "university", "playground",
    "microscope", "skyscraper", "basketball", "lighthouse", "notebook", "handkerchief", "experiment", "encyclopedia", "vocabulary", "xylophone",
    "hippopotamus", "aeroplane", "submarine", "chandelier", "binoculars", "architecture", "photography", "constellation", "firefighter", "chameleon"
]

import random
import string

def get_vaid_word(words):
  word = random.choice(words)
  while '_' in word or ' ' in word:
    word = random.choice(words)
  return word.upper()

def hangman():
  word = get_vaid_word(words)
  word_letters = set(word)
  alphabet = set(string.ascii_uppercase)
  used_letters = set()

  lives = 6

  while len(word_letters) > 0 and lives > 0:

    print('You have used these letters: ', ' '.join(used_letters))

    word_list = [letter if letter in used_letters else '_' for letter in word]
    print('Current word: ', ' '.join(word_list),"\n")

    user_letter = input('Guess a letter :').upper()
    if(user_letter) in alphabet -used_letters:
      used_letters.add(user_letter)
      if user_letter in word_letters:
        word_letters.remove(user_letter)
      else:
        lives -= 1
        print("\nLetter is not in word\n")
    elif user_letter in used_letters:
      print('You have already used that character. Please try again')
    else:
      print('Invalid character. Please try again')

  if lives == 0:
    print('You died, sorry. The word was', word)
  else:
    print('You guessed the word', word, '!!')

hangman()