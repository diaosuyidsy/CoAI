import sys

import pygame

white = 255, 255, 255


class App:

    def __init__(self):
        self._running = True
        self._screen = None
        self.player = None
        self.size = self.weight, self.height = 1200, 1200
        self.player_pos = [0, 0]
        self.player_mr, self.player_ml, self.player_mu, self.player_md = False, False, False, False

    def on_init(self):
        pygame.init()
        self._screen = pygame.display.set_mode(self.size)
        self._running = True
        self.player = pygame.image.load("Main.png")

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.player_mr = True
            if event.key == pygame.K_a:
                self.player_ml = True
            if event.key == pygame.K_w:
                self.player_mu = True
            if event.key == pygame.K_s:
                self.player_md = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.player_mr = False
            if event.key == pygame.K_a:
                self.player_ml = False
            if event.key == pygame.K_w:
                self.player_mu = False
            if event.key == pygame.K_s:
                self.player_md = False

    def on_loop(self):
        if self.player_mr:
            self.player_pos[0] += 0.01
        if self.player_ml:
            self.player_pos[0] -= 0.01
        if self.player_mu:
            self.player_pos[1] -= 0.01
        if self.player_md:
            self.player_pos[1] += 0.01

    def on_render(self):
        self._screen.fill(white)
        self._screen.blit(
            self.player, (self.player_pos[0] * 50, self.player_pos[1] * 50))
        pygame.display.flip()

    def on_cleanup(self):
        sys.exit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
