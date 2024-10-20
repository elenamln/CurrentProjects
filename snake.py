import pygame
import time
import random

# Game constants
WIDTH = 600
HEIGHT = 600
CELL_SIZE = 20
FPS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = RIGHT

    def move(self):
        x, y = self.body[0]
        dx, dy = self.direction
        new_x = (x + dx * CELL_SIZE) % WIDTH
        new_y = (y + dy * CELL_SIZE) % HEIGHT
        self.body.insert(0, (new_x, new_y))
        self.body.pop()

    def grow(self):
        x, y = self.body[-1]
        dx, dy = self.direction
        new_x = (x + dx * CELL_SIZE) % WIDTH
        new_y = (y + dy * CELL_SIZE) % HEIGHT
        self.body.append((new_x, new_y))

    def check_collision(self, food):
        if self.body[0] == food.position:
            return True
        for segment in self.body[1:]:
            if self.body[0] == segment:
                return True
        return False

class Food:
    def __init__(self):
        self.position = (random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE,
                         random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE)

def draw_grid(screen):
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y))

def draw_snake(screen, snake):
    for segment in snake.body:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

def draw_food(screen, food):
    pygame.draw.rect(screen, RED, (food.position[0], food.position[1], CELL_SIZE, CELL_SIZE))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()

    snake = Snake()
    food = Food()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != DOWN:
                    snake.direction = UP
                elif event.key == pygame.K_DOWN and snake.direction != UP:
                    snake.direction = DOWN
                elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                    snake.direction = LEFT
                elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                    snake.direction = RIGHT

        snake.move()
        if snake.check_collision(food):
            snake.grow()
            food.position = (random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE,
                             random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE)

        screen.fill(BLACK)
        draw_grid(screen)
        draw_snake(screen, snake)
        draw_food(screen, food)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()