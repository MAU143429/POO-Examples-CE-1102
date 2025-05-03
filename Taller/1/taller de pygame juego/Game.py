import pygame

pygame.init()

class Player:
    def __init__(self,x,y):
        self. rect= pygame.Rect(x,y,64,64)
        self.action = "standing"
        self.direction="right"
        self.falling= False
        self.jump= 0

   #movimiento
    def _update_(self):
        if self.action == "walking":
            if self.direction== "left":
                self.rect.left -= 10

            elif self.direction == "right":
                self.rect.right +=10

            #movimiento y gravedad

            if self.falling and self.jump <= 0:
                self.rect.top +=5
            elif self.jump > 0:
                self.rect.top -= 5
                self.jump -= 5


        def _draw_(self,frame):
            pygame.draw.rect(frame,(255,0,0),self.rect)

class Gamescreen:
    def __init__(self,frame):
        self.frame = frame
        self.player = Player(10,10)
        self.flag = True

    def _update_(self):
        
        self.player:_update_()

    def _draw_(self):
        self.frame.fill((0,255,0))
        self.player._draw_(self.frame)

    def event(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.player.action= "walking"
                self.player.direction = "left"
            if event.key == pygame.K_RIGHT:
                self.player.action= "walking"
                self.player.direction = "right"

    def event(self,event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.player.action= "standing"
                self.player.direction = "left"
            if event.key == pygame.K_RIGHT:
                self.player.action= "standing"
                self.player.direction = "right"

                






pygame.quit()
