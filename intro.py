alien = Actor('alien_resize')
alien.topleft = 0, 0

WIDTH = 800
HEIGHT = 800

TILE_SIZE = 40

def draw():
    screen.clear()
    alien.draw()

'''
def update():
    alien.left += 2
    if alien.left > WIDTH:
        #alien.right = 20
'''

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()

def on_key_down(key):
    # player movement
    row = int(alien.y / TILE_SIZE)
    column = int(alien.x / TILE_SIZE)
    print(row, column)
    if key == keys.UP and alien.y > 0:
        alien.y -= 40
    if key == keys.DOWN and alien.y < 800:
         alien.y += 40
    if key == keys.LEFT:
        alien.x -= 40
    if key == keys.RIGHT:
        alien.x += 40
    

def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 1.0)


def set_alien_normal():
    alien.image = 'alien'