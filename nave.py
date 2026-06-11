##Definir as variaveis
combustivel = 100
tripulantes = []

##Definir funcoes:

def viajar():
    ##aqui vamos gastar combustivel
    global combustivel ##Avisa que vamos modificar uma variavel externa
    if(combustivel>=30):
        combustivel = combustivel - 30
        print("A nave viajou")
    else:
        print("Você está sem combustivel suficiente.Abasteça!")

def abastecer():
    global combustivel
    combustivel = 100
    print("Tanque cheio!")

def status_nave():
    print("----- STATUS DA NAVE -----")
    print(f"Temos {combustivel} de cumbustivel")
    print(f"Os tripulantes sao: {tripulantes}")
    print("-------------------------- \n")

def registrarTripulante():
    ##Essa funcao pergunta o nome do tripulante e ad0iciona na lista de tripulantes
    novotripulante = input("Qual o nome do novo tripulante?: ")
    tripulantes.append(novotripulante)
    print("Tripulante inserido com sucesso! ")


##cria uma função que tira o ultimo tripulante
def tirarTripulante():
    tripulantes.pop()
    print("Tripulante removido ")


## criar um menu

while True:
    print("\nBem vindo ao menu interativo da nave. Por favor selecione uma opção:")
    print("\n1- Mostrar status da nave| 2- Viajar | 3- Abastecer | 4- Novo Tripulante | 5- Sair | 6- tirarTripulante")
    opcao = input("Escolha: ")
    if (opcao == "1"):
        status_nave()
    elif (opcao == "2"):
        viajar()
    elif (opcao =="3"):
        abastecer()
    elif (opcao =="4"):
        registrarTripulante()
    elif (opcao =="5"):
        print("Viagem encerrada!")
        break
    elif (opcao =="6"):
        if len(tripulantes) ==0:
          print("nenhum tripulante foi removido pois não há tripulantes")
        else:
           tirarTripulante()


