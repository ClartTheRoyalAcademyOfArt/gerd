import pygame




class RenderLevel:

    def __init__(self, game:object, level_grid:list):
        
        self.game = game
        self.level_grid = level_grid

        self.CELL_SIZE = 40



    def render_level(self):
        
        for row_idx, row in enumerate(self.level_grid):

            for col_idx, color in enumerate(row):

                x = col_idx * self.CELL_SIZE
                y = row_idx * self.CELL_SIZE

                pygame.draw.rect(self.game.SCREEN, color, (x, y, self.CELL_SIZE, self.CELL_SIZE))