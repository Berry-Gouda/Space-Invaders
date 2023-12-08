import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self) -> None:
        super().__init__()
        self.bulletImage = pygame.image.load('data/bullet.png')
        self.rect = self.bulletImage.get_rect()
        self.yCurrentLoc = 0
        self.xCurrentLoc = 0
        self.direction = 0
        self.speed = 1

    def __del__(self):
        pass
        
    def Move(self):
        self.yCurrentLoc += (self.direction*self.speed)
        self.rect.center = self.GetCurrentLocation()

    def GetImage(self):
        return self.bulletImage
    
    def GetCurrentLocation(self) -> tuple[int, int]:
        return (self.xCurrentLoc, self.yCurrentLoc)

