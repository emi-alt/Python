import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
PINK = (167, 6, 204) #constants always in caps
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((111, 91, 194))
    #solid circle
    pygame.draw.circle(screen, PINK, (120, 120), 100)
    #after pink - (x,y), radius


    pygame.draw.circle(screen, PINK, (400, 400), 100, 5)
    #after pink - (x,y), radius, width of outline
    pygame.display.flip()