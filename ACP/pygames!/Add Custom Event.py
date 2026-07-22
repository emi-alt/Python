import pygame
import random
W, H = 500, 400
SPEED = 5
pygame.init()
background_image = pygame.transform.scale(pygame.image.load("pygames!/fa34293071f987c8d969a09e35b4a830.jpg"),(W, H))
#ADD BACKGROUND IMAGE
font = pygame.font.SysFont("Times New Roman", 72)
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
p1 = pygame.Color('#4B3876')
p2 = pygame.Color('#6B50AA')
p3 = pygame.Color("#B9AADB")
class Sprite(pygame.sprite.Sprite):

    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(
            pygame.Color('#C56389'))
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()

    def move(self, x_change, y_change):
        self.rect.x = max(
            min(self.rect.x + x_change, W - self.rect.width), 0)
        self.rect.y = max(
            min(self.rect.y + y_change, H - self.rect.height), 0)
    
    def change_color(self):
        self.image.fill(random.choice([p1, p2, p3]))

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Sprite Collision")
all_sprites = pygame.sprite.Group()

sprite1 = Sprite(pygame.Color("#7960B4"), 20, 30)
sprite1.rect.x, sprite1.rect.y = random.randint(
    0, W - sprite1.rect.width), random.randint(
        0, H - sprite1.rect.height)
all_sprites.add(sprite1)
    
sprite2 = Sprite(pygame.Color('#7BAE65'), 20, 30)
sprite2.rect.x, sprite2.rect.y = random.randint(
    0, W - sprite2.rect.width), random.randint(
        0, H - sprite2.rect.height)
all_sprites.add(sprite2)

running, won = True, False
clock = pygame.time.Clock()

def colors(SPRITE_COLOR_CHANGE_EVENT, sprite1, event):
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        evt = (pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
        pygame.event.post(evt)
    if event.type == SPRITE_COLOR_CHANGE_EVENT:
        sprite1.change_color()

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False
            
    colors(SPRITE_COLOR_CHANGE_EVENT, sprite1, event)
    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] -keys[pygame.K_LEFT]) * SPEED
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * SPEED
        sprite1.move(x_change, y_change)

        if sprite1.rect.colliderect(sprite2.rect):
            all_sprites.remove(sprite2)
            won = True
    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)
    if won:
        win_text = font.render("You win!", True, pygame.Color('black'))
        screen.blit(win_text, ((W - win_text.get_width()) // 2,(H - win_text.get_height()) // 2))

    pygame.display.flip()
    clock.tick(120)

pygame.quit()
