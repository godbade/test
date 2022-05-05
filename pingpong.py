from pygame import*
okno = display.set_mode((600,600))
game = True
clock = time.Clock()

class gameobject(sprite.Sprite):
    def __init__(self, img, x,y,q,q1):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(img), (q,q1))
        self.rect = self.image.get_rect()

while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
 
    display.update()
