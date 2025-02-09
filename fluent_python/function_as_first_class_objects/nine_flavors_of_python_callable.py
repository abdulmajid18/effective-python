# 1. Functions
def function():
    return "I am a function!"


# 2. Instance Methods
class MyClass:
    def method(self):
        return "I am an instance method!"


# 3. Class Methods
class MyClassWithClassMethod:
    @classmethod
    def class_method(cls):
        return "I am a class method!"


# 4. Static Methods
class MyClassWithStaticMethod:
    @staticmethod
    def static_method():
        return "I am a static method!"


# 5. Classes (Callable because of __init__)
class CallableClass:
    def __init__(self):
        print("I am a class instance!")


# 6. Objects with __call__
class CallableObject:
    def __call__(self):
        return "I am callable!"


# 7. Generator Functions
def generator_function():
    yield "I am a generator!"


# 8. Native Coroutines (async function)
import asyncio


async def coroutine_function():
    return "I am a coroutine!"


# 9. Asynchronous Generators (async generator function)
async def async_generator_function():
    yield "I am an async generator!"


# Testing the callables
print(function())  # Regular function
print(MyClass().method())  # Instance method
print(MyClassWithClassMethod.class_method())  # Class method
print(MyClassWithStaticMethod.static_method())  # Static method
CallableClass()  # Instantiating a class
print(CallableObject()())  # Callable object
print(next(generator_function()))  # Generator function


# Running async functions
async def main():
    print(await coroutine_function())  # Coroutine function
    async for val in async_generator_function():
        print(val)  # Async generator function


asyncio.run(main())
