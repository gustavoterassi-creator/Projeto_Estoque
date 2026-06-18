## kauan me ajudou 


estoqueP = [
    [1,"Teclado",4,"Prateleira 01"],
    [2,"Mouse",3,"Prateleira 02"],
    [3,"Monitor",2,"Prateleira 03"],
    [4,"Mouse pad",3,"Prateleira 04"]
]
for linha in estoqueP:
    print(linha)


def registrarProduto():
    novoproduto = input("Qual o nome do novo produto?: ")
    idProduto = input("Qual o id do produto: ")
    quantidadesdp = input("Qual a quantidade dos produtos: ")
    localizaçaop = input("Qual a localizaçao do pruduto:")
    estoqueP.append([novoproduto,idProduto,quantidadesdp,localizaçaop])
    print("Produto inserido com sucesso! ")

def idProdutos():
    idProduto = int(input("Qual o id do produto:"))
    linhaProcurada = -1
    for i in range(len(estoqueP)):
         if(estoqueP[i][0] == idProdutos):
            linhaProcurada = i
    print(f"O produto é {estoqueP[linhaProcurada]}")
 
 
def listaP():
    print("----- Produtos -----")
    print(f"Temos {estoqueP} de estoque disponivel:")
    print("--------------------------")

def atualizarE():
   idProdutos = int(input("Qual o id do produto?"))
   linhaprocurada = -1
   for i in range(len(estoqueP)):
       if(estoqueP[i][0] == idProdutos):
           linhaProcurada = i

   print("a atualização do produto é {estoqueP[linhaprocurada]}")
   quantidade = int(input("Qual a quantidade?: "))
   estoqueP[linhaProcurada][2] = quantidade



while True:
    print("\nBem vindo ao menu interativo do estoque. Por favor selecione uma opção:")
    print("\n1- NovoProduto| 2-idProdutos | 3-lista produtos| 4- atualizarE | 5- Sair:")
    opcao = input("Escolha: ")
    if (opcao == "1"):
        registrarProduto()
    elif (opcao == "2"):
        idProdutos()
    elif (opcao =="3"):
        listaP()
    elif (opcao =="4"):
        atualizarE()
    elif (opcao =="5"):
        print("Saindo do estoque!!!🚀")
        break
    
       
       


    







 
 
 
 
