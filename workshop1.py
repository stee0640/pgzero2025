import pgzrun

WIDTH = 600
HEIGHT = 600
bg_y = -600

rumskib = Actor("rumskib1")
rumskib.bottom = HEIGHT
rumskib.x = WIDTH//2

def draw():
    screen.blit("stjerner.png", (0, bg_y))
    rumskib.draw()

def rumskib_update():
    if keyboard.left: 
        rumskib.x -= 5
    if keyboard.right: 
        rumskib.x += 5
    if keyboard.up: 
        rumskib.y -= 5
    if keyboard.down: 
        rumskib.y += 5

def update():
    global bg_y
    bg_y += 2
    if bg_y > 0:
        bg_y -= 1200
    rumskib_update()
    
pgzrun.go()

