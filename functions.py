import pygame
import sys

from constants import WIDHT, HEIGHT


def gameover(window, font, score):
    img = pygame.transform.scale(pygame.image.load("gameover_screen.png"),
                                 (WIDHT, HEIGHT))
    window.blit(img, (0, 0))
    window.blit(font.render("ВЫ ПРОИГРАЛИ ВАШ СЧЕТ",
                            1, (255, 255, 255)), (10, 10))
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

