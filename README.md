<div style="border: 0px solid #00f; padding: 10px; display: flex; justify-content: center;">
    <div style="box-shadow: 3px 3px 5px #888; display: flex; align-items: center; text-align: center; font-family: 'Verdana', sans-serif;">        
        <h1 style="margin: 0; text-shadow: 2px 2px 3px #888;">RenatoMor-DevProjects</h1>
    </div>
</div>

<br>
<div style="border: 0px solid #00f; padding: 10px; display: flex; align-items: center; justify-content: center; text-align: center; font-family: 'Lato', sans-serif;">
    <h2 style="margin: 0; text-shadow: 2px 2px 3px #888; font-family: 'Helvetica', sans-serif; text-decoration: none;">Jogo de Adivinhação em Python</h2>
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

---

### Menu

**• [Descrição](#descrição---footprints)**

**• [Funcionalidades](#funcionalidades---footprints)**

**• [Como Jogar](#como-jogar---footprints)**

**• [Como Utilizar](#como-utilizar---footprints)**

**• [Estrutura do Código](#estrutura-do-código---footprints)**

**• [Licença](#licença-traffic_light)**

**• [Agradecimentos](#agradecimentos-tada)**


## Descrição :footprints:

Bem-vindo ao Jogo de Adivinhação em Python! Este projeto simples permite que você teste suas habilidades de adivinhação ao tentar adivinhar um número gerado aleatoriamente dentro de um intervalo definido.

## Funcionalidades - :footprints:

- Geração aleatória de um número dentro de um intervalo especificado.
- Feedback interativo durante as tentativas de adivinhação.
- Limite de tentativas baseado na fórmula logarítmica para uma experiência equilibrada.
- 
## Como Jogar - :footprints:

1. Execute o programa em um ambiente Python.
2. Insira o limite inferior quando solicitado.
3. Insira o limite superior quando solicitado.
4. Tente adivinhar o número gerado dentro do número máximo de tentativas.
   
## Como Utilizar - :footprints:

- Executar:
     
```python
python jogo_adivinhacao.py
```
- Exemplo de Uso:

```python
Insira o limite Baixo: 1
Insira o limite alto: 100

Você só tem 7 chances de adivinhar o número inteiro!

Adivinhe um número: 50
Você apostou muito alto!

Adivinhe um número: 25
Você apostou muito baixo!

Adivinhe um número: 37
Parabéns, ganhou em 3 tentativa(s)!
```
## Estrutura do Código - :footprints: 

#### **O código-fonte está organizado da seguinte forma:**

**jogo_adivinhacao.py:** O script principal que contém a lógica do jogo.

**funcoes.py:** Módulo contendo funções utilizadas no script principal.

### Detalhes das Funções

- **obter_limites()**

A função **obter_limites()** solicita ao usuário os limites inferior e superior do intervalo desejado e retorna esses valores.
```python
def obter_limites():
    menor = int(input("Insira o limite menor: "))
    maior = int(input("Insira o limite maior: "))
    return menor, maior
```

- **gerar_numero_aleatorio(menor, maior)**

A função **gerar_numero_aleatorio(menor, maior)** gera um número aleatório dentro do intervalo especificado pelos argumentos menor e maior.
```python
def gerar_numero_aleatorio(menor, maior):
    return random.randint(menor, maior)
```

- **calcular_max_tentativas(menor, maior)**

A função **calcular_max_tentativas(menor, maior)** calcula o número máximo de tentativas com base no intervalo definido por menor e maior, usando a fórmula logarítmica.
```python
def calcular_max_tentativas(menor, maior):
    return round(math.log(maior - menor + 1, 2))
```

- **adivinhacao(menor, maior)**

A função **adivinhacao(menor, maior)** implementa a lógica principal do jogo. Ela gera o número a ser adivinhado, define o número máximo de tentativas e interage com o usuário, fornecendo feedback durante as tentativas.
```python
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
```

- **main()**

A função **main()** inicia a execução do jogo, chamando as funções necessárias.
```python
def main():
    menor, maior = obter_limites()
    adivinhacao(menor, maior)
```
**" __ main __"**

Garante que o código em main() só será executado se o script for executado diretamente (não se for importado como um módulo em outro script). Isso é uma boa prática em Python para evitar a execução de código indesejado ao importar módulos.
```python
if __name__ == "__main__":
    main()
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

