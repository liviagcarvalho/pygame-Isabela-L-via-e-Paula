import pygame
import random



K = 0 
def fase2 (): 
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

    #imagem da fada mal
    imagem_fada_mal = pygame.image.load('assets/img/FADAmal.png').convert_alpha()
    fada_mal_width = 120
    fada_mal_height = 80
    imagem_fada_mal = pygame.transform.scale(imagem_fada_mal, (fada_mal_width, fada_mal_height))
    fada_mal_rect = imagem_fada_mal.get_rect()
    fada_mal_rect.centery = HEIGHT/2  # Centraliza a fada má verticalmente
    fada_mal_rect.right = 120


    #imagem fada bem 
    fada_bem_width = 100
    fada_bem_height = 70
    imagem_fada_bem = pygame.image.load('assets/img/FADAbem.png').convert_alpha()
    imagem_fada_bem = pygame.transform.scale(imagem_fada_bem, (fada_bem_width, fada_bem_height))
    ### dentro do classe 



    # Carregando imagens dos lasers
    LASER_img_roxo = pygame.image.load('assets/img/Laser_roxo.png').convert_alpha()
    LASER_img_azul = pygame.image.load('assets/img/Laser_azul.png').convert_alpha()
    LASER_img_rosa = pygame.image.load('assets/img/Laser_rosa.png').convert_alpha()
    LASER_img_verde = pygame.image.load('assets/img/Laser_verde.png').convert_alpha()
    LASER_img_verdeagua = pygame.image.load('assets/img/Laser_verdeagua.png').convert_alpha()
    LASER_img_amarelo = pygame.image.load('assets/img/Laser_amarelo.png').convert_alpha()

    # Redimensionando imagens dos lasers
    LASER_WIDTH = 10
    LASER_HEIGHT = 50
    LASER_img_roxo_small = pygame.transform.scale(LASER_img_roxo, (LASER_WIDTH, LASER_HEIGHT))
    LASER_img_azul_small = pygame.transform.scale(LASER_img_azul, (LASER_WIDTH, LASER_HEIGHT))
    LASER_img_rosa_small = pygame.transform.scale(LASER_img_rosa, (LASER_WIDTH, LASER_HEIGHT))
    LASER_img_verde_small = pygame.transform.scale(LASER_img_verde, (LASER_WIDTH, LASER_HEIGHT))
    LASER_img_verdeagua_small = pygame.transform.scale(LASER_img_verdeagua, (LASER_WIDTH, LASER_HEIGHT))
    LASER_img_amarelo_small = pygame.transform.scale(LASER_img_amarelo, (LASER_WIDTH, LASER_HEIGHT))








    # ----- CLASSE FADA BEM 
    class FADA_BEM(pygame.sprite.Sprite):
        def _init_(self, img, all_sprites):
        #def _init_(self, img, all_sprites, all_tiros, imagem_tiro):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite._init_(self)

            self.image = img
            self.rect = self.image.get_rect()
            self.rect.centerx = WIDTH - 50
            self.rect.bottom = HEIGHT/2 
            self.speedx = 0
            self.speedy = 0
            self.all_sprites = all_sprites
            # self.all_tiro = all_tiros
            # self.imagem_img = imagem_tiro

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
        def _init_(self, img):
            pygame.sprite.Sprite._init_(self)
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(0, WIDTH - LASER_WIDTH)
            self.rect.y = random.randint(-100, -LASER_HEIGHT)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(3,10) #(2, 9) # velocidade (4,12) - para ultima fase (3,10) segunda fase 

        def update(self):
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
                self.rect.x = random.randint(0, WIDTH - LASER_WIDTH)
                self.rect.y = random.randint(-100, -LASER_HEIGHT)
                self.speedx = random.randint(-3, 3)
                self.speedy = random.randint (3,10) #(2, 9) # velocidade (4,12) - para ultima fase (3,10) segunda fase 




    # ----- Definindo outras variáveis do jogo
    game = True 
    clock = pygame.time.Clock()
    FPS = 30




    # # ----- Criando um grupo de sprites para os lasers 
    all_sprites = pygame.sprite.Group()
    all_lasers = pygame.sprite.Group()

    # Criando o jogador
    jogador = FADA_BEM(imagem_fada_bem, all_sprites)
    all_sprites.add(jogador)


    # ----- Criando os lasers e adicionando ao grupo de sprites
    lasers = [LASER(LASER_img_roxo_small), LASER(LASER_img_azul_small), LASER(LASER_img_rosa_small), LASER(LASER_img_verde_small), LASER(LASER_img_verdeagua_small), LASER(LASER_img_amarelo_small)]

    for laser in lasers:
        all_sprites.add(laser)
        all_lasers.add(laser)






    # ----- Criando os lasers e adicionando ao grupo de sprites
    l1 = LASER(LASER_img_roxo_small)
    l2 = LASER(LASER_img_azul_small)
    l3 = LASER(LASER_img_rosa_small)
    l4 = LASER(LASER_img_verde_small)
    l5 = LASER(LASER_img_verdeagua_small)
    l6 = LASER(LASER_img_amarelo_small)
    all_sprites.add(l1, l2, l3, l4, l5, l6)

    # #AUMENTA QUANTIDADE DE LASER PARA FASES FUTURAS!!!!!!!!!
    # # Criando mais lasers e adicionando ao grupo de sprites
    # num_lasers = 12  # Aumentando a quantidade de lasers
    # for _ in range(num_lasers):
    #     l = LASER(random.choice([LASER_img_roxo_small, LASER_img_azul_small, LASER_img_rosa_small, LASER_img_verde_small, LASER_img_amarelo_small, LASER_img_verdeagua_small]))
    #     all_sprites.add(l)

    #AUMENTA QUANTIDADE DE LASER PARA FASES FUTURAS!!!!!!!!!
    # Criando mais lasers e adicionando ao grupo de sprites
    num_lasers = 10  # Aumentando a quantidade de lasers
    for _ in range(num_lasers):
        l = LASER(random.choice([LASER_img_roxo_small, LASER_img_azul_small, LASER_img_rosa_small, LASER_img_verde_small, LASER_img_amarelo_small, LASER_img_verdeagua_small]))
        all_sprites.add(l)
        all_lasers.add(l)



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
                    jogador.speedx -= 4 #8
                if event.key == pygame.K_RIGHT:
                    jogador.speedx += 4 #8
                if event.key == pygame.K_UP:
                    jogador.speedy = -5
                if event.key == pygame.K_DOWN:
                    jogador.speedy = 5

            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    jogador.speedx = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    jogador.speedy = 0





        # Atualiza estado do jogo
        all_sprites.update()

        window.fill ((0,0,0))
        # Atualiza a posição da imagem de fundo.
        imagem_fundo_rect.x += speed_fundo
        # Se o fundo saiu da janela, faz ele voltar para dentro.
        if imagem_fundo_rect.left > WIDTH:
            imagem_fundo_rect.x -= imagem_fundo_rect.width
        # Desenha o fundo e uma cópia para a direita.
        # Assumimos que a imagem selecionada ocupa pelo menos o tamanho da janela.
        # Além disso, ela deve ser cíclica, ou seja, o lado esquerdo deve ser continuação do direito.
        window.blit (imagem_fundo, imagem_fundo_rect)
        # Desenhamos a imagem novamente, mas deslocada da largura da imagem em x.
        imagem_fundo_rect_2 = imagem_fundo_rect.copy()
        imagem_fundo_rect_2.x -= imagem_fundo_rect_2.width
        window.blit (imagem_fundo, imagem_fundo_rect_2)







    # Verifica se houve colisão entre laser
        if pygame.sprite.spritecollide(jogador, all_lasers, False):
            import perdeu_laser
            perdeu_laser()


            #em vez de game= False -> mostrar imagem de voce perdeu recomecar clicando 


    # Verifica se houve colisão entre fadas
        if jogador.rect.colliderect(fada_mal_rect):
            K+= 1 




    # Gera saídas
        # window.blit(imagem_fundo, (0, 0))  # Desenha o fundo
        window.blit(imagem_fada_mal, fada_mal_rect)  # Desenha a fada mal
        all_sprites.draw(window)



        pygame.display.update()

fase2 ()
# Finalização
pygame.quit()