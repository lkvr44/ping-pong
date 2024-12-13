from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,pl_picture,pl_x,pl_y,pl_speed, size_x, size_y, ):
        super().__init__()
        self.image = transform.scale(image.load(pl_picture),(size_x,size_y))
        self.speed = pl_speed
        self.rect = self.image.get_rect()
        self.rect.x = pl_x
        self.rect.y = pl_y
        self.side = 'right'
        self.sidey = 'up'
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

class Ball(GameSprite):
    def update(self):
        if self.side == 'right':
            if self.rect.x < 510:
                self.rect.x += self.speed
            else:
                self.rect.x -= self.speed
                self.side = 'left'
        elif self.side == 'left':
            if self.rect.x > 5:
                self.rect.x -= self.speed
            else:
                self.rect.x += self.speed
                self.side = 'right'
        if self.sidey == 'up':
            if self.rect.y < 510:
                self.rect.y += self.speed
            else:
                self.rect.y -= self.speed
                self.sidey = 'down'
        elif self.sidey == 'down':
            if self.rect.y > 5:
                self.rect.y -= self.speed
            else:
                self.rect.y += self.speed
                self.sidey = 'up'
background = (200, 255, 255)
wind_width = 600
wind_height = 500
window = display.set_mode((wind_width, wind_height))
window.fill(background)

game = True
finish = False
clock = time.Clock()
FPS = 60

player_l = Player('racket.png' ,30, 200, 5, 50, 150)
player_r = Player('racket.png' ,520, 300, 5, 50, 150)
ball = Ball('tenis_ball.png' ,200, 200, 4, 50, 50)

speed_x = 3
speed_y = 3

font.init()
font= font.SysFont('Arial', 70)
win_l = font.render('Left WIN!', True, (255, 200, 0))
win_r = font.render('Right LOSE!', True, (255, 200, 0))

left_score=0
right_score=0

while game:
    for e in event.get():
            if e.type == QUIT:
                game= False


    if not finish:

        window.blit(background,(0,0))

        player_l.update_l()
        player_r.update_r()
        ball.update()

        ball.reset()

        text = font.render('Счет: ' + str(left_score) + '/3', 1, (255,255,255))
        window.blit(text,(10,20))

        text_lose = font.render('Пропущено: ' + str(right_score) + '/3', 1, (255,255,255))
        window.blit(text_lose,(10,50))

        clock.tick(FPS)

        if left_score >= 3:
            text = font.render('Счет: ' + str(left_score) + '/3', 1, (255,255,255))
            window.blit(text,(10,20))
            finish = True
            window.blit(win_l, (200,200))

        if right_score >= 3:
            text_lose = font.render('Пропущено: ' + str(right_score) + '/3', 1, (255,255,255))
            window.blit(text_lose,(10,50))
            finish = True
            window.blit(win_r, (200,200))

    display.update()




