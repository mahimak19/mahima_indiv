## TT1 Loops and Lists

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

## TT0 Python Menu Individual Task

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
