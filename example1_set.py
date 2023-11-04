person={}

while True:
    name = input('My name is : ')
    age = input('My age is  : ')
    person[name]=age

    another = input('Would you like to add another?  y/n: ')
    if another == 'y':
        continue
    else : 
        break

ages = list(person.values())

for age in set(ages):
    count = ages.count(age)
    print(f'{age} years old - {count}')