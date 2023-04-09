# Import required modules
import pygame

# Initialize Pygame
pygame.init()

#color and screen size
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CANVAS_SIZE = (640, 480)
x = 250
y = 200
size = 50
#screen
screen = pygame.display.set_caption("paint")
screen = pygame.display.set_mode(CANVAS_SIZE)
screen.fill(WHITE)
#font
font = pygame.font.Font(None, 24)
#tools and color of drawing line
drawing_color = BLACK
drawing_tool = "line"
erasersize = 1000
# Set up the button area
button_area = pygame.Rect(0, 0, CANVAS_SIZE[0], 50)
# Set up the last mouse position
last_mouse_pos = None
#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                drawing_tool = "square"
            elif event.key == pygame.K_2:
                drawing_tool = "righttriangle"
            elif event.key == pygame.K_3:
                drawing_tool = "equi"
            elif event.key == pygame.K_4:
                drawing_tool = "rhombus"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #if the mouse was pressed
            if button_area.collidepoint(event.pos):
            #check which button was pressed
                if event.button == 1:
                    if event.pos[0] < 70:
                        drawing_tool = "line"
                    elif event.pos[0] < 140:
                        drawing_tool = "rectangle"
                    elif event.pos[0] < 220:
                        drawing_tool = "circle"
                    elif event.pos[0] < 300:
                        drawing_tool = "eraser"
                    elif event.button == 3:
                        # Open a color picker dialog box
                        color = pygame.Color(drawing_color[0], drawing_color[1], drawing_color[2])
                        new_color = pygame.colordialog.askcolor(color)
                        if new_color[0]:
                            drawing_color = new_color[0]

                # Draw on the canvas
                else:
                    if event.button == 1:
                # Check which drawing tool is selected
                        mouse_pos = pygame.mouse.get_pos()
                    if drawing_tool == "line":
                        if last_mouse_pos:
                            pygame.draw.line(screen, drawing_color, last_mouse_pos, mouse_pos, 2)
                        last_mouse_pos = mouse_pos
                    elif drawing_tool == "rectangle":
                        if last_mouse_pos:
                            pygame.draw.rect(screen, WHITE, (last_mouse_pos, mouse_pos))
                            #calculating top-left pos of rect and its x and y for diff
                            rect = pygame.Rect((min(mouse_pos[0], last_mouse_pos[0]), min(mouse_pos[1], last_mouse_pos[1])), (abs(mouse_pos[0] - last_mouse_pos[0]), abs(mouse_pos[1] - last_mouse_pos[1]))) 
                            pygame.draw.rect(screen, drawing_color, rect)
                        last_mouse_pos = mouse_pos
                    elif drawing_tool == "circle":
                        if last_mouse_pos:
                            #calculating the size of circle
                            radius = int(((mouse_pos[0] - last_mouse_pos[0]) ** 2 + (mouse_pos[1] - last_mouse_pos[1]) ** 2) ** 0.5)
                            pygame.draw.circle(screen, drawing_color, last_mouse_pos, radius, 2)
                        last_mouse_pos = mouse_pos
                    elif drawing_tool == "eraser":
                        pygame.draw.circle(screen, WHITE, mouse_pos, erasersize)
                    elif drawing_tool == "clear":
                        screen.fill(WHITE)
                    elif drawing_tool == "square":
                        if last_mouse_pos:   
                            #Color, coordinates and size
                            pygame.draw.rect(screen, (0, 0, 0), (x, y, size, size))
                        last_mouse_pos = mouse_pos
                    elif drawing_tool == "righttriangle":
                        if last_mouse_pos:
                            pygame.draw.polygon(screen, (0, 0, 0), [(x, y), (x, y + size), (x + size, y + size)])
                        last_mouse_pos = mouse_pos
                    elif drawing_tool == "equi":
                        if last_mouse_pos:
                            pygame.draw.polygon(screen, (0, 0, 0), [(x, y), (x + size, y), (x + size / 2, y + size)])
                        last_mouse_pos = mouse_pos
                    elif drawing_tool == "rhombus":
                        if last_mouse_pos:
                            pygame.draw.polygon(screen, (0, 0, 0), [(x, y + size / 2), (x + size / 2, y), (x + size, y + size / 2), (x + size / 2, y + size)])
                        last_mouse_pos = mouse_pos

        elif event.type == pygame.MOUSEBUTTONUP:
            last_mouse_pos = None

        elif event.type == pygame.MOUSEMOTION:
            # Draw on the canvas
            if event.buttons[0] == 1:
            # Check which drawing tool is selected
                mouse_pos = pygame.mouse.get_pos()
                if drawing_tool == "line":
                    if last_mouse_pos:
                        pygame.draw.line(screen, drawing_color, last_mouse_pos, mouse_pos, 2)
                    last_mouse_pos = mouse_pos
                elif drawing_tool == "rectangle":
                    if last_mouse_pos:
                        pygame.draw.rect(screen, WHITE, (last_mouse_pos, mouse_pos))
                        rect = pygame.Rect((min(mouse_pos[0], last_mouse_pos[0]), min(mouse_pos[1], last_mouse_pos[1])), (abs(mouse_pos[0] - last_mouse_pos[0]), abs(mouse_pos[1] - last_mouse_pos[1])))
                        pygame.draw.rect(screen, drawing_color, rect)
                    last_mouse_pos = mouse_pos
                elif drawing_tool == "circle":
                    if last_mouse_pos:
                        radius = int(((mouse_pos[0] - last_mouse_pos[0]) ** 2 + (mouse_pos[1] - last_mouse_pos[1]) ** 2) ** 0.5)
                        pygame.draw.circle(screen, drawing_color, last_mouse_pos, radius, 2)
                    last_mouse_pos = mouse_pos
                elif drawing_tool == "eraser":
                    pygame.draw.circle(screen, WHITE, mouse_pos, erasersize)
                elif drawing_tool == "square":
                    if last_mouse_pos:   
                            pygame.draw.rect(screen, (0, 0, 0), (x, y, size, size))
                    last_mouse_pos = mouse_pos
                elif drawing_tool == "righttriangle":
                    if last_mouse_pos:
                            pygame.draw.polygon(screen, (0, 0, 0), [(x, y), (x, y + size), (x + size, y + size)])
                    last_mouse_pos = mouse_pos
                elif drawing_tool == "equi":
                    if last_mouse_pos:
                            pygame.draw.polygon(screen, (0, 0, 0), [(x, y), (x + size, y), (x + size / 2, y + size)])
                    last_mouse_pos = mouse_pos
                elif drawing_tool == "rhombus":
                    if last_mouse_pos:
                            pygame.draw.polygon(screen, (0, 0, 0), [(x, y + size / 2), (x + size / 2, y), (x + size, y + size / 2), (x + size / 2, y + size)])
                    last_mouse_pos = mouse_pos

    pygame.draw.rect(screen, BLACK, button_area)
    pygame.draw.line(screen, WHITE, (10, 25), (60, 25), 2)
    pygame.draw.rect(screen, RED, (80, 10, 50, 30))
    pygame.draw.rect(screen, GREEN, (150, 10, 50, 30))
    pygame.draw.rect(screen, BLUE, (220, 10, 50, 30))
    pygame.draw.rect(screen, BLACK, (290, 10, 50, 30))
    #pygame.draw.circle(screen, WHITE, (325, 25), erasersize)
    pygame.draw.rect(screen, BLACK, (355, 10, 50, 30))
    button_text = font.render("Line", True, WHITE)
    screen.blit(button_text, (25 - button_text.get_width() // 2, 25 - button_text.get_height() // 2))
    button_text = font.render("Rectangle", True, WHITE)
    screen.blit(button_text, (95 - button_text.get_width() // 2, 25 - button_text.get_height() // 2))
    button_text = font.render("Circle", True, WHITE)
    screen.blit(button_text, (165 - button_text.get_width() // 2, 25 - button_text.get_height() // 2))
    button_text = font.render("Eraser", True, WHITE)
    screen.blit(button_text, (235 - button_text.get_width() // 2, 25 - button_text.get_height() // 2))
    button_text = font.render("Color", True, WHITE)
    screen.blit(button_text, (325 - button_text.get_width() // 2, 25 - button_text.get_height() // 2))
    button_text = font.render("Clear", True, WHITE)
    screen.blit(button_text, (385 - button_text.get_width() // 2, 25 - button_text.get_height() // 2))                
    pygame.display.update()