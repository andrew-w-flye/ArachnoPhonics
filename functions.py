import random

# Prompts user for guess. Checks through the word to see if it contains the letter guessed by the user. Returns the number of wrong guesses
def check_word(correct, incorrect, word, tries):
  guess = input("Guess a letter: ").lower()
  
  if len(guess) != 1 or not guess.isalpha():
    print("Please enter a single letter")
    check_word(correct,incorrect,word,tries)
  elif guess in incorrect or guess in correct:
    print('You already guessed that!')
    check_word(correct,incorrect,word,tries) 
  elif guess in word:
    correct.append(guess)
    print("Nice! The letter is there\n")
  else:
    incorrect.append(guess)
    tries += 1
    print("Uh oh, that was wrong\n")
  return tries

# Returns the word to the console containing "_" for any letter not guessed by the user.
#Takes in the correct word and the list of correct guesses as parameters
def print_word(word,correct):
  progress = ""
  for character in word:
    if character in correct:
      progress = progress + character
    else:
      progress = progress + "_"
  return progress

# Prints spider from the spider drawing functions in the spiderDraw.py file. Takes the number of wrong guesses and the list of spider drawing functions as parameters.

def print_spider(tries,spiderList):
  spiderList[tries]()

def introduction():
  print("Welcome to ArachnoPhonics!\n")
  playerName = input("What is your name? ")
  print(f"\n{playerName}, your goal is to guess the word, letter by letter\n")
  print("Don't let the spider get you!\n")

def generate_word():
  wordList = open("words.txt").read().split()
  word = random.choice(wordList)
  print('Word = ' + "_"*len(word))
  return word