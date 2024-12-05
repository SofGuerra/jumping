import sys
import pygame
import pymunk


class Platform:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 255, 0), self.rect)

# Crear el jugador
player = cat()

# Crear algunas plataformas
platforms = [
    Platform(200, 400, 400, 20),
    Platform(100, 300, 200, 20),
    Platform(400, 200, 200, 20)
]

# Función para verificar colisiones
def check_collisions(player, platforms):
    for platform in platforms:
        if player.rect.colliderect(platform.rect):
            # Colisión detectada
            if player.rect.bottom > platform.rect.top and player.rect.top < platform.rect.top:
                player.rect.bottom = platform.rect.top  # Colisiona por encima
            elif player.rect.top < platform.rect.bottom and player.rect.bottom > platform.rect.bottom:
                player.rect.top = platform.rect.bottom  # Colisiona por debajo
            elif player.rect.right > platform.rect.left and player.rect.left < platform.rect.left:
                player.rect.right = platform.rect.left  # Colisiona por la izquierda
            elif player.rect.left < platform.rect.right and player.rect.right > platform.rect.right:
                player.rect.left = platform.rect.right  # Colisiona por la derecha
