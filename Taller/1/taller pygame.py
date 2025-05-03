import pygame
from juego player import*
displayWidth = 760
displayHeight = 420

FPS=32

pygame.init()
def main():
    displayFlag = True


    frame = pygame.display.set_mode((displayWidth,displayHeight))
    pygame.display.set_caption("Game")
    clock = pygame.time.Clock()

    while displayFlag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                displayFlag= False

            if gameScreen.flag:
                gameScreen.events(event)

            if gameScreen.flag:
                gameScreen._update_()
                gameScreen._draw_()

    pygame.display.flip()
    clock.tick(FPS)

main()
pygame.quit()
