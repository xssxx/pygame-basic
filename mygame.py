import sys, pygame
pygame.init()

size = width, height = 800, 600
posX = 350
posY = 400
move = 0.2

screen = pygame.display.set_mode(size)

bg = pygame.image.load("bg.gif")
zombie = pygame.image.load("zombie.png")
zombie_small = pygame.transform.scale(zombie, (120, 100))

jumping = False

y_gravity = 1
jump_height = 10
y_velocity = jump_height

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and posX > 0:
        posX -= move
    if keys[pygame.K_RIGHT] and posX < 600:
        posX += move
    if keys[pygame.K_SPACE]:
        jumping = True

    if jumping:
        posY -= y_velocity
        y_velocity -= y_gravity
        if y_velocity < -jump_height:
            jumping = False
            y_velocity = jump_height

    screen.blit(bg,(0,0))
    screen.blit(zombie_small, (posX,posY))
    pygame.display.update()

