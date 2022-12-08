import pygame
import random


class Car(pygame.sprite.Sprite):

    def __init__(self, image, coords, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(*group)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = coords[0]
        self.rect.y = coords[1]
        self.flag = True

    def animate_car(self):
        if self.rect.x <= 500 and self.flag:
            self.rect.x += 10
        else:
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect.x -= 10
            self.flag = False


    def update(self, *args):
        self.animate_car()

