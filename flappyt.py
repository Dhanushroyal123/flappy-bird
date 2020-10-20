import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

birdImg = pygame.image.load(r'E:\Programming\Python\Gaming in python\Flappy bird\bird.png')

pipeImg = pygame.image.load(r'E:\Programming\Python\Gaming in python\Flappy bird\pipe3.jpg')

pipex, pipey, pipe_change = 600, 0, 0

pipex1, pipey1 = 600, 389

rectX, rectY, rectW, rectH, rect_change = 100, 200, 64, 64, 0 

birdx, birdy, bird_change = 100, 200, 0

clock = pygame.time.Clock()

FPS = 900 

def pipe(x, y):
	screen.blit(pipeImg, (x, y))

def pipe2(x, y):
	screen.blit(pipeImg, (x, y))

def bird(x, y):
	screen.blit(birdImg, (x, y))

running = True

while running:
	clock.tick(FPS)
	screen.fill((0, 255, 255))
	if pipex<-64:
		pipex, pipex1 = 799, 799
	pipe_change = -0.6
	for event in pygame.event.get():
		bird_change, rect_change = 0.4, 0.4
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				bird_change, rect_change = -0.3, -0.3
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				bird_change, rect_change = 0.4, 0.4
	birdy+=bird_change
	rectY+=rect_change
	#print('rectY : ',rectY)
	pipex+=pipe_change
	pipex1+=pipe_change
	#print('pipex : ',pipex)
	bird(birdx, birdy)
	pygame.draw.rect(screen, (0, 255, 255), (rectX, rectY, rectW, rectH), 2)
	pipe(pipex, pipey)
	pipe2(pipex1, pipey1)
	if (int(birdy)<200 and int(pipex) == 164) or ():
		running = False
	pygame.display.update()

