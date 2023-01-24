import stage
import ugame

class Ball(stage.Sprite):
    def __init__(self, x, y):
        super().__init__(bank, 1, x, y)
        self.dx = 2
        self.dy = 1

    def update(self):
        super().update()
        self.set_frame(self.frame % 4 + 1)
        self.move(self.x + self.dx, self.y + self.dy)
        if not 0 < self.x < 144:
            self.dx = -self.dx
        if not 0 < self.y < 112:
            self.dy = -self.dy


bank = stage.Bank.from_bmp16('ball.bmp')
# by default the first tile is show
bg = stage.Grid(bank, 10, 8)
# numbers are sprite pos, and x and y coords
ball_1 = Ball(64, 0)
ball_2 = Ball(0, 76)
ball_3 = Ball(111, 64)
balls = [ball_1, ball_2, ball_3]
text = stage.Text(12, 1)
text.move(32, 60)
text.text('Monkey Balls')

# second param is the fps
gm = stage.Stage(ugame.display, 12)
gm.layers = [text] + balls + [bg]
gm.render_block()



while True:
    for ball in balls:
        ball.update()
    gm.render_sprites(balls)
    gm.tick()