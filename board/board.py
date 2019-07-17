import os
import pygame
import random
from .field import Field


class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.NumberOfRows = 13
        self.NumberOfColumns = 20
        self.fields = {}

    def generate_field_array(self):
        '''
        crates new instance of the playarea
        :return: none
        '''

        # go through all board. depending on its position, assign a type
        # type 0: unplayable area - white
        # type 1: roboter position - blue
        # type 2: free field - green
        # type 3: blocked field - red (generated randomly)

        for x in range(self.NumberOfColumns):
            for y in range(self.NumberOfRows):
                # blue robot square
                if 7 < x < 12 and y < 4:  # blue

                    self.generate_rect(x, y, 1)
                # first and second row of playarea
                elif 2 < x < 17 and 5 < y < 8:  # green
                    if random.randrange(1, 100) > 10:
                        self.generate_rect(x, y, 2)

                    else:  # red
                        self.generate_rect(x, y, 3)

                # third row of playarea
                elif 3 < x < 16 and y == 8:  # green
                    if random.randrange(1, 100) > 10:
                        self.generate_rect(x, y, 2)

                    else:  # red
                        self.generate_rect(x, y, 3)

                # fourth row of playarea
                elif 4 < x < 15 and y == 9:  # green
                    if random.randrange(1, 100) > 10:
                        self.generate_rect(x, y, 2)

                    else:  # red
                        self.generate_rect(x, y, 3)

                # fifth row of playarea
                elif 6 < x < 13 and y == 10:  # green
                    if random.randrange(1, 100) > 10:
                        self.generate_rect(x, y, 2)

                    else:  # red
                        self.generate_rect(x, y, 3)

                # area around the playable area
                else:  # white
                    self.generate_rect(x, y, 0)


    def generate_rect(self, x, y, type):
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
        ident = alphabet[x] + str(y)
        temp_field = Field(ident, x, y, type)
        self.fields.update({ident: temp_field})

    def draw_board(self,win):

        red = (255, 0, 0)
        green = (0, 255, 0)
        blue = (0, 0, 255)
        white = (255, 255, 255)
        black = (0, 0, 0)

        for field in self.fields.values():
            if field.type == 1:  # blue
                pygame.draw.rect(win, blue, [field.x_px, field.y_px, field.width, field.height])
                pygame.draw.rect(win, black, [field.x_px, field.y_px, field.width, field.height], 1)
            elif field.type == 2:  # green
                pygame.draw.rect(win, green, [field.x_px, field.y_px, field.width, field.height])
                pygame.draw.rect(win, black, [field.x_px, field.y_px, field.width, field.height], 1)
            elif field.type == 3:  # red
                pygame.draw.rect(win, red, [field.x_px, field.y_px, field.width, field.height])
                pygame.draw.rect(win, black, [field.x_px, field.y_px, field.width, field.height], 1)
            else:  # white
                pygame.draw.rect(win, white, [field.x_px, field.y_px, field.width, field.height])
                pygame.draw.rect(win, black, [field.x_px, field.y_px, field.width, field.height], 1)