import pygame,sys
from pygame.locals import *
pygame.init()
pygame.display.set_caption("First Program")
screen = pygame.display.set_mode((640,380))
xpos=50
clock = pygame.time.Clock()

while 1:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	pressed_keys= pygame.key.get_pressed()
#	print(type(pygame.key.get_pressed()))
	if pressed_keys[K_RIGHT]:
		xpos+=5
	if pressed_keys[K_LEFT]:
		xpos-=5
	screen.fill((233,133,255))
#print(pygame.key.get_pressed())
	pygame.draw.circle(screen,(0,244,0),(xpos,200),20)
	pygame.display.update()
