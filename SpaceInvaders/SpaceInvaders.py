import pygame
from SIManager import SpaceInvaderManager
import time
from pygame import mixer


# initializing pygame
pygame.init()

SIM = SpaceInvaderManager()

# creating screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# caption
pygame.display.set_caption("Welcome to Space Invaders Game -- Lets Protect Earth")

# Background Music
mixer.music.load('data/background.wav')
mixer.music.play(-1)




#Score Variables and function
scoreX = 5
scoreY = 5
font = pygame.font.Font('freesansbold.ttf', 20)

def show_score():
	score = font.render("Points: " + str(SIM.GetScore()),
						True, (255,255,255))
	screen.blit(score, (scoreX, scoreY))

running = True

startTime = time.time()

while running:

	screen.fill((0, 0, 0))  

	#Get Events
	for event in pygame.event.get():
		#Quit Game
		if event.type == pygame.QUIT:
			running = False
		#FireBullet
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				SIM.FireBullet()

	#Movement Keys Pressed
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		SIM.player.MoveX(-1)
	if keys[pygame.K_RIGHT]:
		SIM.player.MoveX(1)

	endTime = time.time()

	if  endTime - startTime >= SIM.GetSpawnInterval():
		SIM.SpawnEnemies()
		startTime = time.time()


	SIM.MoveBullets()
	SIM.MoveAllEnemies()
	SIM.CheckCollisions()

	for s in SIM.GetAllSprite():
		screen.blit(s.GetImage(), s.GetCurrentLocation() )

	show_score()
		
	pygame.display.update()
