from enum import Enum

class Colour(Enum):
    VISIBLE = (100,100,100)
    NOT_VISIBLE = (150,150,150)
    NEIGHBOURING_MINES = [(0,0,255),    #Blue
                        (0,255,0),     #Green
                        (255,0,0),     #Red
                        (255,0,255),   #Purple
                        (0,0,0),       #Black
                        (128,0,0),     #Maroon
                        (50,50,50), #Gray
                        (64,224,208)   #Turqouise
            ]
