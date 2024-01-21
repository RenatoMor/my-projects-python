import random
import math

#! Entrada de Limites:------------------------------------------------

menor = int(input("Insira o limite menor:- "))
maior = int(input("Insira o limite maior:- "))

#! Gerando número aleatório entre o maior e o menor:------------------

x = random.randint (menor, maior)

#! Cálculo do Número Máximo de Tentativas:----------------------------

print("\n\tVocê só tem ",
round(math.log(maior - menor + 1, 2)),
" chances de adivinhar o número inteiro!\n")

#! Loop de Adivinhação::----------------------------------------------

contagem = 0

#? Cálculo do número mínimo de suposições dependem do intervalo:------
while contagem <math.log(maior - menor + 1, 2):

    contagem += 1

#! Pegando o número adivinhado como entrada:--------------------------
    
    adivinhar = int(input("Adivinhe um número:- "))

#! Teste de condição:-------------------------------------------------
    
    if x == adivinhar:
        print("Parabéns, você fez isso em ", contagem, "tentar")
        break
    elif x > adivinhar:
        print("Você adivinhou muito pequeno!")
    elif x < adivinhar:
        print("Você acertou muito alto!")

#! Se adivinhar for mais do que as suposições necessárias,
#! mostra esta saída.
        
if contagem >= math.log(maior - menor + 1, 2):
    print("\nO número é %d" % x)
print("\tMelhor sorte da próxima vez!")