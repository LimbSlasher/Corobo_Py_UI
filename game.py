import pygame
import os
import random
from tiles.tile import Tile
from fields.field import Field
import tuio

class Listener(tuio.observer.AbstractListener):

    # Implements a Listener
    def notify(self, event):
        ident = event.object.id
        if ident in g.poses:
            del g.poses[ident]
        x = event.object.xpos
        y = event.object.ypos
        rad = event.object.angle
        pos = [x, y, rad]
        g.poses[ident] = pos

class Game:

    def __init__(self):
        self.width = 1600
        self.height = 900
        # self.NumberOfRows = 13
        # self.NumberOfColumns = 20
        self.win = pygame.display.set_mode((self.width, self.height))
        self.fields = []

        # self.bg = pygame.image.load(
        #     os.path.join('assets', 'bg_default.png'))  # bg picture -> needs to be random in future
        #
        # self.bg = pygame.transform.scale(self.bg, (self.width, self.height))

        self.tiles = {}  # contains every tile on the field
        self.poses = {}  # contains the current poses of every tile on the field


    def run(self):
        '''
        gameloop
        :return: none
        '''
        run = True
        clock = pygame.time.Clock()

        while run:
            clock.tick(60)  # fps = 60
            tuio.tracking.update()  # update for the Tuiolistener
            if len(self.poses) != 0:
                for key in self.poses:
                    temp = self.poses[key]  # the curren pose of the 'key', which is the same as in tiles

                    if key not in self.tiles:  # checks if the tile is already existing if not it'll be created
                        self.create_tile(key, temp[0] * self.width, temp[1] * self.height, temp[2])
                        print('new Tile: ', key)
                    else:
                        self.tiles[key].update(temp[0] * self.width, temp[1] * self.height)
            # print(len(self.poses), self.poses)
            for event in pygame.event.get():  # unused so far maybe later vor mouse or touch input to select level

                if event.type == pygame.QUIT:
                    run = False

            self.draw()
        pygame.quit()

    def draw(self):
        '''
        draws the field
        :return: none
        '''
        self.win.fill([255, 255, 255])
        # self.drawField()
        # self.win.blit(self.bg, (0, 0))
        '''
        redraw every tile every tick. Tile.draw(local window)
        '''
        for k, v in self.tiles.items():
            temp_tile = v
            temp_tile.draw(self.win)

        pygame.display.update()

    listener = Listener("Event Listener", tuio.getEventManager())

    def create_tile(self, name, pos_x, pos_y, rot):
        '''
        crates new instance of class Tile and adds ot to the tiles dict.
        :param name: ident of tile
        :param pos_x: float
        :param pos_y: float
        :param rot: int
        :return: none
        '''
        ident = Tile(name, pos_x, pos_y, rot)
        self.tiles[name] = ident


g = Game()
g.run()
