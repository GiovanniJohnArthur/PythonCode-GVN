# print('hi')
# print(__name__)


def display(name):
    return name


def do_something():
    print('This function is doing something')


if __name__ == "__main__":
    print('This is demo_main.py')
    name = input('Enter your name: ')
    print(display(name))
    do_something()
