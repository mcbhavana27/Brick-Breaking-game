from colorama import *
from enemies import *
from values import *
from board import *
import os

SCREEN=210

os.system('clear')
def title(SCREEN):
    print(Fore.WHITE + Back.BLUE + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.BLUE + Style.BRIGHT + "BRICK BREAKER".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.BLUE+ Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)





''' set obstacles in a position '''

# def generatescene(scene):
#     # clouds
#     x = 0
#     for y in range(10, 500, 30):
#         cloud = Cloud(3,6)
#         x = (x+2) % 7
#         cloud.setPos(scene, x, y)
     # walls and pits

    # Pit.draw_pit(scene, 15, 78)

    # Wall.draw_wall(scene, 6, 9, 108)
    # Pit.draw_pit(scene, 8, 117)
    # Wall.draw_wall(scene, 4, 17, 125)
    # Pit.draw_pit(scene, 8, 142)

    # wall = Wall(3, 10)
    # wall.setPos(scene, groundx-8, 170)

    # # place enemy on top
    # wall = Wall(3, 15)
    # wall.setPos(scene, groundx-10, 186)

    # Pit.draw_pit(scene, 14, 188)

    # wall = Wall(3, 10)
    # wall.setPos(scene, groundx-8, 210)

    # Pit.draw_pit(scene, 15, 230)

    # wall = Wall(3, 5)
    # wall.setPos(scene, groundx-7, 233)

    # Wall.draw_wall(scene, 6, 10, 245)

    # wall = Wall(3, 7)
    # wall.setPos(scene, groundx-13, 258)

    # Pit.draw_pit(scene, 15, 255)
    # Wall.draw_wall(scene, 15, 10, 270)

    # wall = Wall(4, 23)
    # wall.setPos(scene, groundx-19, 285)
    # wall = Wall(3, 22)
    # wall.setPos(scene, groundx-27, 300)

    # Pit.draw_pit(scene, 50, 280)

    # Wall.draw_wall(scene, 15, 15, 330)
    # Pit.draw_pit(scene, 10, 345)
    # Wall.draw_wall(scene, 6, 10, 355)
    # Pit.draw_pit(scene, 10, 365)

    # Pit.draw_pit(scene, 100, 390)

    # wall = Wall(3, 20)
    # wall.setPos(scene, groundx-10, 390)

    # wall = Wall(3, 20)
    # wall.setPos(scene, groundx-18, 400)

    # wall = Wall(3, 20)
    # wall.setPos(scene, groundx-27, 410)

    # wall = Wall(3, 20)
    # wall.setPos(scene, groundx-10, 430)

    # wall = Wall(3, 20)
    # wall.setPos(scene, groundx-20, 440)

    # wall = Wall(3, 13)
    # wall.setPos(scene, groundx-25, 464)

    # wall = Wall(3, 5)
    # wall.setPos(scene, groundx-8, 480)
