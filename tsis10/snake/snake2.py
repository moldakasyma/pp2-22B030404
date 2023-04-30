import pygame, psycopg2, time
from random import randrange, choice
from config import conn

#Name of the player
name = input("Enter your name: ")

#Connecting database
config = psycopg2.connect(**conn)
current = config.cursor()

pygame.init()

#Global variables
WIDTH, HEIGHT = 400, 450
cell = 20
score_pos = (20, 410)
level_pos = (325, 410)

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (221,160,221)

#Initialization
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')

#Creating the Clock
clock = pygame.time.Clock()

#Creating the font for texts
font_big = pygame.font.SysFont("verdana", 20)
font = pygame.font.SysFont("verdana", 10)

#Creating the text for winning
winning = font.render(f'YOU WON! CONGRATULATIONS', True, BLACK)



class Food:
    def __init__(self,color):
        self.x = randrange(0, WIDTH, cell)
        self.y = randrange(0, HEIGHT-50, cell)
        self.color=color
          

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, cell, cell)) 
      
       
    def redraw(self):
        self.x = randrange(0, WIDTH, cell)
        self.y = randrange(0, HEIGHT-50, cell)
        

class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, cell, cell))

class Snake:
    def __init__(self):
        self.speed = cell
        self.body = [[80, 80]]
        self.dx = self.speed
        self.dy = 0
        self.destination = ''
        self.color = GREEN
    
    def move(self):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.destination != 'right':
                    self.dx = -self.speed
                    self.dy = 0
                    self.destination = 'left'
                if event.key == pygame.K_RIGHT and self.destination != 'left':
                    self.dx = self.speed
                    self.dy = 0
                    self.destination = 'right'
                if event.key == pygame.K_UP and self.destination != 'down':
                    self.dx = 0
                    self.dy = -self.speed
                    self.destination = 'up'
                if event.key == pygame.K_DOWN and self.destination != 'up':
                    self.dx = 0
                    self.dy = self.speed
                    self.destination = 'down'

        #Movement of the snake
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i][0] = self.body[i - 1][0]
            self.body[i][1] = self.body[i - 1][1]

        #Change snake's head position
        self.body[0][0] += self.dx
        self.body[0][1] += self.dy

        #Movement outside the playing area
        self.body[0][0] %= WIDTH
        self.body[0][1] %= HEIGHT - 50

    def draw(self):
        for block in self.body:
            pygame.draw.rect(screen, self.color, (block[0], block[1], cell, cell))
    
    #Collision with food
    def collide_food(self, f: Food):
        global SCORE
        global cnt
        if self.body[0][0] == f.x and self.body[0][1] == f.y:
            self.body.append([1000, 1000])
         
            cnt += 1
            SCORE+=1

        
    #Collision with snake       
    def collide_self(self):
        global lose
        if self.body[0] in self.body[1:]:
            lose = True

    #Checking the place of food appearance
    def check_food(self, f: Food):
        if [f.x, f.y] in self.body:
            f.redraw()

restart = True
flag = False
while restart:
    FPS = 7

    finished = False
    lose = False
    win = False
    pause = False
    exist = False

    food = Food(pygame.Color('red'))  
    snake = Snake()
    

    level = 1
    SCORE = 0
    cnt = 0   #for level up
    while not finished:
        clock.tick(FPS)
        screen.fill(BLACK)



        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                finished = True
                restart = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                finished = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                pause = True #pause

        #Reading the txt files of walls
        walls_coor = open(f'level{level}.txt', 'r').readlines()
        walls = []
        for i, line in enumerate(walls_coor):
            for j, each in enumerate(line):
                if each == '#':
                    walls.append(Wall(j * cell, i * cell))

        #Drawing and moving the objects
        food.draw()
        snake.draw()
        snake.move()
        
        #Snake's collision
        snake.collide_food(food)
        snake.collide_self()
        snake.check_food(food)

        #Drawing the walls
        for wall in walls:
            wall.draw()

            #Checking the food appearance
            if food.x == wall.x and food.y == wall.y:
                food.redraw()
            


            #Collision with walls
            if snake.body[0][0] == wall.x and snake.body[0][1] == wall.y:
                lose = True

        #Increasing the speed and level up
        if cnt == 5:
            FPS += 2 
            level += 1
            cnt = 0
        
        #Winning condition
        if level == 5:
            win = True

        #Texts
        losing = font.render(f'GAME OVER!YOUR SCORE:{SCORE}', True, BLACK)
        on_level = font.render(f'level:{level}', True, BLACK)
        tapping = font.render(f'TAP SPACE TO RESTART', True, BLACK)
        pausing = font.render(f'GAME IS PAUSED! YOUR SCORE {SCORE} p', True, BLACK)
        an_tapping = font.render(f'TAP U TO UNPAUSE', True, BLACK)

        while pause:
            pygame.draw.rect(screen, WHITE, (100, 100, 200, 200))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    restart = False
                    finished = True
                    pause = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_u:
                    pause = False #unpause

            if pause:
                screen.blit(pausing, (WIDTH // 2 - 84 , HEIGHT // 2 - 50))
                screen.blit(on_level, (WIDTH // 2 - 34 , HEIGHT // 2 - 30))
                screen.blit(an_tapping, (WIDTH // 2 - 74 , HEIGHT // 2 - 5))
                pygame.display.update()

                insert_int = '''
                INSERT INTO snake VALUES (%s, %s, %s);
                '''
                try:
                    #getting the highscore and level
                    get = f'''
                        SELECT highscore, level FROM snake WHERE username = '{name}';
                    '''
                    current.execute(get)
                    output = current.fetchone()
                    high_score = int(output[0])
                    lvl = int(output[1])
                    exist = True
                except:
                    pass
                
                #if the known user comparing the previous data 
                if exist:
                    if SCORE > high_score:
                        update_sc = '''
                            UPDATE snake SET highscore = %s WHERE username = %s;
                        '''
                        current.execute(update_sc, (SCORE,name))
                    if level > lvl:
                        update_l = '''
                            UPDATE snake SET level = %s WHERE username = %s;
                        '''
                        current.execute(update_l, (level,name))
                #otherwise inserting
                else:
                    current.execute(insert_int, (f'{name}', f'{SCORE}', f'{level}'))
        #     cursor.close()
        #     db.commit()
        #     db.close()
        pygame.display.flip()

        while lose or win:
            pygame.draw.rect(screen, WHITE, (100, 100, 200, 200))
            if lose:
                screen.blit(losing, (WIDTH // 2 - 84 , HEIGHT // 2 - 50))
                screen.blit(on_level, (WIDTH // 2 - 34 , HEIGHT // 2 - 30))
                screen.blit(tapping, (WIDTH // 2 - 74 , HEIGHT // 2 - 5))

                pygame.display.update()
                time.sleep(5)

                insert_into = '''
                INSERT INTO snake VALUES (%s, %s, %s);
                '''
                try:
                    #getting the highscore and level
                    get = f'''
                        SELECT highscore, level FROM snake WHERE username = '{name}';
                    '''
                    current.execute(get)
                    output = current.fetchone()
                    high_score = output[0]
                    lvl = output[1]
                    exist = True
                except:
                    pass
                #if the known user comparing the previous data
                if exist:
                    if SCORE > high_score:
                        update_s = '''
                            UPDATE snake SET highscore = %s WHERE username = %s;
                        '''
                        current.execute(update_s,(SCORE,name))
                    if level > lvl:
                        update_l = '''
                            UPDATE snake SET level = %s WHERE username = %s;
                        '''
                        current.execute(update_l,(level,name))
                #otherwise inserting
                else:
                    current.execute(insert_into, (f'{name}', f'{SCORE}', f'{level}'))
                current.close()
                config.commit()
                config.close()
            
            #finished = True
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    restart = False
                    finished = True
                    lose = False
                    win = False
                    pause = False

                #restart by tapping the space   
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    lose = False
                    win = False
                    pause = False
                    finished = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_u:
                    pause = False
            

            if win:
                screen.blit(winning, (WIDTH // 2 - 84 , HEIGHT // 2 - 50))
                screen.blit(tapping, (WIDTH // 2 - 74 , HEIGHT // 2 - 30))

            pygame.display.flip()
        
        #Texts
        score_text = font_big.render(f'SCORE: {SCORE}', True, WHITE)
        level_text = font_big.render(f'LEVEL: {level}', True, WHITE)
        screen.blit(score_text, (30,410))
        screen.blit(level_text, (300,410))
        
        pygame.display.flip()
    
    pygame.display.flip()
pygame.quit()