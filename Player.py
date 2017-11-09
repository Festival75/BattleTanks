# -*- coding: utf-8 -*-
from Constants import *
import pygame


class Player():
    def __init__(self, name):
        self.direction = RIGHT
        self.color = RED
        self.name = name
        self.image_pack = {"BLUE": {"BODY": "data/tank/tankBody_blue.png",
                                    "BARREL_TYPE1": "data/tank/tankBlue_barrel1.png",
                                    "BARREL_TYPE2": "data/tank/tankBlue_barrel2.png",
                                    "BARREL_TYPE3": "data/tank/tankBlue_barrel3.png"},
                           "DARK": {"BODY": "data/tank/tankBody_dark.png",
                                    "BARREL_TYPE1": "data/tank/tankDark_barrel1.png",
                                    "BARREL_TYPE2": "data/tank/tankDark_barrel2.png",
                                    "BARREL_TYPE3": "data/tank/tankDark_barrel3.png"},
                           "GREEN": {"BODY": "data/tank/tankBody_green.png",
                                     "BARREL_TYPE1": "data/tank/tankGreen_barrel1.png",
                                     "BARREL_TYPE2": "data/tank/tankGreen_barrel2.png",
                                     "BARREL_TYPE3": "data/tank/tankGreen_barrel3.png"},
                           "RED": {"BODY": "data/tank/tankBody_red.png",
                                   "BARREL_TYPE1": "data/tank/tankRed_barrel1.png",
                                   "BARREL_TYPE2": "data/tank/tankRed_barrel2.png",
                                   "BARREL_TYPE3": "data/tank/tankRed_barrel3.png"},
                           "SAND": {"BODY": "data/tank/tankBody_sand.png",
                                    "BARREL_TYPE1": "data/tank/tankSand_barrel1.png",
                                    "BARREL_TYPE2": "data/tank/tankSand_barrel2.png",
                                    "BARREL_TYPE3": "data/tank/tankSand_barrel3.png"}
                           }

    def move(self):
        pass

    def render(self):
        pass

    def render_ui(self):
        pass
