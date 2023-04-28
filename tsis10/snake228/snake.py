import random
import time
import pygame
import psycopg2

conn = psycopg2.connect(
    database="snake",
    user="postgres",
    password="12345",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

user = input('Enter your username: ')
select_command = "SELECT level FROM users WHERE first_name = %s"
cur.execute(select_command, (user,))
result = cur.fetchone()
print(result)
pygame.init()
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
FORESTGREEN = (34, 139, 34)
BLOCK_SIZE = 40
WHITE = (255, 255, 255)
SPEED = 5
SCORE = 0
level = 1
clock = pygame.time.Clock()

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
win = font.render("Congratulation", True, BLACK)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    def __init__(self):
        self.body = [
            Point(
                x=WIDTH // BLOCK_SIZE // 2,
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
            Point(
                x=WIDTH // BLOCK_SIZE // 2 + 1,
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
        ]

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(
            SCREEN,
            RED,
            pygame.Rect(
                head.x * BLOCK_SIZE,
                head.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
        for body in self.body[1:]:
            pygame.draw.rect(
                SCREEN,
                BLUE,
                pygame.Rect(
                    body.x * BLOCK_SIZE,
                    body.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )

    def move(self, dx, dy):
        for idx in range(len(self.body) - 1, 0, -1):
            self.body[idx].x = self.body[idx - 1].x
            self.body[idx].y = self.body[idx - 1].y
        self.body[0].x += dx
        self.body[0].y += dy

        if self.body[0].x > WIDTH // BLOCK_SIZE:
            self.body[0].x = 0
        elif self.body[0].x < 0:
            self.body[0].x = WIDTH // BLOCK_SIZE
        elif self.body[0].y < 0:
            self.body[0].y = WIDTH // BLOCK_SIZE
        elif self.body[0].y > HEIGHT // BLOCK_SIZE:
            self.body[0].y = 0

    def check_collision(self, food):
        if food.location.x != self.body[0].x:
            return False
        if food.location.y != self.body[0].y:
            return False
        return True
    
    def check_collision_wall(self, wall):
        for i in range(0, len(wall.walls)):
            if wall.walls[i].x == self.body[0].x and wall.walls[i].y == self.body[0].y:
                return True
        return False

class Food:
    def __init__(self, x, y):
        self.location = Point(x, y)
        self.color = GREEN

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            self.color,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
class Wall():
    def __init__(self, x_list, y_list):
        self.walls = []
        for i in range(0, len(x_list)):
            self.walls.append( Point(x_list[i],y_list[i]))

    def draw(self): 
        for wall in self.walls:
            pygame.draw.rect(
                SCREEN,
                RED,
                pygame.Rect(
                    wall.x * BLOCK_SIZE,
                    wall.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )


def main():
    global result
    global user
    global SCORE
    global SPEED
    global level
    running = True
    snake = Snake()
    food = Food(5, 5)
    x1_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 ] 
    y1_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    x2_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    y2_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    x3_list = [18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18]
    y3_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    level1 = Wall( x1_list, y1_list)
    level2 = Wall( x2_list, y2_list)
    level3 = Wall( x3_list, y3_list)
    dx, dy = 0, 0
    FOOD_SPAWNER = pygame.USEREVENT + 1
    pygame.time.set_timer(FOOD_SPAWNER, 8000)

    while running:
        SCREEN.fill(BLACK)

        if ( SCORE == 0): 
            current_level = level1
        if ( SCORE == 4): 
            current_level = level2
            SPEED = 8
            level = 2
            while ( len( snake.body ) < 3):
                snake.body.pop()
        if ( SCORE == 8):
            current_level = level3
            SPEED = 12
            level = 3
        if ( SCORE == 12):
            time.sleep( 0.5 )
            SCREEN.fill(RED)
            SCREEN.blit(win, (7 * BLOCK_SIZE, 10 * BLOCK_SIZE))
            pygame.display.update()
            time.sleep(2)
            inserting_score( result, user, SCORE, str(level) )
            conn.commit()
            cur.close()
            conn.close()
            pygame.quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == FOOD_SPAWNER:
                condition = True
                while condition:
                    current_color = random.choice( [GREEN, FORESTGREEN] )
                    food.color = current_color
                    xtest = random.randint(0, WIDTH // BLOCK_SIZE - 1)
                    ytest = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
                    if xtest not in range( snake.body[0].x, snake.body[-1].x):
                        for i in range(0, len(current_level.walls)):
                            if current_level.walls[i].x != xtest:
                                if ytest not in range( snake.body[0].y, snake.body[-1].y):
                                    for i in range(0, len(current_level.walls)):
                                        if current_level.walls[i].y != ytest:
                                            condition = False
                food.location.x = xtest
                food.location.y = ytest   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    dx, dy = 0, -1
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, +1
                elif event.key == pygame.K_RIGHT:
                    dx, dy = 1, 0
                elif event.key == pygame.K_LEFT:
                    dx, dy = -1, 0

        scores = font_small.render(str(SCORE), True, RED)
        level_tab = font_small.render('level: ' + str(level), True, RED)

        current_level.draw()
        snake.move(dx, dy)
        if snake.check_collision(food):
            if food.color == GREEN:
                SCORE += 1 
                snake.body.append(
                    Point(snake.body[-1].x, snake.body[-1].y)
                )

            if food.color == FORESTGREEN:
                SCORE += 2 
                snake.body.append(
                    Point(snake.body[-1].x, snake.body[-1].y)
                )
                snake.body.append(
                    Point(snake.body[-1].x, snake.body[-1].y)
                )               
            pygame.time.set_timer(FOOD_SPAWNER, 0)
            pygame.time.set_timer(FOOD_SPAWNER, 8000)

            current_color = random.choice( [GREEN, FORESTGREEN])
            food.color = current_color
            condition = True
            while condition:
                xtest = random.randint(0, WIDTH // BLOCK_SIZE - 1)
                ytest = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
                if xtest not in range( snake.body[0].x, snake.body[-1].x):
                    for i in range(0, len(current_level.walls)):
                        if current_level.walls[i].x != xtest:
                            if ytest not in range( snake.body[0].y, snake.body[-1].y):
                                for i in range(0, len(current_level.walls)):
                                    if current_level.walls[i].y != ytest:
                                        condition = False
            food.location.x = xtest
            food.location.y = ytest   
        if snake.check_collision_wall( current_level):
            time.sleep( 0.5 )
            SCREEN.fill(RED)
            SCREEN.blit(game_over, (7 * BLOCK_SIZE, 10 * BLOCK_SIZE))
            pygame.display.update()
            time.sleep(2)
            inserting_score( result, user, SCORE, level )
            conn.commit()
            cur.close()
            conn.close()
            pygame.quit()

        snake.draw()
        food.draw()
        SCREEN.blit(scores, (10,10))
        SCREEN.blit(level_tab, (10,50))
        pygame.display.flip()
        clock.tick(SPEED)

def inserting_score( result, user, score, level ):
        print( result, user, score, level)
        if result is None:
            insert_command = "INSERT INTO (first_name, level) VALUES (%s, %s)"
            cur.execute(insert_command, (user, level))
            insert_command = "INSERT INTO user_score (username, score) VALUES (%s, %s)"
            cur.execute(insert_command, (user, str(score)))
        else:
            update_command = "UPDATE user_score SET score = %s WHERE username = %s"
            cur.execute(update_command, (str(score), user))
        
        

if __name__ == '__main__':
    main()