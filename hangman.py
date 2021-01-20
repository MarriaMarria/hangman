#!/usr/bin/env python3

import logging
import random
import requests as req
import urllib.request

logging.info("creating list with ascii art for hangman: start")

hangman_art = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
logging.info("creating list with ascii art for hangman: start")


hangman_art.reverse()
#logging configuration
logging.info("logging configuration: start")
logging.basicConfig(filename='hangman_log.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
logging.info("logging configuration: end")

#accessing the list from the internet
logging.info("checking if site we get words from is working properly: start")
if urllib.request.urlopen("http://www.mit.edu/~ecprice/wordlist.10000").getcode() != 200:
    f = open("words.txt", "r")
    new_list = f.read()
    word_list = new_list.split(",")
    logging.info("checking if site we get words from is working properly: end")
else:
    logging.info("accessing the list from the internet: start")
    resp = req.get("http://www.mit.edu/~ecprice/wordlist.10000")
    logging.info("accessing the list from the internet: end")

    list_of_words = resp.content #reponse en bytes

    reply = list_of_words.decode('utf-8') #transformer le type byte de content en string
    word_list = reply.split("\n") #transforming in list
    # print(word_list)

#hangman art




#choosing random word
logging.info("choosing a random word from the list: start")
chosen_word = random.choice(word_list)
print(chosen_word)


# printing _ for each letter in chosen_word
guess_list = []
for letter in range(len(chosen_word)):
    guess_list.append("_")

print(guess_list)


logging.info("choosing a random word from the list: start")

# condition for end of game
end_of_game = False
life = 6

while end_of_game == False: # while we have lives left

    guess = input("\nPlease guess a letter\n")
    logging.info("going throw our random word and checking if the letter is there, if it is we replace _ with the guess letter: start")
    hangman_art[life]
    if guess in chosen_word:
      print(f"You guessed {guess}. Good job! Guess another letter!")

    ki = 0 #compteur i                      # we walk throw our word and check if we guessed the letter
    for i in chosen_word:                   # and we change the _ with guessed letter
        if guess == i:                      # 
            guess_list[ki] = guess          #
                                            #
        ki += 1
    print(guess_list)
    if not "_" in guess_list:
      print("You guessed the word! You won!")
      break


    
    if guess not in chosen_word:

      life = life - 1
      print(f"You guessed wrong! You have {life} lives left")
      print(hangman_art[life])
      
      print(guess_list)

      if life == 0:
        print("You lost")
        end_of_game = True #we quit the boucle

        # logging.info("going throw our random word and checking if the letter is there, if it is we replace _ with the guess letter: start")






# if guess in chosen_word:




