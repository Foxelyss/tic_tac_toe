import pygame

resolution = [600, 600]
map = [0, 0, 0], [0, 0, 0], [0, 0, 0]
game_ended = False

whichplayerturn = 1

pygame.init()

timer = pygame.time.Clock()

tic = pygame.image.load("tic.png")
tac = pygame.image.load("tac.png")

screen = pygame.display.set_mode(resolution)

pygame.display.set_caption("Крестики,нолики")

white_color = (255, 255, 255)
red_color = (255, 0, 12)


def draw_white_line(start, end):
    pygame.draw.line(screen, white_color, start, end, 2)


def draw_red_line(start, end):
    pygame.draw.line(screen, red_color, start, end, 4)


def draw_diagonal_lines():
    draw_white_line(((resolution[0] / 3), 0), ((resolution[0] / 3), resolution[1]))
    draw_white_line((((resolution[0] / 3) * 2), 0), (((resolution[0] / 3) * 2), resolution[1]))


def draw_horizontal_lines():
    draw_white_line((0, (resolution[1] / 3)), (resolution[0], (resolution[1] / 3)))
    draw_white_line((0, ((resolution[1] / 3) * 2)), (resolution[0], ((resolution[1] / 3) * 2)))


def draw_grid():
    draw_diagonal_lines()
    draw_horizontal_lines()


def draw_tic(y):
    for x in range(3):
        if map[y][x] == 1:
            screen.blit(
                tic,
                (
                    (resolution[0] / 3) * (x + 1) - resolution[0] / 3,
                    (resolution[1] / 3) * (y + 1) - resolution[1] / 3,
                ),
            )


def draw_tac(y):
    for x in range(3):
        if map[y][x] == 2:
            screen.blit(
                tac,
                (
                    (resolution[0] / 3) * (x + 1) - resolution[0] / 3,
                    (resolution[1] / 3) * (y + 1) - resolution[1] / 3,
                ),
            )


def test_horizontal_win(b):
    global game_ended

    if map[b][0] == map[b][1] == map[b][2] != 0:
        draw_red_line(
            (0, ((resolution[1] / 3) * (b + 1) - (resolution[1] / 3) / 2)),
            (resolution[0], ((resolution[1] / 3) * (b + 1) - (resolution[1] / 3) / 2)),
        )
        game_ended = True


def test_vertical_win(b):
    global game_ended

    if map[0][b] == map[1][b] == map[2][b] != 0:
        draw_red_line(
            (((resolution[0] / 3) * (b + 1) - (resolution[0] / 3) / 2), 0),
            (((resolution[1] / 3) * (b + 1) - (resolution[1] / 3) / 2), resolution[1]),
        )
        game_ended = True


def test_diagonal_lines():
    global game_ended

    if map[0][0] == map[2][2] == map[1][1] != 0:
        draw_red_line((0, 0), (resolution[0], resolution[1]))
        game_ended = True
    elif map[0][2] == map[2][0] == map[1][1] != 0:
        draw_red_line((resolution[0], 0), (0, resolution[1]))
        game_ended = True


def write_piece_if_empty(y, x, flag):
    global map
    if map[y][x] == 0 and not game_ended:
        map[y][x] = flag


def clear_map():
    global map, game_ended
    game_ended = False
    map = [0, 0, 0], [0, 0, 0], [0, 0, 0]
    screen.fill((0, 0, 0))


def change_player():
    global whichplayerturn
    if whichplayerturn == 1:
        whichplayerturn = 2
    else:
        whichplayerturn = 1


run = True
while run:
    for event in pygame.event.get():  # Handling events
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_KP_0:
                    clear_map()
                case pygame.K_KP_1:
                    write_piece_if_empty(2, 0, whichplayerturn)
                    change_player()
                case pygame.K_KP_2:
                    write_piece_if_empty(2, 1, whichplayerturn)
                    change_player()
                case pygame.K_KP_3:
                    write_piece_if_empty(2, 2, whichplayerturn)
                    change_player()
                case pygame.K_KP_4:
                    write_piece_if_empty(1, 0, whichplayerturn)
                    change_player()
                case pygame.K_KP_5:
                    write_piece_if_empty(1, 1, whichplayerturn)
                    change_player()
                case pygame.K_KP_6:
                    write_piece_if_empty(1, 2, whichplayerturn)
                    change_player()
                case pygame.K_KP_7:
                    write_piece_if_empty(0, 0, whichplayerturn)
                    change_player()
                case pygame.K_KP_8:
                    write_piece_if_empty(0, 1, whichplayerturn)
                    change_player()
                case pygame.K_KP_9:
                    write_piece_if_empty(0, 2, whichplayerturn)
                    change_player()

    for y in range(3):
        draw_tac(y)
        draw_tic(y)
    for y in range(3):
        test_horizontal_win(y)
        test_vertical_win(y)

    test_diagonal_lines()

    draw_grid()
    pygame.display.update()
    timer.tick(30)
