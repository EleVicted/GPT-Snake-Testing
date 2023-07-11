import pygame, random, time

class Game:
    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Initialize screen resolution
        self.screen_resolution = (800, 600)

        # Initialize screen
        self.screen = pygame.display.set_mode(self.screen_resolution)
        pygame.display.set_caption("Snake Game")

        # Initialize clock
        self.clock = pygame.time.Clock()

        # Initialize score and high score
        self.player_score = 0
        self.high_score = 0

        # Initialize player snake
        self.player_snake = []

        # Initialize game modes
        self.game_modes = {
            'arcade': 'Arcade Mode',
            'endless': 'Endless Mode'
        }

        # Initialize game state
        self.game_over = False
        self.game_mode = None

    def title_screen(self):
        # Initialize pygame font module
        pygame.font.init()

        # Display game title, options (Start, Endless, High Scores)
        # Handle events: quit, keypress to select option
        print("Title screen")
        font = pygame.font.Font(None, 36)
        title_text = font.render("Snake Game", True, (255, 255, 255))
        start_text = font.render("1. Start (Arcade Mode)", True, (255, 255, 255))
        endless_text = font.render("2. Endless Mode", True, (255, 255, 255))
        high_scores_text = font.render("3. High Scores", True, (255, 255, 255))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_1:
                        self.game_mode = 'arcade'
                        self.game_loop(time_limit=120)
                    elif event.key == pygame.K_2:
                        self.game_mode = 'endless'
                        self.game_loop()
                    elif event.key == pygame.K_3:
                        self.high_scores_screen()

            self.screen.fill((0, 0, 0))
            self.screen.blit(title_text, (self.screen_resolution[0] // 2 - title_text.get_width() // 2, 100))
            self.screen.blit(start_text, (self.screen_resolution[0] // 2 - start_text.get_width() // 2, 200))
            self.screen.blit(endless_text, (self.screen_resolution[0] // 2 - endless_text.get_width() // 2, 250))
            self.screen.blit(high_scores_text, (self.screen_resolution[0] // 2 - high_scores_text.get_width() // 2, 300))
            pygame.display.update()
            self.clock.tick(60)

    def high_scores_screen(self):
        # TODO: Implement high scores screen
        pass

    def game_loop(self, time_limit=None):
        # TODO: Implement game loop
        pass

    def spawn_food(self):
        # TODO: Implement food spawning logic
        pass

    def update_difficulty(self):
        # TODO: Implement difficulty update logic
        pass

    def reset_game(self):
        # TODO: Implement game reset logic
        pass

if __name__ == "__main__":
    game = Game()
    game.title_screen()
