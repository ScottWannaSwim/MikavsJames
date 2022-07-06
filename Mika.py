import pygame,sys
import random
pygame.init()
FPS = 30
clock = pygame.time.Clock()

SCREENWIDTH = 800
SCREENHEIGHT = 600
RED = (255,0,0)
screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
title = pygame.display.set_caption("Tình yêu của Mika")
icon = pygame.image.load("love.png")
pygame.display.set_icon(icon)
background = pygame.image.load("background.png")
def display_background():
    screen.blit(background,(0,0))
# 
scale = 0.2
catImg = pygame.image.load("Mika.png")
catImg = pygame.transform.scale(catImg,(catImg.get_width()*scale,catImg.get_height()*scale))
catx = 400
caty= 500
catx_change = 0
caty_change = 0

def display_cat(x,y):
    screen.blit(catImg,(x,y))
#James
scale = 0.2
humanImg = []
humanx = []
humany = []
humanx_change = []
humany_change = []
num_of_humans = 5
image = pygame.image.load("James.png")
img = pygame.transform.scale(image,(image.get_width()*scale,image.get_height()*scale))
for i in range(num_of_humans):
    humanImg.append(img)
    humanx.append(random.randint(100,700))
    humany.append(random.randint(50,100))
    humanx_change.append(5)
    humany_change.append(40)
def display_human(x,y,i):
    screen.blit(humanImg[i],(x,y))

heartImg = pygame.image.load("heart.png")
heart_rect = heartImg.get_rect()
heartx = catx
hearty= 500
heartx_change = 0
hearty_change = -7

ban = False

def display_heart(x,y):
    global ban
    ban = True
    screen.blit(heartImg,(x+16,y+10))

running = True
screen_y = 0

score_value = 0
font = pygame.font.SysFont("Arial",30)
big_font = pygame.font.SysFont("Arial",70)

while running:
    screen.fill(RED)
    display_background()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                catx_change = -5
            if event.key == pygame.K_RIGHT:
                catx_change = 5
            if event.key == pygame.K_SPACE:
                if ban == False:
                    heartx = catx
                    display_heart(heartx,hearty)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                catx_change = 0
           
    # cat 
    if catx <= 0:
        catx = 0
    elif catx >= 716:
        catx = 716

    catx += catx_change
    display_cat(catx,caty)

    # heart
    heart_rect.topleft = (heartx,hearty)
    if ban:
        hearty += hearty_change
        display_heart(heartx,hearty)

    if hearty <= -30:
        hearty = caty
        ban = False

    # James
    for i in range(num_of_humans):

        # game over
        if humany[i] >= 200:
            heart_x = -1000
            heart_y = 0
            for j in range(num_of_humans):
                humany[j] = 2000
            catx_change = 0
            pygame.draw.rect(screen,(255,0,0),(0,0,SCREENWIDTH,screen_y))
            if screen_y <= SCREENHEIGHT:
                screen_y += 1
            lose_game_word = big_font.render("Thua",True,(255,255,255))
            screen.blit(lose_game_word,(SCREENWIDTH//2 - 100,SCREENHEIGHT//2 - 70))

        if humanx[i] <= -10:
            humanx_change[i] = 5
            humany[i] += humany_change[i]
        if humanx[i] >= 740:
            humanx_change[i] = -5
            humany[i] += humany_change[i]
        humanx[i] += humanx_change[i]
        human_rect = humanImg[i].get_rect()
        human_rect.topleft = (humanx[i],humany[i])
        display_human(humanx[i],humany[i],i)

        if heart_rect.colliderect(human_rect):
            hearty = -100
            humanx[i] = random.randint(100,700)
            humany[i] = random.randint(50,100)
            score_value += 1

    # score
    score_word = font.render("SCORE x " + str(score_value),True,(255,255,255))
    screen.blit(score_word,(10,10))

    clock.tick(FPS)
    pygame.display.update()