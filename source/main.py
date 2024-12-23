import pygame
import sys

import Scripts.generateLevel





class Game:

    def __init__(self):
        
        pygame.init()

        # -----  Game vars  ----- #
        # Clock stuff
        self.clock = pygame.time.Clock()
        self.fps_options = {
            "30" : 30,
            "60" : 60
        } 
        self.DEFAULT_FPS = self.fps_options["60"]
        self.fps = self.DEFAULT_FPS


        # Screen stuff
        self.resolutions = {
            "1280x720" : (1280, 720),    # 720p
            "1920x1080" : (1920, 1080),  # 1080p
            "2560x1440" : (1560, 1440),  # 1440p
            "3840x2160" : (3840, 2160)   # 4k
        }
        self.DEFAULT_RESOLUTION = self.resolutions["1280x720"]
        self.resolution = self.DEFAULT_RESOLUTION
        

        # Screen defined
        self.SCREEN = pygame.display.set_mode((self.resolution))
        pygame.display.set_caption("War Strats ONG FRFR")      # DISPLAY WINDOW CAPTION, CHANGE TO GAME TITLE


        # Fonts
        self.game_fonts = {
            "Awake" : "gerd/source/Assets/Fonts/Awake.ttf",
            "Wacky Pixels" : "gerd/source/Assets/Fonts/Wacky Pixels"
        }



    def main_game_loop(self):

        # Main game loop
        self.mainloop = True

        while self.mainloop == True:

            self.dt = self.clock.tick(self.fps) / 1000.0 # Define Delta-Time

            # Initial renders
            self.SCREEN.fill((20, 20, 20)) # Fill the first display layer with dark grey

            # Make fps display go brrrrr
            fps_text = pygame.font.Font(self.game_fonts["Awake"], 40).render(f"{round(self.clock.get_fps())}", True, (0, 100, 0))
            self.SCREEN.blit(fps_text, (10, 10))


            # Mainloop function calls
            self.handle_event()


            pygame.display.update()
    


    def handle_event(self):

        for event in pygame.event.get():

            # Handle quit event
            if event.type == pygame.QUIT:

                self.quit_game()



    def quit_game(self):

        pygame.quit()
        sys.exit()





if __name__ == "__main__":

    game = Game()
    game.main_game_loop()