import pygame
from colour import Colour

class Renderer:
    def __init__(self, w, h, cell_size):
        self.w = w
        self.h = h

        self.cell_size = cell_size
        
        self.screen = pygame.display.set_mode((w,h))

        self.font = pygame.font.SysFont("Consolas", 10)

    def render(self, state):

        self.screen.fill((255,255,255))
        
        for row in range(state.h):
            for col in range(state.w):
                
                cell_coords = (cell_size * col, cell_size * row, cell_size, cell_size)

                if state.visible_board[row][col]:
                    pygame.draw.rect(self.screen,
                                     Colour.VISIBLE,
                                     cell_coords
                                     )
                    pygame.draw.rect(pygame.draw.rect(self.screen,
                                     (0,0,0),
                                     cell_coords,
                                     1))
                    
                    if state.board[row][col] > 0:
                        text = self.font.render(str(state.board[row][col]), True, Colour.NEIGHBOURING_MINES[state.board[row][col]-1])
                        screen.blit(text, cell_coords)
                        
                else:
                    pygame.draw.rect(self.screen,
                                     Colour.NOT_VISIBLE,
                                     cell_coords
                                     )
                    pygame.draw.rect(pygame.draw.rect(self.screen,
                                     (0,0,0),
                                     cell_coords,
                                     1))
                    
                    
