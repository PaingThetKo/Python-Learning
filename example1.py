person={}

while True:
    name = input('Your name is: ')
    age = input('Your age is : ')
    person[name]=age

    another = input('Would you like to add another?  y/n: ')
    if another == 'y':
        continue
    else : 
        break

for (key,value) in person.items():
    print(f'{key} is {value} years old.')