

**By 2019101100**
# The Brick-Breaker
This game is a terminal version of arcade game.

## Setup

Libraries used :

pip3 install colorama

## Execution

To play :

python3 main.py

## Rules

**a** - To move left

**d** - To move right

**b** - To drop the ball

**q** - To quit


## Features

* Ball moves (vertical, horizontal and 45 degrees) appear through the course of the game

* When the paddle touches the ball,it moves along 45 and ball will collide the bricks and score get increased.If the ball touches below diagonal the lives get decreased.

## Concepts Used
* Inheritance: Common attributes of the parent class inherited by the child classes. (Helps in avoiding redundant code)

```python
class Scene():

    #Class defining generic 
    def __init__(self,length,width):
        #Protected variables to be inherited
        self.start = 0
        self.length = length
        self.width = width
        self.fullwidth = fullwidth
        self.scenematrix = []
        self.flag=0

    def displayScene(self):

    def leftmove(self,paddle):
    
```

* Polymorphism: Utililizing the same function of a parent class for different functionalites of child classes based on the list of parameters passed

```python 
class Obstacle:

   def __init__(self, length, width):
        self.length = length
        self.width = width
        self.x = None
        self.y = None
        self.matrix = []
   def setpos(self,scene,x,y):
	blitobject(scene, self, x, y)
        self.x = x
        self.y = y


    def drawbrick(scene,length,width,x,y):
        #POLYMORPHISM USED TO SHOW/DISPLAY ALL OBJECTS
         brick= Brick(length, width)
        brick.setPos(scene, x, y)
```

* Encapsulation: Every component on the enemies is an object of a class. This instantiation encapsulates the methods and attributes of the objects.
```python
class Obstacle:

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.x = None
        self.y = None
        self.matrix = []

class Cloud(Obstacle):

    def __init__(self, length, width):
        ''' Initialize as a type of obstacke '''
        Obstacle.__init__(self, length, width)
        self.x = 0
        self.y = 0
        p = colors['White']+'/'+RESET
        q = colors['White']+'\\'+RESET
        r=colors['White']+'-'+RESET
        self.matrix = [[p, q, p, q, p, q],
                       [q, ' ', ' ', ' ', ' ', p],
                       ['.',r,r,r,r,'.']]

class Brick(Obstacle):

    def __init__(self, length, width):
        ''' Initialize as a type of obstacke '''
        Obstacle.__init__(self, length, width)
        self.x = 0
        self.y = 0
        self.matrix = [[colors['Cyan']+'D'+RESET for i in range(0, width)]
        for j in range(0, length)]
        

    def draw_brick(scene, length, width,x, y):
        brick= Brick(length, width)
        brick.setPos(scene, x, y)

```

* Abstraction: The functions of each class hide the inner details of the function enabling users to use just the function name.
-> used in creating bricks

