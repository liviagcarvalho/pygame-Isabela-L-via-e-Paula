import pygame
import random

pygame.init()

# ----- Gera tela principal
WIDTH = 500
HEIGHT = 700
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('🧚🏼🧚🏼‍♀️Fairy Game🧚🏼‍♀️🧚🏼')

game = True

imagem_fundo = pygame.image.load('assets/img/Fundo_pygame.png').convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (WIDTH, HEIGHT))

LASER_WIDTH = 50
LASER_HEIGHT = 38
font = pygame.font.SysFont(None, 48)
LASER_img = pygame.image.load('assets/img/Laser_roxo.png').convert_alpha() 
LASER_img_small = pygame.transform.scale(LASER_img, (LASER_WIDTH, LASER_HEIGHT))

LASER_x = 200
# y negativo significa que está acima do topo da janela. O meteoro começa fora da janela
LASER_y = -LASER_HEIGHT
LASER_speedx = 3
LASER_speedy = 4


# ===== Loop principal =====

while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(imagem_fundo, (0, 0))

    LASER_x += LASER_speedx
    LASER_y += LASER_speedy
    # Se o meteoro passar do final da tela, volta para cima
    if LASER_y > HEIGHT or LASER_x + LASER_WIDTH < 0 or LASER_x > WIDTH:
        # meteor_x = 200
        # meteor_y = -METEOR_HEIGHT
        LASER_x = random.randint(0, WIDTH-LASER_WIDTH) 
        LASER_y = random.randint(-100, -LASER_HEIGHT) 
        LASER_speedx = random.randint(-3, 3) 
        LASER_speedy = random.randint(2, 9)

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(imagem_fundo, (0, 0)) # desenha imagem de fundo 
    window.blit(LASER_img_small, (LASER_x, LASER_y)) # desenha imagem do meteoro n
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados













# # ----- Inicia estruturas de dados
# # Definindo os novos tipos
# class Meteor(pygame.sprite.Sprite):
#     def __init__(self, img):
#         # Construtor da classe mãe (Sprite). # Todo Sprite deve definir um atributo image e um rect, eles são utilizados para desenhar a imagem.
#         pygame.sprite.Sprite.__init__(self)
#         # O rect define a posição do retângulo da imagem
#         self.image = img
#         self.rect = self.image.get_rect()
#         self.rect.x = random.randint(0, WIDTH-LASER_WIDTH)
#         self.rect.y = random.randint(-100, -LASER_HEIGHT)
#         self.speedx = random.randint(-3, 3)
#         self.speedy = random.randint(2, 9)

#     def update(self):
#         # Atualizando a posição do meteoro
#         self.rect.x += self.speedx
#         self.rect.y += self.speedy
#         # Se o meteoro passar do final da tela, volta para cima e sorteia
#         # novas posições e velocidades
#         if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
#             self.rect.x = random.randint(0, WIDTH-LASER_WIDTH)
#             self.rect.y = random.randint(-100, -LASER_HEIGHT)
#             self.speedx = random.randint(-3, 3)
#             self.speedy = random.randint(2, 9)

# game = True
# # Variável para o ajuste de velocidade
# clock = pygame.time.Clock()
# FPS = 30

# # Criando dois meteoros
# meteor1 = Meteor(LASER_img)
# meteor2 = Meteor(LASER_img)
# meteor3 = Meteor(LASER_img)
# meteor4 = Meteor(LASER_img)

# # ===== Loop principal =====
# while game:
#     clock.tick(FPS)

#     # ----- Trata eventos
#     for event in pygame.event.get():
#         # ----- Verifica consequências
#         if event.type == pygame.QUIT:
#             game = False

#     # ----- Atualiza estado do jogo
#     # Atualizando a posição dos meteoros
#     meteor1.update()
#     meteor2.update()
#     meteor3.update()
#     meteor4.update()
#     # ----- Gera saídas
#     window.fill((0, 0, 0))  # Preenche com a cor branca
#     window.blit(imagem_fundo, (0, 0))
#     # Desenhando meteoros
#     window.blit(meteor1.image, meteor1.rect)
#     window.blit(meteor2.image, meteor2.rect)
#     window.blit(meteor3.image, meteor3.rect)
#     window.blit(meteor4.image, meteor4.rect)

#     pygame.display.update()  # Mostra o novo frame para o jogador

# # ===== Finalização =====
# pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

