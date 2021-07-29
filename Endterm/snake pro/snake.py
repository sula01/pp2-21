import pygame
import random

from os import path

WIDTH = 800
HEIGHT = 600
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# создаем игру и окно
pygame.init()
pygame.display.set_caption("SNAKEEEE")
clock = pygame.time.Clock()

texture_dir = path.join(path.dirname(__file__), 'Textures')

screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load(path.join(texture_dir, 'green.png')).convert()
background_rect = background.get_rect()

# Load sound directory and main theme for game
# sound_dir = path.join(path.dirname(__file__), 'Sound')
# pygame.mixer.init()
# pygame.mixer.music.load(path.join(sound_dir, 'ost.wav'))
# pygame.mixer.music.play(-1)  # for loop
# pygame.mixer.music.set_volume(10)


# classes for game
class Snake:

    def __init__(self):
        self.size = 1
        self.elements = [[100, 100]]
        self.radius = 10
        self.x = self.elements[0][0]
        self.y = self.elements[0][1]
        self.dx = 5
        self.dy = 0
        self.score = 0
        self.is_add = False

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, WHITE, element, self.radius)

    def add_to_snake(self):
        self.size += 1
        self.elements.append([0, 0])
        self.is_add = False

    def move(self):
        if self.is_add:
            self.add_to_snake()

        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy


class Food:

    def __init__(self):
        self.image = pygame.image.load(path.join(texture_dir, 'food.png'))
        self.x = random.randint(10, 780)
        self.y = random.randint(10, 570)
        self.elements = [[100, 100]]
        self.rect = 10

    def draw(self):
        for self.element in self.elements:
            screen.blit(self.image, (self.x, self.y))


def collision():
    if (snake.elements[0][0] - food.image.get_size()[0] <= food.x < snake.elements[0][0] +
        food.image.get_size()[0]) and (
            snake.elements[0][1] - food.image.get_size()[1] <= food.y < snake.elements[0][1] +
            food.image.get_size()[1]):
        snake.is_add = True
        if snake.is_add:
            snake.score += 1
            food.x = random.randint(10, 780)
            food.y = random.randint(10, 570)


# Start menu for a new game
def start_menu():
    screen.blit(background, background_rect)
    render(screen, "Welcome to Snake Game", 48, WIDTH / 2, HEIGHT / 4)
    render(screen, "Arrow W A S D to move", 25, WIDTH / 2, HEIGHT / 1.5)
    render(screen, "Press any key to begin", 22, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    menu = True
    while menu:
        clock.tick(FPS)
        for key in pygame.event.get():
            if key.type == pygame.QUIT:
                pygame.quit()
            if key.type == pygame.KEYUP:
                menu = False


# Render text in the window
def render(surface, text, size, x, y):
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)


# End Menu after game over of player
def end_menu():
    screen.blit(background, background_rect)
    render(screen, "YOU ARE LOSER", 64, WIDTH / 2, HEIGHT / 4)
    render(screen, "Your Scores:" + str(snake.score), 32, WIDTH / 2, HEIGHT / 2)
    render(screen, "Press ESCAPE To End", 22, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    end = True
    while end:
        clock.tick(FPS)
        for key in pygame.event.get():
            key_pressed = pygame.key.get_pressed()
            if key.type == pygame.QUIT:
                pygame.quit()
            if key_pressed[pygame.K_ESCAPE]:
                pygame.quit()


snake = Snake()
food = Food()

# Initial parameters
game = True
velocity = 5
New_Game = True
Game_Over = False
Scores = 0

# Main loop
while game:
    clock.tick(FPS)
    if New_Game:
        start_menu()
        New_Game = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game = False
            if event.key == pygame.K_d:
                snake.dx = velocity
                snake.dy = 0
            if event.key == pygame.K_s:
                snake.dx = 0
                snake.dy = velocity
            if event.key == pygame.K_a:
                snake.dx = -velocity
                snake.dy = 0
            if event.key == pygame.K_w:
                snake.dx = 0
                snake.dy = -velocity
            if snake.elements[0] in snake.elements[1:]:
                Game_Over = True

    # Borders
    if snake.elements[0][0] > WIDTH:
        Game_Over = True
    if snake.elements[0][0] < 0:
        Game_Over = True
    if snake.elements[0][1] > HEIGHT:
        Game_Over = True
    if snake.elements[0][1] < 0:
        Game_Over = True

    if Game_Over:
        end_menu()

    screen.fill(BLACK)
    screen.blit(background, background_rect)
    snake.move()
    collision()
    snake.draw()
    food.draw()
    render(screen, str("Scores: " + str(snake.score)), 30, WIDTH / 2, 20)
    pygame.display.flip()


pygame.quit()