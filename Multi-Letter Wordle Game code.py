#Multi-word Wordle Code
#opens a file
try:
    filename = input('Enter file name: ')
    file = open(filename, 'r')
    file_2 = file.read()
    file_1 = file_2.split()
except:
    print('Didn\'t work')

list = list()
for words in file_1:
    list,append(words)

#importing random a word form the selected file
import random
random_word = random.choice(list)