import pgzrun

WIDTH=600
HEIGHT=600
bg_y = -600

def draw():
    screen.clear()
    screen.blit("stjerner.png", (0, bg_y))
    
def update():
    global bg_y
    bg_y += 2
    if bg_y > 0:
        bg_y -= 1200


pgzrun.go()