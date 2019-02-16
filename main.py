import pygame
import sys


from keel import Keel
from ball import Ball
from board import Board
from functions import gameover, drop, newgame, winwin
from constants import WIDHT, HEIGHT

score = 0
pygame.init()
window = pygame.display.set_mode((WIDHT, HEIGHT))

white_ball = Ball(window, 0, (WIDHT - WIDHT // 4 + 50, HEIGHT // 2 - 30))
balls = [white_ball]
for i in range(4):
    for j in range(i + 1):
        balls.append(Ball(window, 1,
                          (WIDHT // 4 - i * 18 + 40,
                           HEIGHT // 2 + j * 21 - i * 10)))

balls.append(Ball(window, 2, (WIDHT - WIDHT // 4, HEIGHT // 2 - 50)))  # желтый
balls.append(Ball(window, 3, (WIDHT - WIDHT // 4, HEIGHT // 2 + 50)))  # зеленый
balls.append(Ball(window, 4, (WIDHT - WIDHT // 4, HEIGHT // 2)))       # коричневый
balls.append(Ball(window, 5, (WIDHT // 2, HEIGHT // 2)))               # синий
balls.append(Ball(window, 6, (WIDHT // 4 + 61, HEIGHT // 2)))          # розовый
balls.append(Ball(window, 7, (WIDHT // 4 - 70, HEIGHT // 2)))          # черный

bd = Board(window)
keel = Keel(window)

pygame.font.init()
my_font = pygame.font.SysFont("Courier", 60)

for ball in balls:
    ball.balls = balls
but = False
chords = white_ball.coords

queue = []
turn = 0
reds = 0
rs = False
colors = ["БЕЛЫЙ", "КРАСНЫЙ", "ЖЕЛТЫЙ",
          "ЗЕЛЕНЫЙ", "КОРИЧНЫЙ", "СИНИЙ",
          "РОЗОВЫЙ", "ЧЕРНЫЙ"]

winwin(window, my_font, score)
newgame(window, my_font)

nxt = -1
while True:
    turnch = False
    fine = 0

    if reds == 10:
        turn = 2
        nxt = 2

    if nxt == 8:
        winwin(window, my_font, score)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            but = True

        if event.type == pygame.MOUSEBUTTONUP and bd.static:
            but = False
            keel.shoot(event.pos, white_ball)
            chords = white_ball.coords

        elif event.type == pygame.MOUSEBUTTONUP:
            but = False

        elif event.type == pygame.MOUSEMOTION and bd.static and but:
            chords = event.pos

    window.fill((0, 0, 0))
    if bd.static:
        window.fill((0, 0, 255))
        for ball in queue:
            if ball.type == 0:
                gameover(window, my_font, score)
            elif ball.type > 1 and not turn:
                drop(ball.type, balls, ball)
                fine += 1
            elif ball.type > 1 and turn == 1:
                drop(ball.type, balls, ball)
                if not turnch:
                    turnch = True
                    score += ball.type
                else:
                    fine += 1
            elif ball.type > 1 and turn == 2:
                if nxt == ball.type:
                    score += ball.type
                    nxt += 1
                else:
                    drop(ball.type, balls, ball)
                    fine += 1
            if ball.type == 1 and not turn:
                score += 1
                reds += 1
                turnch = True
            elif ball.type == 1 and turn == 1:
                score += 1
                reds += 1
        queue = []
    if turnch:
        turn = 1 - turn

    score -= fine

    if fine:
        rs = True

    if bd.static and rs:
        window.fill((255, 0, 0))

    window.blit(my_font.render("ВАШ СЧЕТ {}".format(str(score)),
                               1, (255, 255, 255)), (50, -5))
    if turn == 1:
        window.blit(my_font.render("ЦВЕТНОЙ", 1, (255, 255, 255)),
                    (50, HEIGHT - 50))
    elif turn == 0:
        window.blit(my_font.render("КАСНЫЙ", 1, (255, 255, 255)),
                    (50, HEIGHT - 50))
    elif turn == 2:
        window.blit(my_font.render(colors[nxt], 1, (255, 255, 255)),
                    (50, HEIGHT - 50))
    bd.draw()
    bd.static = True

    for ball in balls:
        ball.draw()
        if ball.vel[0] or ball.vel[1]:
            bd.static = False
        a = ball.update()
        if type(a) == int:
            queue.append(ball)

    if bd.static and but:
        keel.draw(chords, white_ball)

    if bd.static and rs:
        pygame.display.update()
        pygame.time.wait(500)
        rs = False
    pygame.display.update()
    pygame.time.wait(1)
