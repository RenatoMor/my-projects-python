import random
import math

#! Entrada de Limites:------------------------------------------------

def obter_limites():
    menor = int(input("Insira o limite menor: "))
    maior = int(input("Insira o limite maior: "))
    return menor, maior 

#! Geração do Número a Ser Adivinhado:--------------------------------

def gerar_numero_aleatorio(menor, maior):
    return random.randint(menor, maior)

#! Cálculo do Número Máximo de Tentativas:----------------------------

def calcular_max_tentativas(menor, maior):
    return round(math.log(maior - menor + 1, 2))

#! Loop de Adivinhação:-----------------------------------------------

def adivinhacao(menor, maior):
    x = gerar_numero_aleatorio(menor, maior)
    max_tentativas = calcular_max_tentativas(menor, maior)

    print(f"\nVocê só tem {max_tentativas} chances de adivinhar o número inteiro!\n")

    for tentativa in range(1, max_tentativas + 1):
        adivinhar = int(input("Adivinhe um número: "))

        if x == adivinhar:
            print(f"Parabéns, você fez isso em {tentativa} tentativa(s)!")
            return

        elif x > adivinhar:
            print("Você adivinhou muito pequeno!")
        elif x < adivinhar:
            print("Você acertou muito alto!")

    print(f"\nO número era {x}")
    print("Melhor sorte da próxima vez!")

#! Função Principal:--------------------------------------------------

def main():
    menor, maior = obter_limites()
    adivinhacao(menor, maior)

#! Execução:----------------------------------------------------------

if __name__ == "__main__":
    main()
