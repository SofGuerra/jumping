import pygame

import scene_manager
from APP.button import Button
from APP.getscoress import ScoresTables
from APP.scene import Scene


class Scores(Scene):
    def __init__(self, screen: pygame.surface):

        super().__init__(screen)
        self.screen = screen
        self.bg = pygame.image.load("IMG/scores.jpg")
        self.bg = pygame.transform.scale(self.bg, (screen.get_width(), screen.get_height()))

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.font = pygame.font.Font("FONTS/PressStart2P.ttf", 24)
        self.back = Button("IMG\\skip.png", lambda: None)
        self.back.set_size((64, 64))
        self.back.pos = (20, screen.get_height() - 20 - 64)

        self.fetched_data = []

    def draw(self):
        self.screen.fill(self.BLACK)
        lines = []
        for id_, time, level in self.fetched_data:
            lines.append(f"Time: {round(time, 1)}".ljust(12) + f" Level: {level}".ljust(10))
        y_offset = self.screen.get_height() // 2 - (len(lines) * 20)
        for line in lines:
            text_surface = self.font.render(line, True, self.WHITE)
            text_rect = text_surface.get_rect(center=(self.screen.get_width() // 2, y_offset))
            self.screen.blit(text_surface, text_rect)
            y_offset += 40

        self.back.draw(self.screen)


    def start(self):
        self.shown = True
        db = ScoresTables()
        self.fetched_data = db.fetch_scores()
        db.close()


    def on_mouse_press (self, event):
        if self.back.contains_point(pygame.mouse.get_pos()):
            self.shown = False
            scene_manager.all_scenes["menu"].shown = True

    def on_mouse_move (self, event):
        if self.back.contains_point(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
