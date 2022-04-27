from random import randint

mapa = [["A","A","A","A","A", "" ,"" ,"A","A","A","A","A"],
        ["A","","","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","" ,"" ,"" ,"A","" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","E","E","E","A","E","E","E","G","G","G","A"],
        ["A","" ,"" ,"" ,"A","G","G","G","G","G","G","A"],
        ["A","E","E","E","A","G","G","G","G","G","G","A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"G","G","G","A"],
        ["A","A","E","E","E","A","A","A","G","G","G","A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","E","" ,"E","E","" ,"E","E","E","E","E","A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" , "A"],
        ["A","A","A","A","A","A","G","G","G","E","E","A"],
        ["A","" ,"" ,"" ,"" ,"" ,"G","G","G","" ,"" ,"A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","E","E","" ,"" ,"E","E","E","E","E","E","A"],
        ["A","" ,"G","G","G","G","" ,"" ,"G","G","G","A"],
        ["A","G","G","G","" ,"" ,"" ,"G","G","" ,"" ,"A"],
        ["A","A","A","A","A","A","G","A","A","A","A","A"]]

pokemon = ["Ratata", "Pidgey", "Weedle", "Caterpie", "Paras", "Charmander", "Bulbasaur", "Squirtle", "Pikachu", "Evee"]
pokedex = {}
stats = {"HP": 0, "Atk": 0, "Def": 0, "Sp. Atk": 0, "Sp. Def" : 0, "Speed": 0}

lAtual = 19
cAtual = 6
posAtual = mapa[lAtual][cAtual]

def aleatorio(valor):
    return randint(0,valor)

def menu():
    print("\nBem-vindo!\nA qualquer momento você pode escolher uma das opções:\n9 - Para abrir esse menu\n8 - Subir\n2- Descer\n4 - Ir para esquerda\n6 - Ir para direta\n5 - Abrir Pokedex\n0 - Sair do Jogo")
    opcao = int(input())

    if opcao == 9:
        menu()

    elif opcao == 8:
        andarCima()
        
    elif opcao == 2:
        andarBaixo()

    elif opcao == 4:
        andarEsq()

    elif opcao == 6:
        andarDir()

    elif opcao == 5:
        menuPokedex()
        
    elif opcao == 0:
        foraMapa()
        
    else:
        opcaoInv()
        
def andarCima():
    global lAtual
    global cAtual
    if lAtual - 1 == -1 and cAtual == 6 or lAtual - 1 == -1 and cAtual == 5:
        foraMapa()
    if mapa[lAtual-1][cAtual] != "A" and mapa[lAtual-1][cAtual] != "E":
        lAtual = lAtual - 1
        posAtual = mapa[lAtual][cAtual]
        print("\nSua posição atual: {} e {}".format(lAtual,cAtual))
        grama()
        menu()
    else:
        bump()

def andarBaixo():
    global lAtual
    global cAtual
    if lAtual + 1 == 20 and cAtual == 6:
        foraMapa()
    if mapa[lAtual+1][cAtual] != "A":
        lAtual = lAtual + 1
        posAtual = mapa[lAtual][cAtual]
        print("\nSua posição atual: {} e {}".format(lAtual,cAtual))
        grama()
        menu()
    else:
        bump()

def andarEsq():
    global lAtual
    global cAtual

    if mapa[lAtual][cAtual-1] != "A" and mapa[lAtual][cAtual-1] != "E":
        cAtual = cAtual - 1
        posAtual = mapa[lAtual][cAtual]
        print("\nSua posição atual: {} e {}".format(lAtual,cAtual))
        grama()
        menu()
    else:
        bump()

def andarDir():
    global lAtual
    global cAtual

    if mapa[lAtual][cAtual+1] != "A" and mapa[lAtual][cAtual+1] != "E":
        cAtual = cAtual + 1
        posAtual = mapa[lAtual][cAtual]
        print("\nSua posição atual: {} e {}".format(lAtual,cAtual))
        grama()
        menu()
    else:
        bump()

def opcaoInv():
    print("Insira uma opção válida!")
    menu()

def foraMapa():
    print("Fim de jogo!")
    exit()

def bump():
    print("Bump!")
    menu()

def grama():
    if mapa[lAtual][cAtual] == "G":
        prob = aleatorio(1)
        if prob == 0:
            print("\nUm pokemon selvagem apareceu!\nCapturar ou correr? [1-Capturar ou 2-Correr]")
            opPok = int(input())
            if opPok == 1:
                aleaPok = aleatorio(9)
                if pokemon[aleaPok] in pokedex:
                    print("Pokemon já capturado")
                else:
                    pokedex[pokemon[aleaPok]] = stats.copy()

                    pokedex[pokemon[aleaPok]]["HP"] = aleatorio(99)
                    pokedex[pokemon[aleaPok]]["Atk"] = aleatorio(99)
                    pokedex[pokemon[aleaPok]]["Def"] = aleatorio(99)
                    pokedex[pokemon[aleaPok]]["Sp. Atk"] = aleatorio(99)
                    pokedex[pokemon[aleaPok]]["Sp. Def"] = aleatorio(99)
                    pokedex[pokemon[aleaPok]]["Speed"] = aleatorio(99)
                

            elif opPok == 2:
                print("\nFujão!")

            else:
                opPok = int(input("Insira uma opção válida!"))
                
        else:
            return menu()

def menuPokedex():
    print(pokedex.keys())
    print("Digite 1 para Listar\nDetalhes 2 para Apagar Registro \n0 para voltar ao menu principal \nEscolha uma ação:")
    acao = int(input())
    if acao == 1:
        pokNome = input("Insira o nome do pokemon em questão:")
        print(pokedex[pokNome])
        return menu()
        
    elif acao == 2:
        pokNome = input("Insira o nome do pokemon em questão:")
        pokedex.pop(pokNome)
        return menu()
        
    elif acao == 0:
        return menu()

    else:
        int(input("Insira uma ação válida:"))
        
print("Entrando na Rota 1")
menu()
