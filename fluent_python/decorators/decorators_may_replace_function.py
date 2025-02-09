def replace_with_dummy(func):
    def dummy():
        print("I am a dummy function!")

    return dummy


@replace_with_dummy
def actual_function():
    print("This should not print!")


actual_function()
