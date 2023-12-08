import pygame

class Enemy(pygame.sprite.Sprite):

    value = 100

    def __init__(self):
        super().__init__()
        self.enemyImage = pygame.image.load('data/alien.png')
        self.rect = self.enemyImage.get_rect()
        self.xCurrentLoc = 0
        self.yCurrentLoc = 0
        self.xSpeed = .25
        self.ySpeed = 50
        self.direction = 0
        
        
    def __del__(self):
        pass

    def UpdatePosition(self):
        self.xCurrentLoc += self.xSpeed * self.direction
        if self.xCurrentLoc <= 20 or self.xCurrentLoc >= 750:
            self.yCurrentLoc += self.ySpeed
            self.direction *= -1

        self.rect.center = self.GetCurrentLocation()

    def GetImage(self):
        return self.enemyImage
    
    def GetCurrentLocation(self) -> tuple[int, int]:
        return (self.xCurrentLoc, self.yCurrentLoc)