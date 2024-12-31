#Multi-word Wordle Code
x = 0
#opens a file
while x == 0:
    try:
        filename = input('Enter file name: ')
        file = open(filename, 'r')
        file_2 = file.read()
        file_1 = file_2.split()
        x = x + 1
    except:
        print('Didn\'t work')

list = list()
for words in file_1:
    list.append(words)

#importing random a word form the selected file
import random
random_word = random.choice(list)

list_2 = list((random_word, random_word.upper(), random_word[0].upper() + random_word[1:], random_word.lower()))
 