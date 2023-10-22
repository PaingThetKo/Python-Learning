# def greet(name):
#     print(f'Good Morning, {name}');
# greet('Paing Thet Ko');
# greet('Kyaw Kyaw');

# def greet(time, name):
#     print(f'Good {time}, {name}');
# greet('Morning', 'Paing Thet Ko');

def greet(name="Paing Thet Ko",time='Evening'):
    print(f'Good {time}, {name}');
greet(name='Kyaw Kyaw', time='Morning');
greet(name='Aung Aung', time='Night');

