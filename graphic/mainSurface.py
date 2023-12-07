import pygame
import pygame_menu
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import *

from graphic.interface import Interface
from graphic.cameraController import CameraController
from graphic.eventController import EventController
from graphic.test_menu import GameMenu

class MainSurface:

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(music_path + "2-15. Crossing the Iron Bridge.flac")
        pygame.mixer.music.play(-1,0.0)

        # Création de la fenêtre
        self.window = pygame.display.set_mode(window_size, pygame.RESIZABLE)
        self.window.fill("black")

        pygame.display.set_caption("Game Of Life")

        # clock pour la gestion des FPS
        self.clock = pygame.time.Clock()

        # surface du jeu, toute la map
        self.game_surface = Interface(screen_size)

        self.camera = CameraController(self.game_surface)

        self.menu=GameMenu(self.window)

        self.event_controller = EventController(self.camera, self.menu)
        
        self.menu.main_menu.enable()
        #self.menu.to_print("main_menu")
        

    def run(self, map):
        current_tick = 1
        while(current_tick < max_framerate):
            self.event_controller.run_events()
            
            if self.menu.main_menu.is_enabled():
                self.menu.main_menu.draw(self.window)

            # Implémenter les ticks
            if self.menu.main_menu.get_current() == self.menu.game_screen:
                self.game_surface.render_game(map, current_tick)
                self.window.blit(self.camera.get_viewpoint(), (0,0))
                self.menu.game_screen.draw(self.window)
        
            pygame.display.flip()

            self.clock.tick(max_framerate)
            current_tick += 1  


if __name__ == '__main__':
    carte ={}
    MainSurface().run(carte)