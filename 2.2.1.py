import pygame
import random
import sys
import time

# sys.setrecursionlimit(10000)


def main():
    x_win = 800
    y_win = 600

    # x_win = 1920
    # y_win = 1080

    level = 5
    RED = (225, 0, 50)
    GREEN = (0, 225, 0)
    get_start_finish(x_win, y_win, level, RED, GREEN)


def get_start_finish(x_win, y_win, level, RED, GREEN):
    start_finish = []
    board = create_board(x_win, y_win)
    win = activate_init(x_win, y_win, RED, GREEN)
    # Что за мифическое число 2? Почему не 3?
    # Поидее подобные констатны нужно запихивать в переменные, что бы код был более читаем,
    # это относится ко всем таким магическим числам в коде
    while len(start_finish) != 2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    start_finish.append((event.pos))
                    if len(start_finish) == 1:
                        pygame.draw.line(win, GREEN, event.pos, event.pos, 1)
                        pygame.draw.circle(win, GREEN, event.pos, 5)
                        mark_on_field(start_finish[0][0], start_finish[0][1], 2, board)
                    else:
                        pygame.draw.line(win, RED, event.pos, event.pos, 1)
                        pygame.draw.circle(win, RED, event.pos, 5)
                        mark_on_field(start_finish[1][0], start_finish[1][1], 6, board)
                    pygame.display.update()
        pygame.time.delay(200)
    time.clock()
    print_way(start_finish,x_win, y_win, board, win, level)


def create_board(x_win, y_win):
    return [[0 for j in range(x_win)] for i in range(y_win)]


def activate_init(x_win, y_win, RED, GREEN):
    pygame.init()
    win = pygame.display.set_mode((x_win, y_win), pygame.FULLSCREEN)
    # win = pygame.display.set_mode((x_win, y_win))
    win.fill((0, 0, 0))
    pygame.display.update()
    pygame.display.set_caption("Генератор Лабиринтов 2.2")

    font = pygame.font.SysFont('arial', 15)
    text = font.render('Генератор лабиринта 2.2',True,GREEN)
    place = text.get_rect(center=(x_win//2, y_win//2))
    win.blit(text, place)
    text = font.render('Введите точку старта и точку финиша (ЛКМ)', True, GREEN)
    place = text.get_rect(center=(x_win//2, (y_win//2)+25))
    win.blit(text, place)
    text = font.render('Чтобы начать нажмите пробел', True, GREEN)
    place = text.get_rect(center=(x_win//2, (y_win//2)+50))
    win.blit(text, place)
    pygame.display.update()

    press = 0
    while press != 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    press = 1
    win.fill((0, 0, 0))
    pygame.display.update()
    return win


def print_field(board):
    for row in board:
        for col in row:
            print(col, end="  ")
        print()


def mark_on_field(x, y, symbol, board):
    board[y][x] = symbol
    return board


def go_left(x, y, long, board, win, way):
    if long < 0:
        pygame.draw.line(win, (225, 255, 255), [x + 1, y], [x - long, y], 1)
    else:
        pygame.draw.line(win, (225, 255, 255), [x - 1, y], [x - long, y], 1)
    pygame.display.update()

    i = 0
    while i != long:
        if long < 0:
            i -= 1
            x += 1
        else:
            x -= 1
            i += 1
        board = mark_on_field(x, y, 1, board)
        way.append((x, y))
    return board, win, way


def go_right(x, y, long, board, win, way):
    if long < 0:
        pygame.draw.line(win, (225, 255, 255), [x - 1, y], [x + long, y], 1)
    else:
        pygame.draw.line(win, (225, 255, 255), [x + 1, y], [x + long, y], 1)
    pygame.display.update()

    i = 0
    while i != long:
        if long < 0:
            x -= 1
            i -= 1
        else:
            x += 1
            i += 1
        board = mark_on_field(x, y, 1, board)
        way.append((x, y))
    return board, win, way


def go_up(x, y, long, board, win, way):
    if long < 0:
        pygame.draw.line(win, (225, 255, 255), [x, y + 1], [x, y - long], 1)
    else:
        pygame.draw.line(win, (225, 255, 255), [x, y - 1], [x, y - long], 1)
    pygame.display.update()

    i = 0
    while i != long:
        if long < 0:
            i -= 1
            y += 1
        else:
            i += 1
            y -= 1
        board = mark_on_field(x, y, 1, board)
        way.append((x, y))
    return board, win, way


def go_down(x, y, long, board, win, way):
    if long < 0:
        pygame.draw.line(win, (225, 255, 255), [x, y - 1], [x, y + long], 1)
    else:
        pygame.draw.line(win, (225, 255, 255), [x, y + 1], [x, y + long], 1)
    pygame.display.update()

    i = 0
    while i != long:
        if long < 0:
            i -= 1
            y -= 1
        else:
            i += 1
            y += 1
        board = mark_on_field(x, y, 1, board)
        way.append((x, y))
    return board, win, way


def print_way(start_finish, x_win, y_win, board, win, level):
    turns = []
    way = []
    x_s = start_finish[0][0]
    y_s = start_finish[0][1]

    x_f = start_finish[1][0]
    y_f = start_finish[1][1]

    a = random.randint(1, 2)
    if y_s < y_f:
        i_x = x_f - x_s
        i_y = y_f - y_s

        if a == 1:
            go_down(x_s, y_s, i_y // 2, board, win, way)
            turns.append((x_s, y_s + i_y // 2))
            go_right(x_s, y_s + i_y // 2, i_x // 2, board, win, way)
            turns.append((x_s + i_x // 2, y_s + i_y // 2))
            go_down(x_s + i_x // 2, y_s + i_y // 2, i_y - i_y // 2, board, win, way)
            turns.append((x_s + i_x // 2, y_f))
            go_right(x_s + i_x // 2, y_f, i_x - i_x // 2 - 1, board, win, way)

        if a == 2:
            go_right(x_s, y_s, i_x // 2, board, win, way)
            turns.append((x_s + i_x // 2, y_s))
            go_down(x_s + i_x // 2, y_s, i_y // 2, board, win, way)
            turns.append((x_s + i_x // 2, y_s + i_y // 2))
            go_right(x_s + i_x // 2, y_s + i_y // 2, i_x - i_x // 2, board, win, way)
            turns.append((x_f, y_s + i_y // 2))
            go_down(x_f, y_s + i_y // 2, i_y - i_y // 2 - 1, board, win, way)

    if y_s > y_f:
        i_x = x_f - x_s
        i_y = y_s - y_f

        if a == 1:
            go_up(x_s, y_s, i_y // 2, board, win, way)
            turns.append((x_s, y_s - i_y // 2))
            go_right(x_s, y_s - i_y // 2, i_x // 2, board, win, way)
            turns.append((x_s + i_x // 2, y_s - i_y // 2))
            go_up(x_s + i_x // 2, y_s - i_y // 2, i_y - i_y // 2, board, win, way)
            turns.append((x_s + i_x // 2, y_f))
            go_right(x_s + i_x // 2, y_f, i_x - i_x // 2 - 1, board, win, way)

        if a == 2:
            go_right(x_s, y_s, i_x // 2, board, win, way)
            turns.append((x_s + i_x // 2, y_s))
            go_up(x_s + i_x // 2, y_s, i_y // 2, board, win, way)
            turns.append((x_s + i_x // 2, y_s - i_y // 2))
            go_right(x_s + i_x // 2, y_s - i_y // 2, i_x - i_x // 2, board, win, way)
            turns.append((x_f, y_s - i_y // 2))
            go_up(x_f, y_s - i_y // 2, i_y - i_y // 2 - 1, board, win, way)

    get_random_points(turns, start_finish, board, win, way, level, x_win, y_win)


def get_random_points(turns, start_finish, board, win, way, level, x_win, y_win):
    points_level = []

    i = 0
    while i < 3 and i != level:
        point = turns[i]
        turns_list = check_turns(point, "way", board, x_win, y_win)
        get_random_turn(point, turns_list, start_finish, board, win, way, points_level, x_win, y_win)
        i += 1

    while i != level:
        coord = random.randint(0, len(way))
        point = way[coord]
        turns_list = check_turns(point, "way", board, x_win, y_win)
        if len(turns_list) != 0:
            get_random_turn(point, turns_list, start_finish, board, win, way, points_level, x_win, y_win)
            i += 1

    if len(points_level) != 0:
        while len(points_level) != 0:
            point = points_level[0]
            turns_list = check_turns(point, "way", board, x_win, y_win)
            get_random_turn(point, turns_list, start_finish, board, win, way, points_level, x_win, y_win)
            points_level.pop(0)

    mark_on_field(start_finish[0][0], start_finish[0][1], 2, board)
    mark_on_field(start_finish[1][0], start_finish[1][1], 6, board)

    t_gen = time.clock()
    print(" ")
    print("Информация: ")
    print("Время генерации лабиринта равно: {0}".format(t_gen))

    get_in(start_finish, board, win, t_gen, x_win, y_win)


def check_turns(point, location, board, x_win, y_win):
    x = point[0]
    y = point[1]
    turns_list = []

    if board[y - 1][x] == 0 and board[y - 1][x - 1] == 0 and board[y - 1][x + 1] == 0 and y - 2 > 0:
        if location == "way":
            turns_list.append("UP")
        elif board[y + 1][x] == 0:
            turns_list.append("UP")

    if board[y + 1][x] == 0 and board[y + 1][x - 1] == 0 and board[y + 1][x + 1] == 0 and y + 2 < y_win - 1:
        if location == "way":
            turns_list.append("DOWN")
        elif board[y - 1][x] == 0:
            turns_list.append("DOWN")

    if board[y][x - 1] == 0 and board[y - 1][x - 1] == 0 and board[y + 1][x - 1] == 0 and x - 2 > 0:
        if location == "way":
            turns_list.append("LEFT")
        elif board[y][x + 1] == 0:
            turns_list.append("LEFT")
    if board[y][x + 1] == 0 and board[y - 1][x + 1] == 0 and board[y + 1][x + 1] == 0 and x + 2 < x_win - 1:
        if location == "way":
            turns_list.append("RIGHT")
        elif board[y][x - 1] == 0:
            turns_list.append("RIGHT")
    return turns_list


def get_random_turn(point, turns_list, start_finish, board, win, way, points_level, x_win, y_win):
    x = point[0]
    y = point[1]
    k = 0

    repeat = random.randint(0, 1)
    if repeat == 1:
        points_level.append((x, y))

    if len(turns_list) > 0:
        # Что за магические переменные типа a,b ? Лучше их то же называть более осознано, я понимаю, что они временные,
        # но старайтесь их называть так, что бы потом через месяц посмотреть на код и вспомнить что они и зачем
        a = random.randint(0, len(turns_list) - 1)
        b = random.randint(0, 1)
        if turns_list[a] == "LEFT":
            long = random.randint(0, x - 3)
            while k != 1:
                if board[y][x - long - 1] == 1:
                    long -= 1
                if board[y - 1][x - long] == 1 or board[y + 1][x - long] == 1:
                    long -= 1
                else:
                    k = 1
            if b == 1:
                points_level.append((x - long, y))
            go_left(x, y, long, board, win, way)

        elif turns_list[a] == "RIGHT":
            long = random.randint(0, x_win - x - 3)
            while k != 1:
                if board[y][x + long + 1] == 1:
                    long -= 1
                if board[y - 1][x + long] == 1 or board[y + 1][x + long] == 1:
                    long -= 1
                else:
                    k = 1
            if b == 1:
                points_level.append((x + long, y))
            go_right(x, y, long, board, win, way)

        elif turns_list[a] == "DOWN":
            long = random.randint(0, y_win - y - 3)
            while k != 1:
                if board[y + long + 1][x] == 1:
                    long -= 1
                if board[y + long][x - 1] == 1 or board[y + long][x + 1] == 1:
                    long -= 1
                else:
                    k = 1
            if b == 1:
                points_level.append((x, y + long))
            go_down(x, y, long, board, win, way)

        elif turns_list[a] == "UP":
            long = random.randint(0, y-3)
            while k != 1:
                if board[y - long - 1][x] == 1:
                    long -= 1
                if board[y - long][x - 1] == 1 or board[y - long][x + 1] == 1:
                    long -= 1
                else:
                    k = 1
            if b == 1:
                points_level.append((x, y - long))
            go_up(x, y, long, board, win, way)

    return points_level


def waiting_close():
    print("Версия генератора лабиринта 2.2.1 (beta testing) ")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                exit()
        pygame.time.delay(200)

# _______________________________________________


X = 2
E = 6
Q = 9
T = 3


def get_in(start_finish, board, win, t_gen, x_win, y_win):
    # global level
    level = board
    x1 = start_finish[0][1]
    y1 = start_finish[0][0]
    x2 = start_finish[1][1]
    y2 = start_finish[1][0]

    screenshot = win.copy()
    rob = pygame.image.load("rob.png")
    rob_rect = rob.get_rect(bottomright=(start_finish[0][0] + 5, start_finish[0][1] + 5))
    win.blit(rob, rob_rect)
    pygame.display.update()
    get_ahead(x1, y1, x2, y2, screenshot, level, win, t_gen, x_win, y_win)


def mark_on_field_2(x1, y1, symbol, win, level, screenshot):
    level[x1][y1] = symbol

    print_ = random.randint(1, 20)
    if print_ == 1:
        win.blit(screenshot, (0, 0))
        rob = pygame.image.load("rob.png")
        rob_rect = rob.get_rect(bottomright=(y1 + 5,  x1 + 5))
        win.blit(rob, rob_rect)
        pygame.display.update()
    return level, win


def get_ahead(x1, y1, x2, y2, screenshot, level, win, t_gen, x_win, y_win):

    pygame.display.update()
    finish = []
    main = []   # старайтесь в рамках одного файла не использовать одинаковые наименования,
                # в данном случае есть уже функция main,в рамках этой программы ничего не сломается, но на будущее стоит учесть
    temp = []
    main.append((x1, y1))
    while True:
        pygame.display.update()

        if level[x1 + 1][y1] == 6:
            mark_on_field_2(x2, y2, Q, win, level, screenshot)
            x1 += 1
            main.append((x2, y2))
            finish.append((x2, y2))
            find_an_exit(finish, main, win, screenshot, t_gen, x_win, y_win)

        elif level[x1 - 1][y1] == 6:
            mark_on_field_2(x2, y2, Q, win, level, screenshot)
            x1 -= 1
            main.append((x2, y2))
            finish.append((x2, y2))
            find_an_exit(finish, main, win, screenshot, t_gen, x_win, y_win)

        elif level[x1][y1 + 1] == 6:
            mark_on_field_2(x2, y2, Q, win, level, screenshot)
            y1 += 1
            main.append((x2, y2))
            finish.append((x2, y2))
            find_an_exit(finish, main, win, screenshot, t_gen, x_win, y_win)

        elif level[x1][y1 - 1] == 6:
            mark_on_field_2(x2, y2, Q, win, level, screenshot)
            y1 -= 1
            main.append((x2, y2))
            finish.append((x2, y2))
            find_an_exit(finish, main, win, screenshot, t_gen, x_win, y_win)
        # какое-то нереально длинное условие, возможно оно и оправдано, но допустим,
        # если через неделю на него посмотреть то будет уже сложно вспомнить,что именно оно проверяет, что можно сделать
        # разбить эти условия на переменные и назвать их соотвествующе, например
            # validate_value = all(y1 > 0, level[x1][y1 - 1] == 1, level[x1 + 1][y1] == 1) в итоге эта переменная станет
            # True или False

        if y1 > 0 and level[x1][y1 - 1] == 1 and level[x1 + 1][y1] == 1 or y1 > 0 and level[x1][y1 - 1] == 1 and level[x1 + 1][y1] == 6 or y1 > 0 and level[x1][y1 - 1] == 6 and level[x1 + 1][y1] == 1:
            mark_on_field_2(x1, (y1 - 1), X, win, level, screenshot)
            y1 -= 1
            temp.append((x1, y1))
            get_ahead(x1, y1, x2, y2, screenshot, level, win, t_gen, x_win, y_win)
            pygame.display.update()
            while True:
                if y1 > 0 and level[x1][y1 - 1] == 1:
                    mark_on_field_2(x1, (y1 - 1), X, win, level, screenshot)
                    y1 -= 1
                    temp.append((x1, y1))

                elif y1 > 0 and level[x1][y1 + 1] == 1:
                    mark_on_field_2(x1, (y1 + 1), X, win, level, screenshot)
                    y1 += 1
                    temp.append((x1, y1))

                elif x1 > 0 and level[x1 + 1][y1] == 1:
                    mark_on_field_2((x1 + 1), y1, X, win, level, screenshot)
                    x1 += 1
                    temp.append((x1, y1))

                elif x1 > 0 and level[x1 - 1][y1] == 1:
                    mark_on_field_2((x1 - 1), y1, X, win, level, screenshot)
                    x1 -= 1
                    temp.append((x1, y1))

                elif level[x1 + 1][y1] == 6 or level[x1 - 1][y1] == 6 or level[x1][y1 + 1] == 6 or level[x1][y1 - 1] == 6:
                    mark_on_field_2(x2, y2, Q, win, level, screenshot)
                    y1 -= 1
                    temp.append((x1, y1))
                    finish.append((x1, y1))
                    find_an_exit(finish, main, win, screenshot, t_gen, x_win, y_win)
                    for i in temp:
                        main.append(i)

                else:
                    temp = []
                    x1, y1 = main[-1]
                    break
                pygame.display.update()

        elif y1 > 0 and level[x1][y1 + 1] == 1 and level[x1 + 1][y1] == 1 or y1 > 0 and level[x1][y1 + 1] == 1 and level[x1 + 1][y1] == 6 or y1 > 0 and level[x1][y1 + 1] == 6 and level[x1 + 1][y1] == 1:
            mark_on_field_2(x1, (y1 + 1), X, win, level, screenshot)
            y1 += 1
            temp.append((x1, y1))
            get_ahead(x1, y1, x2, y2, screenshot, level, win, t_gen, x_win, y_win)
            pygame.display.update()
            while True:
                if y1 > 0 and level[x1][y1 + 1] == 1:
                    mark_on_field_2(x1, (y1 + 1), X, win, level, screenshot)
                    y1 += 1
                    temp.append((x1, y1))

                elif y1 > 0 and level[x1][y1 - 1] == 1:
                    mark_on_field_2(x1, (y1 - 1), X, win, level, screenshot)
                    y1 -= 1
                    temp.append((x1, y1))

                elif x1 > 0 and level[x1 + 1][y1] == 1:
                    mark_on_field_2((x1 + 1), y1, X, win, level, screenshot)
                    x1 += 1
                    temp.append((x1, y1))

                elif x1 > 0 and level[x1 - 1][y1] == 1:
                    mark_on_field_2((x1 - 1), y1, X, win, level, screenshot)
                    x1 -= 1
                    temp.append((x1, y1))

                elif level[x1 + 1][y1] == 6 or level[x1 - 1][y1] == 6 or level[x1][y1 + 1] == 6 or level[x1][y1 - 1] == 6:
                    mark_on_field_2(x2, y2, Q, win, level, screenshot)
                    y1 += 1
                    temp.append((x1, y1))
                    finish.append((x1, y1))
                    find_an_exit(finish, main, win, screenshot, t_gen, x_win, y_win)
                    for i in temp:
                        main.append(i)

                else:
                    temp = []
                    x1, y1 = main[-1]
                    break
                pygame.display.update()

        elif y1 > 0 and level[x1][y1 - 1] == 1 and level[x1 - 1][y1] == 1 or y1 > 0 and level[x1][y1 - 1] == 1 and level[x1 - 1][y1] == 6 or y1 > 0 and level[x1][y1 - 1] == 6 and level[x1 - 1][y1] == 1:
            mark_on_field_2(x1, (y1 - 1), X, win, level, screenshot)
            y1 -= 1
            temp.append((x1, y1))
            get_ahead(x1, y1, x2, y2, screenshot, level, win, t_gen, x_win, y_win)
            pygame.display.update()
            while True:
                if y1 > 0 and level[x1][y1 - 1] == 1:
                    mark_on_field_2(x1, (y1 - 1), X, win, level, screenshot)
                    y1 -= 1
                    temp.append((x1, y1))

                elif y1 > 0 and level[x1][y1 + 1] == 1:
                    mark_on_field_2(x1, (y1 + 1), X, win, level, screenshot)
                    y1 += 1
                    temp.append((x1, y1))

                elif x1 > 0 and level[x1 + 1][y1] == 1:
                    mark_on_field_2((x1 + 1), y1, X, win, level, screenshot)
                    x1 += 1
                    temp.append((x1, y1))

                elif x1 > 0 and level[x1 - 1][y1] == 1:
                    mark_on_field_2((x1 - 1), y1, X, win, level, screenshot)
                    x1 -= 1
                    temp.append((x1, y1))

                elif level[x1 + 1][y1] == 6 or level[x1 - 1][y1] == 6 or level[x1][y1 + 1] == 6 or level[x1][y1 - 1] == 6:
                    mark_on_field_2(x2, y2, Q, win, level, screenshot)
                    y1 -= 1
                    temp.append((x1, y1))
                    finish.append((x1, y1))
                    find_an_exit(finish, main, win, screenshot, t_gen, x_win, y_win)

                    for i in temp:
                        main.append(i)

                else:
                    temp = []
                    x1, y1 = main[-1]
                    break
                pygame.display.update()

        elif y1 > 0 and level[x1][y1 + 1] == 1 and level[x1 - 1][y1] == 1 or y1 > 0 and level[x1][y1 + 1] == 1 and level[x1 - 1][y1] == 6 or y1 > 0 and level[x1][y1 + 1] == 6 and level[x1 - 1][y1] == 1:
            mark_on_field_2(x1, (y1 + 1), X, win, level, screenshot)
            y1 += 1
            temp.append((x1, y1))
            get_ahead(x1, y1, x2, y2, screenshot, level, win, t_gen, x_win, y_win)
            pygame.display.update()
            while True:
                if y1 > 0 and level[x1][y1 + 1] == 1:
                    mark_on_field_2(x1, (y1 + 1), X, win, level, screenshot)
                    y1 += 1
                    temp.append((x1, y1))

                elif y1 > 0 and level[x1][y1 - 1] == 1:
                    mark_on_field_2(x1, (y1 - 1), X, win, level, screenshot)
                    y1 -= 1
                    temp.append((x1, y1))

                elif x1 > 0 and level[x1 + 1][y1] == 1:
                    mark_on_field_2((x1 + 1), y1, X) # в эту функцию передали не все аргументы
                    x1 += 1
                    temp.append((x1, y1))

                elif x1 > 0 and level[x1 - 1][y1] == 1:
                    mark_on_field_2((x1 - 1), y1, X, win, level, screenshot)
                    x1 -= 1
                    temp.append((x1, y1))

                elif level[x1 + 1][y1] == 6 or level[x1 - 1][y1] == 6 or level[x1][y1 + 1] == 6 or level[x1][y1 - 1] == 6:
                    mark_on_field_2(x2, y2, Q, win, level, screenshot)
                    y1 += 1
                    temp.append((x1, y1))
                    finish.append((x1, y1))
                    find_an_exit(finish, main, win, screenshot, t_gen, x_win, y_win)

                    for i in temp:
                        main.append(i)

                else:
                    temp = []
                    x1, y1 = main[-1]
                    break
                pygame.display.update()

        elif x1 > 0 and level[x1 + 1][y1] == 1 and level[x1 - 1][y1] == 1 or x1 > 0 and level[x1 + 1][y1] == 1 and level[x1 - 1][y1] == 6 or x1 > 0 and level[x1 + 1][y1] == 6 and level[x1 - 1][y1] == 1:
            mark_on_field_2((x1 + 1), y1, X, win, level, screenshot)
            x1 += 1
            temp.append((x1, y1))
            get_ahead(x1, y1, x2, y2, screenshot, level, win, t_gen, x_win, y_win)
            pygame.display.update()
            while True:
                if y1 > 0 and level[x1][y1 + 1] == 1:
                    mark_on_field_2(x1, (y1 + 1), X, win, level, screenshot)
                    y1 += 1
                    temp.append((x1, y1))

                elif y1 > 0 and level[x1][y1 - 1] == 1:
                    mark_on_field_2(x1, (y1 - 1), X, win, level, screenshot)
                    y1 -= 1
                    temp.append((x1, y1))

                elif x1 > 0 and level[x1 + 1][y1] == 1:
                    mark_on_field_2((x1 + 1), y1, X, win, level, screenshot)
                    x1 += 1
                    temp.append((x1, y1))

                elif x1 > 0 and level[x1 - 1][y1] == 1:
                    mark_on_field_2((x1 - 1), y1, X, win, level, screenshot)
                    x1 -= 1
                    temp.append((x1, y1))

                elif level[x1 + 1][y1] == 6 or level[x1 - 1][y1] == 6 or level[x1][y1 + 1] == 6 or level[x1][y1 - 1] == 6:
                    mark_on_field_2(x2, y2, Q, win, level, screenshot)
                    y1 += 1
                    temp.append((x1, y1))
                    finish.append((x1, y1))
                    find_an_exit(finish, main, win, screenshot, t_gen, x_win, y_win)
                    for i in temp:
                        main.append(i)

                else:
                    temp = []
                    x1, y1 = main[-1]
                    break
                pygame.display.update()

        elif y1 > 0 and level[x1][y1 + 1] == 1 and level[x1][y1 - 1] == 1 or y1 > 0 and level[x1][y1 + 1] == 1 and level[x1][y1 - 1] == 6 or y1 > 0 and level[x1][y1 + 1] == 6 and level[x1][y1 - 1] == 1:
            mark_on_field_2(x1, (y1 + 1), X, win, level, screenshot)
            y1 += 1
            temp.append((x1, y1))
            get_ahead(x1, y1, x2, y2, screenshot, level, win, t_gen, x_win, y_win)
            pygame.display.update()
            while True:
                if y1 > 0 and level[x1][y1 + 1] == 1:
                    mark_on_field_2(x1, (y1 + 1), X, win, level, screenshot)
                    y1 += 1
                    temp.append((x1, y1))

                elif y1 > 0 and level[x1][y1 - 1] == 1:
                    mark_on_field_2(x1, (y1 - 1), X, win, level, screenshot)
                    y1 -= 1
                    temp.append((x1, y1))

                elif x1 > 0 and level[x1 + 1][y1] == 1:
                    mark_on_field_2((x1 + 1), y1, X, win, level, screenshot)
                    x1 += 1
                    temp.append((x1, y1))

                elif x1 > 0 and level[x1 - 1][y1] == 1:
                    mark_on_field_2((x1 - 1), y1, X, win, level, screenshot)
                    x1 -= 1
                    temp.append((x1, y1))

                elif level[x1 + 1][y1] == 6 or level[x1 - 1][y1] == 6 or level[x1][y1 + 1] == 6 or level[x1][y1 - 1] == 6:
                    mark_on_field_2(x2, y2, Q, win, level, screenshot)
                    y1 += 1
                    temp.append((x1, y1))
                    finish.append((x1, y1))
                    find_an_exit(finish, main, win, screenshot, t_gen, x_win, y_win)

                    for i in temp:
                        main.append(i)

                else:
                    temp = []
                    x1, y1 = main[-1]
                    break
                pygame.display.update()

        elif y1 > 0 and level[x1][y1 + 1] == 1:
            mark_on_field_2(x1, (y1 + 1), X, win, level, screenshot)
            y1 += 1
            main.append((x1, y1))
        elif y1 > 0 and level[x1][y1 - 1] == 1:
            mark_on_field_2(x1, (y1 - 1), X, win, level, screenshot)
            y1 -= 1
            main.append((x1, y1))
        elif x1 > 0 and level[x1 + 1][y1] == 1:
            mark_on_field_2((x1 + 1), y1, X, win, level, screenshot)
            x1 += 1
            main.append((x1, y1))
        elif x1 > 0 and level[x1 - 1][y1] == 1:
            mark_on_field_2((x1 - 1), y1, X, win, level, screenshot)
            x1 -= 1
            main.append((x1, y1))
        elif level[x1 + 1][y1] == 6 or level[x1 - 1][y1] == 6 or level[x1][y1 + 1] == 6 or level[x1][y1 - 1] == 6:
            mark_on_field_2(x2, y2, Q, win, level, screenshot)
            y1 -= 1
            main.append((x2, y2))
            finish.append((x2, y2))
            find_an_exit(finish, main, win, screenshot, t_gen, x_win, y_win)
        else:
            # pygame.display.update()
            # print(main)
            # print(temp)
            # p()
            return


def find_an_exit(finish, main, win, screenshot, t_gen, x_win, y_win):

    print("Выход успешно найден за время равное: {0}".format(time.clock() - t_gen))

    win.blit(screenshot, (0, 0))
    rob = pygame.image.load("rob.png")
    rob_rect = rob.get_rect(bottomright=(finish[0][1] + 5,  finish[0][0] + 5))
    win.blit(rob, rob_rect)

    font = pygame.font.SysFont('arial', 25)
    text = font.render('Выход успешно найден', True, (0, 225, 0))
    place = text.get_rect(center=(x_win//2, y_win//2 - 25))
    win.blit(text, place)

    pygame.display.update()

    pygame.time.delay(2000)

    back(main, win, screenshot)


def back(main, win, screenshot):

    win.blit(screenshot, (0, 0))
    pygame.display.update()

    # Будущий цикл возрата !!!!!!!!!!!!!!!!!!!!!!!!!!
    # while len(main) != 0:
    #     print("1")
    #     x1 = main[len(main) - 1][0]
    #     y1 = main[len(main) - 1][1]
    #
    #     mark_on_field_2(x1, y1, "*")
    #     main.pop(len(main) - 1)
    #     pygame.display.update()

    # print_field(level)
    waiting_close()


if __name__ == '__main__':

    main()
# в питоне функция это объект первого класса как и любая переменная, это означает, что её можно передавать как параметр
# в другую функцию и называю переменные и функции одинаково можно выстрелить себе в ногу)