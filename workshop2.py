import pgzrun

WIDTH = 600
HEIGHT = 600

rumskib = Actor("rumskib1")
rumskib.bottom = HEIGHT
rumskib.x = WIDTH//2

import random

stjerne_liste = []
for _ in range(50):
    stjerne = Actor('stjerne.png')
    stjerne.x = random.randrange(WIDTH+1)
    stjerne.y = random.randrange(HEIGHT+1)
    stjerne_liste.append(stjerne)

skud_liste = []
ufo = Actor('ufo1', pos=(300,100))
            
def draw():
    screen.clear() # Kun hvis kode til blit af baggrund er fjernet
    for stjerne in stjerne_liste:
        stjerne.draw()
    ufo.draw()
    for skud in skud_liste:
        skud.draw()
    rumskib.draw()

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

def update():
    for stjerne in stjerne_liste:
        if stjerne.y < HEIGHT + 8:
            stjerne.y += 1
        else:
            stjerne.x = random.randrange(WIDTH+1)
            stjerne.y = -8
    rumskib_update()
    for skud in skud_liste:
        skud.y -= 6
        if skud.bottom < 0:
            skud_liste.remove(skud)
        if skud.colliderect(ufo):
            skud_liste.remove(skud)
            animate(ufo, x = random.randrange(WIDTH+1))

pgzrun.go()