# -*- coding: utf-8 -*-
DIRECTIONS = [0, 45, 90, 135, 180, 225, 270, 315]
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640


NORTH = 0
NORTHEAST = 1
EAST = 2
SOUTHEAST = 3
SOUTH = 4
SOUTHWEST = 5
WEST = 6
NORTHWEST = 7


PLAYER_SPEED = 2

COLOR = 0
BARREL = 1

BLUE = 0
DARK = 1
GREEN = 2
RED = 3
SAND = 4

TILE_GRASS_TYPE1 = 0
TILE_GRASS_TYPE2 = 1
TILE_SAND_TYPE1 = 2
TILE_SAND_TYPE2 = 3

START_X = 0
START_Y = 0

# MAPS
SAND_RIVER = [1, 0, 1, 0, 1, 0, 1, 0, 1, 2,
              0, 1, 0, 1, 0, 1, 0, 1, 0, 3,
              1, 3, 2, 0, 1, 0, 1, 0, 2, 3,
              0, 2, 3, 1, 0, 1, 0, 3, 2, 3,
              1, 0, 1, 0, 1, 0, 1, 2, 3, 2,
              0, 1, 0, 1, 0, 1, 0, 3, 2, 3,
              1, 0, 1, 0, 1, 0, 2, 3, 2, 0,
              0, 1, 0, 1, 0, 3, 2, 3, 0, 1,
              1, 0, 1, 0, 0, 2, 3, 2, 1, 0,
              0, 1, 0, 1, 3, 2, 3, 1, 0, 1]
MAP = SAND_RIVER
