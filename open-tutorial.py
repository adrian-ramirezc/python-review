# File_object = open('filename, 'mode')

# mode:
# 'r' read data from a file
# 'w' write data into a file / overwrite data if existed
# 'a' append data to a file
# 'r+' read or write mode
# 'a+' read or

print('Way 0: We need to manually close the file')
Filename_with_fullpath = r"C:\Users\adrian\Desktop\git\dima\openTutorial\sample.txt"
File_object = open(Filename_with_fullpath, 'r')
print(File_object.read())
File_object.close() 
print('')

# Way 1
print('Way 1')
with open('sample.txt', 'r') as File_object: 
    print(File_object.read())
    print('')

# Way 2
print('Way 2')
with open('sample.txt', 'r') as File_object: 
    print(File_object.readlines())
    print('')

# Way 3
print('Way 3')
with open('sample.txt', 'r') as File_object: 
    for line in File_object:
        print(line)
    print('')