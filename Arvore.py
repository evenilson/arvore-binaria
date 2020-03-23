

import time

#************************************************* CLASSE PARA OS NÓS ********************************************#
class Node:
     
    def __init__(self, chave, direitinha, esquerdinha):
        self.valor = chave
        self.dir = direitinha
        self.esq = esquerdinha
#*************************************************** FINAL DA CLASSE *********************************************#


#************************************************* CLASSE PARA AS ÁRVORES ****************************************#
class Tree:

    def __init__(self):
        self.raiz = Node(None,None,None)
        self.raiz = None

  #------------------------------------------------------ INSERIR ----------------------------------------------#
    def insert(self, valor):
        novo = Node(valor,None,None) 
        if self.raiz == None:
            self.raiz = novo
        else: 
            atual = self.raiz
            while True:
                anterior = atual
                if valor <= atual.valor: 
                    atual = atual.esq
                    if atual == None:
                        anterior.esq = novo
                        return             
                else: 
                    atual = atual.dir
                    if atual == None:
                        anterior.dir = novo
                        return
  #---------------------------------------------------------------------------------------------------------------#

  #------------------------------------------------------ BUSCAR -------------------------------------------------#                
    def search(self, chave):
        if self.raiz == None:
            return None 
        atual = self.raiz 
        while atual.valor != chave: 
            if chave < atual.valor:
                atual = atual.esq 
            else:
                atual = atual.dir 
                if atual == None:
                    return None
        return atual   
  #---------------------------------------------------------------------------------------------------------------#

  #---------------------------------------------------- NO SUCESSOR-----------------------------------------------#
    def noSucessor(self, apaga): 
        paidosucessor = apaga
        sucessor = apaga
        atual = apaga.dir

        while atual != None: 
            paidosucessor = sucessor
            sucessor = atual
            atual = atual.esq 

        if sucessor != apaga.dir: 
            paidosucessor.esq = sucessor.dir 
            sucessor.dir = apaga.dir 

        return sucessor
  #---------------------------------------------------------------------------------------------------------------#

  #---------------------------------------------------- -REMOVER -------------------------------------------------#
    def searchAndRemove(self, valor):
        if self.raiz == None:
            return False 
        atual = self.raiz
        pai = self.raiz
        filhoEsq = True


        # ********************* Buscando o valor *************************
        while atual.valor!= valor:
            pai = atual
            if valor < atual.valor: 
                atual = atual.esq
                filhoEsq = True 
            else: 
                atual = atual.dir 
                filhoEsq = False 
            if atual == None:
                return False
         
        if atual.esq == None and atual.dir == None:
            if atual == self.raiz:
                self.raiz = None 
            else:
                if filhoEsq:
                    pai.esq =  None 
                else:
                    pai.dir = None 

        elif atual.dir == None:
            if atual == self.raiz:
                self.raiz = atual.esq 
            else:
                if filhoEsq:
                    pai.esq = atual.esq 
                else:
                    pai.dir = atual.esq 
         
        elif atual.esq == None:
            if atual == self.raiz:
                self.raiz = atual.dir 
            else:
                if filhoEsq:
                    pai.esq = atual.dir
                else:
                    pai.dir = atual.dir 

        else:
            sucessor = self.noSucessor(atual)
            if atual == self.raiz:
                self.raiz = sucessor
            else:
                if filhoEsq:
                    pai.esq = sucessor 
                else:
                    pai.dir = sucessor 
            sucessor.esq = atual.esq   

        return True
  #---------------------------------------------------------------------------------------------------------------#
     
#*************************************************** FINAL DA CLASSE *********************************************#


#************************************************* INICIO DA PRINCIPAL *******************************************#
arvore = Tree()
opcao = 0
while opcao != 4:
    print("+--------------------------------->>> ARVORE DE BUSCA BINÁRIA <<<---------------------------------+")
    print("|                                                                                                 |")
    print("|                                                                                                 |")
    print("|                                     +----------------------+                                    |")
    print("|                                     |     1 - INSERIR      |                                    |")
    print("|                                     +----------------------+                                    |")
    print("|                                     |     2 - EXCLUIR      |                                    |")
    print("|                                     +----------------------+                                    |")
    print("|                                     |     3 - BUSCAR       |                                    |")
    print("|                                     +----------------------+                                    |")
    print("|                                     |     4 - SAIR         |                                    |")
    print("|                                     +----------------------+                                    |")
    print("|                                                                                                 |")
    print("|                                                                                                 |")
    print("+------------------------------------------------------------------------------------------------+|")
    opcao = int(input("-> "))
    if opcao == 1:
        valor = int(input(" DIGITE O VALOR QUE DESEJA INSERIR -> "))
        arvore.insert(valor)
        print(" -------------> O VALOR FOI INSERDO <-------------")
        print(" -------->>> ESTAMOS VOLTANDO PRO MENU <<<--------")
        time.sleep(4) 
    
    elif opcao == 2:
        valor = int(input(" DIGITE O VALOR QUE DESEJA EXCLUIR -> "))
        if arvore.searchAndRemove(valor) == True:
            print(" --------> REMOVIDO COM SUCESSO <--------")
        else:
            print(" ------> O VALOR NÃO FOI ENCONTRADO <-----")
        print(" ---->>> ESTAMOS VOLTANDO PRO MENU <<<----")
        time.sleep(4) 

    elif opcao == 3:
        valor = int(input(" DIGITE O VALOR QUE DESEJA BUSCAR -> "))
        if arvore.search(valor) != None:
            print(" ---------> O NUMÉRO ", valor ,"FOI ENCONTRADO NA ARVORE <-------------")
        else:
            print(" --------> O NUMÉRO ", valor,"NÃO FOI ENCONTRADO NA ARVORE <--------")
        print(" ----------->>> ESTAMOS VOLTANDO PRO MENU <<<--------------")
        time.sleep(4) 
    elif opcao == 4:
        break
#********************************************************* FIM **************************************************#