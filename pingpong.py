from pygame import*
okno = display.set_mode((600,600))
game = True
clock = time.Clock()

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
        if knopki[K_w] and self.rect.x < 600:
            self.rect.y -= 1
        if knopki[K_s] and self.rect.x > 0:
            self.rect.y += 1    
            
            
            
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
 
    display.update()
