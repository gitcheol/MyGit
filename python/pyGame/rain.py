import pygame, sys,random, time
from pygame.locals import *

class Raindrop:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.speed=random.randint(5,18)

    def move(self):
        self.y+=self.speed

    def draw(self):
        pygame.draw.line(screen,(0,0,0),(self.x,self.y),(self.x,self.y+5),1)

    def off_screen(self):
        return self.y>800

class Hahee:
	def __init__(self):
		self.x=300
		self.y=400
	def draw(self):
		screen.blit(mike_umbrella_image,(self.x,self.y))
	def hit_by(self,raindrop):
		return pygame.Rect(self.x,self.y,170,192).collidepoint((raindrop.x,raindrop.y))

class Cloud:
    def __init__(self):
        self.x=300
        self.y=50
    def draw(self):
        screen.blit(cloud_image,(self.x,self.y))
    def rain(self):
        raindrops.append(Raindrop(random.randint(self.x,self.x+300),self.y+100))
    def move(self):
        if pressed_keys[K_RIGHT]:
            self.x+=5
        if pressed_keys[K_LEFT]:
            self.x-=5
    def hit_by(self,raindrop):
        return pygame.Rect(self.x,self.y,170,192).collidepoint((raindrop.x,raindrop.y))
			  
pygame.init()
pygame.display.set_caption("rain")
screen = pygame.display.set_mode((1000,600))
clock = pygame.time.Clock()
#rain_y=0
#rain_x=random.randint(0,1000)
raindrop_spawn_time=0
raindrops=[]
hahee_image=pygame.image.load("/Users/gichulkim/Downloads/Mike.png").convert()
mike_umbrella_image=pygame.image.load("/Users/gichulkim/Downloads/Mike_umbrella.png").convert()

cloud_image=pygame.image.load("/Users/gichulkim/Downloads/cloud.png").convert()
hahee=Hahee()
cloud=Cloud()


while 1:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
	pressed_keys=pygame.key.get_pressed()	
	#raindrops.append(Raindrop()) 
	screen.fill((255,255,255))
	hahee.draw()
	cloud.draw()
	cloud.rain()
	cloud.move()
	#rain_y+=4
	#pygame.draw.line(screen,(0,0,0),(rain_x,rain_y),(rain_x,rain_y+5),1)
	'''
	for raindrop in raindrops:
		raindrop.move()
		raindrop.draw()
	'''
	i=0
	while i<len(raindrops):
		raindrops[i].move()
		raindrops[i].draw()
		if raindrops[i].off_screen() or hahee.hit_by(raindrops[i]):
			del raindrops[i]
			i-=1
		i+=1
	pygame.display.update()


