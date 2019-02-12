import pygame
import sys


from keel import Keel
from ball import Ball
from board import Board
from constants import WIDHT, HEIGHT

pygame.init()
window = pygame.display.set_mode((WIDHT, HEIGHT))

white_ball = Ball(window, 0, (WIDHT - WIDHT // 4 + 50, HEIGHT // 2 - 30))
balls = [white_ball]
for i in range(4):
    for j in range(i + 1):
        balls.append(Ball(window, 1,
                          (WIDHT // 4 - i * 18 + 40, HEIGHT // 2 + j * 21 - i * 10)))

balls.append(Ball(window, 2, (WIDHT - WIDHT // 4, HEIGHT // 2 - 50)))
balls.append(Ball(window, 3, (WIDHT - WIDHT // 4, HEIGHT // 2 + 50)))
balls.append(Ball(window, 4, (WIDHT - WIDHT // 4, HEIGHT // 2)))
balls.append(Ball(window, 5, (WIDHT // 2, HEIGHT // 2)))
balls.append(Ball(window, 6, (WIDHT // 4 + 61, HEIGHT // 2)))
balls.append(Ball(window, 7, (WIDHT // 4 - 70, HEIGHT // 2)))

bd = Board(window)
keel = Keel(window)


for ball in balls:
    ball.balls = balls
but = False
chords = white_ball.coords

while True:

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
    bd.draw()
    bd.static = True

    for ball in balls:
        ball.draw()
        if ball.vel[0] or ball.vel[1]:
            bd.static = False
        ball.update()

    if bd.static and but:
        keel.draw(chords, white_ball)
    pygame.display.update()
    pygame.time.wait(1)
