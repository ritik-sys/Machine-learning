def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def multiply(a, b):
    return a*b


def divide(a, b):
    return a//b


# this part will only be executed when we run simple.py
# means when we export this file this part wont be running
if __name__ == '__main__':
    print('hello')
    a = int(input())
    b = int(input())
    print(a+b)
