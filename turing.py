def resumo():
    mensagem = "Alan Mathison Turing foi um matemático britânico, pioneiro da computação e considerado o pai da ciência computacional e da inteligência artificial."
    return mensagem

def doutorado():
    mensagem = "Alan Turing concluiu seu doutorado na Universidade de Princeton em 1938, onde trabalhou sob a orientação de Alonzo Church. Durante seu doutorado, ele aprofundou sua pesquisa sobre lógica matemática e teoria da computação."
    return mensagem

def contribuicoes():
    mensagem = "Turing fez diversas contribuições notáveis, incluindo o conceito da 'Máquina de Turing', essencial para a teoria da computação. Ele também ajudou a decifrar os códigos alemães Enigma durante a Segunda Guerra Mundial, trabalho que foi fundamental para a vitória dos Aliados."
    return mensagem

def artigos():
    mensagem = "Alguns dos principais artigos de Turing incluem:\n- 'On Computable Numbers, with an Application to the Entscheidungsproblem' (1936)\n- 'Systems of Logic Based on Ordinals' (1938)\n- 'Computing Machinery and Intelligence' (1950), onde ele propõe o famoso 'Teste de Turing'."
    return mensagem

def citacoes():
    mensagem = "Citações de Alan Turing:\n- 'Uma máquina digital pode, se adequadamente programada, simular o comportamento de qualquer outra máquina digital.'\n- 'Podemos ver apenas um curto trecho do futuro, mas podemos ver o suficiente para perceber que há muito a ser feito.'"
    return mensagem

def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem

def erro():
    mensagem = "\nOpção inválida!"
    return mensagem



print("\nBoa noite! Você está aprendendo sobre Allan Turing.\n")

continuar = True
while continuar == True:

    opcao = int(
        input(
"""
\nDigite o número correspondente ao menu que você deseja acessar:
1 - Resumo
2 - Doutorado
3 - Contribuições
4 - Principais Artigos
5 - Citações
6 - Sair\n
"""
        )
    )

    if opcao == 1:
        print("1 - Resumo")
        mensagem = resumo()

    elif opcao == 2:
        print("2 - Doutorado")
        mensagem = doutorado()

    elif opcao == 3:
        print("3 - Contribuições")
        mensagem = contribuicoes()

    elif opcao == 4:
        print("4 - Principais Artigos")
        mensagem = artigos()

    elif opcao == 5:
        print("5 - Citações")
        mensagem = citacoes()

    elif opcao == 6:
        mensagem = sair()
        continuar = False

    else:
        mensagem = erro()

    print(mensagem)
