from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,pl_picture,pl_x,pl_y,pl_speed, size_x, size_y, ):
        super().__init__()
        self.image = transform.scale(image.load(pl_picture),(size_x,size_y))
        self.speed = pl_speed
        self.rect = self.image.get_rect()
        self.rect.x = pl_x
        self.rect.y = pl_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y < -80:
            self.rect.y += self.speed
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
    def update_l(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_s] and self.rect.y < -80:
            self.rect.y += self.speed
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

background = (200, 255, 255)
wind_width = 600
wind_height = 500
widow = display.set_mode((wind_width, wind_height))
widow.fill(background)

game = True
finish = False
clock = time.Clock()
FPS = 60

player_l = Player('racket.png' ,30, 200, 5, 50, 150)
player_r = Player('racket.png' ,520, 300, 5, 50, 150)
ball = GameSprite('tenis_ball.png' ,200, 200, 4, 50, 50)

speed_x = 3
speed_y = 3

font.init()
font= font.SysFont('Arial', 70)
win_l = font.render('Left WIN!', True, (255, 200, 0))
win_r = font.render('Right LOSE!', True, (255, 200, 0))










