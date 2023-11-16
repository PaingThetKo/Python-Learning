file = open('./text.txt') #open the file

# for line in file: #read with FOR LOOP
#     print(line)
# file.seek(0) # start read file from start(0), if not, program at end of line and will continue with nothing
# linelist = file.readline() # readline function
# print(linelist)

file.seek(22)              # read from 10th word
paragraph = file.read(37)  # read until 20th word
print(paragraph)

file.close() # close file, if not, program performance could reduce