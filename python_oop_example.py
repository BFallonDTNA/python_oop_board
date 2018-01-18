



import pygame
import sys
import os

import board_map

ani = 4   # animation cycles

DICE_LEVELS = (4, 6, 8, 10, 12, 20)

STARTING_MONEY = 10
PLAYER_PAWNS = 16
STARTING_FOOD = 16

RES = "C:/Users/bfallon/Desktop/oop_example/res"

class Game(object):
    """
    The class that manages a round of the game

    Attributes:
    
    Methods:

    """

    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        self.name = name


class Board(object):
    """
    The container for interaction between pieces on a map, Like a board game board.

    Attributes:
    
    Methods:

    """

    def __init__(self, name, balance=0.0):
        """
        Needs a name
        """
        self.name = name
        

class Map(object):
    """
    Used to define the layout of a board

    Attributes:
    
    Methods:

    """

    def __init__(self, name, balance=0.0):
        """
        Needs a name
        """
        self.name = name


class Player(object):
    """
    The class that manages a round of the game

    Attributes:

        is_cpu:
        pieces:
    
    Methods:

    """

    def __init__(self, name, is_cpu):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        self.name = name
        self.is_cpu = is_cpu
        self.pieces = []
        self.stash = Stash()


class Stash(object):
    """
    Keeps track of what a player owns (money, dice, pawns, food, etc.)

    Attributes:


    
    Methods:

    """

    def __init__(self):
        """
        """
        self.gold = STARTING_MONEY
        self.pawns = PLAYER_PAWNS
        self.food = STARTING_FOOD


class Compass(object):
    """
    Used to move pieces on the board, given a direction

    Attributes:
    
    Methods:

    """

    def __init__(self, name, balance=0.0):
        """
        Needs a name
        """
        self.name = name


class Di(object):
    """
    Roll to get a number

    Attributes:
    
    Methods:

    """

    def __init__(self, name, balance=0.0):
        """
        Needs a name
        """
        self.name = name








class PlayerTest(pygame.sprite.Sprite):
    '''
    Spawn a player
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []
        for i in range(1,5):
            img = pygame.image.load(os.path.join(RES, "512", "upg_sword.png"))
            self.images.append(img)
            self.image = self.images[0]
            self.rect  = self.image.get_rect()

    def control(self,x,y):
        '''
        control player movement
        '''
        self.movex += x
        self.movey += y

    def update(self):
        '''
        Update sprite position
        '''

        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

        # moving left
        if self.movex < 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]

        # moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]


class CursorIcon():
    '''
    The image that follows the cursor. There is also the system cursor drawn at click hotspot.
    '''
    def __init__(self):
        self.image = pygame.image.load(s.path.join(RES,"cursors",'glove1.png')

def main():
    '''
    Setup
    '''
    worldx = 1900
    worldy = 1080

    fps = 40  # frame rate
    clock = pygame.time.Clock()
    pygame.init()

    # Color theme pallette
    WHITE = (254,254,254)
    BLACK = (0, 0, 0)
    BROWN = (230, 204, 179)
    BLUE  = (50,80,200)
    GREEN = (191, 255, 128)
    GREY  = (194, 194, 214)

    DIRT = board_map.Land("dirt", BROWN)
    GRAS = board_map.Land("grass", GREEN)
    MNTN = board_map.Land("mountain", GREY)

    no_mtn_a  = [DIRT, DIRT, GRAS, GRAS, GRAS, DIRT, DIRT, DIRT, DIRT, DIRT]
    no_mtn_b  = [DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, GRAS, GRAS, GRAS]
    one_mtn = [DIRT, DIRT, DIRT, DIRT, DIRT, MNTN, DIRT, DIRT, DIRT, DIRT]

    map_40x40 = [
        one_mtn + one_mtn,
        no_mtn_a + one_mtn,
        no_mtn_a + no_mtn_b,
        no_mtn_b + one_mtn,
    ]*4

    my_map = map_40x40

    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(my_map)

    the_map = board_map.BoardMap("Test map", my_map, BLACK)


    screen = pygame.display.set_mode([worldx,worldy])
    backdrop = pygame.image.load(os.path.join(os.path.join(RES, "bg_test.png"))).convert()
    backdropbox = screen.get_rect()
    player = PlayerTest()   # spawn player
    player.rect.x = 0
    player.rect.y = 0
    player_list = pygame.sprite.Group()
    player_list.add(player)
    steps = 10      # how fast to move

    # Cursor init
    pygame.mouse.set_cursor(*pygame.cursors.broken_x)
    cursor_xy = None

    '''
    Main loop
    '''
    looping = True
    while looping:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
                looping = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    player.control(-steps,0)
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    player.control(steps,0)
                if event.key == pygame.K_UP or event.key == ord('w'):
                    print('jump')

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    player.control(steps,0)
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    player.control(-steps,0)
                if event.key == ord('q'):
                    pygame.quit()
                    sys.exit()
                    looping = False

        new_xy = pygame.mouse.get_pos() 
        if new_xy != cursor_xy:
            cursor_xy = new_xy
            print(cursor_xy)
            cursor_icon

    #    screen.fill(BLACK)
        screen.blit(backdrop, backdropbox)
        the_map.draw(screen)
        player.update()
        player_list.draw(screen) #refresh player position
        pygame.display.flip()
        clock.tick(fps)


    return


if __name__ == "__main__":
    main()