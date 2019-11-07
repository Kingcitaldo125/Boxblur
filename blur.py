import time
import pygame
import random
import sys

pygame.display.init()

#surface = pygame.image.load("CircleBlack.PNG")
#surface = pygame.image.load("TriangleBlack.PNG")
#surface = pygame.image.load("bholeimg.jpg")
#surface = pygame.image.load("TerryCrews.jpg")
#surface = pygame.image.load("flowers.jpg")
surface = pygame.image.load(str(sys.argv[1])) # python .\blur.py .\cityscapeclear.jpg


scrnSize = surface.get_rect().size
print("Size:",scrnSize)
print("Press spacebar to blur; Esc to quit.")
screen = pygame.display.set_mode(scrnSize, 0, 32)
winX = scrnSize[0]
winY = scrnSize[1]


def reset(screen):
	screen.fill((255,255,255))
	screen.blit(surface,(0,0))
	screen.set_at((winX, winY),(255,255,255))
	pygame.display.flip()


def blur(screen, rotations=1):
	global winX
	global winY

	for rots in range(rotations):
		avgColor = None
		for i in range(winX-1):
			for j in range(winY-1):
				# Get the Left,Middle,Right of each pixel
				# in the Moore's Neighborhood of the current pixel on the screen
				topLcolor = (0,0,0)
				topMcolor = (0,0,0)
				topRcolor = (0,0,0)
				
				middleLcolor = (0,0,0)
				middleMcolor = (0,0,0)
				middleRcolor = (0,0,0)
				
				bottomLcolor = (0,0,0)
				bottomMcolor = (0,0,0)
				bottomRcolor = (0,0,0)
				
				
				if i == 0 and j == 0:
					middleMcolor = screen.get_at((i, j))
					middleRcolor = screen.get_at((i+1, j))
					
					bottomMcolor = screen.get_at((i, j+1))
					bottomRcolor = screen.get_at((i+1, j+1))
				elif j == 0:
					middleLcolor = screen.get_at((i-1, j))
					middleMcolor = screen.get_at((i, j))
					middleRcolor = screen.get_at((i+1, j))
					
					bottomLcolor = screen.get_at((i-1, j+1))
					bottomMcolor = screen.get_at((i, j+1))
					bottomRcolor = screen.get_at((i+1, j+1))
				elif j == winY:
					topLcolor = screen.get_at((i-1, j-1))
					topMcolor = screen.get_at((i, j-1))
					topRcolor = screen.get_at((i+1, j-1))
					
					middleLcolor = screen.get_at((i-1, j))
					middleMcolor = screen.get_at((i, j))
					middleRcolor = screen.get_at((i+1, j))
				elif i == 0:
					topMcolor = screen.get_at((i, j-1))
					topRcolor = screen.get_at((i+1, j-1))
					
					middleMcolor = screen.get_at((i, j))
					middleRcolor = screen.get_at((i+1, j))
					
					bottomMcolor = screen.get_at((i, j+1))
					bottomRcolor = screen.get_at((i+1, j+1))
				elif i == winX:
					topLcolor = screen.get_at((i-1, j-1))
					topMcolor = screen.get_at((i, j-1))
					
					middleLcolor = screen.get_at((i-1, j))
					middleMcolor = screen.get_at((i, j))
					
					bottomLcolor = screen.get_at((i-1, j+1))
					bottomMcolor = screen.get_at((i, j+1))
				elif i == winX and j == winY:
					topLcolor = screen.get_at((i-1, j-1))
					topMcolor = screen.get_at((i, j-1))
					
					middleLcolor = screen.get_at((i-1, j))
					middleMcolor = screen.get_at((i, j))
				else:
					topLcolor = screen.get_at((i-1, j-1))
					topMcolor = screen.get_at((i, j-1))
					topRcolor = screen.get_at((i+1, j-1))
					
					middleLcolor = screen.get_at((i-1, j))
					middleMcolor = screen.get_at((i, j))
					middleRcolor = screen.get_at((i+1, j))
					
					bottomLcolor = screen.get_at((i-1, j+1))
					bottomMcolor = screen.get_at((i, j+1))
					bottomRcolor = screen.get_at((i+1, j+1))
				
				# Get the average pixel color in the moore's neighborhood
				avgColorR = (topLcolor[0] + topMcolor[0] + topRcolor[0] + \
							middleLcolor[0] + middleMcolor[0] + middleRcolor[0] + \
							bottomLcolor[0] + bottomMcolor[0] + bottomRcolor[0]) / 9
				
				avgColorG = (topLcolor[1] + topMcolor[1] + topRcolor[1] + \
							middleLcolor[1] + middleMcolor[1] + middleRcolor[1] + \
							bottomLcolor[1] + bottomMcolor[1] + bottomRcolor[1]) / 9
							
				avgColorB = (topLcolor[2] + topMcolor[2] + topRcolor[2] + \
							middleLcolor[2] + middleMcolor[2] + middleRcolor[2] + \
							bottomLcolor[2] + bottomMcolor[2] + bottomRcolor[2]) / 9
				
				avgColor = (avgColorR, avgColorG, avgColorB)
				screen.set_at((i, j), avgColor)

	pygame.display.flip()

done = False
pixelArray = []

doBlur = False

reset(screen)
while not done:
	events = pygame.event.get()
	for e in events:
		if e.type == pygame.QUIT:
			done = True
		elif e.type == pygame.KEYDOWN:
			if e.key == pygame.K_SPACE:
				doBlur = True
			if e.key == pygame.K_ESCAPE:
				done = True
	
	if doBlur:
		print("Blurring")
		blur(screen, 6)
		print("Done")
		doBlur = False
	time.sleep(0.5)

pygame.display.quit()
