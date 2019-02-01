import pygame

class ResourceHandler:
    def __init__(self):
        self.resource_dict = {}
        self.current_res_handle = 0

    def add_resource(self, path):
        self.resource_dict[self.current_res_handle] = pygame.image.load(path)
        self.current_res_handle += 1
        return self.current_res_handle - 1

    def get_resource(self, handle):
        return self.resource_dict[handle]
