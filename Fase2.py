
import pygame
import random

def fase2():
    pygame.init()

    # ----- Gera tela principal
    WIDTH = 900
    HEIGHT = 600
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('🧚🏼🧚🏼‍♀️Fairy Game🧚🏼‍♀️🧚🏼')

    # ----- Carrega imagens
    # Carregando a imagem de fundo
    imagem_fundo = pygame.image.load('assets/img/Fundo_pygame3.png').convert()
    imagem_fundo = pygame.transform.scale(imagem_fundo, (WIDTH, HEIGHT))
    imagem_fundo_rect = imagem_fundo.get_rect()
    speed_fundo = 10

    # Imagem da fada mal
    imagem_fada_mal = pygame.image.load('assets/img/FADAmal.png').convert_alpha()
    fada_mal_width = 120
    fada_mal_height = 80
    imagem_fada_mal = pygame.transform.scale(imagem_fada_mal, (fada_mal_width, fada_mal_height))
    fada_mal_rect = imagem_fada_mal.get_rect()
    fada_mal_rect.centery = HEIGHT / 2  # Centraliza a fada má verticalmente
    fada_mal_rect.right = 120

    # Imagem fada bem
    fada_bem_width = 100
    fada_bem_height = 70
    imagem_fada_bem = pygame.image.load('assets/img/FADAbem.png').convert_alpha()
    imagem_fada_bem = pygame.transform.scale(imagem_fada_bem, (fada_bem_width, fada_bem_height))

    # Carregando imagens dos lasers
    LASER_WIDTH = 10
    LASER_HEIGHT = 50
    laser_colors = ['roxo', 'azul', 'rosa', 'verde', 'verdeagua', 'amarelo']
    laser_images = {}
    for color in laser_colors:
        img = pygame.image.load(f'assets/img/Laser_{color}.png').convert_alpha()
        laser_images[color] = pygame.transform.scale(img, (LASER_WIDTH, LASER_HEIGHT))

    # ----- CLASSE FADA BEM 
    class FADA_BEM(pygame.sprite.Sprite):
        def __init__(self, img, all_sprites):
            pygame.sprite.Sprite.__init__(self)
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.centerx = WIDTH - 50
            self.rect.bottom = HEIGHT / 2
            self.speedx = 0
            self.speedy = 0
            self.all_sprites = all_sprites

        def update(self):
            # Atualização da posição da fada
            self.rect.x += self.speedx
            self.rect.y += self.speedy

            # Mantem dentro da tela
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT
            if self.rect.top < 0:
                self.rect.top = 0

    # ----- CLASSE LASER 
    class LASER(pygame.sprite.Sprite):
        def __init__(self, img):
            pygame.sprite.Sprite.__init__(self)
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(0, WIDTH - LASER_WIDTH)
            self.rect.y = random.randint(-100, -LASER_HEIGHT)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(3, 10)

        def update(self):
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
                self.rect.x = random.randint(0, WIDTH - LASER_WIDTH)
                self.rect.y = random.randint(-100, -LASER_HEIGHT)
                self.speedx = random.randint(-3, 3)
                self.speedy = random.randint(3, 10)

    # ----- Definindo outras variáveis do jogo
    game = True
    clock = pygame.time.Clock()
    FPS = 30

    # ----- Criando um grupo de sprites para os lasers 
    all_sprites = pygame.sprite.Group()
    all_lasers = pygame.sprite.Group()

    # Criando o jogador
    jogador = FADA_BEM(imagem_fada_bem, all_sprites)
    all_sprites.add(jogador)

    # ----- Criando os lasers e adicionando ao grupo de sprites
    num_lasers = 6
    for _ in range(num_lasers):
        laser = LASER(random.choice(list(laser_images.values())))
        all_sprites.add(laser)
        all_lasers.add(laser)

    # Variável para controlar o tempo e adicionar mais lasers
    laser_add_counter = 0
    laser_add_interval = 200  # Intervalo para adicionar lasers 

    # ===== Loop principal =====
    K =0
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
                if event.key == pygame.K_UP:
                    jogador.speedy = -5
                if event.key == pygame.K_DOWN:
                    jogador.speedy = 5

            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    jogador.speedx = 0
                if event.key in [pygame.K_UP, pygame.K_DOWN]:
                    jogador.speedy = 0

        # Atualiza estado do jogo
        all_sprites.update()

        window.fill((0, 0, 0))
        # Atualiza a posição da imagem de fundo.
        imagem_fundo_rect.x += speed_fundo
        # Se o fundo saiu da janela, faz ele voltar para dentro.
        if imagem_fundo_rect.left > WIDTH:
            imagem_fundo_rect.x -= imagem_fundo_rect.width
        # Desenha o fundo e uma cópia para a direita.
        window.blit(imagem_fundo, imagem_fundo_rect)
        imagem_fundo_rect_2 = imagem_fundo_rect.copy()
        imagem_fundo_rect_2.x -= imagem_fundo_rect_2.width
        window.blit(imagem_fundo, imagem_fundo_rect_2)

        # Verifica se houve colisão entre laser
        if pygame.sprite.spritecollide(jogador, all_lasers, False):
            import perdeu_laser
            perdeu_laser()

        # Verifica se houve colisão entre fadas
        if jogador.rect.colliderect(fada_mal_rect):
            # import tela_prox_nivel
            K = 3 


        # Adiciona mais lasers após um intervalo
        laser_add_counter += 1
        if laser_add_counter >= laser_add_interval:
            laser_add_counter = 0
            for _ in range(2):  # Adiciona 2 novos lasers a cada intervalo
                laser = LASER(random.choice(list(laser_images.values())))
                all_sprites.add(laser)
                all_lasers.add(laser)

        # Gera saídas
        window.blit(imagem_fada_mal, fada_mal_rect)  # Desenha a fada mal
        all_sprites.draw(window)
        pygame.display.update()

fase2()

# Finalização
pygame.quit()