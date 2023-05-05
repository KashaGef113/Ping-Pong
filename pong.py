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

rocket1 = Player('player1.png', 0, 420, 30, 100, 10)
rocket2 = Player('player1.png', 650, 420, 30, 100, 10)
pong_ball = GameSprite('pong_ball1.png', 300, 300, 50, 50, 9)

while game:
    window.blit(background,(0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False

    rocket1.updater()
    rocket1.reset()
    rocket2.updatel()
    rocket2.reset()
    pong_ball.reset()
    display.update()
    clock.tick(60)
