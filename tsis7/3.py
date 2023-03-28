import pygame
pygame.init()
width=500
height=500
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Ball")
radius=25
circle_x=(width-radius)//2
circle_y=(height-radius)//2




running = True
while running:
    screen.fill("white")

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      elif event.type==pygame.KEYDOWN:
          if event.key==pygame.K_UP:
              circle_y-=20
          elif event.key==pygame.K_DOWN:
              circle_y+=20
          elif event.key==pygame.K_LEFT:
              circle_x-=20
          elif event.key==pygame.K_RIGHT:
              circle_x+=20
    #to keep ball within the screen       
    circle_x=max(circle_x,radius)
    circle_y=max(circle_y,radius)
    circle_x=min(circle_x,width-radius)
    circle_y=min(circle_y,height-radius)
    
              
        
        
    pygame.draw.circle(screen,pygame.Color("red"),(circle_x,circle_y),radius)
    
    

    pygame.display.update()


pygame.quit()