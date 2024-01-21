<div style="border: 0px solid #00f; padding: 10px; display: flex; justify-content: center;">
    <div style="box-shadow: 3px 3px 5px #888; display: flex; align-items: center; text-align: center; font-family: 'Verdana', sans-serif;">        
        <h1 style="margin: 0; text-shadow: 2px 2px 3px #888;">RenatoMor-DevProjects</h1>
    </div>
</div>

<br>
<div style="border: 0px solid #00f; padding: 10px; display: flex; align-items: center; justify-content: center; text-align: center; font-family: 'Lato', sans-serif;">
    <h2 style="margin: 0; text-shadow: 2px 2px 3px #888; font-family: 'Helvetica', sans-serif; text-decoration: none;">Jogo da forca em Python</h2>
</div>


<div style="border: 0px solid #00f; padding: 10px; display: flex; align-items: center; justify-content: center; text-align: center;">
    <div style="display: flex; align-items: center; justify-content: center;">
               <h4 style="margin: 0; text-shadow: 2px 2px 3px #888; font-family: 'Raleway', sans-serif;">I ❤️ Front-End Development!</h4>
    </div>
</div>


<h3>Encontre-me :handshake: </h3> 


<p align="center">
    <a href="https://www.linkedin.com/in/renatomoreira-rm/" target="_blank">
        <img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0077B5?style=plastic&logo=linkedin&logoColor=white">
    </a>
    <a href="https://github.com/RenatoMor" target="_blank">
        <img alt="GitHub" src="https://img.shields.io/badge/GitHub-181717?style=plastic&logo=github&logoColor=white">
    </a>
    <a href="https://discord.com/channels/@me/1123380010779152444/" target="_blank">
        <img alt="Discord" src="https://img.shields.io/badge/Discord-5865F2?style=plastic&logo=discord&logoColor=white">
    </a>
</a>
    <a href="https://kovihq.slack.com/" target="_blank">
        <img alt="Slack" src="https://img.shields.io/badge/Slack-4A154B?style=plastic&logo=slack&logoColor=white">
    </a>
    <a href="https://www.instagram.com/renatomorspider/" target="_blank">
        <img alt="Instagram" src="https://img.shields.io/badge/Instagram-E4405F?style=plastic&logo=instagram&logoColor=white">
    </a>
    <a href="mailto:piano.tato@gmail.com" target="_blank">
        <img alt="Gmail" src="https://img.shields.io/badge/Gmail-EA4335?style=plastic&logo=gmail&logoColor=white">
    </a>
</p>
</p>
<br>



## Menu

### • [Descrição](#descrição-footprints)

### • [Funcionalidades](#funcionalidades---footprints)

### • [Como Jogar](#como-jogar---footprints)

### • [Como Utilizar](#como-utilizar---footprints)

### • [Estrutura do Código](#estrutura-do-código---footprints)

### • [Licença](#licença-traffic_light)

### • [Agradecimentos](#agradecimentos-tada)



## Descrição :footprints:

O Jogo da Forca em Python é uma implementação simples do clássico jogo de palavras. Desenvolvido em Python, este projeto proporciona uma experiência interativa e divertida, desafiando os jogadores a adivinharem uma palavra letra por letra antes de serem "enforcados".

## Funcionalidades - :footprints:

- **Escolha Aleatória de Palavras:** O programa seleciona aleatoriamente palavras para garantir variedade e desafio.
 
- **Exibição Gráfica da Forca:** À medida que o jogador comete erros, uma figura da forca é progressivamente construída, proporcionando uma experiência visual.

- **Feedback Interativo:** Mensagens interativas informam o jogador sobre o progresso e os resultados de cada tentativa.
  
## Como Jogar - :footprints:

1. Execute o script Python **jogo_da_forca.py.**
2. O programa escolherá aleatoriamente uma palavra.
3. Tente adivinhar a palavra digitando uma letra por vez.
4. Você tem um número limitado de tentativas antes de ser "enforcado".
   
## Estrutura do Código - :footprints: 

### **1. Importação de Bibliotecas:**

```python
import random
from collections import Counter
```
**random:** Utilizado para escolher aleatoriamente uma palavra da lista.

**Counter:** Utilizado para contar a ocorrência de letras na palavra escolhida.

### 2. Definição da Função 

- `exibir_palavra(palavra, adivinhou_letra)`

```python
def exibir_palavra(palavra, adivinhou_letra):
    for letra in palavra:
        if letra in adivinhou_letra:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print()
```
- Essa função exibe a palavra oculta durante o jogo.
- Para cada letra na palavra:
  
    - Se a letra já foi adivinhada (letra in adivinhou_letra), ela é exibida.
    - Caso contrário, um underscore (_) é exibido.
  
- A função adiciona uma nova linha no final para melhor formatação.
### 3. Definição da Função 

-`adivinhar_letra()`
```python
def adivinhar_letra():
    while True:
        try:
            palpite = input('Digite uma letra para adivinhar: ').lower()
        except KeyboardInterrupt:
            print('\nTchau! Tente novamente.')
            exit()
        
        if not palpite.isalpha() or len(palpite) != 1:
            print('Digite apenas uma única letra!')
        else:
            return palpite
```
- Essa função obtém a entrada do usuário para adivinhar uma letra.
- Um loop ``while True`` garante que o código continue pedindo uma entrada até que uma entrada válida seja fornecida.
- O bloco ``try`` obtém a entrada do usuário e converte para minúsculas usando ``lower()`` para garantir consistência.
- Em caso de exceção (como ``KeyboardInterrupt``), o programa exibe uma mensagem e encerra.
- **adivinhacao(menor, maior)**

### 4. Definição da Função 

- ``jogar()``
```python
def jogar():
    algumas_palavras = 'maça banana manga morango laranja uva abacaxi damasco limão coco melancia cereja mamão pera pêssego ameixa melão'
    palavra = random.choice(algumas_palavras.split())
    
    print('Adivinha a palavra! Dica: A palavra é o nome de uma fruta.')
    
    exibir_palavra(palavra, '')
    
    adivinhou_letra = ''
    chances = len(palavra) + 2
    correto = 0
    
    while chances > 0:
        print()
        chances -= 1
        
        palpite = adivinhar_letra()
        
        if palpite in adivinhou_letra:
            print('Você já tentou essa letra!')
            continue
        
        if palpite in palavra:
            adivinhou_letra += palpite * palavra.count(palpite)
            correto += palavra.count(palpite)
        else:
            print('Palpite errado!')
        
        exibir_palavra(palavra, adivinhou_letra)
        
        if correto == len(palavra):
            print('Parabéns, Você ganhou!')
            break
    
    if chances <= 0 and correto < len(palavra):
        print('Você perdeu! Tente novamente...')
        print(f'A palavra era {palavra}')


```
- ``algumas_palavras`` é uma string contendo várias palavras de frutas.
  
- ``random.choice`` é usado para escolher aleatoriamente uma palavra da lista.
O jogo começa com a exibição da palavra oculta usando ``exibir_palavra``.

- Um loop ``while`` controla as tentativas do jogador.

- ``adivinhar_letra()`` é chamada para obter uma letra do usuário.

- Se a letra estiver correta, ela é adicionada a ``adivinhou_letr``a. Caso contrário, uma mensagem é exibida.

- ``exibir_palavra(palavra, adivinhou_letra)`` é chamada para exibir a palavra atualizada.

- O jogo continua até que o jogador adivinhe corretamente ou esgote suas chances.

- Uma mensagem final é exibida, indicando se o jogador venceu ou perdeu.
  
**" __ main __"**

Garante que o código em main() só será executado se o script for executado diretamente (não se for importado como um módulo em outro script). Isso é uma boa prática em Python para evitar a execução de código indesejado ao importar módulos.
```python
if __name__ == '__main__':

    jogar()
```

## Licença :traffic_light:
Este projeto está licenciado sob a Licença consulte o arquivo 
 [MIT](https://opensource.org/licenses/MIT).


## Agradecimentos :tada:

**Digital Innovation One:** Agradeço à Digital Innovation One por proporcionar recursos educacionais valiosos que contribuíram para o desenvolvimento dos meus projetos.

<a href="https://digitalinnovation.one/" target="_blank">
  <img src="https://digitalinnovationone.github.io/roadmaps/assets/logo-dio.svg" width="100" alt="Digital Innovation One">
</a>


**Python:**
Agradeço profundamente à comunidade Python e à equipe de desenvolvimento por criar uma linguagem poderosa, versátil e amigável. O Python tem sido uma ferramenta incrível que tornou possível transformar minhas ideias em realidade de maneira eficiente e elegante.

<a href="https://www.python.org/" target="_blank">
  <img src="https://www.python.org/static/community_logos/python-logo.png" width="100" alt="Python">
</a>


**VS Code:** Agradeço à equipe do Visual Studio Code pelo incrível editor que facilita o desenvolvimento deste projeto.

[<img src="https://code.visualstudio.com/assets/favicon.ico" width="30">](https://code.visualstudio.com/)


**GitHub:** Agradeço à equipe do GitHub por fornecer uma plataforma de desenvolvimento colaborativo que facilita o compartilhamento de projetos.

**HTML** Agradeço ao HTML, a linguagem fundamental que possibilita a estruturação e apresentação de conteúdo na web.

[<img src="https://www.w3.org/html/logo/downloads/HTML5_1Color_white.svg" width="50">](https://www.w3.org/TR/html52/)


**GitHub:** Agradeço à equipe do GitHub por fornecer uma plataforma de desenvolvimento colaborativo que facilita o compartilhamento de projetos.

[![GitHub](https://github.githubassets.com/favicons/favicon.png)](https://github.com/RenatoMor)

Copyright © 2024 / RenatoMor



[def]: #descricao---footprints