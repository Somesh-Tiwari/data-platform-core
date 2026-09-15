#Day 7 - Functions

def hello_func():
    print("Hello from a function!")

hello_func()

#DRY - Don't Repeat Yourself is a principle of software development aimed at reducing the repetition of code patterns. It emphasizes the importance of creating reusable functions or modules to avoid redundancy and improve maintainability. By following the DRY principle, developers can write cleaner, more efficient code that is easier to understand and modify.

def hello_func_with_args(greeting, name = 'Guest'):
    return f"{greeting} {name}"

print(hello_func_with_args("Hello", "Somesh"))

def automated_greeting():
    name = input("Enter your name: ").title().strip()
    print(f"Hello {name}")

automated_greeting()

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'English', name='Somesh', age=25)

courses = ['History', 'Math', 'English', 'Geography', 'Science']
info = {'name': 'Somesh', 'age': 25, 'city': 'New York'}

student_info(*courses, **info)  #unpacking the list and dictionary into the function


#Function example
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def is_leap(year):
    """Return True for leap years, False for non-leap years."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_a_month(year, month):
    """Return the number of days in a month for a given year."""
    if not 1 <= month <= 12:
        return "Invalid Month"
    elif month == 2 and is_leap(year):
        return 29
    return days_in_month[month - 1]

print(is_leap(2020))  
print(days_in_a_month(2020, 2))
