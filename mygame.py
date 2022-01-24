import pygame
import sys

pygame.init()

#initialisation
WIDTH = 800
HEIGHT = 600
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BG = (144, 201, 120)
clock = pygame.time.Clock()
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Naruto-Ramen') #caption

#player_movement_variables
moving_left = False
moving_right = False

bullet_img = pygame.image.load('bullet.png').convert_alpha()

def draw_bg():
	screen.fill(BG)


class Player(pygame.sprite.Sprite):
	def __init__(self, x, y, scale, speed):
		pygame.sprite.Sprite.__init__(self)
		
		self.speed = speed
		self.direction = 1
		self.flip = False
		img = pygame.image.load('naruto.png')
		self.image = pygame.transform.scale(img,(int(img.get_width() * scale),int(img.get_height() * scale)))
		self.rect = self.image.get_rect()
		self.rect.center = (x,y)
	
	def move(self, moving_left, moving_right):
		#reset movement variables
		dx = 0
		dy = 0

		if moving_left:
			dx = -self.speed
			self.flip = True
			self.direction = -1

		if moving_right:
			dx = self.speed
			self.flip = False
			self.direction = 1

		self.rect.x += dx
		self.rect.y += dy


		

	def draw(self):
		screen.blit(pygame.transform.flip(self.image, self.flip, False),self.rect)

class Bullet(pygame.sprite.Sprite):
	def __init__(self,x,y,direction):
		pygame.sprite.Sprite.__init__(self)
		self.speed = 10
		self.image = bullet_img
		self.rect = self.image.get_rect()
		self.rect.center = (x,y)
		self.direction = direction




bullet_group = pygame.sprite.Group()
player = Player(420,540,1,5)
 





#naruto_img = pygame.image.load('naruto.png').convert()
# rect = naruto_img.get_rect()
# rect.center = WIDTH//2 , HEIGHT//2

# background = pygame.image.load('background.jpg')
# backgroundimg = screen.get_rect()

game_over = False

while not game_over:

	clock.tick(FPS)
	draw_bg()
	player.draw()
	player.move(moving_left, moving_right)
	
	bullet_group.update()
	bullet_group.draw(screen)


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				moving_left = True
			if event.key == pygame.K_d:
				moving_right = True
	
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_a:
				moving_left = False
			if event.key == pygame.K_d:
				moving_right = False
	

	# screen.blit(background,backgroundimg)
	# player_list.draw(screen)
	pygame.display.update()
	clock.tick(60)