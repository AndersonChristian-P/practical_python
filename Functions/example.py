def hello():
    print('Howdy!')
    print('Howdy!!')
    print('Hello There!!!')

hello()
hello()
hello()


def hi(name):
    print('Hello ' + name)

hi('Alice')
hi('Bob')


def number(word):
    print(word + ' has ' + str(len(word)) + ' letters in it.')

number('hello')
number('Carl')


def plusOne(number):
    return number + 1
newNumber = plusOne(5)
print(newNumber)
