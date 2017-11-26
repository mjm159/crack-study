from menu import Menu


def foo1():
    print('foo1')

def foo2():
    print('foo2')

def foo3():
    print('foo3')

menu = Menu()
menu.title = "Crack Study\n==========="
menu.options = [
    ('Foo 1', foo1),
    ('Foo 2', foo2),
    ('Foo 3', foo3),
    ('Quit', Menu.CLOSE),
    ]


menu.open()
menu.close()
