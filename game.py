import time
from random import randint
import pygame

CLOCK = pygame.time.CLOCK()

#Initialize
pygame.init()
w = 1366
h = 768

AUTOMATE = 0

icon = pygame.image.load("img/icon.jpg")
GD = pygame.display.set_mode((w, h), pygame.RESIZABLE)
pygame.display.set_caption("Snakes N' Ladders 2")
pygame.display.set_icon(icon)
pygame.display.update()

#Graphics:
BLACK = (10, 10, 10)
WHITE = (250, 250, 250)
RED = (200, 0, 0)
B_RED = (240, 0, 0)
GREEN = (0, 200, 0)
B_GREEN = (0, 230, 0)
BLUE = (0, 0, 200)
GREY = (50, 50, 50)
YELLOW = (150, 150, 0)
PURPLE = (43, 3, 132)
B_PURPLE = (60, 0, 190)

board = pygame.image.load("img/Snakes-and-Ladders-Bigger.jpg")
DICE1 = pygame.image.load("img/Dice1.png")
DICE2 = pygame.image.load("img/Dice2.png")
DICE3 = pygame.image.load("img/Dice3.png")
DICE4 = pygame.image.load("img/Dice4.png")
DICE5 = pygame.image.load("img/Dice5.png")
DICE6 = pygame.image.load("img/Dice6.png")

REDGOTI = pygame.image.load("img/REDGOTI.png")
YELLOWGOTI = pygame.image.load("img/YELLOWGOTI.png")
GREENGOTI = pygame.image.load("img/GREENGOTI.png")
BLUEGOTI = pygame.image.load("img/BLUEGOTI.png")
menubg = pygame.image.load("img/menu.jpg")
p = pygame.image.load("img/playbg.jpg")
INTRO_PIC = pygame.image.load("img/intropic.png")
CREDITS_PIC = pygame.image.load("img/credits.jpg")

pygame.mixer.music.load("wav/music.wav")
snakesound = pygame.mixer.Sound("wav/snake.wav")
WIN = pygame.mixer.Sound("wav/WIN.wav")
lose = pygame.mixer.Sound("wav/lose.wav")
ladder = pygame.mixer.Sound("wav/ladder.wav")

#mouse pos
mouse = pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()


#Message displaying for buttons
def message_display(text, x, y, fs):
    LARGETEXT = pygame.font.Font('freesansbold.ttf', fs)
    TEXTSURF, TextRect = text_objects(text, LARGETEXT)
    TextRect.center = (x, y)
    GD.blit(TEXTSURF, TextRect)


def text_objects(text, font):
    TEXTSURFACE = font.render(text, True, WHITE)
    return TEXTSURFACE, TEXTSURFACE.get_rect()

#Message displaying for field
def message_display1(text, x, y, fs, c):
    LARGETEXT = pygame.font.Font('freesansbold.ttf', fs)
    TEXTSURF, TextRect = text_objects1(text, LARGETEXT)
    TextRect.center = (x, y)
    GD.blit(TEXTSURF, TextRect)
def text_objects1(text, font, c):
    TEXTSURFACE = font.render(text, True, c)
    return TEXTSURFACE, TEXTSURFACE.get_rect()

#Goti movement function
def goti(a):
    l1 = [[406, 606], [456, 606], [506, 606], [556, 606], [606, 606],
          [656, 606], [706, 606], [756, 606], [806, 606], [856, 606],
          [906, 606], [906, 560], [856, 560], [806, 560], [756, 560],
          [706, 560], [656, 560], [606, 560], [556, 560], [506, 560],
          [456, 560], [456, 506], [506, 506], [556, 506], [606, 506],
          [656, 506], [706, 506], [756, 506], [806, 506], [856, 506],
          [906, 506], [906, 460], [856, 460], [806, 460], [756, 460],
          [706, 460], [656, 460], [606, 460], [556, 460], [506, 460],
          [456, 460], [456, 406], [506, 406], [556, 406], [606, 406],
          [656, 406], [706, 406], [756, 406], [806, 406], [856, 406],
          [906, 406], [906, 360], [856, 360], [806, 360], [756, 360],
          [706, 360], [656, 360], [606, 360], [556, 360], [506, 360],
          [456, 360], [456, 306], [506, 306], [556, 306], [606, 306],
          [656, 306], [706, 306], [756, 306], [806, 306], [856, 306],
          [906, 306], [906, 260], [856, 260], [806, 260], [756, 260],
          [706, 260], [656, 260], [606, 260], [556, 260], [506, 260],
          [456, 260], [456, 206], [506, 206], [556, 206], [606, 206],
          [656, 206], [706, 206], [756, 206], [806, 206], [856, 206],
          [906, 206], [906, 160], [856, 160], [806, 160], [756, 160],
          [706, 160], [656, 160], [606, 160], [556, 160], [506, 160],
          [456, 160]]
    l2 = l1[a]
    x = l2[0] - 25
    y = l2[1] - 25
    return x, y

def text_objects1(text, font):
    TEXTSURFACE = font.render(text, True, BLACK)
    return TEXTSURFACE, TEXTSURFACE.get_rect()

#Ladder check
def ladders(x):
    if x == 1:
        return 38
    elif x == 4:
        return 14
    elif x == 9:
        return 31
    elif x == 28:
        return 84
    elif x == 21:
        return 42
    elif x == 51:
        return 67
    elif x == 80:
        return 99
    elif x == 72:
        return 91
    else:
        return x

#Snake Check
def snakes(x):
    if x == 17:
        return 7
    elif x == 54:
        return 34
    elif x == 62:
        return 19
    elif x == 64:
        return 60
    elif x == 87:
        return 36
    elif x == 93:
        return 73
    elif x == 95:
        return 75
    elif x == 98:
        return 79
        return x

def dice(a):
    if a == 1:
        a = DICE1
    elif a == 2:
        a = DICE2
    elif a == 3:
        a = DICE3
    elif a == 4:
        a = DICE4
    elif a == 5:
        a = DICE5
    elif a == 6:
        a = DICE6

    time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - time < 1000:
        GD.blit(a, (300, 500))
        pygame.display.update()
#for mute and unmute
def BUTTON2(text, xmouse, ymouse, x, y, w, h, i, a, fs):
    #mouse pos
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > xmouse > x and y + h > ymouse > y:
        pygame.draw.rect(GD, a, [x - 2.5, y - 2.5, w + 5, h + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            return True
    else:
        pygame.draw.rect(GD, i, [x, y, w, h])
    message_display(text, (x + w + x) / 2, (y + h + y) / 2, fs)
#Buttons for playing:
def BUTTON1(text, xmouse, ymouse, x, y, w, h, i, a, fs):
    #mouse pos
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > xmouse > x and y + h > ymouse > y:
        pygame.draw.rect(GD, a, [x - 2.5, y - 2.5, w + 5, h + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            return True
    else:
        pygame.draw.rect(GD, i, [x, y, w, h])
    message_display(text, (x + w + x) / 2, (y + h + y) / 2, fs)
#Turn
def turn(score, l, s):
    a = randint(1, 6)#player dice roll
    if a == 6:
        six = bool(True)
    else:
        six = bool(False)
    p = dice(a)
    score += a
    if score <= 100:
        lad = ladders(score) #checking for ladders for player
        if lad != score:
            l = True
            pygame.mixer.Sound.play(ladder)
            time = pygame.time.get_ticks()
            score = lad
        snk = snakes(score)
        if snk != score: #checking for snakes for player
            s = True
            pygame.mixer.Sound.play(snakesound)
            score = snk
    else: #checks if player score is not grater than 100
        score -= a
        time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time < 1500:
            message_display1("Can't move!", 650, 50, 35, BLACK)
            pygame.display.update()
    return score, l, s, six
#Quitting:
def Quit():
    pygame.quit()
    quit()

def automatefunction():
    AUTOMATE = 1
#Buttons:
def button(text, xmouse, ymouse, x, y, w, h, i, a, fs, b):
    if x + w > xmouse > x and y + h > ymouse > y:
        pygame.draw.rect(GD, a, [x - 2.5, y - 2.5, w + 5, h + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if b == 1:
                options()
            elif b == 5:
                return 5
            elif b == 0:
                Quit()
            elif b == "s" or b == 2 or b == 3 or b == 4:
                return b
            elif b == 7:
                options()
            else:
                return True
    else:
        pygame.draw.rect(GD, i, [x, y, w, h])
    message_display(text, (x + w + x) / 2, (y + h + y) / 2, fs)


def BUTTON3(text, xmouse, ymouse, x, y, w, h, i, a, fs):
    if x + w > xmouse > x and y + h > ymouse > y:
        pygame.draw.rect(GD, a, [x - 2.5, y - 2.5, w + 5, h + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            automatefunction()
    else:
        pygame.draw.rect(GD, i, [x, y, w, h])
    message_display(text, (x + w + x) / 2, (y + h + y) / 2, fs)
#def pause():
    #j=True
    #while j:
        #mouse pos
        #mouse=pygame.mouse.get_pos()
        #click=pygame.mouse.get_pressed()
        #GD.blit(pause_bg,(0,0))
        #mouse=pygame.mouse.get_pos()
        #click=pygame.mouse.get_pressed()
        #if button("Resume",mouse[0],mouse[1],(w/2)-150,350,300,50,GREEN,B_GREEN,30,10):
            #j=False
        #if button("Main Menu",mouse[0],mouse[1],(w/2)-150,500,300,50,red,B_RED,30,10):
            #main()
        #pygame.display.update()
def intro():
    time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - time < 1000:
        GD.blit(INTRO_PIC, (0, 0))
        pygame.display.update()
    return
def credit():
    while True:
        GD.blit(CREDITS_PIC, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
        #mouse pos
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if button("Back", mouse[0], mouse[1], w/2-100, 700, 200, 50, RED, B_RED, 25, 20):
            main()
        pygame.display.update()
#Main Menu
def main():
    pygame.mixer.music.play(-1)
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()

        #mouse pos
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        GD.blit(menubg, (0, 0))
        button("Play", mouse[0], mouse[1], (w / 2 - 100) - 200, (h / 2) + 300, 200, 50,
              	GREEN, B_GREEN, 25, 1)
        button("Quit", mouse[0], mouse[1], (w / 2 - 100) + 200, (h / 2) + 300, 200, 50,
        	      RED, B_RED, 25, 0)
        mouse = pygame.mouse.get_pos()
        if BUTTON2("Mute Music", mouse[0], mouse[1], 1166, 0, 200, 50, PURPLE, B_PURPLE, 25):
            pygame.mixer.music.pause()
        if BUTTON2("Play Music", mouse[0], mouse[1], 1166, 75, 200, 50, PURPLE, B_PURPLE, 25):
            pygame.mixer.music.unpause()
        if BUTTON2("Credits", mouse[0], mouse[1], 1166, 150, 200, 50, PURPLE, B_PURPLE, 25):
            credit()
        pygame.display.update()

#Options Menu:
def options():
    flag = True
    while flag == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()


        #mouse pos
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        BUTTON1 = BUTTON2 = BUTTON3 = BUTTON4 = BUTTON5 = -1
        GD.blit(menubg, (0, 0))
        #Single player button
        BUTTON1 = button("Single Player", mouse[0], mouse[1], (w/2-150), 225, 300, 50, GREEN,
                         B_GREEN, 30, "s")
        #2 player button
        BUTTON2 = button("2 Players", mouse[0], mouse[1], (w/2)-150, 325, 300, 50, GREEN,
                         B_GREEN, 30, 2)
        #3 player
        BUTTON3 = button("3 Players", mouse[0], mouse[1], (w/2)-150, 425, 300, 50, GREEN,
                         B_GREEN, 30, 3)
        #4 player
        BUTTON4 = button("4 Players", mouse[0], mouse[1], (w/2)-150, 525, 300, 50, GREEN,
                         B_GREEN, 30, 4)
        #Back button
        BUTTON5 = button("Back", mouse[0], mouse[1], (w/2)-150, 625, 300, 50, RED, B_RED, 30, 5)
        if BUTTON5 == 5:
            main()
        if BUTTON1 == "s":
            play(21)
        if BUTTON2 == 2:
            play(2)
        if BUTTON3 == 3:
            play(3)
        if BUTTON4 == 4:
            play(4)
        pygame.display.update()
options()

def play(b):
    b6 = -1
    time = 3000
    if b6 == 7:
        options()
    GD.blit(p, (0, 0))
    GD.blit(board, (w / 2 - 250, h / 2 - 250))
    xcr = xcy = xcg = xcb = 406 - 25
    ycr = ycy = ycg = ycb = 606 - 25
    GD.blit(REDGOTI, (xcy, ycy))
    if  5 > b > 1 or b == 21:
        GD.blit(YELLOWGOTI, (xcy, ycy))
    if 5 > b > 2 or b == 21:
        GD.blit(GREENGOTI, (xcg, ycg))
    if 5 > b > 2:
        GD.blit(BLUEGOTI, (xcb, ycb))
    p1 = "Player 1"
    p1score = 0
    if b == 21:
        p2 = "Computer"
        p2score = 0
    if 5 > b > 1:
        p2 = "Player 2"
        p2score = 0
    if 5 > b > 2:
        p3 = "Player 3"
        p3score = 0
    if 5 > b > 3:
        p4 = "Player 4"
        p4score = 0
    t = 1
    play = True
    while True:

        l = False
        s = False
        time = 3000
        GD.blit(p, (0, 0))
        GD.blit(board, (w/2-250, h/2-250))
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            # Reduced nested loop here [Amal]
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN
             			                             and event.key == pygame.K_ESCAPE):
                Quit()
        if b == 21:
            #(player,score,text,xmouse,ymouse,x,y,w,h,i,a,fs)
            if BUTTON1("Player 1", mouse[0], mouse[1], 100, 700, 200, 50, RED, GREY, 30):
                print mouse[0], mouse[1]
                if t == 1:
                    p1score, l, s, six = turn(p1score, l, s)
                    if not six:
                        t += 1
                    xcr, ycr = goti(p1score)
                    if p1score == 100:
                        time = pygame.time.get_ticks()
                        while pygame.time.get_ticks()-time < 2000:
                            message_display1("Player 1 Wins", 650, 50, 50, BLACK)
                            pygame.mixer.Sound.play(WIN)
                            pygame.display.update()
                        break
            BUTTON1("Computer", mouse[0], mouse[1], 400, 700, 200, 50, YELLOW, GREY, 30)
            if True:
                if t == 2:
                    p2score, l, s, six = turn(p2score, l, s)
                    xcy, ycy = goti(p2score)
                    if not six:
                        t += 1
                        if b < 3 or b == 21:
                            t = 1
                    if p2score == 100:
                        time = pygame.time.get_ticks()
                        while pygame.time.get_ticks()-time < 2000:
                            message_display1("Computer Wins", 650, 50, 50, BLACK)
                            pygame.mixer.Sound.play(lose)
                            pygame.display.update()
                        break
        if 5 > b > 1:
            if BUTTON1("Player 1", mouse[0], mouse[1], 100, 700, 200, 50, RED, GREY, 30):
                if t == 1:
                    p1score, l, s, six = turn(p1score, l, s)
                    xcr, ycr = goti(p1score)
                    if not six:
                        t += 1
                    if p1score == 100:
                        time = pygame.time.get_ticks()
                        while pygame.time.get_ticks()-time < 2000:
                            message_display1("Player 1 Wins", 650, 50, 50, BLACK)
                            pygame.mixer.Sound.play(WIN)
                            pygame.display.update()
                        break
            if BUTTON1("Player 2", mouse[0], mouse[1], 400, 700, 200, 50, YELLOW, GREY, 30):
                if t == 2:
                    p2score, l, s, six = turn(p2score, l, s)
                    xcy, ycy = goti(p2score)
                    if not six:
                        t += 1
                        if b < 3:
                            t = 1
                    if p2score == 100:
                        time = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time < 2000:
                            message_display1("Player 2 Wins", 650, 50, 50, BLACK)
                            pygame.mixer.Sound.play(WIN)
                            pygame.display.update()
                        break
        if 5 > b > 2:
            if BUTTON1("Player 3", mouse[0], mouse[1], 700, 700, 200, 50, GREEN, GREY, 30):
                if t == 3:
                    p3score, l, s, six = turn(p3score, l, s)
                    xcg, ycg = goti(p3score)
                    if not six:
                        t += 1
                        if b < 4:
                            t = 1
                    if p3score == 100:
                        time = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time < 2000:
                            message_display1("Player 3 Wins", 650, 50, 50, BLACK)
                            pygame.mixer.Sound.play(WIN)
                            pygame.display.update()
                        break
        if 5 > b > 3:
            if BUTTON1("Player 4", mouse[0], mouse[1], 1000, 700, 200, 50, BLUE, GREY, 30):
                if t == 4:
                    p4score, l, s, six = turn(p4score, l, s)
                    xcb, ycb = goti(p4score)
                    if not six:
                        t += 1
                        if b < 5:
                            t = 1
                    if p4score == 100:
                        time = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time < 2000:
                            message_display1("Player 4 Wins", 650, 50, 50, BLACK)
                            pygame.mixer.Sound.play(WIN)
                            pygame.display.update()
                        break
        b6 = button("Back", mouse[0], mouse[1], 0, 0, 200, 50, RED, B_RED, 30, 7)
        BUTTON4 = BUTTON3("Test", mouse[0], mouse[1], 1166, 0, 200, 50, RED, B_RED, 30)
        GD.blit(REDGOTI, (xcr, ycr))
        if 5 > b > 1 or b == 21:
            GD.blit(YELLOWGOTI, (xcy + 2, ycy))
        if 5 > b > 2:
            GD.blit(GREENGOTI, (xcg + 4, ycg))
        if 5 > b > 3:
            GD.blit(BLUEGOTI, (xcb + 6, ycb))
        if l:
            time = pygame.time.get_ticks()
            while pygame.time.get_ticks()-time < 2000:
                message_display1("There's a Ladder!", 650, 50, 35, BLACK)
                pygame.display.update()
        if s:
            time = pygame.time.get_ticks()
            while pygame.time.get_ticks()-time < 2000:
                message_display1("There's a Snake!", 650, 50, 35, BLACK)
                pygame.display.update()
        CLOCK.tick(7)
        pygame.display.update()
intro()
main()
