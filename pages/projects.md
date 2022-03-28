{% include navigation.html %}

## Week 2 Classy Functions

Hack 1: Organize files, directories and menus for the first 3 weeks. 
-Replit python files organized by week, menu reflects the same
```
week0 = {
    1: {
        "display":"ship",
        "exec":ship,
        "type":"func"
    },
   
    2: {
        "display":"Swap ",
        "exec":swap,
        "type":"func"},
    
    0: {
        "display": "Quit",
        "exec":quit,
        "type":"func"
    }
}
week1 = {
  1: {
    "display": "Fibonacci",
    "exec": fib,
    "type": "func"
  },
  2: {
    "display": "Lists & Loops",
    "exec": ll,
    "type": "func"
  },
  0: {
    "display": "Quit",
    "exec": quit,
    "type": "func"
  }
}
week2 = {
    1: {
        "display":"Factorial",
        "exec":fac,
        "type":"func"
    },
    2: {
        "display":"Math Function: Factors",
        "exec":driver,
        "type":"func"
    },
    3: {
        "display":"Factors No Class",
        "exec":print_factors,
        "type":"func"
    },
    0: {
        "display":"Quit",
        "exec":quit,
        "type":"func"
    }
}

mainMenu = {
    1: {
        "display": "Week 0",
        "exec": week0,
        "type": "submenu"
    },
    2: {
        "display": "Week 1",
        "exec": week1,
        "type": "submenu"
    },
    3: {
        "display": "Week 2",
        "exec": week2,
        "type": "submenu"
    },

    0: {
        "display": "Quit",
        "exec":quit,
        "type":"func"
    }
}
```

Hack 2: Write Factorial function using classes, providing implementation of call.
-create a class called Factorial, define an object, create 'fac' function with try and except

```
class Factorial:
    def __init__(self):
        self.factorial = 1

        
'''
The call function/method is a special to Python, when implemented inside a class, this gives its
 object the ability to behave like a regular Python function.
Definition of call. The call method is defined inside the Python class. The method allows the 
construct object to invoke this method using a "object_name()" notation. The "def call(self, n):" 
has keyword "self" in the parameter list, this means that the object itself is part of this 
functions properties. The parameter "n" means it is expecting a value to be passed, 
in Factorial case it is for the Factorial of n - (n!).
'''        
def __call__(self, n):
        if n == 1 or n == 0:
            return 1
        else:
            # Compute the requested Fibonacci number
            self.factorial = n * self(n - 1)
        return self.factorial


def fac():
    # Make a fibonacci object
    fact_of = Factorial()
    n = input("Enter a number for factorial: ")
    try:
        n = int(n)
        # Validate the value of n
        if n < 0 or n > 99:
            raise ValueError

        print(f"Factorial  of {n}  is: ", fact_of(n))
    except ValueError:
        print(f'Positive integer number in range 2 to 99 is expected, got "{n}" Try again.')


if __name__ == "__main__":
  fac()
```

Hack 3: Select your own Math function. Write it in Imperative and OOP form. 

Factor Function OOP Form:

```
class factors:
    def __init__(self):
        self.allfactors = []

    ''' 
   __call__ is a special function/method in Python, when implemented inside a class, this gives its instances 
   (or objects) the ability to behave like a function. The __call__ method inside the  Python class allows 
   instance to invoke this method using object like a function.  
   This method has a n as a parameter which is used to calculate the factors of the number.

    '''

    def __call__(self,num):
        for value in range(1, num + 1):
            if num % value == 0:
                self.allfactors.append(value)
        return self.allfactors

def driver():
    # Make a factors object
    while True:
        fact = factors()
        n = input("Enter the number to find factors: ")
        try:
            n = int(n)
            # Validate the value of n
            if n < 2 or n > 99:
                raise ValueError
            # Produces a list of factors for input
            print(f"Factors of {n} are: ", fact(n))
            break
        except ValueError:
            print(f'Positive integer number in range 2 to 99 is expected, got "{n}" Try again.')

if __name__ == "__main__":
    driver()
```
Imperative Form:

```
num = int(input("Type a number "))
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

print_factors(num)
```


## Week 1 Loops and Lists
<iframe frameborder="0" width="100%" height="500px" src="https://repl.it/@MahimaKrovvidy/mahima_indiv-1?embed=true"></iframe>



Hack 1: Creating the Lists

-Each list has a length greater than 3
-there are 2 lists
-List within a list: Favorite Books

```
InfoDb = []
# List with dictionary records placed in a list
InfoDb.append({
    "FirstName": "Mahima",
    "LastName": "Krovvidy",
    "DOB": "November 19",
    "Email": "mahikro@gmail.com",
    "Favorite Books":["Harry Potter and the Chamber of Secrets","One of Us Is Lying","Sherlock Holmes","Everything,Everything", "Inferno"]
})
InfoDb.append({
    "FirstName": "Dora",
    "LastName": "The Explorer",
    "DOB": "September 40th",
    "Email": "delicioso@swiper.com",
    "Favorite Books":["Harry Potter and the Chamber of Secrets","One of Us Is Lying","Sherlock Holmes","Everything,Everything", "Inferno"]
})
```


Hack 2: Create 3 different loops (for, while, recursive) to access information from InfoDb

-For loop:

```
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)
for_loop()
#print(InfoDb[1]["FirstName"])
```
We defined the for loop, for each element in list, print the data, then we called the function

-While loop:

```
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
while_loop(0)
```
Define the while loop, print data, add 1 to n, call the while loop with initial index 0

-Recursive loop:

```
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition
recursive_loop(0)
```
Define recursive loop, call the same function repeatedly and add n+1. Start the loop at 0.

-Fibonacci
```
y = int(input("How many Fibonacci? "))


def recursion_fib(x):
  if x <= 1:
    return 1
  else:
    return(recursion_fib(x-1) + recursion_fib(x-2))


for i in range(y):
  fib = recursion_fib(i)
  print(fib)
```
Using a recursive loop, we are able to print a series of numbers where the next number is the sum of the previous two numbers, except when x is less than or equal to 1. 

## Week 0 Python Menu Individual Task

Making a Python Menu

```
import shipbetter


# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders

# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = [
    ["swap", "swap2.py"],
    ["ship", "ship.py"],
    ["shipbetter", "shipbetter.py"]
  

    
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
    ["Factors", None],
    ["GCD", None],
    ["LCM", None],
    ["Primes", None],
]


# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


# def patterns_submenuc
# using patterns_sub_menu list:
# patterns_submenuc works similarly to menuc
def patterns_submenuc():
    title = "Class Submenu" + banner
    m = questy.Menu(title, patterns_sub_menu)
    m.menu()


# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    buildMenu(title, menu_list)



# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)


def patterns_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, patterns_sub_menu)


def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again

menu()

if __name__ == "__main__":
    menu()
```
- The code for the menu is put into the main.py file
- A submenu was not needed, since I put in only 2 programs
- A series of try, except and finally statements demonstrates selection of the user, determines which program to run

One of the functions we inputted is the swap function from last tri

```
x = input ("Type a number ")
y = input ("Type another number ")
print (x,y)
def swap (x,y):
    q = x
# we set one of our variables to a temporary variable
    x = y
#swap the original two variables
    y = q
#set y equal to the temp

    return x,y

a,b= swap(x,y)
print(a, b)

```

Ship Animation

-The less efficient way is to print multiple ships in different spots and create time intervals for each one so that when code runs, the ships move like an animation

-The os.system (cls) was causing issues with runtime
-Link to runtime: 
