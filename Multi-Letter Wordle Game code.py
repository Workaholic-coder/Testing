#Multi-word Wordle Code
#opens a file
try:
    filename = input('Enter file name: ')
except:
    print('Didn\' t work')
else:
    file = open(filename, 'r')
    file_2 = file.read()
    file_1 = file_2.split()