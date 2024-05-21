import pygame
import random
import time

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
imagem_fundo_rect_2 = imagem_fundo_rect.copy()
imagem_fundo_rect_2.x -= imagem_fundo_rect_2.width
speed_fundo = 10 

# ----- Função para mostrar a tela inicial
def show_start_screen():
    window.blit(imagem_fundo, imagem_fundo_rect)
    window.blit(imagem_fundo, imagem_fundo_rect_2)
    
    # Fonte maior e cor rosa choque brilhante para o título
    title_font = pygame.font.SysFont(None, 72)
    title = title_font.render("Fairy Game", True, (255, 20, 147))  # Rosa choque brilhante
    
    # Fonte menor para a história
    font = pygame.font.SysFont(None, 40)
    story = [
        "O mundo das fadas está em perigo por causa da fada má",
        "e você, vai ajudar a salvar o reino!",
        "Sua missão é alcançar a fada má sem ser pego",
        "por um dos lasers laçados por ela.",
        "",
    ]

    font_inicio = pygame.font.SysFont(None, 30)
    inicio = font_inicio.render("Clique em qualquer botão para iniciar o jogo.", True, (255, 255, 255))

    # Desenha o título
    window.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 4))
    pygame.display.flip()
    
    # Desenha a história de forma animada
    for i, line in enumerate(story):
        rendered_line = ""
        for char in line:
            rendered_line += char
            text = font.render(rendered_line, True, (255, 255, 255))
            window.blit(imagem_fundo, imagem_fundo_rect)
            window.blit(imagem_fundo, imagem_fundo_rect_2)
            window.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 4))
            for j in range(i):
                previous_text = font.render(story[j], True, (255, 255, 255))
                window.blit(previous_text, (WIDTH // 2 - previous_text.get_width() // 2, HEIGHT // 3 + 40 * (j + 1)))
            window.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 3 + 40 * (i + 1)))
            pygame.display.flip()
            pygame.time.wait(50)  # Delay de 50ms entre cada letra

    window.blit(inicio, (WIDTH // 2 - inicio.get_width() // 2, HEIGHT // 38))
    pygame.display.flip()

    # Aguarda o jogador pressionar uma tecla ou botão do mouse para iniciar o jogo
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONUP:
                waiting = False


show_start_screen()