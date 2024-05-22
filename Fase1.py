
import pygame
import random
from inicio import*
def fase1():
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

    # Imagem da fada má
    imagem_fada_mal = pygame.image.load('assets/img/FADAmal.png').convert_alpha()
    fada_mal_width = 120
    fada_mal_height = 80
    imagem_fada_mal = pygame.transform.scale(imagem_fada_mal, (fada_mal_width, fada_mal_height))
    fada_mal_rect = imagem_fada_mal.get_rect()
    fada_mal_rect.centery = HEIGHT / 2
    fada_mal_rect.right = 120

    # Imagem da fada bem
    fada_bem_width = 100
    fada_bem_height = 70
    imagem_fada_bem = pygame.image.load('assets/img/FADAbem.png').convert_alpha()
    imagem_fada_bem = pygame.transform.scale(imagem_fada_bem, (fada_bem_width, fada_bem_height))

    # Carregando imagens dos lasers
    laser_imgs = {
        'roxo': pygame.image.load('assets/img/Laser_roxo.png').convert_alpha(),
        'azul': pygame.image.load('assets/img/Laser_azul.png').convert_alpha(),
        'rosa': pygame.image.load('assets/img/Laser_rosa.png').convert_alpha(),
        'verde': pygame.image.load('assets/img/Laser_verde.png').convert_alpha(),
        'verdeagua': pygame.image.load('assets/img/Laser_verdeagua.png').convert_alpha(),
        'amarelo': pygame.image.load('assets/img/Laser_amarelo.png').convert_alpha(),
    }

    # Redimensionando imagens dos lasers
    LASER_WIDTH = 10
    LASER_HEIGHT = 50
    for color in laser_imgs:
        laser_imgs[color] = pygame.transform.scale(laser_imgs[color], (LASER_WIDTH, LASER_HEIGHT))

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
            self.rect.x += self.speedx
            self.rect.y += self.speedy

            # Mantém dentro da tela
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
            self.speedy = random.randint(2, 9)

        def update(self):
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
                self.rect.x = random.randint(0, WIDTH - LASER_WIDTH)
                self.rect.y = random.randint(-100, -LASER_HEIGHT)
                self.speedx = random.randint(-3, 3)
                self.speedy = random.randint(2, 9)

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

    # Criando os lasers e adicionando ao grupo de sprites
    for color, img in laser_imgs.items():
        laser = LASER(img)
        all_sprites.add(laser)
        all_lasers.add(laser)

    # ===== Loop principal =====
    while game:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    jogador.speedx -= 4
                if event.key == pygame.K_RIGHT:
                    jogador.speedx += 4
                if event.key == pygame.K_UP:
                    jogador.speedy = -5
                if event.key == pygame.K_DOWN:
                    jogador.speedy = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    jogador.speedx = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    jogador.speedy = 0

        # Atualiza estado do jogo
        all_sprites.update()

        window.fill((0, 0, 0))
        # Atualiza a posição da imagem de fundo.
        imagem_fundo_rect.x += speed_fundo
        if imagem_fundo_rect.left > WIDTH:
            imagem_fundo_rect.x -= imagem_fundo_rect.width
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
            import salvou_reino
            salvou_reino()

        window.blit(imagem_fada_mal, fada_mal_rect)  # Desenha a fada má
        all_sprites.draw(window)

        pygame.display.update()

    pygame.quit()

fase1()