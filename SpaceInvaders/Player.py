import pygame
from Bullet import Bullet
from pygame import mixer

class Player(pygame.sprite.Sprite):


    def __init__(self) -> None:
        super().__init__()
        pygame.mixer.init()
        self.playerImage = pygame.image.load('data/spaceship.png')
        self.rect = self.playerImage.get_rect()
        self.xStartLoc = 370
        self.yStartLoc = 523
        self.xCurrentLoc = self.xStartLoc
        self.yCurrentLoc = self.yStartLoc
        self.yBulletSpawnOffset = 30
        self.xBulletSpawnOffset = 15
        self.bulletDirection = -1
        self.bulletSound = mixer.Sound('data/bullet.wav')
        self.speed = .5
        self.MoveX(0)
        

    def MoveX(self, direction:int):
        self.xCurrentLoc += (self.speed * direction)
        #Lock Player to screen
        if self.xCurrentLoc <= -10:
            self.xCurrentLoc = -10
        if self.xCurrentLoc >= 750:
            self.xCurrentLoc = 750

        self.rect.center = self.GetCurrentLocation()

    def FireBullet(self)->Bullet:
        b = Bullet()
        b.xCurrentLoc = self.xCurrentLoc + self.xBulletSpawnOffset
        b.yCurrentLoc = self.yCurrentLoc - self.yBulletSpawnOffset
        b.direction = self.bulletDirection
        self.bulletSound.play()
        return b
    
    def GetImage(self):
        return self.playerImage
    
    def GetCurrentLocation(self) -> tuple[int, int]:
        return (self.xCurrentLoc, self.yCurrentLoc)

