import pygame
import time
import random
pygame.init()
pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

snake_position = [100, 50]
snake_body = [  [100, 50],
                [90, 50],
                
            ]

food_position = [random.randrange(1, (600//10)) * 10,random.randrange(1, (600//10)) * 10]
food_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(f'Foods:{score} ' , True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

    
def show_score2(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(f'level:{level}', True, color)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (50,30)
    game_window.blit(score_surface, score_rect)
def game_over():
    my_font = pygame.font.SysFont('Verdana', 60)
    game_over_surface = my_font.render("Game over", True, pygame.Color('red'))
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (300, 260)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


while True:
    snake_speed = 8
    level = 0
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
 
    # If two keys pressed simultaneously
    
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 
    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()
    if not food_spawn:
        food_position = [random.randrange(1, (600//10)) * 10,random.randrange(1, (600//10)) * 10]
    scores = range(score+1)
    for i in scores:
        if (i % 4 == 0 and i != 0):
            snake_speed += 1
            level += 1
    food_spawn = True
    game_window.fill(pygame.Color('black'))
     
    for pos in snake_body:
        pygame.draw.rect(game_window, pygame.Color('green'), pygame.Rect(
          pos[0], pos[1], 10, 10))
         
    pygame.draw.rect(game_window, pygame.Color('red'), pygame.Rect(
      food_position[0], food_position[1], 10, 10))
 
    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > 590:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > 590:
        game_over()
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
    # displaying score countinuously
    show_score(1, pygame.Color('white'), 'Verdana', 20)
   
    show_score2(1, pygame.Color('white'), 'Verdana', 20)
     
    # Refresh game screen
    pygame.display.update()
 
    # Frame Per Second /Refresh Rate
    clock.tick(snake_speed)