import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 2
    y = 2
    mode = 'blue'
    points = []
    painting_mode = 'circle'
    
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determine if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_l:
                    painting_mode = 'rectangle'
                elif event.key == pygame.K_c:
                    painting_mode = 'circle'
                elif event.key == pygame.K_e:
                    painting_mode = 'eraser'
                elif event.key == pygame.K_1:
                    painting_mode = 'equilateral triangle'
                elif event.key == pygame.K_2:
                    painting_mode = 'right triangle'
                elif event.key == pygame.K_3:
                    painting_mode = 'rhombus'

            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                position = event.pos
                points = points + [position]
                points = points[-256:]
                
        screen.fill((0, 0, 0))
        
        # draw all points
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode, painting_mode)
            i += 1
        
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode, painting_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    #differences between the x and y coords of the start&end points of the line
    #setting number of iterations to the max of diffs
    #determining the number of time the func will loop to draw
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations #length of a line for iter of cycle
        aprogress = 1 - progress #line from end to start
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        if painting_mode == 'circle':
            pygame.draw.circle(screen, color, (x, y), width)
        if painting_mode == 'rect':
            pygame.draw.rect(screen, color, (x, y, width + 30, width + 30))
        if painting_mode == 'equilateral triangle':
            pygame.draw.polygon(screen, color, ((x - width, y), (x, y - width), (x+ width, y)))
        if painting_mode == 'right triangle':
            pygame.draw.polygon(screen, color, ((x - 0.5 * width, y), (x, y - width), (x+ 0.5 *width, y)))
        if painting_mode == 'rhombus':
            pygame.draw.polygon(screen, color, ((x - width, y), (x, y - width), (x+ width, y), (x, y + width)))            
        if painting_mode == 'eraser':
            pygame.draw.rect(screen, (0, 0, 0), (x, y, width, width))


main()