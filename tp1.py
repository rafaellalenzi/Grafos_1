import numpy as np
import random as random

class Grafo():
    def __init__(self, tipo_grafo, txt):
        if tipo_grafo == "matriz":
            self.grafo = GrafoMatriz(txt)
        if tipo_grafo =="lista":
            self.grafo = GrafoLista(txt)
              
class GrafoMatriz():
   
    def __init__(self,txt):
        arquivo = open(txt, 'r')
        
        self._vertices = int(arquivo.readline())         #Total de vertices
        self._arestas = 0
        self._matriz = np.zeros([self._vertices, self._vertices], dtype = int)
        #A matriz começa em 0, portanto os vértices serão representados na matriz com a posição "Vértice - 1"
        for linha in arquivo: #Criar Matrizes
            split = linha.split()
            self._matriz[int(linha.split()[0])-1][int(linha.split()[1])-1] = 1
            self._matriz[int(linha.split()[1])-1][int(linha.split()[0])-1] = 1 
            self._arestas += 1 #Total de arestas
        
        arquivo.close()
            
    def vertices(self):
        return self._vertices
    
    def arestas(self):
        return self._arestas
    
    def grau_max(self):
        soma = np.sum(self._matriz, axis= 0)
        grau_max = np.argmax(soma)
        return soma[grau_max]
    
    def grau_min(self):
        soma = np.sum(self._matriz, axis= 0)
        grau_min = np.argmin(soma)
        return soma[grau_min]

    def grau_med(self):
        soma = np.sum(self._matriz, axis= 0)
        soma2 = np.sum(soma, axis= 0)
        grau_med = soma2/self.vertices
        return grau_med
    
    def grau_median(self):
        soma = np.sum(self._matriz, axis= 0)
        grau_median = np.median(soma)
        return int(grau_median)
            
    def busca_largura(self,raiz,nome_arquivo,print):
        vetor_marcacao = np.zeros(self._vertices, dtype = int) #Lembrando novamente que o vertice X estará na posição X-1
        vetor_graus = np.array([-1] * self._vertices, dtype = int) #Lembrando novamente que o vertice X estará na posição X-1
        vetor_pais = np.array([-1] * self._vertices, dtype = int) #Lembrando novamente que o vertice X estará na posição X-1
        fila_execucao = []
        vetor_marcacao[raiz-1] = 1
        vetor_pais[raiz-1] = 0
        vetor_graus[raiz-1] = 0
        fila_execucao.append(raiz)
        while fila_execucao != []:
            pai = fila_execucao.pop(0)
            vizinhos = self.retorna_vizinhos(pai)
            for w in vizinhos:
                if vetor_marcacao[w-1] == 0:
                    vetor_marcacao[w-1] = 1
                    vetor_pais[w-1] = pai
                    vetor_graus[w-1] = vetor_graus[pai-1] + 1 
                    fila_execucao.append(w) 

        if print == 1:          
            self.escrever_busca(nome_arquivo, vetor_graus, vetor_pais)
        # -1 = fora da componente conexa; 0 = raiz ; >= 1 = valor do vértice pai
        return [vetor_pais,vetor_graus]
        
    def retorna_vizinhos(self,vertice):
        vizinhos = []
        linha_vertice = self._matriz[vertice - 1]
        indice = 1
        for i in linha_vertice:
            if i == 1:
                vizinhos.append(indice)
            indice += 1
        return vizinhos

    def busca_profundidade(self,raiz,nome_arquivo, print):
        vetor_marcacao = np.zeros(self._vertices, dtype = int) #Lembrando novamente que o vertice X estará na posição X-1
        pilha_execucao = [raiz]
        vetor_graus = np.array([-1] * self._vertices, dtype = int) #Lembrando novamente que o vertice X estará na posição X-1
        vetor_pais = np.array([-1] * self._vertices, dtype = int) #Lembrando novamente que o vertice X estará na posição X-1
        vetor_pais[raiz-1] = 0
        vetor_graus[raiz-1] = 0
        while pilha_execucao != []:
            pai = pilha_execucao.pop(-1)
            if vetor_marcacao[pai-1] == 0:
                vetor_marcacao[pai-1] = 1
                vizinhos = self.retorna_vizinhos(pai)
                for w in reversed(vizinhos):
                    pilha_execucao.append(w)
                    if vetor_marcacao[w-1] == 0:
                        vetor_pais[w-1] = pai
                        vetor_graus[w-1] = vetor_graus[pai-1] + 1
        if print == 1:
            self.escrever_busca(nome_arquivo, vetor_graus, vetor_pais)
        
        return vetor_pais # -1 = fora da componente conexa; 0 = raiz ; >= 1 = valor do vértice pai

    def escrever_busca(self, nome_arquivo, vetor_graus, vetor_pais):
        arquivo = open(nome_arquivo, 'w', encoding = "utf-8")
        escrita = ''
        for v in range(self._vertices):
            escrita += f'Vértice: {v+1} - Nivel: {vetor_graus[v]}\n'
        escrita +=  '\nVetor de pais: \n'
        escrita += f' {str(list(range(1,self._vertices + 1))).replace(", ","  ")[1:-1]}\n'
        escrita += str(vetor_pais)[1:-1]
        arquivo.write('Se o Nivel é -1 o vértice fora da componente conexa\n\n'+f'{escrita}')
        arquivo.close()
          
          
          
    def distancia(self,partida, chegada):
        vetor_pais = self.busca_largura(partida,'dump.txt',0)[0]

        atual = chegada
        distancia = 0
        while atual != partida:
            atual = vetor_pais[atual - 1]
            if atual == -1:
                return atual
            distancia += 1
        return distancia
    
    def componentes_conexas(self, nome_arquivo):
        componentes_conexas = []
        vetor_pais = np.array([-1] * self._vertices, dtype = int) #Lembrando novamente que o vertice X estará na posição X-1
        
        vetor_pais[0] = 0
        for i in range(1, self._vertices + 1):
            if vetor_pais[i-1] == -1:
                pilha_execucao = [i]
                vetor_marcacao = np.zeros(self._vertices, dtype = int) #Lembrando novamente que o vertice X estará na posição X-1
                while pilha_execucao != []:
                    pai = pilha_execucao.pop(-1)
                    if vetor_marcacao[pai-1] == 0:
                        vetor_marcacao[pai-1] = 1
                        vizinhos = self.retorna_vizinhos(pai)
                        for w in reversed(vizinhos):
                            pilha_execucao.append(w)
                            if vetor_marcacao[w-1] == 0:
                                vetor_pais[w-1] = pai
                componentes_conexas.append(vetor_marcacao)

        self.escrever_componentes(nome_arquivo, componentes_conexas)

    def escrever_componentes(self, nome_arquivo, componentes):
        arquivo = open(nome_arquivo, 'w', encoding = "utf-8")
        arquivo.write(f'Total de componentes conexas:{len(componentes)}\n\n')

        tratadas = []
        for componente in componentes:
            lista_vertices = []
            for i in range(len(componente)):
                if componente[i] == 1:
                    lista_vertices.append(i + 1)
            tratadas.append(lista_vertices)
        
        tratadas = sorted(tratadas, key = lambda x: len(x), reverse= True)
        for i in tratadas:
            arquivo.writelines(f'Tamanho da componente: {len(i)} - Vértices: {i}\n')
        arquivo.close()

class ListaVizinhos:
    #Cada lista dessa classe representa a lista de vizinhos de um vértice
    #Cada lista dessas será um elemento do vetor de vértices da lista de adjacência
    def __init__(self):
        self.head = None
        self.size = 0
    def add(self, vizinho):
        vizinho.proximo = self.head
        self.head = vizinho
        self.size += 1


class Vizinho:
    #Cada vizinho dessa classe será um nó da lista de vizinhos
    def __init__(self, vizinho):
        self.vizinho = vizinho
        self.proximo = None
    def __repr__(self):
        return (self.vizinho)

class GrafoLista():
    def __init__(self,txt):
        arquivo = open(txt, 'r')
        self._vertices = int(arquivo.readline())         #Total de vertices
        self._arestas = 0
        self._vetor = []
        for vertice in range(self._vertices):    #Inicializando as listas
            self._vetor.append(ListaVizinhos())
        for linha in arquivo:   #Adicionando vizinhos às listas
            split = linha.split()
            self._vetor[int(linha.split()[0])-1].add(Vizinho(int(linha.split()[1])))
            self._vetor[int(linha.split()[1])-1].add(Vizinho(int(linha.split()[0])))
            self._arestas += 1 #Total de arestas
        arquivo.close

    def vertices(self):
        return self._vertices
    
    def arestas(self):
        return self._arestas
    
    def graus(self):
        graus = np.zeros(self._vertices, dtype = int)
        vertice = 0
        for lista in self._vetor:
            graus[vertice] = lista.size
            vertice+=1
        return graus
    def grau_max(self):
        graus = self.graus()
        return graus.max()
    
    def grau_min(self):
        graus = self.graus()
        return graus.min()

    def grau_med(self):
        graus = self.graus()
        return graus.mean()
    
    def grau_median(self):
        graus = self.graus()
        mediana = np.median(graus, axis=0)
        return int(mediana)

    def busca_largura(self,raiz,nome_arquivo, print):
        vetor_marcacao = np.zeros(self._vertices, dtype = int) #Lembrando novamente que o vertice X estará na posição X-1
        vetor_graus = np.array([-1] * self._vertices, dtype = int) #Lembrando novamente que o vertice X estará na posição X-1
        vetor_pais = np.array([-1] * self._vertices, dtype = int) #Lembrando novamente que o vertice X estará na posição X-1
        fila_execucao = [raiz]
        vetor_marcacao[raiz-1] = 1
        vetor_pais[raiz-1] = 0
        vetor_graus[raiz-1] = 0
        while fila_execucao != []:
            pai = fila_execucao.pop(0)
            lista_vertice = self._vetor[pai - 1]
            proximo_vizinho = lista_vertice.head
            while proximo_vizinho != None:
                w = proximo_vizinho.vizinho
                if vetor_marcacao[w-1] == 0:
                    vetor_marcacao[w-1] = 1
                    vetor_pais[w-1] = pai
                    vetor_graus[w-1] = vetor_graus[pai-1] + 1 
                    fila_execucao.append(w)
                proximo_vizinho = proximo_vizinho.proximo

        if print == 1:            
            self.escrever_busca(nome_arquivo, vetor_graus, vetor_pais)
        # -1 = fora da componente conexa; 0 = raiz ; >= 1 = valor do vértice pai
        return [vetor_pais,vetor_graus] 
        
    def busca_profundidade(self,raiz,nome_arquivo, print):
        vetor_marcacao = np.zeros(self._vertices, dtype = int) #Lembrando novamente que o vertice X estará na posição X-1
        pilha_execucao = [raiz]
        vetor_graus = np.array([-1] * self._vertices, dtype = int) #Lembrando novamente que o vertice X estará na posição X-1
        vetor_pais = np.array([-1] * self._vertices, dtype = int) #Lembrando novamente que o vertice X estará na posição X-1
        vetor_pais[raiz-1] = 0
        vetor_graus[raiz-1] = 0
        while pilha_execucao != []:
            pai = pilha_execucao.pop(-1)
            if vetor_marcacao[pai-1] == 0:
                vetor_marcacao[pai-1] = 1
                lista_vertice = self._vetor[pai - 1]
                proximo_vizinho = lista_vertice.head 
                while proximo_vizinho != None:
                    w = proximo_vizinho.vizinho
                    pilha_execucao.append(w)
                    if vetor_marcacao[w-1] == 0:
                        vetor_pais[w-1] = pai
                        vetor_graus[w-1] = vetor_graus[pai-1] + 1
                    proximo_vizinho = proximo_vizinho.proximo

        if print == 1:
            self.escrever_busca(nome_arquivo, vetor_graus, vetor_pais)
        
        return vetor_pais # -1 = fora da componente conexa; 0 = raiz ; >= 1 = valor do vértice pai
    def escrever_busca(self, nome_arquivo, vetor_graus, vetor_pais):
        arquivo = open(nome_arquivo, 'w', encoding = "utf-8")
        escrita = ''
        for v in range(self._vertices):
            escrita += f'Vértice: {v+1} - Nivel: {vetor_graus[v]}\n'
        escrita +=  '\nVetor de pais: \n'
        escrita += f' {str(list(range(1,self._vertices + 1))).replace(", ","  ")[1:-1]}\n'
        escrita += str(vetor_pais)[1:-1]
        arquivo.write('Se o Nivel é -1 o vértice fora da componente conexa\n\n'+f'{escrita}')
        arquivo.close()
          
          
    def distancia(self,partida, chegada):
        vetor_pais = self.busca_largura(partida,'dump.txt',0)[0]

        atual = chegada
        distancia = 0
        while atual != partida:
            atual = vetor_pais[atual - 1]
            if atual == -1:
                return atual
            distancia += 1
        return distancia

    def diametro(self):
        if self._vertices < 1000:
            diametro = 0
            for linha in range(self._vertices):
                vetor_graus = self.busca_largura(linha+1,'dump.txt',0)[1] #Lembrando novamente que o vertice X estará na posição X-1
                maior=np.max(vetor_graus)
                if maior > diametro:
                    diametro = maior
        else:
            diametro = 0
            for i in range(1500):
                vertice = random.randint(1, self._vertices)
                print(vertice)
                vetor_graus = self.busca_largura(vertice, 'dump.txt',0)[1] 
                maior=np.max(vetor_graus)
                if maior > diametro:
                    diametro = maior
                
        return diametro

    
    def componentes_conexas(self, nome_arquivo):
        componentes_conexas = []
        vetor_pais = np.array([-1] * self._vertices, dtype = int) #Lembrando novamente que o vertice X estará na posição X-1
        
        vetor_pais[0] = 0
        for i in range(1, self._vertices + 1):
            if vetor_pais[i-1] == -1:
                pilha_execucao = [i]
                vetor_marcacao = np.zeros(self._vertices, dtype = int) #Lembrando novamente que o vertice X estará na posição X-1
                while pilha_execucao != []:
                    pai = pilha_execucao.pop(-1)
                    if vetor_marcacao[pai-1] == 0:
                        vetor_marcacao[pai-1] = 1
                        lista_vertice = self._vetor[pai - 1]
                        proximo_vizinho = lista_vertice.head 
                        while proximo_vizinho != None:
                            w = proximo_vizinho.vizinho
                            pilha_execucao.append(w)
                            if vetor_marcacao[w-1] == 0:
                                vetor_pais[w-1] = pai
                            proximo_vizinho = proximo_vizinho.proximo
                componentes_conexas.append(vetor_marcacao)

        self.escrever_componentes(nome_arquivo, componentes_conexas)

        return componentes_conexas

    def escrever_componentes(self, nome_arquivo, componentes):
        arquivo = open(nome_arquivo, 'w', encoding = "utf-8")
        arquivo.write(f'Total de componentes conexas:{len(componentes)}\n\n')

        tratadas = []
        for componente in componentes:
            lista_vertices = []
            for i in range(len(componente)):
                if componente[i] == 1:
                    lista_vertices.append(i + 1)
            tratadas.append(lista_vertices)
        
        tratadas = sorted(tratadas, key = lambda x: len(x), reverse= True)
        for i in tratadas:
            arquivo.writelines(f'Tamanho da componente: {len(i)} - Vértices: {i}\n')
        arquivo.close()
