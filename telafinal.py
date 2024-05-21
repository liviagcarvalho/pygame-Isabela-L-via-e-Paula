# import pygame
# import random
# import sys

# pygame.init()

# # ----- Gera tela principal
# WIDTH = 600
# HEIGHT = 800
# window = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption('🧚🏼🧚🏼‍♀️Fairy Game🧚🏼‍♀️🧚🏼')

# # ----- Carrega imagens

# # Carregando a imagem de fundo
# imagem_fundo = pygame.image.load('assets/img/Fundo_pygame.png').convert()
# imagem_fundo = pygame.transform.scale(imagem_fundo, (WIDTH, HEIGHT))

# # imagem da fada mal
# imagem_fada_mal = pygame.image.load('assets/img/FADAmal.png').convert_alpha()
# fada_mal_width = 120
# fada_mal_height = 80
# imagem_fada_mal = pygame.transform.scale(imagem_fada_mal, (fada_mal_width, fada_mal_height))
# fada_mal_rect = imagem_fada_mal.get_rect()
# fada_mal_rect.centerx = WIDTH // 2  # Centraliza a fada mal horizontalmente
# fada_mal_rect.top = 0  # Posiciona a fada mal no topo da janela

# # imagem fada bem
# fada_bem_width = 120
# fada_bem_height = 80
# imagem_fada_bem = pygame.image.load('assets/img/FADAbem.png').convert_alpha()
# imagem_fada_bem = pygame.transform.scale(imagem_fada_bem, (fada_bem_width, fada_bem_height))

# # tiro brilho
# imagem_tiro = pygame.image.load('assets/img/Raio_fada_bem.png').convert_alpha()

# # Carregando imagens dos lasers
# LASER_img_roxo = pygame.image.load('assets/img/Laser_roxo.png').convert_alpha()
# LASER_img_azul = pygame.image.load('assets/img/Laser_azul.png').convert_alpha()
# LASER_img_rosa = pygame.image.load('assets/img/Laser_rosa.png').convert_alpha()
# LASER_img_verde = pygame.image.load('assets/img/Laser_verde.png').convert_alpha()
# LASER_img_verdeagua = pygame.image.load('assets/img/Laser_verdeagua.png').convert_alpha()
# LASER_img_amarelo = pygame.image.load('assets/img/Laser_amarelo.png').convert_alpha()

# # Redimensionando imagens dos lasers
# LASER_WIDTH = 100
# LASER_HEIGHT = 50
# LASER_img_roxo_small = pygame.transform.scale(LASER_img_roxo, (LASER_WIDTH, LASER_HEIGHT))
# LASER_img_azul_small = pygame.transform.scale(LASER_img_azul, (LASER_WIDTH, LASER_HEIGHT))
# LASER_img_rosa_small = pygame.transform.scale(LASER_img_rosa, (LASER_WIDTH, LASER_HEIGHT))
# LASER_img_verde_small = pygame.transform.scale(LASER_img_verde, (LASER_WIDTH, LASER_HEIGHT))
# LASER_img_verdeagua_small = pygame.transform.scale(LASER_img_verdeagua, (LASER_WIDTH, LASER_HEIGHT))
# LASER_img_amarelo_small = pygame.transform.scale(LASER_img_amarelo, (LASER_WIDTH, LASER_HEIGHT))

# # ----- CLASSE FADA BEM
# class FADA_BEM(pygame.sprite.Sprite):
#     def __init__(self, img, all_sprites, all_tiros, imagem_tiro):
#         # Construtor da classe mãe (Sprite).
#         pygame.sprite.Sprite.__init__(self)

#         self.image = img
#         self.rect = self.image.get_rect()
#         self.rect.centerx = WIDTH / 2
#         self.rect.bottom = HEIGHT - 10
#         self.speedx = 0
#         self.all_sprites = all_sprites
#         self.all_tiro = all_tiros
#         self.imagem_img = imagem_tiro

#     def update(self):
#         # Atualização da posição da fada
#         self.rect.x += self.speedx

#         # Mantem dentro da tela
#         if self.rect.right > WIDTH:
#             self.rect.right = WIDTH
#         if self.rect.left < 0:
#             self.rect.left = 0

#     def shoot(self):
#         # A nova bala vai ser criada logo acima e no centro horizontal da nave
#         new_tiro = TIRO(self.imagem_img, self.rect.top, self.rect.centerx)
#         self.all_sprites.add(new_tiro)
#         self.all_tiro.add(new_tiro)

# # ----- CLASSE LASER
# class LASER(pygame.sprite.Sprite):
#     def __init__(self, img):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = img
#         self.rect = self.image.get_rect()
#         self.rect.x = random.randint(0, WIDTH - LASER_WIDTH)
#         self.rect.y = random.randint(-100, -LASER_HEIGHT)
#         self.speedx = random.randint(-3, 3)
#         self.speedy = random.randint(2, 9) # velocidade (4,12) - para ultima fase (3,10) segunda fase

#     def update(self):
#         self.rect.x += self.speedx
#         self.rect.y += self.speedy
#         if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
#             self.rect.x = random.randint(0, WIDTH - LASER_WIDTH)
#             self.rect.y = random.randint(-100, -LASER_HEIGHT)
#             self.speedx = random.randint(-3, 3)
#             self.speedy = random.randint(2, 9) # velocidade (4,12) - para ultima fase (3,10) segunda fase

import pygame
import random
import sys

pygame.init()

# ----- Gera tela principal
WIDTH = 600
HEIGHT = 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('🧚🏼🧚🏼‍♀️Fairy Game🧚🏼‍♀️🧚🏼')

# ----- Carrega imagens

# Carregando a imagem de fundo
imagem_fundo = pygame.image.load('assets/img/Fundo_pygame.png').convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (WIDTH, HEIGHT))

# imagem da fada mal
imagem_fada_mal = pygame.image.load('assets/img/FADAmal.png').convert_alpha()
fada_mal_width = 120
fada_mal_height = 80
imagem_fada_mal = pygame.transform.scale(imagem_fada_mal, (fada_mal_width, fada_mal_height))
fada_mal_rect = imagem_fada_mal.get_rect()
fada_mal_rect.centerx = WIDTH // 2  # Centraliza a fada mal horizontalmente
fada_mal_rect.top = 0  # Posiciona a fada mal no topo da janela

# imagem fada bem
fada_bem_width = 120
fada_bem_height = 80
imagem_fada_bem = pygame.image.load('assets/img/FADAbem.png').convert_alpha()
imagem_fada_bem = pygame.transform.scale(imagem_fada_bem, (fada_bem_width, fada_bem_height))

# tiro brilho
imagem_tiro = pygame.image.load('assets/img/Raio_fada_bem.png').convert_alpha()

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

# ----- CLASSE FADA BEM
class FadaBem(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)
        self.speed_x = random.randint(-3, 3)
        self.speed_y = random.randint(-3, 3)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        # Inverte a direção se atingir as bordas da tela
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed_x = -self.speed_x
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.speed_y = -self.speed_y

# ----- CLASSE FADA MAL
class FadaMal(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)
        self.speed_x = random.randint(-3, 3)
        self.speed_y = random.randint(-3, 3)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        # Inverte a direção se atingir as bordas da tela
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed_x = -self.speed_x
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.speed_y = -self.speed_y

# ----- CLASSE FADA BEM
class FADA_BEM(pygame.sprite.Sprite):
    def __init__(self, img, all_sprites, all_tiros, imagem_tiro):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.all_sprites = all_sprites
        self.all_tiro = all_tiros
        self.imagem_img = imagem_tiro

    def update(self):
        # Atualização da posição da fada
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        # A nova bala vai ser criada logo acima e no centro horizontal da nave
        new_tiro = TIRO(self.imagem_img, self.rect.top, self.rect.centerx)
        self.all_sprites.add(new_tiro)
        self.all_tiro.add(new_tiro)

# ----- CLASSE LASER
class LASER(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - LASER_WIDTH)
        self.rect.y = random.randint(-100, -LASER_HEIGHT)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9) # velocidade (4,12) - para ultima fase (3,

# Criação das fadas do bem e do mal
fadas_bem = pygame.sprite.Group()
fadas_mal = pygame.sprite.Group()

# Criando fadas do bem
for _ in range(5):
    fada_bem = FadaBem(imagem_fada_bem)
    fadas_bem.add(fada_bem)

# Criando fadas do mal
for _ in range(5):
    fada_mal = FadaMal(imagem_fada_mal)
    fadas_mal.add(fada_mal)

# Atualização das fadas do bem e do mal
fadas_bem.update()
fadas_mal.update()

# Desenho das fadas do bem e do mal na tela
fadas_bem.draw(window)
fadas_mal.draw(window)



# ----- CLASSE TIRO
class TIRO(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, img, bottom, centerx):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()

        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedy = -10  # Velocidade fixa para cima

    def update(self):
        # A bala só se move no eixo y
        self.rect.y += self.speedy

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()

# ----- Definindo outras variáveis do jogo
def game_over_screen(window, WIDTH, HEIGHT):
    font = pygame.font.Font(None, 50)
    subfont = pygame.font.Font(None, 36)  # Fonte menor para a submensagem
    text = font.render('Game Over', True, (0, 0, 0))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    subtext = subfont.render('Pressione qualquer tecla para reiniciar', True, (0, 0, 0))
    subtext_rect = subtext.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

        window.blit(text, text_rect)
        window.blit(subtext, subtext_rect)
        window.blit(imagem_fada_mal, fada_mal_rect) 
        pygame.display.flip()

def victory_screen(window, WIDTH, HEIGHT):
    font = pygame.font.Font(None, 50)
    subfont = pygame.font.Font(None, 36)  # Fonte menor para a submensagem
    text1 = font.render('Parabéns, você derrotou a fada má', True, (0, 0, 0))
    text_rect1 = text1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 35))
    text2 = font.render('e salvou o Reino das Fadas!', True, (0, 0, 0))
    text_rect2 = text2.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    subtext = subfont.render('Pressione qualquer tecla para reiniciar', True, (0, 0, 0))
    subtext_rect = subtext.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False
        
        window.blit(text1, text_rect1)
        window.blit(text2, text_rect2)
        window.blit(subtext, subtext_rect)
        window.blit(imagem_fada_mal, fada_mal_rect) 
        pygame.display.flip()



def main():
    game = True
    clock = pygame.time.Clock()
    FPS = 30

    all_sprites = pygame.sprite.Group()
    all_tiros = pygame.sprite.Group()

    # Criando o jogador
    jogador = FADA_BEM(imagem_fada_bem, all_sprites, all_tiros, imagem_tiro)
    all_sprites.add(jogador)

    # Criando os lasers e adicionando ao grupo de sprites
    l1 = LASER(LASER_img_roxo_small)
    l2 = LASER(LASER_img_azul_small)
    l3 = LASER(LASER_img_rosa_small)
    l4 = LASER(LASER_img_verde_small)
    l5 = LASER(LASER_img_verdeagua_small)
    l6 = LASER(LASER_img_amarelo_small)
    all_sprites.add(l1, l2, l3, l4, l5, l6)

    player_won = False
    player_lost = True

    # ===== Loop principal =====
    while game:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    jogador.speedx -= 4
                if event.key == pygame.K_RIGHT:
                    jogador.speedx += 4
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    jogador.speedx += 4
                if event.key == pygame.K_RIGHT:
                    jogador.speedx -= 4

        # Atualiza estado do jogo
        all_sprites.update()

        # Gera saídas
        window.blit(imagem_fundo, (0, 0))  # Desenha o fundo
        window.blit(imagem_fada_mal, fada_mal_rect)  # Desenha a fada mal
        all_sprites.draw(window)

        pygame.display.flip()

        # Verifica condições de vitória e derrota
        # Aqui você deve adicionar a lógica real para determinar vitória e derrota
        # Este é apenas um exemplo simplificado
        if player_lost:
            game_over_screen(window, WIDTH, HEIGHT)
            # Reinicia o jogo ou faz algo apropriado aqui
            player_lost = False  # reset para teste
        if player_won:
            victory_screen(window, WIDTH, HEIGHT)
            # Reinicia o jogo ou faz algo apropriado aqui
            player_won = False  # reset para teste

    # Finalização
    pygame.quit()

if __name__ == "__main__":
    main()

