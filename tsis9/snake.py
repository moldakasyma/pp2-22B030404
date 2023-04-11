import pygame
import random
def game():
    
    pygame.init()
    
    #setting screen and name for a game
    screen = pygame.display.set_mode((400,500))
    pygame.display.set_caption("Snake")
    #colors
    black = (0,0,0)
    red = (255,0,0)
    white = (255,255,255)
    green = (0, 255, 0)
    yellow = (238,255,27)
    #black line to divide monitor
    head_line_start = (0,100)
    head_line_end = (400,100)
    #Food
    food = (random.randint(1, screen.get_width() / 10 - 1) * 10, random.randint(10, screen.get_height() / 10 - 1) * 10)
    food_spawn = True
    
    food2 = (random.randint(1, screen.get_width() / 10 - 1) * 10, random.randint(10, screen.get_height() / 10 - 1) * 10)
    food2_spawn = True
    food3 = (random.randint(1, screen.get_width() / 10 - 1) * 10, random.randint(10, screen.get_height() / 10 - 1) * 10)
    food3_spawn = True
    #score and level
    score = 0
    speed = 1
    level = ['1','2','3','4', '5']
    score_font = pygame.font.SysFont('Verdana',20)
    #direction of snake
    change = 'right'
    direction = 'right'
    #starting position
    player = [200, 200]
    snake = [[220, 200], [230, 200]]
    
    clock = pygame.time.Clock()
    
    # for timer food2-fruit
    pygame.time.set_timer(pygame.USEREVENT, 9000)
    food3_timer = True
    check = True
    while check:
        for action in pygame.event.get():
        #Exit
            if action.type == pygame.QUIT:
                check = False
                #pygame.quit()
            elif action.type == pygame.USEREVENT:
                food3_timer = not food3_timer
    
            
            # Moving the snake
            if action.type == pygame.KEYDOWN:
                if action.key == pygame.K_UP:
                    change = 'up'
                if action.key == pygame.K_DOWN:
                    change = 'down'
                if action.key == pygame.K_LEFT:
                    change = 'left'
                if action.key == pygame.K_RIGHT:
                    change = 'right'
            
        # If two keys pressed simultaneously
        if direction != 'up' and change == 'down':
            direction = 'down'
        if direction != 'down' and change == 'up':
            direction = 'up'
        if direction != 'left' and change == 'right':
            direction = 'right'
        if direction != 'right' and change == 'left':
            direction = 'left'
        
        #Speed of snake (0 - x, 1 - y cordinates)
        if direction == 'up':
            player[1] -= 10
        if direction == 'down':
            player[1] += 10 
        if direction == 'left':
            player[0] -= 10 
        if direction == 'right':
            player[0] += 10  
        
        
        #food spawn (random) if food generated in otherside, so this food delete
        while food_spawn:
            food = (random.randint(1,screen.get_width() / 10 - 1) * 10, random.randint(10, screen.get_height() / 10 - 1) * 10)
            if food not in snake:
                food_spawn = False
        while food2_spawn:
            food2 = (random.randint(1,screen.get_width() / 10 - 1) * 10, random.randint(10, screen.get_height() / 10 - 1) * 10)
            if food2 not in snake:
                food2_spawn = False
        while food3_spawn:
                food3 = (random.randint(1,screen.get_width() / 10 - 1) * 10, random.randint(10, screen.get_height() / 10 - 1) * 10)
                if food3 not in snake:
                    food3_spawn = False
                
        snake.insert(0, list(player))
        
        screen.fill((white))
        if food3_timer:
            #drawing food
            pygame.draw.rect(screen, pygame.Color('pink'), pygame.Rect(food3[0],food3[1], 10, 10))
            pygame.draw.rect(screen, red, pygame.Rect(food[0], food[1], 10, 10))
           
            pygame.draw.rect(screen, yellow, pygame.Rect(food2[0], food2[1], 10, 10))
        #Eat food and change score 
        if (player[0] == food[0] and player[1] == food[1]) or (player[0] == food2[0] and player[1] == food2[1]) or (player[0] ==food3[0] and player[1] == food3[1]):
            speed = score // 4 + 1
            if player[0] == food[0] and player[1] == food[1]:
                score += 1
                food_spawn = True 
            elif player[0] == food2[0] and player[1] == food2[1]:
                score += 2
                food2_spawn = True
            elif player[0] == food3[0] and player[1] == food3[1]:
                score += 1
                food3_spawn = True
        else:
            snake.pop()
        
        
        #line
        pygame.draw.line(screen, black, head_line_start, head_line_end, 1)
        
        #borders
        if ((player[0] < -5 or player[0] > screen.get_width() - 5) or (player[1] < 100 or player[1] > screen.get_height() - 5)):
            break
        
        #in case if we run into ourself , so we won't eat ourself
        if player in snake[1:]:
            break
         
        #drawing the snake
        for pos in snake:
            pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))
        

        
        #Show score and level
        screen.blit(score_font.render(f'Score: {score}' , True, black) , (20,38))
        #Текущий уровень игры
        if speed <= 7:
            screen.blit(score_font.render(f'Speed: {level [speed - 1]}', True, black), (20,58))
        else:
            screen.blit(score_font.render(f'Speed: death', True, black), (20,58))
        
        pygame.display.update()
        #to not to overload the system we need to update fps 
        clock.tick(10 + speed * 2)
    
    #to close the window after game over
    while check:
        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                check = False
        
                screen.fill(white)
        
        screen.blit(score_font.render('Game over' , True, black), (145,200))
        pygame.display.update()
game()
pygame.quit()