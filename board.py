import pygame
from constants import WIDHT, HEIGHT


class Board:
    def __init__(self, window):
        self.window = window
        self.static = True

    def draw(self):
        window = self.window
        
        pygame.draw.rect(window, (90, 90, 0),
                         (50, 50, WIDHT - 100, HEIGHT - 100))
        pygame.draw.rect(window, (0, 128, 0),
                         (70, 70, WIDHT - 140, HEIGHT - 140))
        pygame.draw.circle(window, (0, 0, 0), (75, 75), 15)
        pygame.draw.circle(window, (0, 0, 0), (WIDHT - 75, 75), 15)
        pygame.draw.circle(window, (0, 0, 0),
                           (WIDHT - 75, HEIGHT - 75), 15)
        pygame.draw.circle(window, (0, 0, 0), (75, HEIGHT - 75), 15)
        pygame.draw.circle(window, (0, 0, 0), (WIDHT // 2, 70), 15)
        pygame.draw.circle(window, (0, 0, 0),
                           (WIDHT // 2, HEIGHT - 70), 15)
