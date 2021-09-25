# This must be run using python3 snake.py rather than python3.8 snake.py

# ----- GLOBALS -----
# imports
import pygame
pygame.init()
import time
import random
from datetime import datetime

# inputs
width = 30
dis_width_input = 800
dis_height_input = 800
difficulty = 8
difficulty_increase = 0.2
score = 0

# color creation
green = (0, 225, 0)
yellow = (225, 225, 10)
black = (0, 0, 0)
white = (225, 225, 225)
blue = (0, 0, 225)
red = (225, 0, 0)
pink = (255, 192, 203)

# necessary equations
clock = pygame.time.Clock()
game_over = False
snake_list = []
snake_length = 2

# display creation and caption creation.
dis_width = round(dis_width_input / width) * width
dis_height = round(dis_height_input / width) * width
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Chloé the Snake")

# snake starting position and initial change
divx = dis_width / 2
divy = dis_height / 2
discx = divx % width
discy = divy % width
x1 = divx + discx
y1 = divy + discy
x2 = 0
y2 = 0

# initial food position
foodw = width
foodx = round(random.randrange(0, (dis_width - width)) / width) * width
foody = round(random.randrange(0, (dis_height - width)) / width) * width

# loop
while not game_over:
    # movement of snake head, and quiting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x2 = -width
                y2 = 0
            elif event.key == pygame.K_RIGHT:
                x2 = width
                y2 = 0
            elif event.key == pygame.K_UP:
                x2 = 0
                y2 = -width
            elif event.key == pygame.K_DOWN:
                x2 = 0
                y2 = width
    x1 += x2
    y1 += y2

    # death by going off screen
    if x1 < 0 or x1 >= dis_width or y1 < 0 or y1 >= dis_height:
        game_over = True

    # creating new food positions
    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, (dis_width - width)) / width) * width
        foody = round(random.randrange(0, (dis_height - width)) / width) * width
        snake_length += 1
        difficulty += difficulty_increase

    #drawing the display, food, and head of snake, and the score text
    dis.fill(black)
    pygame.draw.rect(dis, red, [foodx, foody, width, width])
    pygame.draw.rect(dis, yellow,[x1, y1, width, width])
    score_font = pygame.font.SysFont("comicsansms", 35)
    text = score_font.render(f"Score: {snake_length - 2}   Speed: {round(difficulty, 1)}", True, white)
    gettext = text.get_rect()
    dis.blit(text, gettext)

    # drawing the rest of the snake, and death if head into self.
    co_list = []
    co_list.append(x1)
    co_list.append(y1)
    snake_list.append(co_list)
    if len(snake_list) >= snake_length:
        del snake_list[0]
    l = len(snake_list)
    if l >= 2:
        for num in [*range(2, l + 1)]:
            xx = snake_list[-num][-2]
            yy = snake_list[-num][-1]
            if xx == x1 and yy == y1:
                game_over = True
            pygame.draw.rect(dis, green, [xx, yy, width, width])

    # updating the display and time keeping
    pygame.display.update()
    clock.tick(difficulty)


#creation of history
file = open("snake_history.txt", "w")
now = datetime.now()
file.write(f"\n\n**********\nScore: {snake_length - 2}\nSpeed: {round(difficulty, 1)}\nDate: {now}\n**********")
file.close()
rfile = open("snake_history.txt")
readfile = rfile.read()
print(readfile)


# quit program
pygame.quit()
quit()

# end of script
