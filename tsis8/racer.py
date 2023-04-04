import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

# Setting up FPS
FPS = 60
clock= pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over_text= font.render("Game Over", True, BLACK)

background = pygame.image.load("street.png")

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

#creating moving enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(64, SCREEN_WIDTH - 64), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(64, SCREEN_WIDTH - 64), 0)
    def draw(self,surface):
        surface.blit(self.image,self.rect)

#creating a player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT-50)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
#creating coins which will appear randomly
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("coin.png")
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(65,SCREEN_WIDTH-65),0)

    def move(self):
        self.rect.move_ip(0,3)
        if self.rect.top>SCREEN_HEIGHT:
            self.rect.center=(random.randint(65,SCREEN_WIDTH-65),0)

    def draw(self,surface):
        surface.blit(self.image,self.rect)




# Setting up Sprites
P1 = Player()
E1 = Enemy()
coin=Coin()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)

coins=pygame.sprite.Group()
coins.add(coin)



all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(coin)

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

captured_coins=0
#collected coins
def all_coins():
    global coin
    coin=Coin()
    coins.add(coin)
    all_sprites.add(coin)
# Game Loop
while True:

    # Cycles through all events occurring
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #setting background and tect score,coin
    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(font_small.render(f'Score:{SCORE}',True,BLACK),(300,10))

    DISPLAYSURF.blit(
        font_small.render(f'Coin:{captured_coins}',True,BLACK),(300,30))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()



    if pygame.sprite.spritecollideany(P1,coins):
        coin.kill()
        captured_coins+=1
        SCORE+=1
        all_coins()

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)

        DISPLAYSURF.fill(BLACK)
        DISPLAYSURF.blit(font.render(f'Game over',True,WHITE), (12, 190))
        DISPLAYSURF.blit(font_small.render(f'Your score:{SCORE}',True,WHITE),(15,270))
        DISPLAYSURF.blit(font_small.render(f'All coins:{captured_coins}',True,WHITE),(15,290))



        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    clock.tick(FPS)
