import pygame
from Player import Player as p
from Bullet import Bullet
from Enemy import Enemy
from pygame import mixer
import random


class SpaceInvaderManager:

    player = p()
    allSprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    enemySpawnTime = 5.0
    numberToSpawn = 5
    score = 0
    explosionSound = mixer.Sound('data/explosion.wav')

    def __init__(self) -> None:
        self.allSprites.add(self.player)
        pygame.mixer.init()

    def AddBullet(self, b:Bullet):
        self.bullets.add(b)
        self.allSprites.add(b)

    def AddEnemy(self, e:Enemy):
        self.enemies.add(e)
        self.allSprites.add(e)
    
    def GetAllSprite(self)->pygame.sprite.Group:
        return self.allSprites
    
    def UpdateScore(self, multiplier:int):
        self.score += (Enemy.value * multiplier)
    
    def GetScore(self)->int:
        return self.score

    def RemoveBullet(self, b:Bullet):
        self.bullets.remove(b)
        self.allSprites.remove(b)
        del b

    def RemoveEnemy(self, e:Enemy):
        self.enemies.remove(e)
        self.allSprites.remove(e)
        del e

    def GetSpawnInterval(self)->float:
        return self.enemySpawnTime
    
    def FireBullet(self):
        self.AddBullet(self.player.FireBullet())

    def MoveBullets(self):
        for b in self.bullets:
            b.Move()
            if(b.yCurrentLoc < 0 or b.yCurrentLoc > 600):
                self.RemoveBullet(b)

    def SpawnEnemies(self):

        for i in range(self.numberToSpawn):
            spawnLocX = random.random()*800
            tempEnemy = Enemy()
            tempEnemy.xCurrentLoc = spawnLocX
            
            if random.random() < .5:
                tempEnemy.direction = -1
            else:
                tempEnemy.direction = 1

            self.AddEnemy(tempEnemy)

    def MoveAllEnemies(self):
        for e in self.enemies:
            e.UpdatePosition()

    def CheckCollisions(self):
        multi = len(pygame.sprite.groupcollide(self.bullets, self.enemies, 1,1).keys())
        self.UpdateScore(multi)
        if(multi):
            self.explosionSound.play()

        if pygame.sprite.spritecollideany(self.player, self.enemies):
            quit()
                
