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
platform1 = Player('platform.png', 0, 150, 60, 75, 150)
platform2 = Player('platform.png', 624, 150, 60, 75, 150)


speed_x = 5
speed_y = 5

font.init()
font = font.Font(None, 50)

finish = False
clock= time.Clock()
FPS = 60
game = True
while game:
    if finish != True:
        window.blit(background, (0, 0))

        ball.reset()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > 500 - 60 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(ball, platform1) or sprite.collide_rect(ball, platform2):
            speed_x *= -1

        if ball.rect.x <= 1:
          lose1 = font.render('Левый игрок проиграл!', True, (255, 255, 255))
          window.blit(lose1, (150, 225))
          finish = False

        if ball.rect.x >= 699:
          lose2 = font.render('Правый игрок проиграл!', True, (255, 255, 255))
          window.blit(lose2, (150, 225))
          finish = False

        platform1.reset()
        platform1.update1()

        platform2.reset()
        platform2.update2()

        for e in event.get():
            if e.type == QUIT:
                game = False
        display.update()
        clock.tick(FPS)
