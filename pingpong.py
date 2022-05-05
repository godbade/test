from pygame import*
okno = display.set_mode((600,600))
game = True
clock = time.Clock()


while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
 
    display.update()
