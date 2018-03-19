#!/usr/bin/env python

import random, os.path

#import basic pygame modules
import pygame
from pygame.locals import *

from PIL import Image


#see if we can load more than standard BMP
if not pygame.image.get_extended():
    raise SystemExit("Sorry, extended image module required")

# food items dict
from food_items import *

#game constants
MAX_SHOTS      = 2      #most player bullets onscreen
ESSEN_ODDS     = 100    #chances a new alien appears
BOMB_ODDS      = 100    #chances a new bomb will drop
ESSEN_RELOAD   = 12     #frames between new aliens
SCREENRECT     = Rect(0, 0, 1200, 800)
SCORE          = 0
main_dir = os.path.split(os.path.abspath(__file__))[0]

def load_image(file):
    "loads an image, prepares it for play"
    file = os.path.join(main_dir, 'data', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface.convert()

def load_images(*files):
    imgs = []
    for file in files:
        imgs.append(load_image(file))
    return imgs


class dummysound:
    def play(self): pass

def load_sound(file):
    if not pygame.mixer: return dummysound()
    file = os.path.join(main_dir, 'data', file)
    try:
        sound = pygame.mixer.Sound(file)
        return sound
    except pygame.error:
        print ('Warning, unable to load, %s' % file)
    return dummysound()



# each type of game object gets an init and an
# update function. the update function is called
# once per frame, and it is when each object should
# change it's current position and state. the Player
# object actually gets a "move" function instead of
# update, since it is passed extra information about
# the keyboard


class Player(pygame.sprite.Sprite):
    speed = 15
    bounce = 24
    gun_offset = -11
    images = []
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=SCREENRECT.midbottom)
        self.reloading = 0
        self.origtop = self.rect.top
        self.facing = -1

    def move(self, direction):
        if direction: self.facing = direction
        self.rect.move_ip(direction*self.speed, 0)
        self.rect = self.rect.clamp(SCREENRECT)
        if direction < 0:
            self.image = self.images[0]
        elif direction > 0:
            self.image = self.images[1]
        self.rect.top = self.origtop - (self.rect.left//self.bounce%2)

    def gunpos(self):
        pos = self.facing*self.gun_offset + self.rect.centerx
        return pos, self.rect.top




class Essen(pygame.sprite.Sprite):
    animciycle = 12
    def __init__(self):
        identity = get_food_item()
        # image
        self.image = load_image(identity[-1])
        # speed (10 is normal)
        self.speed = identity[2]
        # type('gscheid', gemuese' or 'boost')
        self.type = identity[1]
        if self.type in 'gscheid':
            self.nutritional_value = identity[-2]
        # init
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.facing = self.speed

        self.rect = self.image.get_rect()
        self.facing = random.choice((-1,1)) * Alien.speed
        self.rect.right = random.randint(a = 1, b = SCREENRECT.right)
        self.frame = 0
        
    def update(self):
        self.rect.move_ip(0, 1)
        if not SCREENRECT.contains(self.rect):
            self.kill()

        self.frame = self.frame + 1

class Explosion(pygame.sprite.Sprite):
    defaultlife = 12
    animcycle = 3
    images = []
    def __init__(self, actor):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=actor.rect.center)
        self.life = self.defaultlife

    def update(self):
        self.life = self.life - 1
        self.image = self.images[self.life//self.animcycle%2]
        if self.life <= 0: self.kill()


class Shot(pygame.sprite.Sprite):

    speed = -11
    images = []
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=pos)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top <= 0:
            self.kill()


class Bomb(pygame.sprite.Sprite):

    speed = 9
    images = []
    def __init__(self, alien):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=
                    alien.rect.move(0,5).midbottom)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom >= 470:
            Explosion(self)
            self.kill()

class Score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(None, 20)
        self.font.set_italic(1)
        self.color = Color('white')
        self.lastscore = -1
        self.update()
        self.rect = self.image.get_rect().move(10, 450)

    def update(self):
        if SCORE != self.lastscore:
            self.lastscore = SCORE
            msg = "Score: %d" % SCORE
            self.image = self.font.render(msg, 0, self.color)



def main(winstyle = 0):
    # Initialize pygame
    pygame.init()
    if pygame.mixer and not pygame.mixer.get_init():
        print ('Warning, no sound')
        pygame.mixer = None

    # Set the display mode
    winstyle = 1  # |FULLSCREEN
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

    #Load images, assign to sprite classes
    #(do this before the classes are used, after screen setup)
    
    img = load_image('fat_guy_beddi.png')
    print(img)
    Player.images = [img, pygame.transform.flip(img, 1, 0)]
    img = load_image('explosion1.gif')
    Explosion.images = [img, pygame.transform.flip(img, 1, 1)]
    Bomb.images = [load_image('bomb.gif')]
    Shot.images = [load_image('shot.gif')]

    #decorate the game window
    icon = pygame.transform.scale(Alien.images[0], (32, 32))
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Sick Simon')
    pygame.mouse.set_visible(0)
    #create the background, tile the bgd image
    bgdtile = load_image('background.gif')
    background = pygame.Surface(SCREENRECT.size)
    for x in range(0, SCREENRECT.width, bgdtile.get_width()):
        background.blit(bgdtile, (x, 0))
    screen.blit(background, (0,0))
    pygame.display.flip()

    #load the sound effects
    boom_sound = load_sound('boom.wav')
    shoot_sound = load_sound('car_door.wav')
    if pygame.mixer:
        music = os.path.join(main_dir, 'data', 'house_lo.wav')
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(-1)

    # Initialize Game Groups
    essen = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    bombs = pygame.sprite.Group()
    all = pygame.sprite.RenderUpdates()
    last_essen = pygame.sprite.GroupSingle()
    #assign default groups to each sprite class
    Essen.containers = essen, all, last_essen
    #assign default groups to each sprite class
    Player.containers = all
    Shot.containers = shots, all
    Bomb.containers = bombs, all
    Explosion.containers = all
    Score.containers = all

    #Create Some Starting Values
    global score
    essen_reload = ESSEN_RELOAD
    kills = 0
    clock = pygame.time.Clock()

    #initialize our starting sprites
    global SCORE
    player = Player()
    Essen() #note, this 'lives' because it goes into a sprite group
    if pygame.font:
        all.add(Score())
        
    while player.alive():

        #get input
        for event in pygame.event.get():
            if event.type == QUIT or \
                (event.type == KEYDOWN and event.key == K_ESCAPE):
                    return
        keystate = pygame.key.get_pressed()

        # clear/erase the last drawn sprites
        all.clear(screen, background)

        #update all the sprites
        all.update()

        #handle player input
        direction = keystate[K_RIGHT] - keystate[K_LEFT]
        player.move(direction)
        firing = keystate[K_SPACE]
        if not player.reloading and firing and len(shots) < MAX_SHOTS:
            Shot(player.gunpos())
            shoot_sound.play()
        player.reloading = firing

        # Create new alien
        if essen_reload:
            essen_reload = essen_reload-1
        elif not int(random.random() * ESSEN_ODDS):
            Essen()
            essen_reload = ESSEN_RELOAD


        # Detect collisions
        
        
        for gericht in pygame.sprite.spritecollide(player, essen, 1):
            # wenn was gscheids dann dick bonus punkte
            if gericht.type in 'gscheid':
                SCORE = SCORE + gericht.nutritional_value
            # wenn gemuese einfach so das wars
            if gericht.type in 'gemuese':
                player.kill()
            # TO DO: IMPLEMENT BOOST FUNCTIONS
            gericht.kill()

        #draw the scene
        dirty = all.draw(screen)
        pygame.display.update(dirty)

        #cap the framerate
        clock.tick(40)

    if pygame.mixer:
        pygame.mixer.music.fadeout(1000)
    pygame.time.wait(1000)
    pygame.quit()



#call the "main" function if running this script
if __name__ == '__main__': main()

