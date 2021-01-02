import os
def introduction():
    print("""
Python is an interpreted, high-level and general-purpose programming language.
Python's design philosophy emphasizes code readability with its notable use
of significant whitespace.
""")

def history():
    print("""
Python was conceived in the late 1980s[33] by Guido van Rossum at Centrum
Wiskunde & Informatica (CWI) in the Netherlands.
Its implementation began in December 1989.
Van Rossum shouldered sole responsibility for the project, as the lead developer,
until 12 July 2018.
""")
    
def syntax():
    print("""
Python is meant to be an easily readable language.
Its formatting is visually uncluttered, and it often uses English keywords where
other languages use punctuation.
It has fewer syntactic exceptions and special cases than C or Pascal.
""")
    
def menu ():
    print("""
Welcome to our Python article!
If you want to learn Python, you can find the following paragraphs:
1. introduction in Python;
2. history of Python;
3. python syntax (authorization required).
""")

def decorator_login(func):
    def wrapper():
        c = input('Enter your login to view: ')
        if c:
            func()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('You are not registered. Return to the menu for registration') 
            menu() 
    return wrapper

syntax_dec = decorator_login(syntax)

menu()
while True:
    a = int(input('Enter the number of paragraph (0 - to the menu; 4 - exit): '))
    if a == 1:
        introduction()  
    elif a == 2:
        history()
    elif a == 3:
        syntax_dec() 
    elif a == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        menu()
    elif a == 4:
        break 
os.system('cls' if os.name == 'nt' else 'clear')
print('Thank you for attention!'.upper())  
        


