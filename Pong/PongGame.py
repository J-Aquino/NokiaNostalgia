import pygame
from Paddles import Paddle
from Ball import Ball

pygame.init()

#Game Colors
olive = (85,107,47)
gold = (218,165,32)
white = (255,255,255)
firebrick = (178,34,34)
grey = (192,192,192)

#Game Map
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Python Pong")

gameActive = True
clock = pygame.time.Clock()

#Player Scores
playerScore1 = 0
playerScore2 = 0
#Paddles

paddleA = Paddle(olive, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(gold, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(firebrick, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

allSprites_list = pygame.sprite.Group()
allSprites_list.add(paddleA)
allSprites_list.add(paddleB)
allSprites_list.add(ball)

while gameActive:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameActive = False
		elif event.type == pygame.K_x:
			gameActive = False
		if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
			while True:
				event = pygame.event.wait()
				if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
					break
		



	#player controls
	keys = pygame.key.get_pressed()
	if keys[pygame.K_w]:
		paddleA.moveUp(5)
	if keys[pygame.K_s]:
		paddleA.moveDown(5)
	if keys[pygame.K_UP]:
		paddleB.moveUp(5)
	if keys[pygame.K_DOWN]:
		paddleB.moveDown(5) 

	allSprites_list.update()

	#ball wall characteristics
	if ball.rect.x >= 690:
		playerScore1 += 1
		ball.velocity[0] = -ball.velocity[0]
	if ball.rect.x <= 0:
		playerScore2 += 1
		ball.velocity[0] = -ball.velocity[0]
	if ball.rect.y >= 490:
		ball.velocity[1] = -ball.velocity[1]
	if ball.rect.y <= 0:
		ball.velocity[1] = -ball.velocity[1]

	if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
		ball.bounce()
      

	screen.fill(grey)
	pygame.draw.line(screen,white, [349, 0],[349,500], 5)
	allSprites_list.draw(screen)
	#Score keeping
	font = pygame.font.Font(None, 74)
	text = font.render(str(playerScore1), 1, white)
	screen.blit(text, (250, 10))
	text = font.render(str(playerScore2), 1, white)
	screen.blit(text, (420, 10))
	pygame.display.flip()
	clock.tick(60)

pygame.quit()
