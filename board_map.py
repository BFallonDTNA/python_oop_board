


import pygame

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

        self.tiles = list()
        for x, row in enumerate(land_grid):
            for y, land in enumerate(row):
                self.tiles.append(Tile(x, y, land, border))

    def draw(self, screen):
        for tile in self.tiles:
            tile.draw(screen)

class Hexa(object):
    def __init__(self):
        # Shape of hex
        self.edge = 40
        self.height = self.edge * 2
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

    def __init__(self, x, y, land, border):
        hexa = Hexa()
        self.corners = hexa.get_corners(x, y)
        self.center = hexa.get_center(x, y)
        self.land = land
        self.border = border # color

    def draw(self, screen):
        pygame.draw.polygon(screen, self.land.color, self.corners)
        pygame.draw.polygon(screen, self.border, self.corners, 5)


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




