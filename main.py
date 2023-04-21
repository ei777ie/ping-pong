from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Ping Pong')
background = transform.scale(image.load('background.jpeg'), (700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.player_speed = player_speed

    def reset(self):

        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_s] and self.rect.y < 380:
            self.rect.y += 10
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= 10


    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y < 380:
            self.rect.y += 10
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= 10

ball = GameSprite('ball.png', 200, 200, 60, 60, 60)
platform1 = Player('platform.png', 0, 150, 60, 125, 125)
platform2 = Player('platform.png', 575, 150, 60, 125, 125)



clock= time.Clock()
FPS = 60
game = True
while game:
    window.blit(background, (0, 0))

    ball.reset()
    ball.update()

    platform1.reset()
    platform1.update1()

    platform2.reset()
    platform2.update2()

    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)
