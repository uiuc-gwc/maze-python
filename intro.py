alien = Actor('alien_resize')
alien.topleft = 0, 40

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
    if key == keys.UP:
        row = row - 1
    if key == keys.DOWN:
        row = row + 1
    if key == keys.LEFT:
        column = column - 1
    if key == keys.RIGHT:
        column = column + 1
    alien.y = row * TILE_SIZE 
    alien.x = column * TILE_SIZE 
    

def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 1.0)


def set_alien_normal():
    alien.image = 'alien'