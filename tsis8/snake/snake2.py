import random

import pygame

pygame.init()
WIDTH, HEIGHT = 800, 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
font = pygame.font.SysFont('arial', 36)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
BLOCK_SIZE = 40
pygame.display.set_caption('Snake v0')

#class Level:
   # def init(self):
      #  self.food_count = 0
      #  self.score = 0
   # def increase_level(self):
        #self.level += 1
        #self.food_count += 1
   # def get_score_for_food(self, food_count):
     #   return food_count * 10
   # def update(self):
        #if self.score >= self.food_count * 3:
           ## self.level += 1
           # self.food_count += 1

class Score:
    def __init__(self):
        self.score = 0
        self.level = 1

    def increment_score(self):
        self.score += 1
        if self.score % 3 == 0:
            self.level += 1

    def display(self):
        font = pygame.font.SysFont(None, 25)
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        level_text = font.render(f"Level: {self.level}", True, WHITE)
        SCREEN.blit(score_text, (10, 10))
        SCREEN.blit(level_text, (WIDTH - level_text.get_width() - 10, 10))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Food:
    def __init__(self, x=None, y=None):
        self.location = Point(x, y)

    @property
    def x(self):
        return self.location.x

    @property
    def y(self):
        return self.location.y

    def generate(self, snake):
        while True:
            x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
            y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
            if (x, y) not in [(p.x, p.y) for p in snake.points] and (x, y) != (self.x, self.y):
                self.location.x = x
                self.location.y = y
            break
        
    def update(self):
        pygame.draw.rect(
        SCREEN,
        YELLOW,
        pygame.Rect(
        self.location.x * BLOCK_SIZE,
        self.location.y * BLOCK_SIZE,
        BLOCK_SIZE,
        BLOCK_SIZE,
        )
    )   

class Snake:
    def __init__(self):
        self.points = [
            Point(WIDTH // BLOCK_SIZE // 2, HEIGHT // BLOCK_SIZE // 2),
            Point(WIDTH // BLOCK_SIZE // 2 + 1, HEIGHT // BLOCK_SIZE // 2),
        ]
        
    def update(self):
        head = self.points[0]

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
        for body in self.points[1:]:
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
        snake = Snake()
        score = Score()
        for idx in range(len(self.points) - 1, 0, -1):
            self.points[idx].x = self.points[idx - 1].x
            self.points[idx].y = self.points[idx - 1].y

        self.points[0].x += dx
        self.points[0].y += dy

        head = self.points[0]
        if head.x > WIDTH // BLOCK_SIZE:
            head.x = 0
        elif head.x < 0:
            head.x = WIDTH // BLOCK_SIZE - 1
        elif head.y > HEIGHT // BLOCK_SIZE:
            head.y = 0
        elif head.y < 0:
            head.y = HEIGHT // BLOCK_SIZE - 1
        head = snake.points[0]
        if head.x < 0 or head.x >= WIDTH // BLOCK_SIZE or head.y < 0 or head.y >= HEIGHT // BLOCK_SIZE:
            print(f"Game over! Score: {score}")
        running = False
    def check_collision(self, food):
        if self.points[0].x != food.x:
            return False
        if self.points[0].y != food.y:
            return False
        return True



score = Score()
#level = Level()
score_text = (f"Score: {score}")
#level_text = (f"Level: {level}")


def main():
    running = True
    snake = Snake()
    food = Food(5, 5)
    dx, dy = 0, 0
    food_eaten = 0
    score = Score()
    #level = Level()

    while running:
        SCREEN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    dx, dy = 0, -1
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, +1
                elif event.key == pygame.K_LEFT:
                    dx, dy = -1, 0
                elif event.key == pygame.K_RIGHT:
                    dx, dy = +1, 0

        snake.move(dx, dy)
        if snake.check_collision(food):
            snake.points.append(Point(food.x, food.y))
            #score += level.get_score_for_food(level.food_count)
            #level.food_count += 1
            food_eaten += 1
            if food_eaten >= 3:
              #  level += 1
                food_eaten = 0
                clock.tick(5)
            food.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
            food.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
           # score += 10
            #if len(snake.points) % 3 == 0:
                #level.increase_level()
                #clock.tick(level.speed)

        food.update()
        snake.update()
        score.display()
        
        pygame.display.flip()
        clock.tick(5 + score.level)


if __name__ == '__main__':
    main()

