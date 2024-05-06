
import random

def criar_cartas():
    numeros = [100, 101, 102, 103]
    cartas = numeros * 2
    random.shuffle(cartas)
    return cartas

def main():
    cartas = criar_cartas()
    cartas_viradas = [False] * 8
    pares_encontrados = 0
    
    while pares_encontrados < 4:  # Ajustado para verificar 4 pares
        for i in range(len(cartas)):
            if cartas_viradas[i]:
                print(cartas[i], end=' ')
            else:
                print('*', end=' ')
            if (i + 1) % 4 == 0:
                print()

        print("Escolha duas cartas para virar (1-8):")
        escolhas = input().split()

        if len(escolhas) != 2:
            print("Você deve escolher duas cartas separadas por um espaço. Tente novamente.")
            continue

        escolha1, escolha2 = map(int, escolhas)
        escolha1 -= 1
        escolha2 -= 1
        
        if escolha1 == escolha2 or escolha1 < 0 or escolha1 > 7 or escolha2 < 0 or escolha2 > 7:
            print("Escolha inválida. Tente novamente.")
            continue
        
        if cartas_viradas[escolha1] or cartas_viradas[escolha2]:
            print("Uma das cartas já foi virada. Tente novamente.")
            continue
        
        cartas_viradas[escolha1] = True
        cartas_viradas[escolha2] = True
        
        print("Carta", escolha1 + 1, ":", cartas[escolha1])
        print("Carta", escolha2 + 1, ":", cartas[escolha2])
        
        if cartas[escolha1] == cartas[escolha2]:
            pares_encontrados += 1
            print("Par encontrado! Você ganhou 1 ponto.")
        else:
            print("Não é um par. Tente novamente.")
            cartas_viradas[escolha1] = False
            cartas_viradas[escolha2] = False
        
    print("Parabéns! Você encontrou todos os pares.")
    print("Pontuação final:", pares_encontrados)

if __name__ == "__main__":
    main()
