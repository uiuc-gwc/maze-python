alien = Actor('alien_resize')
alien.topleft = 0, 40

WIDTH = 800
HEIGHT = 800

TILE_SIZE = 40
from df_maze import give_maze
import numpy as np

maze = give_maze()
where = np.where(maze == 1)
#print(where)

mazeSet = set((where[0][i],where[1][i]) for i in range(where[0].shape[0]))
#print(mazeSet)

RED = 200, 0, 0
BOX = Rect((20, 20), (100, 100))



def draw():
    screen.clear()
    for i in range(20):
        for j in range(20):
            if maze[i,j] == 1:
                screen.blit('maze', (i*40, j*40))
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

    new_row = row - (key == keys.UP) + (key == keys.DOWN)
    new_col = column - (key == keys.LEFT) + (key == keys.RIGHT)

    print("OLD", row, column)
    print("NEW", new_row, new_col)

    if not (new_col,new_row) in mazeSet:
        if key == keys.UP and row > 0:
            alien.y -= 40
        if key == keys.DOWN and row < 19:
            alien.y += 40
        if key == keys.LEFT and column > 0:
            alien.x -= 40
        if key == keys.RIGHT and column < 19:
            alien.x += 40
    

def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 1.0)


def set_alien_normal():
    alien.image = 'alien_resize'





