from values import *
from board import *
from enemies import *
from header import *


def blitobject(scene, item, x, y):
    # print("blit",x,y)
    itemmatrix = item.returnmatrix()
    scenematrix = scene.returnmatrix()
    # item.x=x
    # item.y=y
    print(item.x,item.length,item.width)
    k = 0
    l = 0
    # deleting previous position
    for i in range(item.x, item.x + item.length):
        for j in range(item.y, item.y + item.width):
            scenematrix[i][j] = ' '
    # putting at new position
    for i in range(x, x + item.length):
        for j in range(y, y + item.width):
            scenematrix[i][j] = itemmatrix[i-x][j-y]
    scene.updatescene(scenematrix)


class Obstacle:

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.x = None
        self.y = None
        self.matrix = []
    def setPos(self, scene, x, y):
        blitobject(scene, self, x, y)
        self.x = x
        self.y = y
        # print("pos",x,y)

    def returnmatrix(self):
        return self.matrix

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

class rbrick(Obstacle):
    def __init__(self,length,width):
        Obstacle.__init__(self,length,width)
        self.x=0
        self.y=0
        self.matrix = [[colors['Red']+'R'+RESET for i in range(0, width)]
        for j in range(0, length)]


    def draw_rbrick(scene, length, width,x, y):
        Rbrick= rbrick(length, width)
        Rbrick.setPos(scene, x, y)

class gbrick(Obstacle):
    def __init__(self,length,width):
        Obstacle.__init__(self,length,width)
        self.x=0
        self.y=0
        self.matrix = [[colors['Green']+'G'+RESET for i in range(0, width)]
        for j in range(0, length)]


    def draw_gbrick(scene, length, width,x, y):
        Gbrick= gbrick(length, width)
        Gbrick.setPos(scene, x, y)

class bbrick(Obstacle):
    def __init__(self,length,width):
        Obstacle.__init__(self,length,width)
        self.x=0
        self.y=0
        self.matrix = [[colors['Brown']+'B'+RESET for i in range(0, width)]
        for j in range(0, length)]


    def draw_bbrick(scene, length, width,x, y):
        Bbrick= bbrick(length, width)
        Bbrick.setPos(scene, x, y)
        

class Paddle(Obstacle):
    '''paddle for ball's bottom'''
    def __init__(self, length, width):
        Obstacle.__init__(self, length, width)
        self.x = 0
        self.y = 0
        p = colors['Green']+'#'+RESET
        self.matrix = [[p,p,p,p,p,p,p,p]]

class Ball(Obstacle):
    def __init__(self, length, width):
        Obstacle.__init__(self, length, width)
        self.x = 36
        self.y = 30
        self.matrix = [['O']]
