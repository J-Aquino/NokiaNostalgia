import pygame
import time
import random
#initializes game
pygame.init()

#handles the redraw of what happens in the game map

pygame.display.set_caption('Learning Game Development by Justin Aquino original concept by Edureka')
#flag to display state of game
gameOver = False

#game map characteristics
white = (255, 255, 255)
grey = (128, 128, 128)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 102)
aqua = (0, 128, 128)

display_width = 600
display_height = 400
border = 10

#game window
display = pygame.display.set_mode((display_width,display_height))
font_style = pygame.font.SysFont("bahnschrift",25)
score_font = pygame.font.SysFont("comicsansms",35)
clock = pygame.time.Clock()

#snake characteristics
snake_block = 10
green = (0, 255, 0)
snake_speed = 15

def snake(snake_block, snake_list):
	for x in snake_list:
		pygame.draw.rect(display, green, [x[0], x[1], snake_block, snake_block])

def score(score):
	value = score_font.render("Your Score is: " + str(score), True, yellow)
	display.blit(value, [0, 0])


def message(msg, color):
	mesg = font_style.render(msg, True, color)
	display.blit(mesg, [display_width/6, display_height/3])

def gameLoop():
	gameOver = False
	gameClose = False
	#starting player coordinates on game map
	x1 = display_width/2
	y1 = display_height/2
	x1_change = 0
	y1_change = 0

	snake_list = []
	snakeLength = 1

	#food location 
	foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
	foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

	while not gameOver:

		while gameClose == True:
			display.fill(aqua)
			message("You Lose! Press Q-quit or C-play again", red)
			score(snakeLength - 1)
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameOver = True
						gameClose = False
					if event.key == pygame.K_c:
						gameLoop()

		for event in pygame.event.get():
		#Player quit event
			if event.type == pygame.QUIT:
				gameOver = True
		#searches to see if keys are being pressed down 
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x1_change = -snake_block
					y1_change = 0
				elif event.key == pygame.K_RIGHT:
					x1_change = snake_block
					y1_change = 0
				elif event.key == pygame.K_UP:
					x1_change = 0
					y1_change = -snake_block
				elif event.key == pygame.K_DOWN:
					x1_change = 0
					y1_change = snake_block
		
		if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
			gameClose = True

		x1 += x1_change
		y1 += y1_change
		display.fill(grey)
		#drawing of food
		pygame.draw.rect(display,blue,[foodx,foody,snake_block,snake_block])		
		snakeHead = []
		snakeHead.append(x1)
		snakeHead.append(y1)
		snake_list.append(snakeHead)

		if len(snake_list) > snakeLength:
			del snake_list[0]

		for x in snake_list[:-1]:
			if x == snakeHead:
				gameClose = True

		snake(snake_block, snake_list)
		score(snakeLength - 1)
		#updates the display to show movement/actions taking place
		pygame.display.update()

		if x1 == foodx and y1 == foody:
			foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
			foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
			snakeLength += 1
		clock.tick(snake_speed)



	pygame.quit()
	quit()


gameLoop()