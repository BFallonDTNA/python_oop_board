


import pygame

from board import palette


class BoardMap(object):
    """
    Used to define the layout of a board

    Attributes:
    
    Methods:

    """

    def __init__(self, name, land_grid, border):
        """
        Needs a name
        """
        self.name = name

        self.compass = Compass()

        self.tiles = dict()
        for y, row in enumerate(land_grid):
            for x, land in enumerate(row):
                self.tiles[(x,y)] = Tile(x, y, land, self.compass)

        self.tile_hover = self.tiles[(0,0)]
        self.tile_active = None

    def draw(self, screen):
        for xy, tile in self.tiles.items():
            if not tile is self.tile_hover:
                tile.draw(screen)
        self.tile_hover.draw(screen)
        

    def update_cursor(self):
        print("updating_map cursor")

        cursor_xy = pygame.mouse.get_pos()
        xy = self.compass.get_tile_xy(cursor_xy)

        tile_hovering = self.tiles[xy]
        if tile_hovering != self.tile_hover:
            self.tile_hover.set_hover(False)
            self.tile_hover = tile_hovering
            self.tile_hover.set_hover(True)




class Hexa(object):
    def __init__(self, compass):
        self.compass = compass

        # Shape of hex
        self.edge = self.compass.tile_size/2
        self.height = self.compass.tile_size
        self.width = (3**0.5)/2 * self.height

        # Grid spacing
        self.vert = self.height * 3/4
        self.horiz = self.width

        self.shape_points = (
            (0, self.height/4),
            (self.width/2, 0),
            (self.width, self.height/4),
            (self.width, 3*self.height/4),
            (self.width/2, self.height),
            (0, 3*self.height/4),
        )

    def get_corners(self, tile_x, tile_y):
        corners = list()
        for coord in self.shape_points:
            x_offset = self.horiz/2 if tile_y%2 else 0
            corners.append((
                coord[0] + tile_x*self.horiz + x_offset,
                coord[1] + tile_y*self.vert
                ))
        return corners

    def get_center(self, tile_x, tile_y):
        x_offset = self.horiz/2 if tile_y%2 else 0
        center = (
            tile_x*self.horiz + x_offset + self.width/2,
            tile_y*self.vert + self.height/2
            )
        return center


class Tile(object):
    """
    Carries information about a location on the board

    What buildings, dudes are on it
    What are the neighboring locations

    Attributes:
    
    Methods:

    """

    def __init__(self, x, y, land, compass):
        self.compass = compass
        self.corners = self.compass.hexa.get_corners(x, y)
        self.center = self.compass.hexa.get_center(x, y)
        self.land = land
        self.border = palette.BLACK
        self.border_width = 4
        self.hover = False

    def draw(self, screen):
        pygame.draw.polygon(screen, self.land.color, self.corners)
        pygame.draw.polygon(screen, self.border, self.corners, self.border_width)

    def set_hover(self, is_hover):
        self.hover = is_hover

        print("hover")

        if self.hover:
            self.border_width = 8
        else:
            self.border_width = 4

class Land(object):
    """
    Defines what type of place we are at and what it looks like

    Attributes:
    
    Methods:

    """

    def __init__(self, name, color):
        """
        Needs a name
        """
        self.name = name
        self.color = color


class Compass(object):
    """
    Handles things like zooming and mapping pixes to tiles
    """

    def __init__(self):
        self.tile_size = 128
        self.hexa = Hexa(self)

    def get_tile_xy(self, cursor_xy):
        y = int(cursor_xy[1]/self.hexa.vert)
        if y & 1:
            offset = self.hexa.horiz/2
        else:
            offset = 0
        x = int((cursor_xy[0] - offset)/self.hexa.horiz)
        
        return (x,y)
