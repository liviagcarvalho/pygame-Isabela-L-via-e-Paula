
import sys
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

# Verifica se houve colisão entre laser
    if pygame.sprite.spritecollide(jogador, all_lasers, False):
        game_over_screen(window, WIDTH, HEIGHT)
        game = False

# Verifica se houve colisão entre fadas
    if jogador.rect.colliderect(fada_mal_rect):
        victory_screen(window, WIDTH, HEIGHT)
        game = False
    

