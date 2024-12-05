import pygame

class Level2 :
    def __init__(self, screen : pygame.surface):
        self.screen = screen
        pygame.mixer.music.load('IMG/level2.mp3')
        pygame.mixer.music.play(-1)
        self.level1 = pygame.image.load("IMG/level2.jpg")



        self.level1 = pygame.transform.scale(self.level1, (screen.get_width(), screen.get_height()))


    def draw(self):

        self.screen.blit(self.level1, (0,0))