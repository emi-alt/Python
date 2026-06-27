import pygame # type: ignore
pygame.init()
w = 500
h = 500
display = pygame.display.set_mode((w, h))
text = pygame.display.set_caption('My first pygame')
image = pygame.transform.scale(pygame.image.load('cat.png').convert_alpha(), (300,300))
img_redirect = image.get_rect(center=(w//2, h//2))
Grey = (58,58,58)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    display.fill(Grey)
    display.blit(image, img_redirect)
    pygame.display.flip()
pygame.quit()