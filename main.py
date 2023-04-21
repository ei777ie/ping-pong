from pygame import *
from random import randint
import time as time_module

rel_time = False
num_fire = 0
start_time = 0

window = display.set_mode((700, 500))
display.set_caption('Shooter')
background = transform.scale(image.load('background.jpg'), (700, 500))

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play(-1)

clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.player_speed = player_speed

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_d] and self.rect.x < 630:
            self.rect.x += 10
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= 10

    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx - 7, self.rect.top, 5, 15, 20)
        bullets.add(bullet)

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

lost = 0

class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.player_speed
        if self.rect.y >= 500:
            self.rect.x = randint(50, 550)
            self.rect.y = 0
            lost -= 1
            '''self.kill() 
            enemy = Enemy('ufo.png', randint(0, 500), 0, randint(1, 3), 80, 60)
            monsters.add(enemy)
            self.kill()
            asteroid = Enemy('asteroid.png', randint(0, 500), 0, randint(1, 10), 80, 60)
            asteroids.add(asteroid)
            self.kill()    '''

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.player_speed
        if self.rect.y <= 0:
            self.kill()

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

player = Player('rocket.png', 350, 410, 10, 60, 80)

monsters = sprite.Group()
asteroids = sprite.Group()
asteroid = Enemy('asteroid.png', randint(0, 500), 0, randint(1, 3), 80, 60)
enemy = Enemy('ufo.png', randint(0, 500), 0, randint(1, 3), 80, 60)
enemy1 = Enemy('ufo.png', randint(0, 500), 0, randint(2, 4), 80, 60)
enemy2 = Enemy('ufo.png', randint(0, 500), 0, randint(3, 4), 80, 60)
monsters.add(enemy)
monsters.add(enemy1)
monsters.add(enemy2)
asteroids.add(asteroid)
bullets = sprite.Group()

font.init()
font = font.Font(None, 40)
finish = False
game = True
Lose = font.render('You Lose!', True, (255, 255, 255))
Win = font.render('You Win!', True, (255, 255, 255))
Reloading = font.render('Reloading!', True, (255, 255, 255))
while game:
    if finish != True:
        window.blit(background, (0, 0))
        bullets.update()
        bullets.draw(window)
        player.reset()
        player.update()
        monsters.update()
        monsters.draw(window)
        asteroids.update()
        asteroids.draw(window)

        if sprite.spritecollide(player, monsters, False):
            finish = True
            window.blit(Lose, (350, 250))

        if sprite.spritecollide(player, asteroids, False):
            finish = True
            window.blit(Lose, (350, 250))

        list_killed = sprite.groupcollide(monsters, bullets, True, True)
        for e in list_killed:
            lost += 1
            enemy = Enemy('ufo.png', randint(0, 500), 0, randint(1, 3), 80, 60)
            monsters.add(enemy)

        if lost >= 30:
            finish = True
            window.blit(Win, (350, 250))

        monsters_lost = font.render('Очки '+ str(lost), True, (255, 255, 255))
        window.blit(monsters_lost, (20, 20))
    
    end_time = time_module.time()
    if int(end_time - start_time) <= 1:
        window.blit(Reloading, (300, 150))
    else:
        rel_time = False
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                if num_fire <= 10 and rel_time == False:
                    player.fire()
                    num_fire += 1
                if num_fire == 10 and rel_time == False:
                    rel_time = True
                    start_time = time_module.time()
                    num_fire = 0

    display.update()
    clock.tick(FPS)
