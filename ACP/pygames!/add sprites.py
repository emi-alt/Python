import pygame
pygame.init()
H = 600
W = 600
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
S1 = ("#9283FB")
S2 = ("#E463F8")
BG= ("#B2D7FB")
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width, x, y):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BG)

        pygame.draw.rect(self.image,
        color,
        pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
    def movement(self):
      keys = pygame.key.get_pressed()
      if keys[pygame.K_LEFT]:
        self.rect.x -= self.speed
      if keys[pygame.K_RIGHT]:
        self.rect.x += self.speed
      if keys[pygame.K_UP]:
        self.rect.y -= self.speed
      if keys[pygame.K_DOWN]:
        self.rect.y += self.speed
      if self.rect.left < 0:
         self.rect.left = 0
      if self.rect.right > W:
         self.rect.right = W
      if self.rect.top < 0:
         self.rect.top = 0
      if self.rect.bottom > H:
         self.rect.bottom = H

        

sprite_1 = Sprite(S1, 70, 80, W/6, H/2)
sprite_2 = Sprite(S2, 40,80, W/4, H/2)

all_sprites = pygame.sprite.Group()
all_sprites.add(sprite_1)
all_sprites.add(sprite_2)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    
    sprite_1.movement()
    screen.fill(BG)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)