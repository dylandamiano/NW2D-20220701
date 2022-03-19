import pygame

active_spills = []

class oil(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('Graphics/ship_oil.png')

        self.image.set_alpha(50)
        # self.color = self.image.set
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


def create_spill(character):
    temp_obj = oil(character.ship.v2Pos.x, character.ship.v2Pos.y)
    active_spills.append(temp_obj)

def draw_spills(surface):
    for spill in active_spills:
        surface.blit(spill.image, spill.rect)