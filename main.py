# This is a tutorial from freeCodeCamp.org that can be followed
# in the link provided in the readme
import pygame
import random
# initialize the pygame
pygame.init()

# Creation of screen
screen = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('battleship.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('battleshipPlayer.png')
playerX = 385
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 0

def player(x, y):
    # blit is basically equivalent to draw
    screen.blit(playerImg, (playerX, playerY))

def enemy(x, y):
    screen.blit(enemyImg, (enemyX, enemyY))

# Game loop
running = True
while running:
    # Option to change the background of the screen
    screen.fill((187, 255, 173))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = +0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    # Update the display
    pygame.display.update()
