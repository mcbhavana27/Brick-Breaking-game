import os
import time
import sys
from values import *
from header import *
from board import *
from enemies import *
from input import *


class Scene:
    """ Making a matrix to represent the game scene """

    def __init__(self, length, width, fullwidth):
        """ Initial matrix """
        self.start = 0
        self.length = length
        self.width = width
        self.fullwidth = fullwidth
        self.scenematrix = []
        self.flag=0
        # scenematrix is a matrix to display all elements(empty screen)
        for x in range(0, fullwidth):
            self.scenematrix.append([])
            for y in range(0, fullwidth):
                self.scenematrix[x].append(' ')
        #to  display the ground
        for x in range(39, length):
            for y in range(0, fullwidth):
                self.scenematrix[x][y] = colors['Purple'] + 'T' + RESET
        for x in range(40, length):
        	for y in range(0, fullwidth):
        		self.scenematrix[x][y] = colors['Purple'] + '-' + RESET


    def displayScene(self):
        """ Print the screen to the terminal """
        sceneprint = ""
        if self.start >= self.fullwidth - self.width:
            self.start = self.fullwidth - self.width
        for i in range(0, self.length):
            for j in range(self.start, self.start + self.width):
                sceneprint += str(self.scenematrix[i][j])
            sceneprint += '\n'
        sceneprint += colors['Cyan'] + "Press q to exit\n" + RESET
        return sceneprint
    def returnmatrix(self):
        return self.scenematrix

    def updatescene(self, updmatrix):
        self.scenematrix = updmatrix

    def leftmove(self,paddle):
        paddle.y=paddle.y-1
        self.scenematrix[paddle.x][paddle.y]='#'
        self.scenematrix[paddle.x][paddle.y+7]=' '

    def rightmove(self,paddle):
        paddle.y=paddle.y+1
        self.scenematrix[paddle.x][paddle.y-1]=" "
        self.scenematrix[paddle.x][paddle.y+6]='#'


    def ballmove(self,ball,paddle):
        if(ball.x>35):
            if(ball.y>paddle.y and ball.y<paddle.y+7):
            #ball in bottom
                self.flag=0
            # self.scenematrix[paddle.x-1][paddle.y+2]="O"
            
        if(ball.x==0):
            #ball in top
            self.flag=1
        #center point
        if(ball.x<11):
            self.flag=3
        #right wall -> ball goes to left
        if(ball.y==145):
            self.flag=2
        #left wall -> ball comes right 
        if(ball.y<0):
            self.flag=3

         #ball goes up
        if(self.flag==0):
            self.scenematrix[ball.x-1][ball.y]="O"
            self.scenematrix[ball.x][ball.y]=" "
            ball.x=ball.x-1

        #ball comes down
        if(self.flag==1):
            self.scenematrix[ball.x+1][ball.y]="O"
            self.scenematrix[ball.x][ball.y]=" "
            ball.x=ball.x+1
            self.flag=2

        #move left 
        if(self.flag==2):
            self.scenematrix[ball.x][ball.y-1]="O"
            self.scenematrix[ball.x][ball.y]=" "
            ball.y=ball.y-1
            ball.x=ball.x

        #move right
        if(self.flag==3):
            self.scenematrix[ball.x+1][ball.y+1]="O"
            self.scenematrix[ball.x][ball.y]=" "
            ball.y=ball.y+1
            ball.x=ball.x+1

    
    def collision(self,ball,paddle):
        print("eyyy")
        #bonus
        if(ball.x >= 20 and ball.x<=23):
            if(ball.y>=100 and ball.y<=107):
                i=ball.x
                j=ball.y
                for i in range(ball.x+1):
                    for j in range(ball.y+1):
                        self.scenematrix[i][j]=" "
                        # Score.score+=5
               
        
        #brown brick1(2 points)
        c=2
        if(ball.x >= 20 and ball.x<22):
            if(ball.y>=30 and ball.y<34):
                # if(self.scenematrix[20][30]=="R") 
                self.scenematrix[20][30]=""
                self.scenematrix[20][31]=" "
                self.scenematrix[20][32]=" "
                self.scenematrix[20][33]=" "
                self.scenematrix[21][30]=" "
                self.scenematrix[21][31]=" "
                self.scenematrix[21][32]=" "
                self.scenematrix[21][33]=" "
            Score.score+=5
                
         #top green brick1
        if(ball.x >= 15 and ball.x<17):
            if(ball.y>=70 and ball.y<74):
                self.scenematrix[15][70]=" "
                self.scenematrix[15][71]=" "
                self.scenematrix[15][72]=" "
                self.scenematrix[15][73]=" "
                self.scenematrix[16][70]=" "
                self.scenematrix[16][71]=" "
                self.scenematrix[16][72]=" "
                self.scenematrix[16][73]=" "
            #top above red
        if(ball.x >= 11 and ball.x<13):
            if(ball.y>=55 and ball.y<59):
                print("hehe")
                self.scenematrix[11][55]=" "
                self.scenematrix[11][56]=" "
                self.scenematrix[11][57]=" "
                self.scenematrix[11][58]=" "
                self.scenematrix[12][55]=" "
                self.scenematrix[12][56]=" "
                self.scenematrix[12][57]=" "
                self.scenematrix[12][58]=" "
                Score.score+=5
            #top above green
        if(ball.x >= 11 and ball.x<13):
            if(ball.y>=60 and ball.y<64):
                print("hehe")
                self.scenematrix[11][60]=" "
                self.scenematrix[11][61]=" "
                self.scenematrix[11][62]=" "
                self.scenematrix[11][63]=" "
                self.scenematrix[12][60]=" "
                self.scenematrix[12][61]=" "
                self.scenematrix[12][62]=" "
                self.scenematrix[12][63]=" "
                Score.score+=5
        
    #brownball2
        if(ball.x >= 28 and ball.x<30):
            if(ball.y>=60 and ball.y<64):
                print("hehe")
                self.scenematrix[28][60]=" "
                self.scenematrix[28][61]=" "
                self.scenematrix[28][62]=" "
                self.scenematrix[28][63]=" "
                self.scenematrix[29][60]=" "
                self.scenematrix[29][61]=" "
                self.scenematrix[29][62]=" "
                self.scenematrix[29][63]=" "
                Score.score+=5

            #bottom red brick
        if(ball.x >= 28 and ball.x<30):
            if(ball.y>=70 and ball.y<74):
                print("hehe")
                self.scenematrix[28][70]=" "
                self.scenematrix[28][71]=" "
                self.scenematrix[28][72]=" "
                self.scenematrix[28][73]=" "
                self.scenematrix[29][70]=" "
                self.scenematrix[29][71]=" "
                self.scenematrix[29][72]=" "
                self.scenematrix[29][73]=" "
                Score.score+=5
            #bottom green brick
        if(ball.x >= 28 and ball.x<30):
            if(ball.y>=90 and ball.y<94):
                    # print("hehe")
                self.scenematrix[28][90]=" "
                self.scenematrix[28][91]=" "
                self.scenematrix[28][92]=" "
                self.scenematrix[28][93]=" "
                self.scenematrix[29][90]=" "
                self.scenematrix[29][91]=" "
                self.scenematrix[29][92]=" "
                self.scenematrix[29][93]=" "
                Score.score+=5

            #bottom brown brick3

        if(ball.x >= 28 and ball.x<30):
            if(ball.y>=100 and ball.y<104):
                    # print("hehe")
                self.scenematrix[28][100]=" "
                self.scenematrix[28][101]=" "
                self.scenematrix[28][102]=" "
                self.scenematrix[28][103]=" "
                self.scenematrix[29][100]=" "
                self.scenematrix[29][101]=" "
                self.scenematrix[29][102]=" "
                self.scenematrix[29][103]=" "
                Score.score+=5
            #up brown ball4
        if(ball.x >= 20 and ball.x<22):
            if(ball.y>=132 and ball.y<136):
                    # print("hehe")
                self.scenematrix[20][132]=" "
                self.scenematrix[20][133]=" "
                self.scenematrix[20][134]=" "
                self.scenematrix[20][135]=" "
                self.scenematrix[21][132]=" "
                self.scenematrix[21][133]=" "
                self.scenematrix[21][134]=" "
                self.scenematrix[21][135]=" "
                Score.score+=5

             #center red brick
        if(ball.x >= 24 and ball.x<28):
            if(ball.y>=80 and ball.y<84):
                    # print("hehe")
                self.scenematrix[24][80]=" "
                self.scenematrix[24][81]=" "
                self.scenematrix[24][82]=" "
                self.scenematrix[24][83]=" "
                self.scenematrix[25][80]=" "
                self.scenematrix[25][81]=" "
                self.scenematrix[25][82]=" "
                self.scenematrix[25][83]=" "
                Score.score+=5
            
           #center green brick
        if(ball.x >= 20 and ball.x<22):
            if(ball.y>=70 and ball.y<74):
                    # print("hehe")
                self.scenematrix[20][70]=" "
                self.scenematrix[20][71]=" "
                self.scenematrix[20][72]=" "
                self.scenematrix[20][73]=" "
                self.scenematrix[21][70]=" "
                self.scenematrix[21][71]=" "
                self.scenematrix[21][72]=" "
                self.scenematrix[21][73]=" "
                Score.score+=5
            
             #top red brick
        if(ball.x >= 15 and ball.x<17):
            if(ball.y>=80 and ball.y<84):
                # print("hehe")
                self.scenematrix[15][80]=" "
                self.scenematrix[15][81]=" "
                self.scenematrix[15][82]=" "
                self.scenematrix[15][83]=" "
                self.scenematrix[16][80]=" "
                self.scenematrix[16][81]=" "
                self.scenematrix[16][82]=" "
                self.scenematrix[16][83]=" "
                Score.score+=5

              #top brown brick
        if(ball.x >= 15 and ball.x<17):
            if(ball.y>=90 and ball.y<94):
                print("hehe")
                self.scenematrix[15][90]=" "
                self.scenematrix[15][91]=" "
                self.scenematrix[15][92]=" "
                self.scenematrix[15][93]=" "
                self.scenematrix[16][90]=" "
                self.scenematrix[16][91]=" "
                self.scenematrix[16][92]=" "
                self.scenematrix[16][93]=" "
                Score.score+=5
              #top green brick
        if(ball.x >= 15 and ball.x<17):
            if(ball.y>=60 and ball.y<64):
                    # print("hehe")
                self.scenematrix[15][60]=" "
                self.scenematrix[15][61]=" "
                self.scenematrix[15][62]=" "
                self.scenematrix[15][63]=" "
                self.scenematrix[16][60]=" "
                self.scenematrix[16][61]=" "
                self.scenematrix[16][62]=" "
                self.scenematrix[16][63]=" "
                Score.score+=5
           
            
            
            
            
            

            
                
            
                

            

