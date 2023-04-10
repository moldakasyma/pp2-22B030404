import pygame
import math
#initialization
pygame.init()
running = True

WINDOW_WIDTH, WINDOW_HEIGHT = (640, 480)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
#setting size and name
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    
color = BLUE
shape = 'line'

clock = pygame.time.Clock()
fps = 60

pygame.display.set_caption('Paint')
screen.fill(BLACK)

width = 15
#previous and current points
prev, cur = None, None






while running:
    #setting keys to work with the keyboard
    for event in pygame.event.get():
        pressed = pygame.key.get_pressed()
        #pressing cltr
        ctrl_pressed = pressed[pygame.K_RCTRL] or pressed[pygame.K_LCTRL]
        #pressing alt
        alt_pressed = pressed[pygame.K_RALT] or pressed[pygame.K_LALT]

        if event.type == pygame.QUIT:
            running = False
        #width of a shape
        if event.type == pygame.KEYDOWN:
            if pressed[pygame.K_DOWN] and width > 1:
                width -= 1
            if pressed[pygame.K_UP]:
                width += 1
        #colors        
            if alt_pressed and pressed[pygame.K_b]:
                color = BLUE
            if alt_pressed and pressed[pygame.K_r]:
                color = RED
            if alt_pressed and pressed[pygame.K_g]:
                color = GREEN
        #shape
            if ctrl_pressed and pressed[pygame.K_c]:
                shape = 'circle'
            if ctrl_pressed and pressed[pygame.K_r]:
                shape = 'rectangle'
            if ctrl_pressed and pressed[pygame.K_l]:
                shape = 'line'
            if ctrl_pressed and pressed[pygame.K_e]:
                shape = 'eraser'
            if ctrl_pressed and pressed[pygame.K_s]:
                shape = 'square'
            if ctrl_pressed and pressed[pygame.K_t]:
                shape = 'right triangle'
            if ctrl_pressed and pressed[pygame.K_g]:
                shape = 'equilateral triangle'
            if ctrl_pressed and pressed[pygame.K_g]:
                shape = 'rhombus'
        #setting line and eraser
        if shape == 'line' or shape == 'eraser':
            if event.type == pygame.MOUSEBUTTONDOWN:
                prev = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEMOTION:
                cur = pygame.mouse.get_pos()
                if prev:
                    if shape == 'line':
                        pygame.draw.line(screen, color, prev, cur, width)
                    if shape == 'eraser':
                        pygame.draw.line(screen, BLACK, prev, cur, width)
                    prev = cur
            if event.type == pygame.MOUSEBUTTONUP:
                prev = None
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                #previous point
                prev = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                #current point
                cur = pygame.mouse.get_pos()
                if shape == 'circle':
                    #coordinates
                    x = (prev[0]+cur[0])/2
                    y = (prev[1]+cur[1])/2
                    #ox, oy radius
                    rx = abs(prev[0]-cur[0])/2
                    ry = abs(prev[1]-cur[1])/2
                    #radius
                    r = (rx + ry)/2
                    pygame.draw.circle(screen, color, (x, y), r, width)
                elif shape == 'rectangle' or shape=='square': #since they are similar
                    
                    #coordinates
                    x = min(prev[0], cur[0])
                    y = min(prev[1], cur[1])
                    #length
                    lx = abs(prev[0]-cur[0])
                    ly = abs(prev[1]-cur[1])
                    if shape=='square':
                        lx = (lx+ly)/2  # length and width of the sqaure
                        ly = lx
                    pygame.draw.rect(screen, color, (x, y, lx, ly), width)
                elif shape=='right triangle' or shape=='equilateral triangle':
                    x=min(prev[0],cur[0])
                    y=min(prev[1],cur[1])
                    lx=abs(prev[0]-cur[0])
                    ly=abs(prev[1]-cur[1])
                    if shape=='right triangle':
                        ly = math.sqrt(lx**2 - (lx/2)**2)  # triangles sides
                        points = (x, y+ly), (x+lx/2, y), (x+lx, y+ly)  # draw by three points
                        pygame.draw.polygon(screen, color, points, width)
                    
                elif shape=='rhombus':
                    x=min(prev[0],cur[0])
                    y=min(prev[1],cur[1])
                    lx=abs(prev[0]-cur[0])
                    ly=abs(prev[1]-cur[1])
                    points = (x+lx/2, y), (x+lx, y+ly/2), (x+lx/2, y+ly), (x, y+ly/2)
                    pygame.draw.polygon(screen, color, points, width)  # draw by points
                        
    pygame.display.flip()
    clock.tick(fps)

