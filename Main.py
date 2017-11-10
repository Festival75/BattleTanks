# -*- coding: utf-8 -*-
from Constants import *
from Battlefield import *
from Player import *
import pygame


class Main:
    def __init__(self, screen):
        self.player = Player(screen, 'Test', 'GREEN', 'BARREL_TYPE3')
        self.battlefield = Battlefield(screen)
        self.screen = screen
        self.background = pygame.image.load('data/background.jpg')
        self.running = True
        self.main_loop()

    def render(self):
        # self.screen.blit(self.background, (0, 0))
        self.battlefield.render_battlefield()
        self.player.move()
        self.player.render()
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.player.direction = RIGHT
                    self.player.moving = [1, 0, 0, 0]
                if event.key == pygame.K_DOWN:
                    self.player.direction = DOWN
                    self.player.moving = [0, 1, 0, 0]
                if event.key == pygame.K_LEFT:
                    self.player.direction = LEFT
                    self.player.moving = [0, 0, 1, 0]
                if event.key == pygame.K_UP:
                    self.player.direction = UP
                    self.player.moving = [0, 0, 0, 1]
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.direction = RIGHT
                    self.player.moving[RIGHT] = 0
                if event.key == pygame.K_DOWN:
                    self.player.direction = DOWN
                    self.player.moving[DOWN] = 0
                if event.key == pygame.K_LEFT:
                    self.player.direction = LEFT
                    self.player.moving[LEFT] = 0
                if event.key == pygame.K_UP:
                    self.player.direction = UP
                    self.player.moving[UP] = 0

    def main_loop(self):
        while self.running:
            self.render()
            self.handle_events()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Main(screen)
