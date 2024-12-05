import pygame


class Scene:
    def __init__(self, screen):
        self.shown = False
        self.screen = screen

    def draw(self):
        pass

    def on_mouse_move(self, event):
        pass

    def on_mouse_press(self, event):
        pass

    def on_key_pressed(self, event):
        pass

    def on_key_released(self, event):
        pass
