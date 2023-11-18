# with open ('./about.txt', 'w') as file:
#     file.write('My name is Paing Thet.')

# with open ('./about.txt', 'a') as file:
#     file.write('\nI am 21 years old.')

list = ['My name is Paing Thet Ko.', '\nI am 21 years old.']
with open ('./about.txt' , 'a') as file :
    file.writelines(list)