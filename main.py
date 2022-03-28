from week0.shipbetter import ship
from week0.swap2 import swap


from week1.fibonacci import fib
from week1.loops import ll

from week2.factorial import fac
from week2.factormath import driver
from week2.factornoclass import print_factors



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


def buildMenu(menu):
    for key,value in menu.items(): 
        display = value["display"]
        print(f"{key} ------ {display}") # each menu item is printed
    print("What is your choice? (enter the number value) ") # user input promp

def presentMenu(menu):
    buildMenu(menu) #print out menu and take input
    choice = int(input())
    while choice not in menu: # ensure that choice is valid
        choice = int(input("Please elect a valid item. "))
    if (choice) in menu:
        if menu[choice]["type"] == "func": #determine whether recursion is needed
            menu[choice]["exec"]() #run function

        else:
            presentMenu(menu[choice]["exec"]) #display submenu

if __name__ == "__main__":
  while True:
    presentMenu(mainMenu)

































