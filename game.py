from random import randint
import pygame
from sys import exit

def spawn_pipe():
    global pipes
    i=len(pipes)
    y=randint(25,275)
    top_rect=pipe_top.get_rect(bottomleft=(800,y))
    bottom_rect=pipe_bottom.get_rect(topleft=(800,y+100))
    pipes.append([top_rect,bottom_rect,True])

def move_pipes():
    global pipes
    for i in pipes:
        i[0].x-=1
        i[1].x-=1
        screen.blit(pipe_top,i[0])
        screen.blit(pipe_bottom,i[1])
        if i[0].x<-50:
            pipes.remove(i)
def counting_score():
    global pipes,score
    for i in pipes:
        if i[2] and i[0].right<70:
            score+=1
            i[2]=False

pygame.init()
screen=pygame.display.set_mode((800,400))
screen.fill((0,100,200))
clock=pygame.time.Clock()

bg=pygame.Surface((800,400)).convert()
bg.fill((200,190,230))

blur_sur=pygame.Surface((800,400)).convert()
pygame.Surface.fill(blur_sur,(0,0,0))
blur_sur.set_alpha(200)


floor=pygame.Surface((800,30))
floor.fill((200,50,0))
floor_rect=floor.get_rect(topleft=(0,370))

pipe_top=pygame.Surface((40,400)).convert()
pipe_bottom=pygame.Surface((40,400)).convert()
pipe_top.fill((0,0,200))
pipe_bottom.fill((0,0,200))
pipes=[[pipe_top.get_rect(topleft=(400,-250)),pipe_bottom.get_rect(topleft=(400,250)),True],[pipe_top.get_rect(topleft=(700,-250)),pipe_bottom.get_rect(topleft=(700,250)),True]]

pipe_event=pygame.USEREVENT+1
pygame.time.set_timer(pipe_event,4000)

bird1=pygame.transform.rotozoom(pygame.image.load("assets\\birb1.png").convert_alpha(),0,0.75)
bird2=pygame.transform.rotozoom(pygame.image.load("assets\\birb2.png").convert_alpha(),0,0.75)
bird=[bird1,bird2]
bird_rect=bird1.get_rect(center=(100,200))

text=pygame.font.Font(None,40)
score=0

gravity,bird_type,angle=0,bird[0],0

game_active,menu,game_over=True,True,False

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    gravity=-3
            if event.type==pipe_event:
                spawn_pipe()
    
    if game_active:
        score_text=text.render(f'{score}',None,(0,0,0))
        score_text_rect=score_text.get_rect(midbottom=(400,80))
        screen.blit(bg,(0,0))
        screen.blit(floor,floor_rect)
        move_pipes()
        if gravity>0:bird_type=bird[1]
        else:bird_type=bird[0]
        # if gravity<0:
        #     if angle<30:angle+=2
        #     bird_type=pygame.transform.rotate(bird_type,angle)
        # else:
        #     if angle>-30:angle-=2
        #     bird_type=pygame.transform.rotate(bird_type,angle)
        screen.blit(bird_type,bird_rect)
        gravity+=0.25
        bird_rect.y+=gravity
        if bird_rect.bottom>370:bird_rect.bottom=370
        for i in pipes:
            if bird_rect.colliderect(i[0]) or bird_rect.colliderect(i[1]):
                game_active=False
                game_over=True
                pipes=[[pipe_top.get_rect(topleft=(400,-250)),pipe_bottom.get_rect(topleft=(400,250)),True],[pipe_top.get_rect(topleft=(700,-250)),pipe_bottom.get_rect(topleft=(700,250)),True]]
                bird_rect.center=(100,200)
                pygame.time.set_timer(pipe_event,0)
        # screen.blit(blur_sur,(0,0)) 
        counting_score()
        screen.blit(score_text,score_text_rect)
    if game_over:
        screen.blit(bg,(0,0))
        temp=text.render(f'YOUR SCORE IS : {score}',None,(0,0,0))
        temp_rect=temp.get_rect(midtop=(400,100))
        screen.blit(temp,temp_rect)
        text=pygame.font.Font(None,70)
        temp=text.render(f'press ENTER to try again!!',None,(100,200,10))
        temp_rect=temp.get_rect(midbottom=(400,350))
        screen.blit(temp,temp_rect)
        key=pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            game_active=True
            game_over=False
            score=0
            pygame.time.set_timer(pipe_event,4000)
        
    pygame.display.update()
    clock.tick(60)