# -*- coding: utf-8 -*-
from Constants import *
import pygame


class Main:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load('data/background.jpg')
        self.running = True
        self.main_loop()

    def render(self):
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def main_loop(self):
        while self.running:
            self.render()
            self.handle_events()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Main(screen)
