import pygame
from colour import Colour

class Renderer:
    def __init__(self, w, h, cell_size):
        self.w = w
        self.h = h

        self.cell_size = cell_size
        self.screen = pygame.display.set_mode((w,h))

        pygame.font.init()
        self.font = pygame.font.SysFont("Consolas", 30)

    def render(self, state):

        self.screen.fill((255,255,255))
        
        for row in range(state.h):
            for col in range(state.w):
                
                cell_coords = (self.cell_size * col, self.cell_size * row, self.cell_size, self.cell_size)

                if state.visible_board[row][col]:
                    pygame.draw.rect(self.screen,
                                     Colour.VISIBLE.value,
                                     cell_coords)
                    pygame.draw.rect(self.screen,
                                     (0,0,0),
                                     cell_coords,
                                     1)
                    
                    if state.board[row][col] > 0:
                        text = self.font.render(str(state.board[row][col]), True, Colour.NEIGHBOURING_MINES.value[state.board[row][col]-1])
                        self.screen.blit(text, (self.cell_size*col + (self.cell_size - text.get_width())//2, self.cell_size*row + (self.cell_size - text.get_height())//2))
                        
                else:
                    pygame.draw.rect(self.screen,
                                     Colour.NOT_VISIBLE.value,
                                     cell_coords)
                    
                    pygame.draw.rect(self.screen,
                                     (0,0,0),
                                     cell_coords,
                                     1)
                    if [row,col] in state.flags:
                        pygame.draw.circle(self.screen, (255,0,0), (self.cell_size*col + self.cell_size//2, self.cell_size*row + self.cell_size//2), 10)

        
        pygame.display.flip()
                    
