import pygame
import sys

from constants import WIDHT, HEIGHT


def newgame(window, font):
    font_2 = pygame.font.SysFont("Lobster", 60, italic=True)
    font_3 = pygame.font.SysFont("Comic Sans", 40)
    pic = pygame.transform.scale(pygame.image.load("pictures/poster.png"),
                                 (WIDHT, HEIGHT))
    tick = 0
    pon = 0

    pix = []
    for i in range(7):
        pix.append(pygame.transform.scale(pygame.image.load("pictures/cadr_" + str(i + 1) + ".jpg"), (100, 100)))

    rules = ["ПРАВИЛА ТАКОВЫ:",
             "ЭКРАН СИНИЙ ЗНАЧИТ МОЖНО БИТЬ",
             "БИТЬ ТОЛЬКО ПО БЕЛОМУ ШАРИКУ",
             "ЭКРАН КРАСНЫЙ -- ЗНАЧИТ ШТРАФ",
             "ЗАБИВАЕТЕ ШАР ЦВЕТА ЧТО НАПИСАН",
             "СЧЕТ СОХРАНЯЕТСЯ"]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                return

        tick += 1
        if tick == 30:
            pon += 1
            pon %= 7
            tick = 0

        window.fill((0, 0, 0))
        window.blit(pic, (0, 0))
        pygame.draw.rect(window, (0, 0, 0), (0, 0, WIDHT, HEIGHT // 6))
        window.blit(font.render("ДОБРО ПОЖАЛОВАТЬ В", 1, (255, 255, 255)),
                    (10, -5))
        window.blit(font_2.render("superpool 2019", 1, (255, 0, 0)),
                    (10, 80))
        window.blit(pix[pon], (WIDHT - 100, HEIGHT - 100))

        for i in range(6):
            window.blit(font_3.render(rules[i], 1, (150, 150, 150)),
                        (10, 150 + i * 45))

        pygame.display.update()


def gameover(window, font, score):
    img = pygame.transform.scale(pygame.image.load("pictures/gameover_screen.png"),
                                 (WIDHT, HEIGHT))
    window.blit(img, (0, 0))
    window.blit(font.render("ВЫ ПРОИГРАЛИ ВАШ СЧЕТ", 1, (255, 255, 255)),
                (10, 10))
    window.blit(font.render(str(score), 1, (255, 255, 255)), (10, 80))
    pygame.display.update()
    pygame.time.wait(3000)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
                    event.type == pygame.MOUSEBUTTONDOWN or \
                    event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()
        window.blit(img, (0, 0))
        window.blit(font.render("ВЫ ПРОИГРАЛИ ВАШ СЧЕТ",
                    1, (255, 255, 255)), (10, 10))
        window.blit(font.render(str(score), 1, (255, 255, 255)), (10, 80))
        pygame.display.update()


def drop(type, balls, bale):
    places = [(WIDHT - WIDHT // 4, HEIGHT // 2 - 50),
              (WIDHT - WIDHT // 4, HEIGHT // 2 + 50),
              (WIDHT - WIDHT // 4, HEIGHT // 2),
              (WIDHT // 2,         HEIGHT // 2),
              (WIDHT // 4 + 61,    HEIGHT // 2),
              (WIDHT // 4 - 70,    HEIGHT // 2)]
    x, y = places[type - 2]
    for ball in balls:
        if (ball.coords[0] - x) ** 2 + (ball.coords[1] - y) ** 2 <= 400:
            for i in range(5, -1, -1):
                x, y = places[i]
                for ball in balls:
                    if (ball.coords[0] - x) ** 2 + (ball.coords[1] - y) ** 2 <= 400:
                        break
                else:
                    bale.coords = (x, y)
                    return
            for i in range(-20, 21):
                a = [0, 0, 0, 0]
                k = [(-i, -20), (-i, 20), (-20, -i), (20, -i)]
                for ball in balls:
                    if (ball.coords[0] - x - i) ** 2 + (ball.coords[1] - y - 20) ** 2 <= 400:
                        a[0] += 1
                    if (ball.coords[0] - x - i) ** 2 + (ball.coords[1] - y + 20) ** 2 <= 400:
                        a[1] += 1
                    if (ball.coords[0] - x - 20) ** 2 + (ball.coords[1] - y - i) ** 2 <= 400:
                        a[2] += 1
                    if (ball.coords[0] - x + 20) ** 2 + (ball.coords[1] - y - i) ** 2 <= 400:
                        a[3] += 1
                for j in range(4):
                    if a[j] == 0:
                        bale.coords = (x + k[j][0], y + k[j][1])
                        return
            break
    else:
        bale.coords = places[type - 2]


def winwin(window, font, score):
    file = open("scores.txt", "a")
    file.write("\n" + str(score))
    file.close()
    file2 = [int(x) if x else score for x in open("scores.txt", "r").read().split("\n")]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        window.fill((0, 0, 0))
        window.blit(font.render("ПОЗДРАВЛЯЮ ВЫ ПОБЕДИЛИ", 1, (255, 255, 255)),
                    (10, 0))
        window.blit(font.render("ВАШ СЧЕТ: " + str(score), 1, (255, 255, 255)),
                    (10, 70))
        window.blit(font.render("РЕКОРД:" + str(max(file2)), 1,
                                (255, 255, 255)), (10, 130))
        pygame.display.update()
