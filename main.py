import pygame
#high priority
resolution = [600,600]
map = [0,0,0],[0,0,0],[0,0,0]
run = True
whichplayerturn = 1
#low priority
pygame.init()
timer = pygame.time.Clock()
tic = pygame.image.load("tic.png")
tac = pygame.image.load("tac.png")
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Крестики,нолики")
linecolor = (255,255,255)
red = (255,0,12)
#рисование
def DrawLine(start, end):
    pygame.draw.line(screen, linecolor, start, end, 2)
def DrawRedLine(start, end):
    pygame.draw.line(screen, red, start, end, 4)

def DrawDiagonalLines():
    #DrawLine((200, 0), (200, 600))
    #DrawLine((400, 0), (400, 600))
    DrawLine(((resolution[0] / 3),0),((resolution[0] / 3),resolution[1]))
    DrawLine((((resolution[0] / 3) * 2), 0), (((resolution[0] / 3) * 2), resolution[1]))
def DrawHorizontalLines():
    #DrawLine((0, 200), (600, 200))
    #DrawLine((0, 400), (600, 400))
    DrawLine((0, (resolution[1] / 3)), (resolution[0], (resolution[1]/3)))
    DrawLine((0, ((resolution[1] / 3) * 2)), (resolution[0], ((resolution[1] / 3)*2)))

def DrawTic(i):
    if map[i][0] == 1:
        screen.blit(tic, (((resolution[0] / 3) * 1 - resolution[0] / 3), (resolution[1] / 3) * (i + 1) - resolution[1] / 3))
    if map[i][1] == 1:
        screen.blit(tic, (((resolution[0] / 3) * 2 - resolution[0] / 3), (resolution[1] / 3) * (i + 1) - resolution[1] / 3))
    if map[i][2] == 1:
        screen.blit(tic, (((resolution[0] / 3) * 3 - resolution[0] / 3), (resolution[1] / 3) * (i + 1) - resolution[1] / 3))
def DrawTac(i):
    if map[i][0] == 2:
        screen.blit(tac, (((resolution[0] / 3) * 1 - resolution[0] / 3), (resolution[1] / 3) * (i + 1) - resolution[1] / 3))
    if map[i][1] == 2:
        screen.blit(tac, (((resolution[0] / 3) * 2 - resolution[0] / 3), (resolution[1] / 3) * (i + 1) - resolution[1] / 3))
    if map[i][2] == 2:
        screen.blit(tac, (((resolution[0] / 3) * 3 - resolution[0] / 3), (resolution[1] / 3) * (i + 1) - resolution[1] / 3))
#игровая логика
def TestHorizontalWin(b):
    if map[b][0] == 1 and map[b][1] == 1 and map[b][2] == 1:
        DrawRedLine((0,((resolution[1] / 3) * (b + 1) - (resolution[1] / 3) / 2)),(resolution[0],((resolution[1] / 3) * (b + 1) - (resolution[1] / 3) / 2)))

    elif map[b][0] == 2 and map[b][1] == 2 and map[b][2] == 2:
        DrawRedLine((0, ((resolution[1] / 3) * (b + 1) - (resolution[1] / 3) / 2)),(resolution[0], ((resolution[1] / 3) * (b + 1) - (resolution[1] / 3) / 2)))


def TestVerticalWin(b):
    if map[0][b] == 1 and map[1][b] == 1 and map[2][b] == 1:
        DrawRedLine((((resolution[0] / 3) * (b + 1) - (resolution[0] / 3) / 2),0),(((resolution[1] / 3) * (b + 1) - (resolution[1] / 3) / 2),resolution[1]))

    elif map[0][b] == 2 and map[1][b] == 2 and map[2][b] == 2:
        DrawRedLine((((resolution[0] / 3) * (b + 1) - (resolution[0] / 3) / 2), 0),(((resolution[1] / 3) * (b + 1) - (resolution[1] / 3) / 2), resolution[1]))

def TestDiagonalLines():
    if map[0][0] == 1 and map[2][2] == 1 and map[1][1] == 1:
        DrawRedLine((0,0),(resolution[0],resolution[1]))

    elif map[0][2] == 1 and map[2][0] == 1 and map[1][1] == 1:
        DrawRedLine((resolution[0], 0), (0, resolution[1]))

    elif map[0][0] == 2 and map[2][2] == 2 and map[1][1] == 2:
        DrawRedLine((0, 0), (resolution[0], resolution[1]))

    elif map[0][2] == 2 and map[2][0] == 2 and map[1][1] == 2:
        DrawRedLine((resolution[0], 0), (0, resolution[1]))



def WriteTacORTic(list,number,g):
    global map
    if map[list][number] == 0:
        map[list][number] = g

def ClearAll():
    global map
    map = [0,0,0],[0,0,0],[0,0,0]
    screen.fill((0,0,0))
def ChangePlayer():
    global whichplayerturn
    if whichplayerturn == 1:
        whichplayerturn = 2
    else:
        whichplayerturn = 1

i = 0
while run:
    if i > 2:
        i = 0
    for event in pygame.event.get():  # Handling events
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_0:
                ClearAll()
            elif event.key == pygame.K_KP_1:
                WriteTacORTic(2,0,whichplayerturn)
                ChangePlayer()
            elif event.key == pygame.K_KP_2:
                WriteTacORTic(2, 1, whichplayerturn)
                ChangePlayer()
            elif event.key == pygame.K_KP_3:
                WriteTacORTic(2, 2, whichplayerturn)
                ChangePlayer()
            elif event.key == pygame.K_KP_4:
                WriteTacORTic(1, 0, whichplayerturn)
                ChangePlayer()
            elif event.key == pygame.K_KP_5:
                WriteTacORTic(1, 1, whichplayerturn)
                ChangePlayer()
            elif event.key == pygame.K_KP_6:
                WriteTacORTic(1, 2, whichplayerturn)
                ChangePlayer()
            elif event.key == pygame.K_KP_7:
                WriteTacORTic(0, 0, whichplayerturn)
                ChangePlayer()
            elif event.key == pygame.K_KP_8:
                WriteTacORTic(0, 1, whichplayerturn)
                ChangePlayer()
            elif event.key == pygame.K_KP_9:
                WriteTacORTic(0, 2, whichplayerturn)
                ChangePlayer()
    DrawTac(i)
    DrawTic(i)

    TestDiagonalLines()
    TestHorizontalWin(i)
    TestVerticalWin(i)
    DrawDiagonalLines()
    DrawHorizontalLines()
    pygame.display.update()
    timer.tick(60)
    i = i + 1

