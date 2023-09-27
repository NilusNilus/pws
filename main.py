import os
import pygame

class Game:
    def __init__(self):
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

    def run(self):
        last = pygame.time.get_ticks() / 1e3

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            first = pygame.time.get_ticks() / 1e3
            dt = first - last
            last = first
            
            self.window.blit(pygame.transform.scale(self.display, self.window_size), (0,0))
            pygame.display.flip()

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
Game().run()