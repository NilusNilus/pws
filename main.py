import os
import pygame

from scripts.entities import PhysicsObject 
from scripts.util import load_image

class Game:
    def __init__(self):
        # WINDOW MANAGEMENT
        info_obj = pygame.display.Info()
        
        scale = 0.9
        desktop_size = [info_obj.current_w * scale, info_obj.current_h * scale]
        display_size = [640, 480]
        self.window_size = [0, 0]

        desktop_ratio = desktop_size[0] / desktop_size[1]
        target_ratio = 4/3

        if desktop_ratio > target_ratio:
            self.window_size[0] = int(desktop_size[1] * target_ratio)
            self.window_size[1] = desktop_size[1]
        else:
            self.window_size[0] = desktop_size[0]
            self.window_size[1] = int(desktop_size[0] / target_ratio)

        self.window = pygame.display.set_mode(self.window_size)
        self.display = pygame.Surface(display_size)

        # GAME
        self.player = PhysicsObject(self, "player", (50, 50), (8, 12))
        self.movement = [False, False]

        self.assets = {
            "player": load_image("player.png")
        }

    def run(self):
        last = pygame.time.get_ticks() / 1e3

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False
            
            first = pygame.time.get_ticks() / 1e3
            dt = first - last
            last = first
            self.player.update(dt, (self.movement[1] - self.movement[0], 0))
            
            self.display.fill((100, 100, 100))
            self.player.render(self.display)
            self.window.blit(pygame.transform.scale(self.display, self.window_size), (0,0))
            pygame.display.flip()
        pygame.quit()
        exit(0)

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
Game().run()