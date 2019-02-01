from state import State
from renderer import Renderer
import pygame

cell_size = 50
state = State(10, 10, 10)
renderer = Renderer(500, 500, cell_size)

def input_callback(state):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()

            row = mouse_pos[1] // cell_size
            col = mouse_pos[0] // cell_size

            print(row,col)

            state.no_mine(row, col)

while True:
    input_callback(state)
    renderer.render(state)
