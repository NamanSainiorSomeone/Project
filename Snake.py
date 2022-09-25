from tkinter import *
import random
from turtle import window_height, window_width
from urllib.parse import _NetlocResultMixinStr

GAME_WIDTH =700
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COL = "light green"
FOOD_COLOR = "RED"
BACKGROUND = "BLACK"



class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.cords = []
        self.square = []
        for i in range (0,BODY_PARTS):
            self.cords.append([0,0])

        for x , y in self.cords:
            square = canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COL,tag='snake')
            self.square.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE
        self.cords = [x,y]

        canvas.create_oval(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=FOOD_COLOR,tag= "food")


def next_turn(snake , food):
    x,y = snake.cords[0]
    if direction== 'up':
        y-= SPACE_SIZE


    elif direction== 'down':
        y+= SPACE_SIZE


    elif direction== 'left':
        x-= SPACE_SIZE

    elif direction== 'right':
        x+= SPACE_SIZE

    snake.cords.insert(0,(x,y))
    square= canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COL)
    snake.square.insert(0,square)

    if x == food.cords[0] and y == food.cords[1]:
        global score

        score += 1

        label.config(text= "Score: {}".format(score))

        canvas.delete("food")

        food = Food()

    else:
        del snake.cords[-1]
        canvas.delete(snake.square[-1])
        del snake.square[-1]
    if check_col(snake):
        game_over()

    else:
    
        window.after(SPEED,next_turn,snake,food)
    
def change_dec(new_dec):
    global direction

    if new_dec == 'left':
        if direction!= 'right':
            direction = new_dec
    elif new_dec == 'right':
        if direction!= 'left':
            direction = new_dec
    elif new_dec == 'up':
        if direction!= 'down':
            direction = new_dec
    elif new_dec == 'down':
        if direction!= 'up':
            direction = new_dec


def check_col(snake):
    x,y = snake.cords[0]
    if x< 0 or x>= GAME_WIDTH:
        return True
    elif y< 0 or y>= GAME_WIDTH:
        return True
    for body_part in snake.cords[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    else :False

def game_over():
    
    canvas.delete(ALL)
    canvas.create_text(350,350,text='GAME OVER',fill='Green',font=('',60),tag='gameo')


window = Tk()
window.title("Snake")
window.resizable(False,False)


score = 0

direction = 'down'
label = Label(window,text='Score: {}'.format(score),font=( "", 30))
label.pack()

canvas = Canvas(window,bg=BACKGROUND,height=GAME_HEIGHT,width=GAME_WIDTH)
canvas.pack()


window.update()


window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x= int((screen_width/2) - (window_width/2))
y= int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")


window.bind('<Left>', lambda event: change_dec('left'))
window.bind('<Right>', lambda event: change_dec('right'))
window.bind('<Up>', lambda event: change_dec('up'))
window.bind('<Down>', lambda event: change_dec('down'))




snake = Snake()
food = Food()


next_turn(snake,food)

window.mainloop()
