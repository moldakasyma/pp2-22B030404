import random
import time
import pygame
# initialization
pygame.init()
clock = pygame.time.Clock()
# frame per seconds
fps = 60  

coins_list = {'1': 'coin.png', '2': 'coin2.png'}
# colors
RED = (255, 0, 0)  
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
# speed of enemy car
SPEED = 5
# player's score
SCORE = 0  
# size of the window
DISPLAYSURF= WINDOW_WIDTH, WINDOW_HEIGHT = 400, 600  
#main screen
screen = pygame.display.set_mode(DISPLAYSURF)  
# big font
font = pygame.font.SysFont('Verdana', 63)  
font_small = pygame.font.SysFont('Verdana', 18)  
# game over label
game_over_text_label = font.render('Game over', True, RED) 
# background image
background = pygame.image.load('street.png')  

# the title of window
pygame.display.set_caption('racer')  
# game not over condition
game_over = False 

class Enemy(pygame.sprite.Sprite):
    #  enemy car is moving and collide with a player
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('enemy.png')  # image of enemy car
        self.rect = self.image.get_rect()  # rectangle of image
        self.rect.center = (random.randint(64, WINDOW_WIDTH - 64), 0)

    def move(self):
        global SPEED, SCORE
        self.rect.move_ip(0, SPEED)  # car is moving by y-axis with some speed

        if self.rect.top > WINDOW_HEIGHT:  # if enemy car reached the bottom of window
            SCORE += 1  # player get point for not collision with enemy car
            self.rect.center = (random.randint(64, WINDOW_WIDTH - 64), 0)

 

    def draw(self, surface):
        surface.blit(self.image, self.rect)  # displaying the enemy car

# Player is moving by x-axis. It can collide with coin or enemy car
class Player(pygame.sprite.Sprite):  
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('player.png')  # image of player
        self.rect = self.image.get_rect()  # rectangle of image
        self.rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50)  # initial coordinates of center

    def move(self):
        pressed_keys = pygame.key.get_pressed()  # player moves by x-axis when some keys are pressed

        if self.rect.left > 0: #to keep it within the screen
            if pressed_keys[pygame.K_LEFT]:  # if left arrow touched, car will move to the left direction
                self.rect.move_ip(-5, 0)
        if self.rect.right < WINDOW_WIDTH :
            if pressed_keys[pygame.K_RIGHT]:  # if right arrow touched, car will move to the right direction
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)  # displaying the player
        

# coin is moving, so it should be extended from Sprite.
class Coin(pygame.sprite.Sprite):
    def __init__(self, _image_name: str, _points=1):
        # we have several coins with different masses
        super().__init__()
        self.image = pygame.image.load(_image_name)  # image of coin
        self.rect = self.image.get_rect()  # rectangle of image
        self.radius = self.rect.width//2  # we need this for setting the limit of generating random coordinates of center of coin
        self.rect.center = (random.randint(40, WINDOW_WIDTH - 40), 0)
        self.points = _points

    def move(self):
        self.rect.move_ip(0, 3)  # it is moving by y-axis with step 3
        if self.rect.top > WINDOW_HEIGHT:  # if coin reached the bottom, it will disappear 
            self.rect.center=(random.randint(40,WINDOW_WIDTH-40),0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)  # displaying coin

# initializing the object of classes
player = Player()  
enemy = Enemy()  
coin = Coin(coins_list['1'])  
coin2 = None

all_sprites = pygame.sprite.Group()
# we add all sprites to the one array for simplify and integrate their actions

all_sprites.add(player)
all_sprites.add(enemy)
all_sprites.add(coin)
# pygame sprite collide method requires array of elements with which player can collide
enemies = pygame.sprite.Group()  
enemies.add(enemy)

coins = pygame.sprite.Group() 
coins.add(coin)

super_coin_group = pygame.sprite.Group()


simple_coins = 0  
small_coins = 0
is_super_coin_generated = False
is_speed_increased = False


def generate_coin(type=1):
    global coin, coin2
    if type == 1:
        coin = Coin(coins_list['1'])
        coins.add(coin)
        all_sprites.add(coin)
    else:
        coin2 = Coin(coins_list['2'])
        super_coin_group.add(coin2)
        all_sprites.add(coin2)


while not game_over:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            game_over = True

    screen.blit(background, (0, 0)) 
    # displaying total score
    screen.blit(
        font_small.render(f'Score: {SCORE}', True, BLACK), (237, 9)
    )  
    # displaying number of touched coins
    screen.blit(
        font_small.render(f'Coins: {simple_coins}', True, BLACK), (237, 30)
    )  
    # displaying number of touched coins
    screen.blit(
        font_small.render(f'Small coins: {small_coins}', True, BLACK), (237, 51)
    )  

    for sprite in all_sprites:
        sprite.move()  # moving and displaying all sprites
        sprite.draw(screen)

    if SCORE % 12 == 0 and SCORE != 0:
        if not is_super_coin_generated:
            is_super_coin_generated = True
            generate_coin(type=2)
    elif SCORE % 12 == 1:
        is_super_coin_generated = False

    total_coins = simple_coins + small_coins

    if total_coins % 7 == 0 and total_coins != 0:
        if not is_speed_increased:
            is_speed_increased = True
            SPEED += 2
    elif total_coins % 7 == 1:
        is_speed_increased = False

    if coin2:
        if pygame.sprite.spritecollideany(player, super_coin_group):
            coin2.kill()
            small_coins += 1
            SCORE += 2

    if pygame.sprite.spritecollideany(player, coins):
        coin.kill()  # coin disappear
        SCORE += 1  # for touching a coin player get one points
        simple_coins += 1  
        generate_coin()  #new coin will appear

    if pygame.sprite.spritecollideany(player, enemies):  # collision with enemy car
        pygame.mixer.music.stop()
        pygame.mixer.Sound('crash.wav').play()  
        time.sleep(1)  # wait of 1 second

        screen.fill((BLACK))  
        screen.blit(game_over_text_label, (12, 190))  # displaying message that game over
        screen.blit(font_small.render(f'Your score: {SCORE}', True, WHITE), (15, 270))  # display score
        screen.blit(font_small.render(f'Simple coins: {simple_coins}', True, WHITE),
                    (15, 290))  # display number of coins
        screen.blit(font_small.render(f'Super coins: {small_coins}', True, WHITE),
                    (15, 311))  # display number of coins

        pygame.display.update()  # updating the screen for showing game over page

        for sprite in all_sprites:
            sprite.kill()  # stopping the game

        time.sleep(2)  # wait for 2 seconds

        game_over = True  # condition of game

    pygame.display.update()  # changing the position of objects
    clock.tick(fps)  # speed of changing the screen

pygame.quit()
