import pygame
from datetime import datetime
import math
RES=WIDTH,HEIGHT=800,800
H_WIDTH,H_HEIGHT=WIDTH//2,HEIGHT//2
RADIUS=H_HEIGHT-50
radius_list={'sec':RADIUS-10,'min':RADIUS-55,'hour':RADIUS-100,'digit':RADIUS-30}

pygame.init()
surface=pygame.display.set_mode(RES)
clock=pygame.time.Clock()
clock12=dict(zip(range(12),range(0,360,30)))
clock60=dict(zip(range(60),range(0,360,6)))
font=pygame.font.SysFont('Vernada',60)
img=pygame.image.load('main-clock.png')
m=pygame.image.load("right-hand.png")
s=pygame.image.load("left-hand.png")



def clock_pos(clock_dict,clock_hand,key):
    x=H_WIDTH+radius_list[key]*math.cos(math.radians(clock_dict[clock_hand])-math.pi/2)
    y=H_HEIGHT+radius_list[key]*math.sin(math.radians(clock_dict[clock_hand])-math.pi/2)
    return x,y
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        
    surface.fill(pygame.Color("white"))
    surface.blit(img,(0,0))

    
    t=datetime.now()
    
    minute,second=t.minute,t.second


    
   
    pygame.draw.line(surface, pygame.Color('blue'),(H_WIDTH,H_HEIGHT),clock_pos(clock60,minute,'min'),7)
    pygame.draw.line(surface,pygame.Color('black'),(H_WIDTH,H_HEIGHT),clock_pos(clock60,second,'sec'),4)
    pygame.draw.circle(surface,pygame.Color('white'),(H_WIDTH,H_HEIGHT),8)
        


    pygame.display.flip()
    clock.tick(20)