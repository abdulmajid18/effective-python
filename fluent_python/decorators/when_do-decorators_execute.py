registry = []  # A global list to keep track of registered functions


def register(func):
    print(f'running register({func})')  # Print when the decorator runs
    registry.append(func)  # Store function in registry
    return func  # Return the function unchanged


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry ->', registry)  # Print the registry list
    f1()  # Call f1
    f2()  # Call f2
    f3()  # Call f3


if __name__ == '__main__':
    main()  # Run main() only if executed directly
