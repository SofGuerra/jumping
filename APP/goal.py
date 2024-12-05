import pygame.image


class Goal:
    def __init__(self, physical_pos, physical_size):
        self.pos = physical_pos
        self.size = physical_size
        self.image = pygame.image.load("IMG\\flag.png")
        self.resized_image = None
        self.last_image_resized_size = None

    def draw(self, screen, transform_physics_to_graphics):
        rect = [self.pos[0], self.pos[1], self.size[0], self.size[1]]
        screen_rect = list(transform_physics_to_graphics(rect))
        screen_size = screen_rect[2], screen_rect[3]
        if screen_size != self.last_image_resized_size:
            self.resized_image = pygame.transform.scale(self.image, screen_size)
            self.last_image_resized_size = screen_size
        screen.blit(self.resized_image, screen_rect)

    def intersect(self, rect):
        goal_left = self.pos[0]
        goal_top = self.pos[1]
        goal_right = goal_left + self.size[0]
        goal_bottom = goal_top + self.size[1]

        rect_left = rect[0]
        rect_top = rect[1]
        rect_right = rect_left + rect[2]
        rect_bottom = rect_top + rect[3]

        return (rect_left < goal_right and
                rect_right > goal_left and
                rect_top < goal_bottom and
                rect_bottom > goal_top)