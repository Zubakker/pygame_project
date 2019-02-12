import pygame


class Keel:
    def __init__(self, screen):
        self.screen = screen

    def draw(self, coords, whiteball):
        pygame.draw.line(self.screen, (255, 255, 255), (int(whiteball.coords[0]), int(whiteball.coords[1])), coords, 3)

    def shoot(self, coords, whiteball):
        whiteball.vx = (whiteball.coords[0] - coords[0]) / 100
        whiteball.vy = (whiteball.coords[1] - coords[1]) / 100
        whiteball.vel = [whiteball.vx, whiteball.vy]

