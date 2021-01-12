# This is a tutorial from freeCodeCamp.org that can be followed
# in the link provided in the readme
import pygame

# initialize the pygame
pygame.init()

# Creation of screen
screen = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('battleship.png')
pygame.display.set_icon(icon)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))