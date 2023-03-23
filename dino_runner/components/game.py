import pygame

from dino_runner.utils.constants import *
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.cloud import Cloud
from dino_runner.utils.music import music, sound
from dino_runner.components.button import Button
from dino_runner.components.powerups.power_up_manager import PowerUpManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.cloud = Cloud()

        self.playing = False
        self.running = False
        self.game_paused = False
        self.menu_state = MAIN_STATE

        self.score_accumulator = 0
        self.score = 0
        self.death_count = 0
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380        

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def reset_score(self):
        self.game_speed = 20
        self.score = 0

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.reset_score()
        music()
        while self.playing:
            self.events()
            self.update()
            self.draw()
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_paused = True
                    self.my_menu()

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.cloud.update(self)
        self.update_score()
        self.power_up_manager.update(self.score, self.game_speed, self.player)

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 5
            sound(SCORE_SOUND)

        if self.score >= self.score_accumulator:
            self.score_accumulator = self.score

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((WHITE_COLOR))
        self.draw_background()
        self.player.draw(self.screen)
        self.cloud.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_message(f"SCORE {self.score}",
                          21,  1000,  50, (BLACK_COLOR))
        self.draw_message("Press ESC to pause", 18, self.half_screen_width -
                          390, self.half_screen_height+270, (BLACK_COLOR))
        self.draw_power_up_time()
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round(
                (self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                self.draw_message(
                    f"{self.player.type.capitalize()} enabled for {time_to_show} seconds",
                    20,
                    SCREEN_WIDTH // 2,
                    (SCREEN_HEIGHT // 2) - 150,
                    (BLACK_COLOR))
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.run()
            elif event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def my_buttons(self):
        self.resume_button = Button(419, 125, BUTTONS[5], 1)
        self.options_button = Button(408, 250, BUTTONS[3], 1)
        self.quit_button = Button(447, 375, BUTTONS[4], 1)
        self.video_button = Button(311, 75, BUTTONS[6], 1)
        self.audio_button = Button(310, 200, BUTTONS[0], 1)
        self.keys_button = Button(338, 325, BUTTONS[2], 1)
        self.back_button = Button(417, 450, BUTTONS[1], 1)

    def my_menu(self):
        background_copy = self.screen.copy()
        self.my_buttons()
        while self.game_paused:
            if self.menu_state == MAIN_STATE:
                if self.resume_button.draw(self.screen):
                    self.game_paused = False
                elif self.options_button.draw(self.screen):
                    self.menu_state = OPT_STATE
                elif self.quit_button.draw(self.screen):
                    self.playing = False
                    pygame.mixer.music.pause()
                self.handle_events_on_menu()
                pygame.display.update()
            elif self.menu_state == OPT_STATE:
                self.screen.blit(background_copy, (0, 0))
                if self.video_button.draw(self.screen):
                    print("Under Development..")
                elif self.audio_button.draw(self.screen):
                    print("Under Development..")
                elif self.keys_button.draw(self.screen):
                    print("Under Development..")
                elif self.back_button.draw(self.screen):
                    self.screen.blit(background_copy, (0, 0))
                    self.menu_state = MAIN_STATE
                self.handle_events_on_menu()
                pygame.display.update()

    def draw_message(self, text, font_size, width, height, color):
        font = pygame.font.Font(FONT_STYLE, font_size)
        text = font.render(text, True, color)
        text_rect = text.get_rect()
        text_rect.center = (width, height)
        self.screen.blit(text, text_rect)

    def show_home_screen(self):
        self.draw_message("RUUUUelcome to the Dino Runner", 35,
                          self.half_screen_width, self.half_screen_height-98, (BLACK_COLOR))
        self.draw_message("Press any key to start", 25,
                          self.half_screen_width, self.half_screen_height-28, (BLACK_COLOR))
        self.draw_message("Developed by Daniel Rody", 15,
                          self.half_screen_width+380, self.half_screen_height+280, (GRAY_COLOR))

    def show_end_screen(self):
        self.draw_message("Press any key to start", 20, self.half_screen_width +
                          20, self.half_screen_height+60, (GRAY_COLOR))
        self.draw_message(f"YOUR SCORE {self.score}", 18,
                          self.half_screen_width+390, self.half_screen_height-90, (GRAY_COLOR))
        self.draw_message(f"HIGHER SCORE {self.score_accumulator}", 22,
                          self.half_screen_width+390, self.half_screen_height-65, (BLACK_COLOR))
        self.draw_message(f"NUMBER OF DEATHS {self.death_count}", 18,
                          self.half_screen_width+385, self.half_screen_height-40, (BLACK_COLOR))
        self.screen.blit(GAME_OVER, (self.half_screen_width - 150, self.half_screen_height - 255))
        self.screen.blit(DEAD, (self.half_screen_width - 25, self.half_screen_height - 60))

    def show_menu(self):
        self.screen.fill((WHITE_COLOR))
        self.half_screen_height = SCREEN_HEIGHT // 2
        self.half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            self.show_home_screen()
        else:
            self.show_end_screen()

        pygame.display.flip()
        self.handle_events_on_menu()
