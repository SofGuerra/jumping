from datetime import datetime, timedelta
import pygame
from APP.button import Button
from APP.scene import Scene
import scene_manager
from intro import Intro
from scores import Scores

# first page of the game
class Menu(Scene):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        self.daybg = pygame.image.load("IMG/daybg.jpg")
        self.nightbg = pygame.image.load("IMG/nightbg.jpg")
        self.jumping1 = pygame.image.load("IMG/jumping1.png")
        pygame.mixer.music.load('IMG/menu.mp3')
        pygame.mixer.music.play(-1)
        self.cat1 = pygame.image.load("IMG/cat1.png")

        self.jumping1 = pygame.transform.scale(self.jumping1, (400, 100))
        self.daybg = pygame.transform.scale(self.daybg, (screen.get_width(), screen.get_height()))
        self.nightbg = pygame.transform.scale(self.nightbg, (screen.get_width(), screen.get_height()))

        self.buttons = []
        self.init_buttons()

    def init_buttons(self):
        padding = 20
        y = 500
        x = self.screen.get_width() // 2


        # First button: "start"
        start_button = Button("IMG/start.png", self.close_self_open_intro)
        start_button.set_center((x, y))
        start_button.set_size_keep_center((150, 70))
        self.buttons.append(start_button)
        y += start_button.get_size()[1] + padding

        # Second button: "scores"
        scores_button = Button("IMG/scores.png", self.close_self_open_scores)
        scores_button.set_center((x, y))
        scores_button.set_size_keep_center((150, 70))
        self.buttons.append(scores_button)
        y += scores_button.get_size()[1] + padding

        # Third button: "exit"
        exit_button = Button("IMG/exit.png", quit)
        exit_button.set_center((x, y))
        exit_button.set_size_keep_center((150, 70))
        self.buttons.append(exit_button)
        y += exit_button.get_size()[1] + padding

    def draw(self):

        current_time = datetime.now()
        #current_time = datetime.now() + timedelta(hours=12)
        if 6 <= current_time.hour <= 18:
            self.screen.blit(self.daybg, (0,0))
        else:
            self.screen.blit(self.nightbg, (0,0))
        self.screen.blit(self.jumping1, (self.screen.get_width() // 2 - self.jumping1.get_width() // 2, self.screen.get_height() // 4 - self.jumping1.get_height()))
        for button in self.buttons:
            button.draw(self.screen)

        self.screen.blit(self.cat1, (self.screen.get_width()//2 - self.cat1.get_width()//2, self.screen.get_height()//2 - self.cat1.get_height()))

    def on_mouse_move(self, event):

         for button in self.buttons:
             if button.contains_point(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                break
             else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)



    def on_mouse_press (self, event):

        for button in self.buttons:
            if button.contains_point(pygame.mouse.get_pos()):
                button.onpress()
                break
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def close_self_open_intro(self):
        self.shown = False
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        scene_manager.all_scenes["intro"].start()

    def close_self_open_scores(self):
        self.shown = False
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        scene_manager.all_scenes["scores"].start()


