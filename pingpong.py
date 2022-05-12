from pygame import*
okno = display.set_mode((600,600))
game = True
clock = time.Clock()
s=int(input())

class gameobject(sprite.Sprite):
    def __init__(self, img, x,y,q,q1):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(img), (q,q1))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))
        
    
class player(gameobject):
    def control(self):
        knopki = key.get_pressed()
        if knopki[K_w]:
            self.rect.y -= s
        if knopki[K_s]:
            self.rect.y += s    
            
class geroi(gameobject):
    def control2(self):
        knopki = key.get_pressed()
        if knopki[K_UP]: 
            self.rect.y -= s
        if knopki[K_DOWN]: 
            self.rect.y += s
class ball(gameobject):
    def move(self,sx,sy):
        self.rect.x+=sx
        self.rect.y+=sy
sx=1
sy=1
p2=geroi("open.png",600,600,10,90)
p1=player("open.png",0,0,10,90)
ball=ball("ball.png",300,300,20,20)
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    okno.fill((0,0,0))
    p1.draw()
    ball.draw()
    p1.control()
    p2.draw()
    p2.control2()
    ball.move(sx,sy)
    if ball.rect.x < 0:
        sx*=-1
    if ball.rect.x > 600:
        sx*=-1  
    if ball.rect.y < 0:
        sy*=-1
    if ball.rect.y > 600:
        sy*=-1         
    clock.tick(60)
    display.update()
