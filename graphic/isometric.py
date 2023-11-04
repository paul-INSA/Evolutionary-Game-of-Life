import numpy as np
from config import *

class Isometric():
    transfer_cart_to_iso = np.array([
            [0.5, -0.5],
            [0.25, 0.25]
        ]) * tile_size
    
    transfer_iso_to_cart = np.linalg.inv(transfer_cart_to_iso)

    @staticmethod
    def apply_x_offset(pos: tuple) -> tuple:
        return pos - (tile_size/2, 0)
    
    @staticmethod
    def cart_to_iso(pos: tuple) -> list:
        return Isometric.transfer_cart_to_iso @ pos
    
    @staticmethod
    def iso_to_cart(pos: tuple) -> list:
        return Isometric.transfer_iso_to_cart @ pos
    
    

if __name__ == '__main__':
    pass