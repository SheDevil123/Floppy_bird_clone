
import pygame
from sys import exit

pygame.init()
screen=pygame.display.set_mode((800,400))
screen.fill((0,100,200))
clock=pygame.time.Clock()

bg=pygame.Surface((800,400))
bg.fill((200,190,230))

floor=pygame.Surface((800,50))
floor_rect=floor.get_rect(topleft=(0,350))

bird1=pygame.Surface((70,70))
bird2=pygame.Surface((70,70))
pygame.Surface.fill(bird1,(0,100,0))
pygame.Surface.fill(bird2,(0,0,100))
bird=[bird1,bird2]
bird_rect=bird1.get_rect(center=(100,200))

gravity,bird_type=0,bird[0]

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                print(1)
                gravity=-20

    screen.blit(bg,(0,0))
    screen.blit(floor,floor_rect)
    if gravity>0:bird_type=bird[1]
    else:bird_type=bird[0]
    screen.blit(bird_type,bird_rect)
    gravity+=1
    bird_rect.y+=gravity
    if bird_rect.bottom>350:bird_rect.bottom=350
    pygame.display.update()
    clock.tick(60)