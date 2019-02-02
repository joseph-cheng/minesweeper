import pygame
from colour import Colour
from resource_handler import ResourceHandler

class Renderer:
    def __init__(self, w, h, cell_size):
        self.w = w
        self.h = h

        self.cell_size = cell_size
        self.screen = pygame.display.set_mode((w,h))

        self.resource_handler = ResourceHandler()
        self.flag_res = self.resource_handler.add_resource("res\\flag.png")
        self.cell_res = self.resource_handler.add_resource("res\\cell.png")

        pygame.font.init()
        self.font = pygame.font.SysFont("Consolas", 15)

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
                    self.screen.blit(self.resource_handler.get_resource(self.cell_res), cell_coords)
                    
                    
                    if [row,col] in state.flags:
                        self.screen.blit(self.resource_handler.get_resource(self.flag_res), cell_coords)
        
        pygame.display.flip()
                    
