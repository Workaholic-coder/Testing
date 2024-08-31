#Multi-word Wordle Code
#opens a file
try:
    filename = input('Enter file name: ')
    file = open(filename, 'r')
    file_2 = file.read()
    file_1 = file_2.split()
except:
    print('Didn\'t work')