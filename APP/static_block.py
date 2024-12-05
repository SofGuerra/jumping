import pygame
import pymunk


class StaticBlock:

    def __init__(self, space: pymunk.Space, center, size, image_filename, texture_vertical_scaling=1):
        self.size = [size[0], size[1]]
        self.body = pymunk.Body()
        self.box_shape = pymunk.Poly.create_box(self.body, size)
        self.box_shape.mass = 100
        self.body.body_type = pymunk.Body.STATIC
        self.body.position = center
        self.space = space
        self.space.add(self.body, self.box_shape)
        self.texture_vertical_scaling = texture_vertical_scaling

        if image_filename is None:
            self.image = None
            self.resized_image = None
        else:
            self.image = pygame.image.load(image_filename)

        self.resized_image = None
        self.last_image_resized_size = None

    def draw(self, screen: pygame.Surface, transform_physics_to_graphics):
        rect = [self.body.position[0] - self.size[0] / 2, self.body.position[1] - self.size[1] / 2, self.size[0], self.size[1]]
        screen_rect = list(transform_physics_to_graphics(rect))
        screen_rect[1] = int(screen_rect[1] - screen_rect[3] * (self.texture_vertical_scaling - 1))
        screen_rect[3] = int(screen_rect[3] * self.texture_vertical_scaling)

        if self.image is None:
            pygame.draw.rect(screen, (255, 255, 255), screen_rect)
        else:
            screen_size = screen_rect[2], screen_rect[3]
            if screen_size != self.last_image_resized_size:
                self.resized_image = pygame.transform.scale(self.image, screen_size)
                self.last_image_resized_size = screen_size
            screen.blit(self.resized_image, screen_rect)
