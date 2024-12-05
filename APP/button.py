import pygame


class Button:
    def __init__(self, image_path, onpress):
        self.pos = (0, 0)
        self.image = pygame.image.load(image_path)
        self.image_scaled = self.image
        self.__size = self.image.get_size()

        self.onpress = onpress

    def get_size(self):
        return self.__size

    def set_size_keep_center(self, size):
        center = self.get_center()
        self.image_scaled = pygame.transform.scale(self.image, size)
        self.__size = size
        self.set_center(center)

    def set_size(self, size):
        self.__size = size
        self.image_scaled = pygame.transform.scale(self.image, size)


    def set_center(self, center):
        self.pos = (center[0] - self.__size[0] // 2, center[1] - self.__size[1] // 2)

    def get_center(self):
        return (self.pos[0] + self.__size[0] // 2, self.pos[1] + self.__size[1] // 2)


    def contains_point(self, pos):
        return \
        pos[0] >= self.pos[0] and \
        pos[1] >= self.pos[1] and \
        pos[0] <= self.pos[0] + self.__size[0] and \
        pos[1] <= self.pos[1] + self.__size[1]

    def draw(self, screen):
        screen.blit(self.image_scaled, self.pos)


