import os
import unicodedata

# Função para normalizar e remover acentos
def remover_acento(palavra):
    return ''.join(c for c in unicodedata.normalize('NFD', palavra)
                   if unicodedata.category(c) != 'Mn')

# Input da palavra que o jogo vai rodar em cima
def coletarPalavra():
    while True:
        print("-" * 60)
        frase_original = input("Insira a frase ou palavra: ")  # Aceita frases com espaços
        if frase_original.isalpha() or " " in frase_original or "-" in frase_original:
            frase_normalizada = remover_acento(frase_original).lower()
            print("-" * 60)
            os.system("cls")
            return frase_original, frase_normalizada

# Contabiliza as vidas
def mostrar_vidas(vida):
    vidas = "❤ "*vida
    return vidas

# Constroi a forca inicialmente
def mostrarForca(palavra, vidas):
    nova_palavra = palavra
    print(vidas)
    for i in list(palavra):
        if i != " " and i != "-":
            nova_palavra = nova_palavra.replace(i, "_ ")
    
    return nova_palavra

# Atualiza a forca a cada jogada
def atualizarForca(palavra, acertos, nova_palavra):
    nova_palavra = ''

    for i in list(palavra):
        if i in acertos or i == " " or i == "-":
            nova_palavra += i
        else:
            nova_palavra += "_ "

    if nova_palavra != palavra:
        return nova_palavra
    else:
        return False 

# Pega o chute do usuário e retorna para a função partida
def jogada(palavra):
    while True:
        tentativa = input("Chute uma letra: ")
        tentativa = remover_acento(tentativa).lower()  # Normaliza o chute
        if len(tentativa) == 1 and tentativa.isalpha(): 
            if tentativa in palavra:
                return (True, tentativa)
            else:
                return (False, tentativa)
        else:
            print("Insira apenas uma letra")

# Adiciona as tentativas às listas. Roda o jogo
def partida(palavra_original, palavra_normalizada, n_vidas):
    tentativas = []
    acertos = []
    vida_atual = n_vidas

    while True:
        nova_palavra = ""
        # Pega o return da jogada
        jogada_player = jogada(palavra_normalizada)
        
        # Verifica se a letra já foi usada
        if not jogada_player[1] in tentativas:
            tentativas.append(jogada_player[1])
        
            # Verifica se o usuário acertou
            if jogada_player[0]:
                # Limpa o terminal
                os.system("cls")

                # Adiciona o chute do usuário à lista de acertos
                acertos.append(jogada_player[1])
                
                # Pega o return tentativa do usuário
                rodada = atualizarForca(palavra_normalizada, acertos, nova_palavra)
                if rodada != False:
                    print(mostrar_vidas(vida_atual))
                    print(rodada)
                    
                    if len(tentativas) != 0:
                        print(f"Letras utilizadas: {', '.join(tentativas)}")
                else:
                    print(f"A palavra era: {palavra_original}")
                    print(f"Fim de jogo! Você ganhou, parabéns!\nVidas restantes: {vida_atual}")
                    break
            else:
                # Limpa o terminal
                os.system("cls")
                vida_atual -= 1
                if vida_atual > 0:
                    print(mostrar_vidas(vida_atual))
                    rodada = atualizarForca(palavra_normalizada, acertos, nova_palavra)
                    print(rodada)
                    if len(tentativas) != 0:
                        print(f"Letras utilizadas: {', '.join(tentativas)}")
                else:
                    # Limpa o terminal
                    os.system("cls")
                    print(f"A palavra era: {palavra_original}")
                    print("Fim de jogo! Você perdeu!")
                    break
        else:
            os.system("cls")
            print("Essa letra já foi usada")
            print(mostrar_vidas(vida_atual))
            print(rodada)

def main():
    n_vidas = 5
    vidas = mostrar_vidas(n_vidas)
    
    palavra_original, palavra_normalizada = coletarPalavra()
    print(mostrarForca(palavra_normalizada, vidas))

    partida(palavra_original, palavra_normalizada, n_vidas)

main()
