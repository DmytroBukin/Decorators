#decorators theory

#1 example

def my_decorator_func(func): #3
    def wrapper(): #4
        print("smth")
        func()
        print("smth again")
    return wrapper

@my_decorator_func #2
def say_hello(): #1
    print("Hello!")
say_hello()


#2 example
'''
import time


def delay_decorator(func):
    def wrapper(*args , **kwargs):
        time.sleep(3)
        return func(*args , **kwargs)
    return wrapper()



@delay_decorator
def sleepy():
    print("I sleep")
sleepy()


'''
#3 example


def cache_decorator(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n] , cache
    return wrapper

@cache_decorator
def fibonacci(n):
    if n in (0,1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10))

