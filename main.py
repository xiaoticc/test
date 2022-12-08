import os
import sys
import pygame
from car import Car


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def game(screen):
    # создадим группу, содержащую все спрайты
    all_sprites = pygame.sprite.Group()
    image = load_image("img.png", -1)
    Car(image, (10, 10), all_sprites)
    FPS = 60
    tick = 0
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        all_sprites.draw(screen)
        all_sprites.update()
        tick += 1
        clock.tick(FPS)
        pygame.display.flip()


# Изображение не получится загрузить
# без предварительной инициализации pygame
pygame.init()
size = width, height = 600, 95
screen = pygame.display.set_mode(size)
game(screen)
