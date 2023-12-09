
class Ship():
    def __init__(self) -> None:
        self.pix_array = [[0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0]]
                            #hp,def,at,as,ac,ms,sh,en
        self.pix_atributes = [0, 0, 0, 0, 0, 0, 0, 0]
        
        self.player_controled = False
        
        self.velocity = (0, 0)
        self.vector = (0, 0)