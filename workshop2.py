import pgzrun
import random

WIDTH = 600
HEIGHT = 600

bg_y = -600

rumskib = Actor("rumskib1")
rumskib.bottom = HEIGHT
rumskib.x = WIDTH//2

stjerne_liste = []
for _ in range(50):
    stjerne = Actor('stjerne.png')
    stjerne.x = random.randrange(WIDTH+1)
    stjerne.y = random.randrange(HEIGHT+1)
    stjerne_liste.append(stjerne)

skud_liste = []
ufo = Actor('ufo1', pos=(300,100))

def rumskib_bliv_paa_banen():
    if rumskib.top < 0: 
        rumskib.top = 0
    if rumskib.bottom > HEIGHT: 
        rumskib.bottom = HEIGHT
    if rumskib.left < 0: 
        rumskib.left = 0
    if rumskib.right > WIDTH: 
        rumskib.right = WIDTH

def on_mouse_down():
    skud = Actor("skud1", pos=rumskib.midtop)
    skud_liste.append(skud)   

def baggrund_update():
    global bg_y
    bg_y += 1
    if bg_y > 0:
        bg_y -= 1200

def stjerner_update():
    for stjerne in stjerne_liste:
        if stjerne.y < HEIGHT + 8:
            stjerne.y += 1.5
        else:
            stjerne.x = random.randrange(WIDTH+1)
            stjerne.y = -8

def rumskib_update():
    if keyboard.left: 
        rumskib.x -= 5
    if keyboard.right: 
        rumskib.x += 5
    if keyboard.down: 
        rumskib.y += 5
    if keyboard.up:
        rumskib.y -= 5
        rumskib.image = "rumskib2.png"
    else:
        rumskib.image = "rumskib1.png"
    rumskib.y += 2
    rumskib_bliv_paa_banen()

def skud_update():
    for skud in skud_liste:
        skud.y -= 6
        if skud.bottom < 0:
            skud_liste.remove(skud)
        if skud.colliderect(ufo):
            skud_liste.remove(skud)
            animate(ufo, x = random.randrange(WIDTH+1))


def draw():
    screen.blit('stjerner.png', (0, bg_y))
    for stjerne in stjerne_liste:
        stjerne.draw()
    ufo.draw()
    for skud in skud_liste:
        skud.draw()
    rumskib.draw()

def update():
    baggrund_update()
    stjerner_update()
    rumskib_update()
    skud_update()

pgzrun.go()