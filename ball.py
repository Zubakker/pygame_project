import pygame

from constants import WIDHT, HEIGHT


class Ball:
    colors = [(255, 255, 255),  # белый
              (200,   0,   0),  # красный
              (230, 230,   0),  # желтый
              (0,   200,   0),  # зеленый
              (120,  60,   0),  # коричневый
              (0,     0, 250),  # синий
              (250, 120, 150),  # розовый
              (0,     0,   0)]  # черный

    def __init__(self, window, type, coords):
        self.screen = window
        self.type = type
        self.coords = coords
        self.vel = [0, 0]
        self.vx, self.vy = 0, 0
        self.balls = []

    def draw(self):
        pygame.draw.circle(self.screen, self.colors[self.type],
                           (int(self.coords[0]),
                            int(self.coords[1])), 10)

    def update(self):
        self.coords = self.coords[0] + self.vx,\
                      self.coords[1] + self.vy
        if WIDHT - 80 < self.coords[0] or self.coords[0] < 80:
            self.vel[0] = -self.vel[0]
            self.vx = -self.vx
        if HEIGHT - 80 < self.coords[1] or self.coords[1] < 80:
            self.vel[1] = -self.vel[1]
            self.vy = -self.vy
        self.vel[0] /= 1.001
        self.vel[1] /= 1.001

        self.vx /= 1.001
        self.vy /= 1.001

        if abs(self.vel[0]) < 0.02:
            self.vel[0] = 0
            self.vx = 0
        if abs(self.vel[1]) < 0.02:
            self.vel[1] = 0
            self.vy = 0

        for cors in [[75, 75],                  [WIDHT - 75, 75],
                     [WIDHT - 75, HEIGHT - 75], [75, HEIGHT - 75],
                     [WIDHT // 2, 70],          [WIDHT // 2, HEIGHT - 70]]:
            if (cors[0] - self.coords[0]) ** 2 +\
                    (cors[1] - self.coords[1]) ** 2 < 15 * 15:
                self.coords = [-100, -100]
                self.vel = [0, 0]
                self.vx, self.vy = 0, 0
                return self.type

        for ball in self.balls:
            if 400 > ((ball.coords[0] - self.coords[0]) ** 2 +
                      (ball.coords[1] - self.coords[1]) ** 2) > 0:
                self.collision(self, ball)

        if max(abs(self.vx), abs(self.vy)) > 3:
            k = 3 / max(abs(self.vy), abs(self.vx))
            self.vx, self.vy = k * self.vx, k * self.vy

        self.vel = [self.vx, self.vy]
        return None

    def collision(self, ball, ball2):
        x1, y1 = ball.coords
        x2, y2 = ball2.coords
        if x1 == x2:
            black_k = 100024000
        else:
            black_k = (y1 - y2) / (x1 - x2)
        black_b = y1 - black_k * x1
        i = ball.vel[0] - ball2.vel[0] + x1
        j = ball.vel[1] - ball2.vel[1] + y1
        if y1 == y2:
            orange_k = 1000024000
        else:
            orange_k = -(x1 - x2) / (y1 - y2)
        orange_b = j - orange_k * i
        x = (orange_b - black_b) / (black_k - orange_k)
        y = orange_k * x + orange_b
        x, y = x - x1, y - y1
        x3, y3 = i - x - x1, j - y - y1
        x4, y4 = x + ball2.vel[0], y + ball2.vel[1]

        if max(abs(x4), abs(y4)) > 3:
            k = 3 / max(abs(x4), abs(y4))
            x4, y4 = k * x4, k * y4

        if max(abs(x3), abs(y3)) > 3:
            o = 3 / max(abs(x3), abs(y3))
            x3, y3 = o * x3, o * y3

        ball2.vx = x4
        ball2.vy = y4
        ball2.vel = [ball2.vx, ball2.vy]

        ball.vel = [x3, y3]
        ball.vx, ball.vy = x3, y3

# ФИЗИКА:


def collision(ball, ball2):
    x1, y1 = ball.coords
    x2, y2 = ball2.coords
    black_k = (y1 - y2) / (x1 - x2)
    black_b = y1 - black_k * x1
    i = ball.vel[0] - ball2.vel[0] + x1
    j = ball.vel[1] - ball2.vel[1] + y1
    orange_k = -(x1 - x2) / (y1 - y2)
    orange_b = j - orange_k * i
    x = (orange_b - black_b) / (black_k - orange_k)
    y = orange_k * x + orange_b
    x, y = x - x1, y - y1
    x3, y3 = i - x, j - y
