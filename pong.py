
from pygame import *
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Pong")
background = transform.scale(image.load('pong1.png'),(win_width,win_height))
clock = time.Clock()
game = True
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, width, height, player_speed):
         super().__init__()
         self.image = transform.scale(image.load(player_image), (width, height))
         self.speed = player_speed
         self.rect = self.image.get_rect()
         self.rect.x = player_x
         self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
class Player(GameSprite):
    def updater(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 0:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 100:
           self.rect.y += self.speed
    
    def updatel(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 0:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 100:
           self.rect.y += self.speed

rocket1 = Player('player1.png', 0, 390, 30, 100, 10)
rocket2 = Player('player1.png', 650, 390, 30, 100, 10)
pong_ball = GameSprite('pong_ball1.png', 300, 300, 50, 50, 9)
speed_x = 3
speed_y = 3
finish = False
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render(
    'PLAYER 1 LOST!', True, (180, 0, 0)
)
font2 = font.Font(None, 35)
lose2 = font2.render(
    'PLAYER 2 LOST!', True, (180, 0, 0)
)


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background,(0, 0))

        rocket1.updater()
        rocket1.reset()
        rocket2.updatel()
        rocket2.reset()
        pong_ball.reset()

        pong_ball.rect.x += speed_x
        pong_ball.rect.y += speed_y

        if pong_ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
        if pong_ball.rect.x > 700:
            finish = True
            window.blit(lose2, (200, 200))

        if pong_ball.rect.y > 450 or pong_ball.rect.y <0:
            speed_y *= -1

        if sprite.collide_rect(pong_ball, rocket1) or sprite.collide_rect(pong_ball, rocket2):
                speed_x *= -1

    display.update()
    clock.tick(60)
