import spiderDraw as sd
import time, os
import functions as md

correct = []  #List of correct letters guessed
incorrect = []  #List of incorrect letters guessed
tries = 0   #Number of incorrect guesses
game = True
spiderList = [sd.spider_0, sd.spider_1, sd.spider_2, sd.spider_3, sd.spider_4, sd.spider_5, sd.spider_6]

md.introduction()   #Prints intro text to console
word = md.generate_word()  #Choses word from random list

while game:
  progress = ""
  tries = md.check_word(correct, incorrect,word, tries)
  time.sleep(1)
  os.system('clear')
  progress = md.print_word(word,correct)
  print(f'Word = {progress}')
  md.print_spider(tries,spiderList)
  print(f'Incorrect Guesses = {incorrect}')
  if "_" not in progress:
    print("Congrats, you won!")
    game = False
  elif tries > 5:
    print("The spider has devoured you!")
    game = False
  