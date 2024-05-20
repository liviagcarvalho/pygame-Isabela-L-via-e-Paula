import pygame
import random

pygame.init()

# ----- Gera tela principal
WIDTH = 600
HEIGHT = 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('🧚🏼🧚🏼‍♀️Fairy Game🧚🏼‍♀️🧚🏼')

# Carregando a imagem de fundo
imagem_fundo = pygame.image.load('assets/img/Fundo_pygame.png').convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (WIDTH, HEIGHT))

# Carregando a imagem da fada mal
imagem_fada_mal = pygame.image.load('assets/img/FADAmal.png').convert_alpha()
fada_mal_width = 120
fada_mal_height = 80
imagem_fada_mal = pygame.transform.scale(imagem_fada_mal, (fada_mal_width, fada_mal_height))
fada_mal_rect = imagem_fada_mal.get_rect()
fada_mal_rect.centerx = WIDTH // 2  # Centraliza a fada mal horizontalmente
fada_mal_rect.top = 0  # Posiciona a fada mal no topo da janela

# Carregando imagens dos lasers
LASER_img_roxo = pygame.image.load('assets/img/Laser_roxo.png').convert_alpha()
LASER_img_azul = pygame.image.load('assets/img/Laser_azul.png').convert_alpha()
LASER_img_rosa = pygame.image.load('assets/img/Laser_rosa.png').convert_alpha()
LASER_img_verde = pygame.image.load('assets/img/Laser_verde.png').convert_alpha()
LASER_img_verdeagua = pygame.image.load('assets/img/Laser_verdeagua.png').convert_alpha()
LASER_img_amarelo = pygame.image.load('assets/img/Laser_amarelo.png').convert_alpha()

# Redimensionando imagens dos lasers
LASER_WIDTH = 100
LASER_HEIGHT = 50
LASER_img_roxo_small = pygame.transform.scale(LASER_img_roxo, (LASER_WIDTH, LASER_HEIGHT))
LASER_img_azul_small = pygame.transform.scale(LASER_img_azul, (LASER_WIDTH, LASER_HEIGHT))
LASER_img_rosa_small = pygame.transform.scale(LASER_img_rosa, (LASER_WIDTH, LASER_HEIGHT))
LASER_img_verde_small = pygame.transform.scale(LASER_img_verde, (LASER_WIDTH, LASER_HEIGHT))
LASER_img_verdeagua_small = pygame.transform.scale(LASER_img_verdeagua, (LASER_WIDTH, LASER_HEIGHT))
LASER_img_amarelo_small = pygame.transform.scale(LASER_img_amarelo, (LASER_WIDTH, LASER_HEIGHT))

game = True 
clock = pygame.time.Clock()
FPS = 30

# CLASSE LASER 
class LASER(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - LASER_WIDTH)
        self.rect.y = random.randint(-100, -LASER_HEIGHT)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH - LASER_WIDTH)
            self.rect.y = random.randint(-100, -LASER_HEIGHT)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 9)

# Criando um grupo de sprites para os lasers
all_sprites = pygame.sprite.Group()

# Criando os lasers e adicionando ao grupo de sprites
l1 = LASER(LASER_img_roxo_small)
l2 = LASER(LASER_img_azul_small)
l3 = LASER(LASER_img_rosa_small)
l4 = LASER(LASER_img_verde_small)
l5 = LASER(LASER_img_verdeagua_small)
l6 = LASER(LASER_img_amarelo_small)
all_sprites.add(l1, l2, l3, l4, l5, l6)

# ===== Loop principal =====
while game:
    clock.tick(FPS)

    # Trata eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    # Atualiza estado do jogo
    all_sprites.update()

    # Gera saídas
    window.blit(imagem_fundo, (0, 0))  
    window.blit(imagem_fada_mal, fada_mal_rect)  
    all_sprites.draw(window)

    pygame.display.flip()

# Finalização
pygame.quit()
