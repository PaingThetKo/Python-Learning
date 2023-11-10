def greet(fun):
    def wrapper(name):
        print('My name is :')
        fun(name)
        print('Nice to meet you.')
    return wrapper

@greet
def sayname(name):
    print(name)
sayname('Paing Thet Ko.')