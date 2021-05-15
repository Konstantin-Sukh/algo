from pygame import *
font.init()

w = 1000
h = 700

window = display.set_mode((w, h))

font = font.Font(None, 50)

class GameSprite(sprite.Sprite):
    def __init__(self, file, W, H, x, y, speed_x, speed_y):
        #sprite.Sprite.__init__(self)
        super().__init__()
        self.file = image.load(file)
        self.file = transform.scale(self.file, (W, H))
        self.rect = self.file.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
    def draw(self):
        window.blit(self.file, self.rect)

class Ball(GameSprite):
    p_01 = 0
    p_02 = 0
    run = True
    def move(self):
        global score
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.x > w - 40:
            self.speed_x *= -1
            self.rect.x = w // 2
            self.rect.y = h // 2
            self.p_01 += 1
            score = font.render(str(ball.p_01) + "  :  " + str(ball.p_02), True, (255, 255, 255))
        if self.rect.x < 0:
            self.speed_x *= -1
            self.rect.x = w // 2
            self.rect.y = h // 2
            self.p_02 += 1
            score = font.render(str(ball.p_01) + "  :  " + str(ball.p_02), True, (255, 255, 255))
        if self.rect.y > h - 40 or self.rect.y < 0:
            self.speed_y *= -1
        if sprite.collide_rect(self, player_01):
            self.speed_x *= -1
        if sprite.collide_rect(self, player_02):
            self.speed_x *= -1
        if self.p_01 >= 3 or self.p_02 >= 3:
            if self.p_01 - self.p_02 >= 2:
                self.win = font.render("THE FIRST PLAYER WINS!", True, (255, 255, 255))
                self.win_rect = self.win.get_rect(centerx = w/2, centery = h/2)
                self.run = False
            if self.p_02 - self.p_01 >= 2:
                self.win = font.render("THE SECOND PLAYER WINS!", True, (255, 255, 255))
                self.win_rect = self.win.get_rect
                self.run = False

class Player(GameSprite):
    def move_01(self):
        keys = key.get_pressed()
        if keys[K_w]:
            if self.rect.y > 0:
                self.rect.y -= self.speed_y
        if keys[K_s]:
            if self.rect.y < h - 100:
                self.rect.y += self.speed_y
    def move_02(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            if self.rect.y > 0:
                self.rect.y -= self.speed_y
        if keys[K_DOWN]:
            if self.rect.y < h - 100:
                self.rect.y += self.speed_y

ball = Ball("ball.png", 40, 40, w // 2, h // 2, 3, 3)
player_01 = Player("player.png", 10, 100, 20, h / 2, 0, 5)
player_02 = Player("player.png", 10, 100, w - 60, h / 2, 0, 5)
score = font.render(str(ball.p_01) + "  :  " + str(ball.p_02), True, (255, 255, 255))
score_rect = score.get_rect(centerx = w / 2, centery = 20)

clock = time.Clock()

game = True
while game:
    window.fill((0, 150, 255))
    for e in event.get():
        if e.type == QUIT:
            game = False
    if ball.run:
        ball.draw()
        ball.move()
        player_01.move_01()
        player_01.draw()
        player_02.move_02()
        player_02.draw()
    else:
        window.blit(ball.win, ball.win_rect)
    window.blit(score, score_rect)
    display.update()
    clock.tick(100)
