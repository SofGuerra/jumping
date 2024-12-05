import time
import pygame
import pymunk
from pygame.transform import scale
import scene_manager

from APP.getscoress import ScoresTables
from APP.goal import Goal
from APP.scene import Scene
from APP.static_block import StaticBlock
from cat import Cat

class Level1(Scene) :
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        self.bg = pygame.image.load("IMG/level1.jpg")
        self.bg = pygame.transform.scale(self.bg, (screen.get_width(), screen.get_height()))
        self.space = pymunk.Space()
        self.space.gravity = [0, -9.8]
        self.start_time = -1


        self.map_width = 3

        self.blocks = [
            StaticBlock(self.space, (0.5, 0), (0.7, 0.15), "IMG\\20241205_083546.png", 8),
            StaticBlock(self.space, (2.0, 0), (0.7, 0.15), "IMG\\20241205_083546.png", 8),
            StaticBlock(self.space, (-1, 0), (2, 100), None, 1),
            StaticBlock(self.space, (self.map_width + 1, 0), (2, 100), None, 1),
        ]

        self.cat = Cat(self.space, (0.2, 3), (0.3, 0.3), "IMG\\cat.png")

        self.goal = Goal((2, 0.2), (0.2, 0.3))

        self.clock = time.perf_counter()

    def physics_to_graphics(self, x, y, w, h):
        scale_ratio = self.screen.get_width() / self.map_width
        height =  int(h * scale_ratio)
        return int(x * scale_ratio), int(self.screen.get_height() -y * scale_ratio - height), int(w * scale_ratio), height

    def physics_to_graphics_1(self, rect):
        return self.physics_to_graphics(rect[0], rect[1], rect[2], rect[3])

    def is_cat_dead(self):
        return self.cat.body.velocity[1] < -15

    def draw(self):

        now = time.perf_counter()
        delta_time = now - self.clock
        if delta_time > 0.05:
            delta_time = 0.05
        self.clock = now
        self.space.step(delta_time / 4)
        self.space.step(delta_time / 4)
        self.space.step(delta_time / 4)
        self.space.step(delta_time / 4)

        self.screen.blit(self.bg, (0,0))
        for block in self.blocks:
            block.draw(self.screen, self.physics_to_graphics_1 )
        self.cat.draw(self.screen, self.physics_to_graphics_1)

        self.goal.draw(self.screen, self.physics_to_graphics_1)
        if self.goal.intersect([self.cat.body.position[0] - self.cat.size[0] / 2, self.cat.body.position[1] - self.cat.size[1] / 2, self.cat.size[0], self.cat.size[1]]):
           self.set_win()

        self.handle_controls()
        if self.is_cat_dead():
            self.start()

    def handle_controls(self):
        if self.cat.control_jump:
            if self.is_cat_grounded():
                self.cat.body.velocity = [self.cat.body.velocity[0], 4]
            self.cat.control_jump = False
        speed = 1
        self.cat.body.velocity = [speed * self.cat.control_horizontal, self.cat.body.velocity[1]]

    def set_win(self):
        self.shown = False
        now = time.perf_counter()
        db = ScoresTables()
        db.add_score(now - self.start_time, 1)
        db.close()
        scene_manager.all_scenes["menu"].shown =True



    def start(self):
        self.shown = True
        pygame.mixer.music.load('IMG/level1.mp3')
        pygame.mixer.music.play(-1)
        self.start_time = time.perf_counter()
        self.cat.body.position = (0.2, 0.4)
        self.cat.body.velocity = [0, 0]

    def is_cat_grounded(self):
        return abs(self.cat.body.velocity[1]) < 0.01


    def on_key_pressed(self, event):
        if event.key == pygame.K_w:
            self.cat.control_jump = True
        if event.key == pygame.K_a:
            self.cat.control_horizontal -= 1
        if event.key == pygame.K_d:
            self.cat.control_horizontal += 1

    def on_key_released(self, event):
        if event.key == pygame.K_a:
            self.cat.control_horizontal += 1
        if event.key == pygame.K_d:
            self.cat.control_horizontal -= 1