import pygame

pygame.init()

w, h = 500, 500
display = pygame.display.set_mode((w,h))
pygame.display.set_caption("Adding image and background to pygame.")

bg_img = pygame.transform.scale(pygame.image.load('outdoor-bg.png').convert(),(w, h)) #resizing bg to the size of screen
penguin_image = pygame.transform.scale(pygame.image.load('penguin.png').convert_alpha(), (200,200)) #resiing the image to a specific size
#.convert_alpha() - to make the object/surface look round by adding tranparency in the background of the image and avoid a blocky/rect shape
penguin_rect = penguin_image.get_rect(center=(w//2,h//2-30)) #doubt

text = pygame.font.Font(None, 26).render("Hello World", True, pygame.Color('black'))
text_rect = text.get_rect(center=(w//2, h//2+110)) #defining the position

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        display.blit(bg_img, (0, 0)) #in the intructions it says"the bg image is drawn in the top left cornr" why in top left corner? and what does (0, 0) mean?
        display.blit(penguin_image, penguin_rect)
        display.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

if __name__ == '__learninggame__':
    game_loop()