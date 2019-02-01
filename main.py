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

            if event.button == 1:
                state.no_mine(row, col)
                state.check_for_win()
            elif event.button == 3:
                state.flag_cell(row, col)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_r:
                state.start_game()

while True:
    input_callback(state)
    renderer.render(state)
