file = open('./text.txt') #open the file

for line in file: #read with FOR LOOP
    print(line)

file.close() # close file, if not, program performance could reduce