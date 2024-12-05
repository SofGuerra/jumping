import pygame
from menu import Menu
from level1 import Level1
from scores import Scores
from intro import Intro
import scene_manager

pygame.init()
pygame.mixer.init()


screen_width = 550
screen_height = 770
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("JUMPING")
icon = pygame.image.load("IMG/kevinp.jpg")
pygame.display.set_icon(icon)

def load_scenes():
    scene_manager.all_scenes["level1"] = Level1(screen)
    scene_manager.all_scenes["intro"] = Intro(screen)
    scene_manager.all_scenes["scores"] = Scores(screen)
    scene_manager.all_scenes["menu"] = Menu(screen)

load_scenes()

scene_manager.all_scenes["menu"].shown = True
while True:
    for event in pygame.event.get():

        for scene in scene_manager.all_scenes.values():
            if not scene.shown:
                continue
            if event.type == pygame.MOUSEMOTION:
                scene.on_mouse_move(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                scene.on_mouse_press(event)
            elif event.type == pygame.KEYDOWN:
                scene.on_key_pressed(event)
            elif event.type == pygame.KEYUP:
                scene.on_key_released(event)

        if event.type == pygame.QUIT:
            quit()

    for scene in scene_manager.all_scenes.values():
        if scene.shown:
            scene.draw()
    pygame.display.update()
