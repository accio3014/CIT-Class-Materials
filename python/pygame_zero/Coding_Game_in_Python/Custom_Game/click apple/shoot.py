# shoot.py
import pgzrun
from random import randint

apple = Actor("apple")
score = 0

def draw():
    screen.clear()
    apple.draw()

def place_apple(): 
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)

def on_mouse_down(pos): 
    global score

    if apple.collidepoint(pos): 
        score += 1

        print("Good shot!")
        place_apple()
    else:
        print("You missed!") 
        print("Your score :", score) 
        quit()


place_apple()
pgzrun.go()