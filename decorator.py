def greet(fun):
    def wrapper():
        print('My name is :')
        fun()
        print('Nice to meet you.')
    return wrapper

@greet
def sayname():
    print('Paing Thet Ko.')
sayname()