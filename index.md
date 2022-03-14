# Mahima's Individual Github Pages Site Tri 3


## 5.1 Beneficial + Harmful effects of Computing


Drones: Fun, easy, but can be used by military

Dopamine: Pleasure hormones, video games and social media can be addictive, constant excitement from them.

Imperative: sequencing, different decisions, like python


### Actions:
1) Come up with three of your own Beneficial and corresponding Harmful Effects of Computing

Beneficial Effects of Computing: Access to a larger range of information and experiences (like video games, online websites and articles), ability to streamline certain tasks to make them easier, help and connect to people across a large distance (like across the world) and learn about their culture

Harmful effects: Can be addictive (dopamine effect, Internet can be a distraction), Privacy issues can occur, Technology and AI can replace jobs done by humans (unemployment, loss of livelihood).

2) Talk about dopamine issues above. Real? Parent conspiracy? Anything that is impacting your personal study and success in High School?

The dopamine problem is real. As teenagers, we constantly try to keep our minds busy with distractions like social media, tv/movies, etc, and it is easy to get addicted to these things. These short term pleasures give instant hits of dopamine, which can impact long-term goals like studying and extracurriculars. For me, scrolling on YouTube is a big distraction from completing my work in a timely manner.


## 5.2 Digital Divide 

-Lack of access to technology in poorer areas, less developed areas. 
-Demographics, geo location, socioeconomic factors
-Can’t get latest updates, Amish choose not to use tech
-PUSD is making people use chromebooks, can impede digital expoloration and flexibility

### Actions:

How does someone empower themself in a digital world?

Create programs and content that serves a purpose in society. A creation that helps people and changes lives. Connecting with other people and sharing ideas digitally is also another way to empower oneself.

How does someone that is empowered help someone that is not empowered? Describe something you could do at Del Norte HS.

People that don't have access to technology may not be able to digitally empower themselves. One thing that empowered people can do is help supply technology to those in poorer areas, as well as educate them on how to use it and accomplish different tasks. One can also offer coding classes to underprivileged people so that even they can create and contribute to the technological world. Something I could do at DNHS is reach out to students who have internet and tech access issues at home and introduce them to computer science and what it has to offer.

Is paper or red tape blocking digital empowerment? Are there such barriers at Del Norte? Elsewhere?

Many classes still use traditional textbooks and notebooks to learn material, and it may not be as accessible or feasible to do this. For example, some classes only have the textbook at school and students have to be at school to learn the material. Students also have to carry large notebooks for some classes, where instead most work can be done online. Access to information is expanded drastically by using the internet too, which some classes may not allow. Also, Del Norte wifi blocks certain sites even though there's nothing bad in them.



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
College Board Requirement: Have tactile, audible or visual output (in this case, the vacation suggestions are the visual output)

Collection Type Use:

A list will be used to have a set of locations that are to be recommended to the user based on the age and personality type they input
The benefit of using a list in the program is it is able to store one variable, without needed each separate individual variable. The for loop also allows for the program to run smoothly and expand as you do not have to write the same sequence, multiple times.
College Board Requirement: Use a list to store data to fulfill the program's purpose (in this case, this is a list of the vacation locations)

Procedure:

Use a series of ‘if’, ‘else’ statements (conditionals) to display different results with specific location recommendations for different ages and personality types. This displays selection, since we are considering different outcomes based on the user's input and are not going through each line of code sequentially the whole time. We also plan on including an aspect of iteration by including if or while loops in order to shorten the process.
College Board Requirement: Sequencing, Selection and Iteration, name the procedure, calls to the procedure.


