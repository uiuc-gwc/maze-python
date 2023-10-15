WIDTH = 800
HEIGHT = 800

TILE_SIZE = 40
alien = Actor('alien_resize')
alien.topleft = 0, 40


from df_maze import give_maze
import numpy as np
import random


maze = give_maze()
where = np.where(maze == 1)
mazeSet = set((where[0][i],where[1][i]) for i in range(where[0].shape[0]))




def draw():
    screen.clear()
    for i in range(20):
        for j in range(20):
            if maze[i,j] == 1:
                screen.blit('maze', (i*40, j*40))
    alien.draw()


def get_possible_directions():
    #NOTATION [UP, LEFT, DOWN, RIGHT]
    #UP = 0, LEFT = 1, DOWN = 2, RIGHT = 3
    row = int(alien.y / TILE_SIZE)
    column = int(alien.x / TILE_SIZE)

    UP = not (column,row - 1) in mazeSet and row > 0
    LEFT = not (column-1,row) in mazeSet and column > 0
    DOWN = not (column,row+1) in mazeSet and row < 19
    RIGHT = not (column+1,row) in mazeSet and column < 19

    return [UP,LEFT,DOWN,RIGHT]

past_moves = [3]
def policy(possible_directions):
    #YOU WILL IMPLEMENT POLICY
    #LEFT, RIGHT
    #POLICY OUTPUTS A NUMBER 0,1,2,3 CORRESPONDING TO UP, LEFT, DOWN, RIGHT
    UP = possible_directions[0]
    LEFT = possible_directions[1]
    DOWN = possible_directions[2]
    RIGHT = possible_directions[3]


    if RIGHT:
        return 3
    if DOWN:
        return 2
    if UP:
        return 0
    if LEFT:
        return 1
    
    

def execute_policy():
    dir = get_possible_directions()
    move = policy(dir)
    #print(move)
    if move == 0:
        move_up()
        past_moves.append(0)
    if move == 1:
        move_left()
        past_moves.append(1)
    if move == 2:
        move_down()
        past_moves.append(2)
    if move == 3:
        move_right()
        past_moves.append(3)

def on_mouse_down(pos):
    execute_policy()
    



def move_left():
    row = int(alien.y / TILE_SIZE)
    column = int(alien.x / TILE_SIZE)

    new_row = row 
    new_col = column - 1 

    if not (new_col,new_row) in mazeSet and column > 0:
        alien.x -= 40
def move_right():
    row = int(alien.y / TILE_SIZE)
    column = int(alien.x / TILE_SIZE)

    new_row = row
    new_col = column + 1

    if not (new_col,new_row) in mazeSet and column < 19:
        alien.x += 40
def move_up():
    row = int(alien.y / TILE_SIZE)
    column = int(alien.x / TILE_SIZE)

    new_row = row - 1 
    new_col = column 

    if not (new_col,new_row) in mazeSet and row > 0:
        alien.y -= 40
def move_down():
    row = int(alien.y / TILE_SIZE)
    column = int(alien.x / TILE_SIZE)

    new_row = row + 1
    new_col = column 

    if not (new_col,new_row) in mazeSet and row < 19:
        alien.y += 40


'''
def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()
'''

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





