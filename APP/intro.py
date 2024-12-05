import pygame
import level1 as Level1
from APP.scene import Scene
import scene_manager
from button import Button



class Intro(Scene):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        pygame.mixer.music.load('IMG/intro.mp3')
        pygame.mixer.music.play(-1)
        # Does not do anything on callback
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.screen = screen
        self.font = pygame.font.Font("FONTS/PressStart2P.ttf", 24)
        self.phrases = [
            "Hey, wake up!",
            "Are you okay?",
            "You fell, \ndon't you remember?",
            "At least you are a cat,\nso you have another\n six lives!",
            "Next time, try \nto land on your feet...",
        ]
        self.current_phrase_index = 0
        self.text = self.phrases[self.current_phrase_index]
        self.display_text = ""
        self.char_index = 0
        self.last_update = 0
        self.update_speed = 100
        self.screen.fill(self.BLACK)

        self.skip = Button("IMG\\skip.png", lambda: None)
        self.skip.set_size((64, 64))
        self.skip.pos = (20, screen.get_height() - 20 - 64)

    def start(self):
        self.shown = True
        self.last_update = pygame.time.get_ticks()
        pygame.mixer.music.load('IMG/intro.mp3')
        pygame.mixer.music.play(-1)


    def draw(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update > self.update_speed:
            if self.char_index < len(self.text):
                self.display_text += self.text[self.char_index]
                self.char_index += 1
                self.last_update = current_time
            elif self.char_index == len(self.text):
                self.last_update = current_time + 300
                self.char_index += 1
            elif current_time - self.last_update > 500:
                self._next_phrase()

        self.screen.fill(self.BLACK)
        lines = self.display_text.split("\n")
        y_offset = self.screen.get_height() // 2 - (len(lines) * 20)
        for line in lines:
            text_surface = self.font.render(line, True, self.WHITE)
            text_rect = text_surface.get_rect(center=(self.screen.get_width() // 2, y_offset))
            self.screen.blit(text_surface, text_rect)
            y_offset += 40
        self.skip.draw(self.screen)

        if current_time - self.last_update > 3000:
            self.start_level_one()


    def _next_phrase(self):
        self.current_phrase_index += 1
        if self.current_phrase_index < len(self.phrases):
            self.text = self.phrases[self.current_phrase_index]
            self.display_text = ""
            self.char_index = 0
            self.last_update = pygame.time.get_ticks()
        else:
            self.finished = True

    def start_level_one(self):
        self.shown = False
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        scene_manager.all_scenes["level1"].start()

    def on_mouse_press (self, event):
        if self.skip.contains_point(pygame.mouse.get_pos()):
            self.start_level_one()

    def on_mouse_move (self, event):
        if self.skip.contains_point(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)





