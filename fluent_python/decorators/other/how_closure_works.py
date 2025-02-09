def outer_function(msg):
    def inner_function():
        print(f"Message: {msg}")  # `msg` is remembered even after `outer_function` returns
    return inner_function  # Return the inner function

closure = outer_function("Hello!")
closure()  # Output: "Message: Hello!"
