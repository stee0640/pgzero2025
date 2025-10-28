import pgzrun
import random

WIDTH = 600
HEIGHT = 600
bg_y = -600

rumskib = Actor('rumskib1.png')
rumskib.bottom = HEIGHT
rumskib.x = WIDTH//2
rumskib.score = 0

stjerne_grafik = [
    's1.png', 's2.png', 's3.png',
    's4.png', 's5.png', 's6.png'
]

eksplosion_liste = []
skud_liste = []
ufo_liste = []
stjerne_liste = []

for _ in range(200):
    stjerne = Actor(random.choice(stjerne_grafik))
    stjerne.x = random.randrange(WIDTH+1)
    stjerne.y = random.randrange(HEIGHT+1)
    stjerne.angle = angle=random.randrange(360)
    stjerne_liste.append(stjerne)

def skab_ufo():
    ny_ufo = Actor('ufo1.png')
    ny_ufo.x = random.randint(0, WIDTH)
    ny_ufo.bottom = 0
    ny_ufo.vx = random.randint(-10, 10)
    ny_ufo.vy = random.randint(2, 10)
    ufo_liste.append(ny_ufo)
    clock.schedule(skab_ufo, 0.5)

clock.schedule(skab_ufo, 2)

def skab_eksplosion(position):
    eksplosion = Actor('eksplosion50.png', pos = position)
    eksplosion.frames = 15
    eksplosion_liste.append(eksplosion)

def on_mouse_down():
    skud = Actor('skud1.png', pos=rumskib.midtop)
    skud_liste.append(skud)   

def baggrund_update():
    global bg_y
    bg_y += 0.8
    if bg_y > 0:
        bg_y -= 1200

def stjerner_update():
    for stjerne in stjerne_liste:
        if stjerne.y < HEIGHT + 8:
            stjerne.y += 1
        else:
            stjerne.x = random.randrange(WIDTH+1)
            stjerne.y = -8

def ufoer_update():
    for ufo in ufo_liste:
        ufo.angle += 1
        ufo.x += ufo.vx
        ufo.y += ufo.vy
        if (ufo.left <= 0 and ufo.vx < 0) or (ufo.right >= WIDTH and ufo.vx > 0):
            ufo.vx = -ufo.vx 
        if ufo.top > HEIGHT:
            ufo_liste.remove(ufo)

def skud_update():
    for skud in skud_liste:
        skud.y -= 6
        if skud.bottom < 0:
            skud_liste.remove(skud)
        for ufo in ufo_liste:
            if skud.colliderect(ufo):
                if skud in skud_liste:
                    skud_liste.remove(skud)
                ufo_liste.remove(ufo)
                rumskib.score += 1
                skab_eksplosion(ufo.pos)

def eksplosion_update():
    for eksplosion in eksplosion_liste:
        eksplosion.frames -= 1
        if eksplosion.frames < 0:
            eksplosion_liste.remove(eksplosion) 
        elif eksplosion.frames == 12:
            eksplosion.image = 'eksplosion75.png'
        elif eksplosion.frames == 8:
            eksplosion.image = 'eksplosion100.png'

def rumskib_bliv_paa_banen():
    if rumskib.top < 0: 
        rumskib.top = 0
    if rumskib.bottom > HEIGHT:
        rumskib.bottom = HEIGHT
    if rumskib.left < 0: 
        rumskib.left = 0
    if rumskib.right > WIDTH:
        rumskib.right = WIDTH

def rumskib_update():
    if keyboard.left: 
        rumskib.x -= 5
    if keyboard.right: 
        rumskib.x += 5
    if keyboard.down: 
        rumskib.y += 5
    if keyboard.up:
        rumskib.y -= 5
        rumskib.image = 'rumskib2.png'
    else:
        rumskib.image = 'rumskib1.png'
    rumskib.y += 2
    rumskib_bliv_paa_banen()

def score_draw():
    screen.draw.text(
        str(rumskib.score),
        color="white",
        midtop=(WIDTH // 2, 10),
        fontsize=70,
        shadow=(1, 1)
    )

def draw():
    screen.blit('baggrund.png', (0, bg_y))
    for stjerne in stjerne_liste:
        stjerne.draw()
    for ufo in ufo_liste:
        ufo.draw()
    for skud in skud_liste:
        skud.draw()
    for eksplosion in eksplosion_liste:
        eksplosion.draw()
    rumskib.draw()
    score_draw()

def update():
    baggrund_update()
    stjerner_update()
    rumskib_update()
    ufoer_update()
    skud_update()
    eksplosion_update()

pgzrun.go()