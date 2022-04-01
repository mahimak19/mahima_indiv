{% include navigation.html %}

## Create Task Info

Program overview:

This program will portray vacation suggestions based on your age and personality type. There are many different personality types that can cause conflict within each other. It is important in this day and age that people of different personality types (Personality type A,B,C or X) are separated from each other to make people more comfortable. We created a program that allows for people of different personality types to be able to be themselves, while surrounded by people who share the same interests.

Functionality of the Program: this program includes a box to put your age, and a box to put your personality type and as a result they will be shown a box of where they should visit/vacation.

Instruction for Input:

The user will choose their personality type from a drop down (they know this by taking the Personality Type Quiz on our website)
The user will enter their age in a text-box
The user will click the submit button
College Board Requirement: Include an input for your program in the form of one or more parameters that go into the program.

```
vacaylist = ['New York City', 'Tokyo', 'Los Angeles', 'Paris', 'San Diego', 'Hawaii', 'Sedona', 'Amsterdam', 'Seoul'  ]




class Vacation:
    
    def __init__(self, pt, age):
        

        self._pt = pt
        self._age = 0
        self._display = []
        self._dict = {}
        self._dictID = 0
        # Duration timeElapsed;
        # Instant start = Instant.now();  // time capture -- start
        self.getV()
        # Instant end = Instant.now();    // time capture -- end
        # this.timeElapsed = Duration.between(start, end);

```
```
<div align="left">
    <section id="done">
        <form id="form" action="" method="POST">
            <input type="text" id="pt" name="pt">
            <label for="pt"> Enter your personality type</label>
            <input type="number" id="age" name="age">
            <label for="age"> Enter your age</label>
```


Instructions for Output:

Using the Python print() function, a list of vacation spots tailored to the user’s age and personality type will be displayed on the screen Pictures of the location will be displayed through show(), which is possible through Python Pillow
College Board Requirement: Have tactile, audible or visual output (in this case, the vacation suggestions are the visual output

```  
  vacay = Vacation("A", 15)
    print(f"Here are some vacay recomendations = {vacay.list}")

    vacay = Vacation ("B", 35)
    print(f"Here are some vacay recomendations = {vacay.list}")
```

Collection Type Use:

A list will be used to have a set of locations that are to be recommended to the user based on the age and personality type they input
The benefit of using a list in the program is it is able to store one variable, without needed each separate individual variable. The for loop also allows for the program to run smoothly and expand as you do not have to write the same sequence, multiple times.
College Board Requirement: Use a list to store data to fulfill the program's purpose (in this case, this is a list of the vacation locations)

```
vacaylist = ['New York City', 'Tokyo', 'Los Angeles', 'Paris', 'San Diego', 'Hawaii', 'Sedona', 'Amsterdam', 'Seoul'  ]
```
Procedure:

Use a series of ‘if’, ‘else’ statements (conditionals) to display different results with specific location recommendations for different ages and personality types. This displays selection, since we are considering different outcomes based on the user's input and are not going through each line of code sequentially the whole time. We also plan on including an aspect of iteration by including if or while loops in order to shorten the process.
College Board Requirement: Sequencing, Selection and Iteration, name the procedure, calls to the procedure.

```
 def getV(self):
        f = [(random.sample(vacaylist,1))]

        if (self._pt) == "A":
            if (self._age < 30):
                display = (vacaylist[0], vacaylist[2])
            elif (self._age > 30):
                display = (vacaylist[1])
            else:
                display = vacaylist[1]


        elif (self._pt) == "B":
            if (self._age < 30):
                display = (vacaylist[4], vacaylist[5])
            if (self._age > 30):
                display = (vacaylist[3])
            else:
                display = vacaylist[3]

        else:
            if (self._age < 30):
                display = (vacaylist[7], vacaylist[8])
            if (self._age > 30):
                display = (vacaylist[6])
            else:
                display = vacaylist[6]

        self._display = display
```

Runtime [Video](https://user-images.githubusercontent.com/89278005/156052527-6e146faf-1c58-48f6-a9f6-0b5f328a8edc.mov)

