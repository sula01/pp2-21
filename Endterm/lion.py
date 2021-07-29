import pygame
import random

WIDTH = 800
HEIGHT = 650
FPS = 30

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

score = 0

#create game and window
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HUNGRY LION!")
clock = pygame.time.Clock()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = random.randint(1, 800), random.randint(1, 650)

    def update(self):
        self.rect.y += 2
        if self.rect.y > HEIGHT:
            self.rect.center = random.randint(1, 800), random.randint(1, 50)


class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25, 20))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = random.randint(1, 800), random.randint(1, 650)

    def update(self):
        self.rect.x += random.randint(-2, 2)


class Lion(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = WIDTH / 2, HEIGHT / 2

    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_DOWN]:
            self.rect.y += 7
        if pressed[pygame.K_UP]:
            self.rect.y -= 7
        if pressed[pygame.K_LEFT]:
            self.rect.x -= 7
        if pressed[pygame.K_RIGHT]:
            self.rect.x += 7


enemies = pygame.sprite.Group()
foods = pygame.sprite.Group()
my_sprite = pygame.sprite.Group()

for x in range(30):
    x = Enemy()
    enemies.add(x)

for f in range(30):
    f = Food()
    foods.add(f)

lion = Lion()
my_sprite.add(lion)

#main loop
running = True

while running:
    #Держим цикл на правильной скорости
    clock.tick(FPS)
    #Ввод процесса (события)
    for event in pygame.event.get():
        #check for closing window
        if event.type == pygame.QUIT:
            running = False
            quit()

    #updates
    enemies.update()
    my_sprite.update()
    foods.update()

    #rendering
    screen.fill(WHITE)

    enemies.draw(screen)
    my_sprite.draw(screen)
    foods.draw(screen)

    for f in foods:
        if pygame.sprite.spritecollide(lion, foods, True):
            score += 1

    for x in enemies:
        if pygame.sprite.spritecollide(lion, enemies, True):
            score -= 1
            enemies.add(Enemy())

    font = pygame.font.SysFont('ComicSans', 40)
    text1 = font.render(f'Score : {score}', 1, (0, 0, 0))
    screen.blit(text1, (20, 20))

    #end
    pygame.display.flip()

pygame.quit()