import pygame

pygame.init()
running = True

WINDOW_WIDTH, WINDOW_HEIGHT = (640, 480)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

color = BLUE
shape = 'line'

clock = pygame.time.Clock()
fps = 60

pygame.display.set_caption('Paint')
screen.fill(BLACK)

width = 15

prev, cur = None, None






while running:

    for event in pygame.event.get():
        pressed = pygame.key.get_pressed()
        ctrl_pressed = pressed[pygame.K_RCTRL] or pressed[pygame.K_LCTRL]
        alt_pressed = pressed[pygame.K_RALT] or pressed[pygame.K_LALT]

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if pressed[pygame.K_DOWN] and width > 1:
                width -= 1
            if pressed[pygame.K_UP]:
                width += 1
            if alt_pressed and pressed[pygame.K_b]:
                color = BLUE
            if alt_pressed and pressed[pygame.K_r]:
                color = RED
            if alt_pressed and pressed[pygame.K_g]:
                color = GREEN
            
            if ctrl_pressed and pressed[pygame.K_c]:
                shape = 'circle'
            if ctrl_pressed and pressed[pygame.K_r]:
                shape = 'rectangle'
            if ctrl_pressed and pressed[pygame.K_l]:
                shape = 'line'
            if ctrl_pressed and pressed[pygame.K_e]:
                shape = 'eraser'

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
                prev = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                cur = pygame.mouse.get_pos()
                if shape == 'circle':
                    x = (prev[0]+cur[0])/2
                    y = (prev[1]+cur[1])/2
                    rx = abs(prev[0]-cur[0])/2
                    ry = abs(prev[1]-cur[1])/2
                    r = (rx + ry)/2
                    pygame.draw.circle(screen, color, (x, y), r, width)
                if shape == 'rectangle':
                    x = min(prev[0], cur[0])
                    y = min(prev[1], cur[1])
                    lx = abs(prev[0]-cur[0])
                    ly = abs(prev[1]-cur[1])
                    pygame.draw.rect(screen, color, (x, y, lx, ly), width)
    pygame.display.flip()
    clock.tick(fps)


