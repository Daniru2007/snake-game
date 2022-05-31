import random
import pygame
from enum import Enum

WINDOW_SIZE = (600, 400)
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("snake game")
clock = pygame.time.Clock()
FPS = 20


class Directions(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4


class Snake(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.direction = Directions.RIGHT
        self.score = 0
        self.snake_objs = [
            pygame.Rect(self.x, self.y, self.width, self.height),
            pygame.Rect(self.x-self.width, self.y, self.width, self.height),
            pygame.Rect(self.x-2*self.width, self.y, self.width, self.height)
            ]

    def move(self, food):
        if self.direction == Directions.RIGHT:
            self.x += self.width
        if self.direction == Directions.LEFT:
            self.x -= self.width
        if self.direction == Directions.UP:
            self.y -= self.height
        if self.direction == Directions.DOWN:
            self.y += self.height

        for obj in self.snake_objs:
            if obj.colliderect(pygame.Rect(self.x, self.y, self.width, self.height)):
                return True
        self.snake_objs.insert(0, pygame.Rect(self.x, self.y, self.width, self.height))
        if food.rect().colliderect(pygame.Rect(self.x, self.y, self.width, self.height)):
            food.change_pos()
            self.score += 1
        else:
            self.snake_objs.pop(-1)
        False

    def display(self, screen):
        for obj in self.snake_objs:
            pygame.draw.rect(screen, (255, 255, 255), (obj.x, obj.y, self.width, self.height))


class Food(object):
    def __init__(self, width, height):
        self.x = random.randint(0, 600)
        self.y = random.randint(0, 400)
        self.width = width
        self.height = height

    def change_pos(self):
        self.x = random.randint(0, 600)
        self.y = random.randint(0, 400)

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def display(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))


snake = Snake(10, 10, 20, 20)
food = Food(20, 20)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.direction = Directions.RIGHT
            if event.key == pygame.K_LEFT:
                snake.direction = Directions.LEFT
            if event.key == pygame.K_UP:
                snake.direction = Directions.UP
            if event.key == pygame.K_DOWN:
                snake.direction = Directions.DOWN

    if snake.move(food):
        run = False

    screen.fill((0, 0, 0))
    food.display(screen)
    snake.display(screen)

    clock.tick(FPS)
    pygame.display.update()
