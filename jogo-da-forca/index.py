
#! Importação de Bibliotecas------------------------------------------------
"""
random  Biblioteca para escolher aleatoriamente uma palavra da lista.
Counter  Biblioteca para contar a ocorrência de letras na palavra escolhida.
"""
import random 
from collections import Counter
#! Função exibir_palavra(palavra, adivinhou_letra) --------------------------   
"""
Essa função exibe a palavra oculta durante o jogo.
Para cada letra na palavra:
    • Se a letra for adivinhada (letra in adivinhou_letra), ela é exibida.
    • Caso contrário, um underscore (_) é exibido.
A função adiciona uma nova linha no final para melhor formatação.
"""
def exibir_palavra(palavra, adivinhou_letra): #? Função para exibir a palavra com as letras adivinhadas.
    for letra in palavra:
        if letra in adivinhou_letra:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print()

#! Função adivinhar_letra()-------------------------------------------------
    """
    • Essa função obtém a entrada do usuário para adivinhar uma letra.
    • Um loop while True garante que o código continue pedindo uma entrada até que uma entrada válida seja fornecida.
    • O bloco try obtém a entrada do usuário e converte para minúsculas usando lower() para garantir consistência.
    • Em caso de exceção (como KeyboardInterrupt), o programa exibe uma mensagem e encerra.
    """    

def adivinhar_letra(): # Função para adivinhar uma letra.
    while True: # Loop infinito até que o usuário digite uma letra válida.
        try: 
            palpite = input('Digite uma letra para adivinhar: ').lower()

        except KeyboardInterrupt: # Caso o usuário pressione Ctrl + C.
            print('\nTchau! Tente novamente.') 
            exit()
        
        if not palpite.isalpha() or len(palpite) != 1: # Caso o usuário digite mais de uma letra ou um caractere que não seja uma letra.
            print('Digite apenas uma única letra!')
        else: 
            return palpite # Retorna a letra digitada pelo usuário.

def jogar(): # Função principal do jogo.
    algumas_palavras = 'maça banana manga morango laranja uva abacaxi damasco limão coco melancia cereja mamão pera pêssego ameixa melão' 
    palavra = random.choice(algumas_palavras.split()) # Escolhe aleatoriamente uma palavra da lista.
    
    print('Adivinha a palavra! Dica: A palavra é o nome de uma fruta.')
    
    exibir_palavra(palavra, '') # Exibe a palavra com as letras adivinhadas.
    
    adivinhou_letra = '' # Variável para armazenar as letras adivinhadas.
    chances = len(palavra) + 2 # Quantidade de chances que o usuário tem para adivinhar a palavra.
    correto = 0 # Variável para armazenar a quantidade de letras adivinhadas corretamente.
    
    while chances > 0: # Loop até que o usuário acerte a palavra ou fique sem chances.
        print() 
        chances -= 1 # Diminui uma chance.
        
        palpite = adivinhar_letra() # Chama a função para adivinhar uma letra.
        
        if palpite in adivinhou_letra: # Caso o usuário digite uma letra que já foi adivinhada.
            print('Você já tentou essa letra!') 
            continue # Volta para o início do loop.
        
        if palpite in palavra: # Caso o usuário digite uma letra que está na palavra.
            adivinhou_letra += palpite * palavra.count(palpite) # Adiciona a letra adivinhada na variável.
            correto += palavra.count(palpite) # Adiciona a quantidade de letras adivinhadas corretamente.
        else: # Caso o usuário digite uma letra que não está na palavra.
            print('Palpite errado!') 
        
        exibir_palavra(palavra, adivinhou_letra) # Exibe a palavra com as letras adivinhadas.
        
        if correto == len(palavra): # Caso o usuário acerte a palavra.
            print('Parabéns, Você ganhou!')
            break # Sai do loop.
    
    if chances <= 0 and correto < len(palavra): # Caso o usuário fique sem chances.
        print('Você perdeu! Tente novamente...')
        print(f'A palavra era {palavra}') # Exibe a palavra correta.

if __name__ == '__main__': # Executa a função jogar() caso o arquivo seja executado diretamente.
    jogar() # Chama a função jogar().
