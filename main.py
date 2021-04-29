import os
import time
import sys
from values import *
from header import *
from board import *
from enemies import *
from input import *

flag=0

gamet=100
timex = time.time()
timey=time.time()
btime=time.time
endtime=10

#setting screen size
scene=Scene(scr_len,scr_wid,scr_size)
#displaying the screen

#cloud
x=0
for y in range(10, 400, 30):
	cloud = Cloud(3,6)
	x = (x+2) % 7
	cloud.setPos(scene, x, y)

posx=37
posy=30



#display paddle
paddle = Paddle(1,7)
paddle.setPos(scene,posx+1,posy-2)

# print(paddle.x)
#display ball
ball = Ball(1,1)
ball.setPos(scene,posx,posy)

#display bricks


# brick = Brick(2,4)
# brick.setPos(scene, groundx-25, 50)

#red bicks
Rbrick = rbrick(2, 4)
Rbrick.setPos(scene, groundx-25, 55)

rbrick.draw_rbrick(scene, 2, 4,15,60)
rbrick.draw_rbrick(scene, 2, 4,15,80)
rbrick.draw_rbrick(scene, 2, 4,24,80)
rbrick.draw_rbrick(scene, 2, 4,28,70)

#green bicks
Gbrick = gbrick(2,4)
Gbrick.setPos(scene, groundx-25, 60)

gbrick.draw_gbrick(scene, 2,4,15,60)
gbrick.draw_gbrick(scene, 2,4,15,70)
gbrick.draw_gbrick(scene, 2,4,20,70)
gbrick.draw_gbrick(scene, 2,4,28,90)

#brown bicks
Bbrick = bbrick(2, 4)
Bbrick.setPos(scene, 20, 132)

bbrick.draw_bbrick(scene, 2,4,15,90)
bbrick.draw_bbrick(scene, 2,4,28,100)
bbrick.draw_bbrick(scene, 2,4,20,30)
bbrick.draw_bbrick(scene, 2,4,28,60)

#bonus bricks
rbrick.draw_rbrick(scene, 2, 2,20,100)
rbrick.draw_rbrick(scene, 2, 2,20,103)
rbrick.draw_rbrick(scene, 2, 2,20,106)

#getting input
def check_lives(scene, lives):
    if lives <= 0:
        os.system('clear')
        print(scene.displayScene())
        print(Fore.RED+Style.BRIGHT+" You lost all lives:( " )
        sys.exit()
    elif(ball.x==38):
	    Live.lives-=1




while True:
	check_lives(scene,Live.lives)
	os.system('clear')
	title(SCREEN)
	ptime =(round(time.time()) - round(timex))
	print(colors['Yellow'] + "time: "+str(ptime)+RESET)
	print(colors['Red'] + "Lives: "+str(Live.lives)+RESET)
	print(colors['Yellow'] +"Score: "+str(Score.score)+RESET)
	print(scene.displayScene())
	input = input_to()


	if input == "b":
		flag=1
	if(flag==1):
		scene.ballmove(ball,paddle)

	#unbreakable
	Brick.draw_brick(scene, 2,4,28 ,80)
	Brick.draw_brick(scene, 2,4, 15,100)
	Brick.draw_brick(scene, 2,4, 15,30)
	Brick.draw_brick(scene, 2,4, 15,131)
	Brick.draw_brick(scene, 2,4, 28,120)

	brick = Brick(2,4)
	brick.setPos(scene, groundx-25, 50)

	k=4

	# #shrink paddle
	# if(ptime==15):
	# 	paddle.y=paddle.y+1
	# 	scene.scenematrix[paddle.x][paddle.y-1]=" "
	# 	scene.scenematrix[paddle.x][paddle.y+k]='#'

	# #expand paddle
	# if(ptime==5):
	# 	paddle.y=paddle.y+1
	# 	scene.scenematrix[paddle.x][paddle.y-1]=" "
	# 	scene.scenematrix[paddle.x][paddle.y+7]='##'

	#paddle movement
	if input == 'a' or input =='A':
		scene.leftmove(paddle)
	elif input == 'd' or input == 'D':
		scene.rightmove(paddle)
	elif input == 'q':
		os.system('clear')
		print(Fore.RED + 'Thanks for playing:)')
		print(Fore.GREEN+ "time: "+str(ptime)+RESET)
		quit()
	
	#checking collision
	scene.collision(ball,paddle)
