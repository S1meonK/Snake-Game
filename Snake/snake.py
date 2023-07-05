import pygame, sys, time, random

# windows sizes
frame_size_x = 1380
frame_size_y = 840

# colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# one snake square size
square_size = 60

class Game:
    def __init__(self, speed):
        self.speed = speed
        check_errors = pygame.init()

        if check_errors[1] > 0:
            print(f"Error {check_errors[1]}")


        # initialise game window
        pygame.display.set_caption("Snake Game")
        self.game_window = pygame.display.set_mode((frame_size_x, frame_size_y))
        self.fps_controller = pygame.time.Clock()
        self.init_vars()

    def init_vars(self):
        self.direction = "RIGHT"
        self.head_pos = [120, 60]
        self.snake_body = [[120, 60]]
        self.food_pos = [random.randrange(1, (frame_size_x // square_size)) * square_size,
                         random.randrange(1, (frame_size_y // square_size)) * square_size]
        self.food_spawn = True
        self.score = 0

    def show_score(self, choice, color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render("Score: " + str(self.score), True, color)
        score_rect = score_surface.get_rect()
        if choice == 1:
            score_rect.midtop = (frame_size_x / 10, 15)
        else:
            score_rect.midtop = (frame_size_x / 2, frame_size_y / 1.25)
        self.game_window.blit(score_surface, score_rect)

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_UP or event.key == ord("w")) and self.direction != "DOWN":
                        self.direction = "UP"
                    elif (event.key == pygame.K_DOWN or event.key == ord("s")) and self.direction != "UP":
                        self.direction = "DOWN"
                    elif (event.key == pygame.K_LEFT or event.key == ord("a")) and self.direction != "RIGHT":
                        self.direction = "LEFT"
                    elif (event.key == pygame.K_RIGHT or event.key == ord("d")) and self.direction != "LEFT":
                        self.direction = "RIGHT"

            if self.direction == "UP":
                self.head_pos[1] -= square_size
            elif self.direction == "DOWN":
                self.head_pos[1] += square_size
            elif self.direction == "LEFT":
                self.head_pos[0] -= square_size
            else:
                self.head_pos[0] += square_size

            if self.head_pos[0] < 0:
                self.head_pos[0] = frame_size_x - square_size
            elif self.head_pos[0] > frame_size_x - square_size:
                self.head_pos[0] = 0
            elif self.head_pos[1] < 0:
                self.head_pos[1] = frame_size_y - square_size
            elif self.head_pos[1] > frame_size_y - square_size:
                self.head_pos[1] = 0

            self.snake_body.insert(0, list(self.head_pos))
            if self.head_pos[0] == self.food_pos[0] and self.head_pos[1] == self.food_pos[1]:
                self.score += 1
                self.food_spawn = False
            else:
                self.snake_body.pop()

            if not self.food_spawn:
                self.food_pos = [random.randrange(1, (frame_size_x // square_size)) * square_size,
                                 random.randrange(1, (frame_size_y // square_size)) * square_size]
                self.food_spawn = True

            self.game_window.fill(black)
            for pos in self.snake_body:
                pygame.draw.rect(self.game_window, green, pygame.Rect(
                    pos[0] + 2, pos[1] + 2,
                    square_size - 2, square_size - 2))

            pygame.draw.rect(self.game_window, red, pygame.Rect(self.food_pos[0],
                                                                self.food_pos[1], square_size, square_size))

            for block in self.snake_body[1:]:
                if self.head_pos[0] == block[0] and self.head_pos[1] == block[1]:
                    self.init_vars()

            self.show_score(1, white, 'consolas', 20)
            pygame.display.update()
            self.fps_controller.tick(self.speed)


if __name__ == "__main__":
    game = Game(10)
    game.play()
