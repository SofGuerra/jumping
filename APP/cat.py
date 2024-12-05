import sys
import pygame
import pymunk


class Cat:

    def __init__(self, space: pymunk.Space, center, size, image_filename):
        self.size = [size[0], size[1]]
        self.body = pymunk.Body()
        self.box_shape = pymunk.Poly.create_box(self.body, size)
        self.box_shape.mass = 4
        self.body.position = center
        self.space = space
        self.space.add(self.body, self.box_shape)

        self.image = pygame.image.load(image_filename)

        self.resized_image = None
        self.resized_image_flip_x = None
        self.last_image_resized_size = None

        self.control_jump = False
        self.control_horizontal = 0

        self.last_used_direction = 1

    def draw(self, screen, transform_physics_to_graphics):
        rect = [self.body.position[0] - self.size[0] / 2, self.body.position[1] - self.size[1] / 2, self.size[0], self.size[1]]
        screen_rect = list(transform_physics_to_graphics(rect))
        screen_size = screen_rect[2], screen_rect[3]
        if screen_size != self.last_image_resized_size:
            self.resized_image = pygame.transform.scale(self.image, screen_size)
            self.last_image_resized_size = screen_size
            self.resized_image_flip_x = pygame.transform.flip(self.resized_image, True, False)

        direction = self.body.velocity[0]
        if direction == 0:
            direction = self.last_used_direction
        if direction < 0:
            screen.blit(self.resized_image, screen_rect)
        else:
            screen.blit(self.resized_image_flip_x, screen_rect)
        self.last_used_direction = direction

