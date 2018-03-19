#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 20:48:19 2018

@author: markus
"""
Basti= "lel"
import pygame


black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (34,139,34)
bright_red = (255,0,0)
bright_green = (0,255,0)

display_width = 800
display_height = 600

clock = pygame.time.Clock()




def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def ez_quit():
    quit()
    
def ez_intro_quit():
    pass

def game_intro(screen):

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.fill(white)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        screen.blit(TextSurf, TextRect)
        
        intro = button(screen,"Quit",550,450,100,50,red,bright_red,pygame.quit)
        intro = button(screen,"GO!",150,450,100,50,green,bright_green,action = ez_intro_quit)
        

        pygame.display.update()
        clock.tick(15)

def button(screen,msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()  
            return False
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))
        

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)
    return True
