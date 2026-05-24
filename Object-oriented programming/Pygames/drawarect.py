import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((111, 91, 194))
    pygame.draw.rect(screen, (41, 128, 143), pygame.Rect(30, 40, 100 ,140))
    #Rect = (x-axis, y-axis, width, height)
    pygame.display.flip()
# pygame.quit()