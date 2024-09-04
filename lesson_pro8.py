# Task 1
def before_and_after_decorator(func):
    def wrapper(*args, **kwargs):
        print("Перед виконанням функції")
        result = func(*args, **kwargs)
        print("Після виконання функції")
        return result
    return wrapper
@before_and_after_decorator
def example_function():
    print("Виконання основної функції")
example_function()
# Task 2
import os
import pickle


def cache_results_to_file(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if os.path.exists(filename):
                with open(filename, 'rb') as file:
                    cache = pickle.load(file)
            else:
                cache = {}
            key = (args, frozenset(kwargs.items()))
            if key in cache:
                print("Завантажено з кешу")
                return cache[key]
            result = func(*args, **kwargs)
            cache[key] = result
            with open(filename, 'wb') as file:
                pickle.dump(cache, file)

            return result
        return wrapper
    return decorator
@cache_results_to_file('function_results.cache')
def expensive_function(x, y):
    print("Обчислення функції...")
    return x * y
print(expensive_function(2, 3))  # Обчислення функції...
print(expensive_function(2, 3))  # Завантажено з кешу
# Task 3
def exception_handler_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Виникла помилка: {e}")
    return wrapper
@exception_handler_decorator
def divide(x, y):
    return x / y
print(divide(10, 2))
print(divide(10, 0))
# Task 4
import time
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Час виконання функції '{func.__name__}': {elapsed_time:.4f} секунд")
        return result
    return wrapper
@timing_decorator
def example_function(seconds):
    time.sleep(seconds)
    return "Готово!"
print(example_function(2))
# Task 5
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def log_arguments_and_results(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Виклик функції '{func.__name__}' з аргументами: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Функція '{func.__name__}' повернула результат: {result}")
        return result
    return wrapper
@log_arguments_and_results
def add(x, y):
    return x + y
result = add(3, 5)
# Task 6
from functools import wraps
def limit_calls(max_calls):
    def decorator(func):
        func._call_count = 0
        @wraps(func)
        def wrapper(*args, **kwargs):
            if func._call_count >= max_calls:
                raise Exception(f"Функцію '{func.__name__}' можна викликати не більше {max_calls} разів")
            func._call_count += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator
@limit_calls(3)
def my_function():
    print("Функція виконується")
my_function()
my_function()
my_function()
my_function()
