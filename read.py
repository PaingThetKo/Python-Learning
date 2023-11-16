file = open('./text.txt') #open the file

for line in file: #read with FOR LOOP
    print(line)

file.seek(0) # start read file from start(0), if not, program at end of line and will continue with nothing

linelist = file.readline()
print(linelist)

file.close() # close file, if not, program performance could reduce