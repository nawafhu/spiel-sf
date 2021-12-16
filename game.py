import sys

import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = player_surf= pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(80, 300))


pygame.init() #Startet alle Hintergrundprozesse  
screen = pygame.display.set_mode((800,400)) 
pygame.display.set_caption("Mein BABA-Spiel")
clock = pygame.time.Clock()

simple_surface = pygame.Surface((200, 100))
simple_surface.fill("blue")
sky_surf = pygame.image.load("graphics/Sky.png").convert()
ground_surf = pygame.image.load("graphics/ground.png").convert()

player = pygame.sprite.GroupSingle()
player.add(Player())

player_surf = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))

while True: #Endlosschleife
    #eventloop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #beendet alle pygame Prozesse
            sys.exit()

        #screen.blit(simple_surface. (200, 150))
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300))

        player.draw(screen)

    pygame.display.update()
    clock.tick(60) #max. Frm 60 fps