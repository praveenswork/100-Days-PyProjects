import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


ran_words=["plant","money","work","bar","click","kitkat","zebra"]               #random words
chosed_word=random.choice(ran_words)

print(chosed_word)
print(f"The given word is {len(chosed_word)} ")



display=[]
word_len=len(chosed_word)

for i in range(word_len):
    display+="_"
print(display)

endgame=False
lives=6

while not endgame:
    guess=input("Guess the word:\n").lower()#user input
    for position in range(word_len):
        letter = chosed_word[position]
        if letter==guess:
            display[position]=letter

    if guess not in chosed_word:
        lives-=1
        if lives==0:
            endgame=True
            print("\n\n\n\t\t\tYou Lose")
    print(f"{' '.join(  display)}")
    

    if "_" not in display:
        endgame=True
        print("\n\n\n\t\t\tYou Win")

    print(stages[lives])
        


                                                                                 

