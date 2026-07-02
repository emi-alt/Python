import pygame
W = 640
H = 480
window = pygame.set_mode((W, H))
window.set_caption("Elements on My Page")
BLUE = (60, 119, 150)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            done = True
    recti = pygame.draw.rect(window, BLUE, pygame.Rect(W/2, H/2, 60, 40))
    pygame.display.flip()
