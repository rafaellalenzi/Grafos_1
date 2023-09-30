# Imports
from grafos import Grafo
import time
import psutil
import random

#Conversão mb <> b
MB = 1048576
 
#Grafo a ser analisado: 
grafo_atual = 'grafo_5' #Basta mudar o número após o '_' para alterar o grafo.

#QUESTAO 1

# Matriz de Adjacencia
#mem_antes_matriz = psutil.virtual_memory()._asdict()['available']
#grafo_matriz = Grafo('matriz',f'{grafo_atual}.txt').grafo
#mem_depois_matriz = psutil.virtual_memory()._asdict()['available']
#consumo_matriz = mem_antes_matriz - mem_depois_matriz
#print('Memoria utilizada pela matriz:', consumo_matriz/MB, 'Megabytes')

# Lista de Adjacencia
mem_antes_lista = psutil.virtual_memory()._asdict()['available']
grafo_lista = Grafo('lista',f'{grafo_atual}.txt').grafo
mem_depois_lista = psutil.virtual_memory()._asdict()['available']
consumo_lista = mem_antes_lista - mem_depois_lista
print('Memoria utilizada pela lista:', consumo_lista/MB, 'Megabytes')

grau_max=grafo_lista.grau_max()
grau_min=grafo_lista.grau_min()
grau_medio=grafo_lista.grau_med()
grau_mediano=grafo_lista.grau_median()
print (f'Grau medio = {grau_medio} \n Grau mediano = {grau_mediano} \n Grau maximo = {grau_max} \n Grau minimo = {grau_min}\n')

numero_vertices = grafo_lista.vertices()
numero_arestas = grafo_lista.arestas()
print (f'Numero de arestas = {numero_arestas} \n Numero de vertices = {numero_vertices}')

#QUESTAO 2
arquivo = open(f'tempo_buscas_largura_{grafo_atual}.txt','w')
#arquivo.writelines('passo,vertice,busca_matriz_largura,busca_lista_largura,busca_matriz_profundidade,busca_lista_profundidade\n')
arquivo.writelines('passo,vertice,busca_lista_largura,busca_lista_profundidade\n')
#busca_matriz_largura= 0
busca_lista_largura = 0
#busca_matriz_profundidade = 0
busca_lista_profundidade = 0
for i in range(100):
    vertice = random.randint(1,grafo_lista._vertices)
    
    #inicio_matriz_l = time.time() 
    #grafo_matriz.busca_largura(vertice,'lixo.txt',0)
    #fim_matriz_l = time.time()

    #inicio_matriz_p = time.time()
    #grafo_matriz.busca_profundidade(vertice,'lixo.txt',0)
    #fim_matriz_p = time.time()

    inicio_lista_l = time.time()
    grafo_lista.busca_largura(vertice,'lixo.txt',0)
    fim_lista_l = time.time()

    inicio_lista_p = time.time()
    grafo_lista.busca_profundidade(vertice,'lixo.txt',0)
    fim_lista_p = time.time()

    #busca_matriz_largura += fim_matriz_l - inicio_matriz_l
    busca_lista_largura += fim_lista_l - inicio_lista_l
    #busca_matriz_profundidade += fim_matriz_p - inicio_matriz_p
    busca_lista_profundidade += fim_lista_p - inicio_lista_p
    #arquivo.writelines(
        #f'{i},{vertice},{fim_matriz_l - inicio_matriz_l},{fim_lista_l - inicio_lista_l}{fim_matriz_p - inicio_matriz_p},{fim_lista_p - inicio_lista_p}\n'
        #)
    #print({i})
    arquivo.writelines(
        f'{i},{vertice},{fim_lista_l - inicio_lista_l},{fim_lista_p - inicio_lista_p}\n'
            )
    print({i})

#print(f'Tempo medio de busca largura matriz = {busca_matriz_largura/100} segundos')
print(f'Tempo medio de busca largura lista = {busca_lista_largura/100} segundos')
#print(f'Tempo medio de busca profundidade matriz = {busca_matriz_profundidade/100} segundos')
print(f'Tempo medio de busca profundidade lista = {busca_lista_profundidade/100} segundos')
arquivo.close()


#QUESTAO 4
#pais1_bfs = grafo_matriz.busca_largura(1,'dump.txt',0)[0]
#pais2_bfs = grafo_matriz.busca_largura(2,'dump.txt',0)[0]
#pais3_bfs = grafo_matriz.busca_largura(3,'dump.txt',0)[0]
#print(f'BFS no 1: Pai do 10: {pais1_bfs[10-1]} - Pai do 20: {pais1_bfs[20-1]} - Pai do 30: {pais1_bfs[30-1]}')
#print(f'BFS no 2: Pai do 10: {pais2_bfs[10-1]} - Pai do 20: {pais2_bfs[20-1]} - Pai do 30: {pais2_bfs[30-1]}')
#print(f'BFS no 3: Pai do 10: {pais3_bfs[10-1]} - Pai do 20: {pais3_bfs[20-1]} - Pai do 30: {pais3_bfs[30-1]}')

#pais1_dfs = grafo_matriz.busca_profundidade(1,'dump.txt',0)
#pais2_dfs = grafo_matriz.busca_profundidade(2,'dump.txt',0)
#pais3_dfs = grafo_matriz.busca_profundidade(3,'dump.txt',0)
#print(f'DFS_matriz no 1: Pai do 10: {pais1_dfs[10-1]} - Pai do 20: {pais1_dfs[20-1]} - Pai do 30: {pais1_dfs[30-1]}')
#print(f'DFS_matriz no 2: Pai do 10: {pais2_dfs[10-1]} - Pai do 20: {pais2_dfs[20-1]} - Pai do 30: {pais2_dfs[30-1]}')
#print(f'DFS_matriz no 3: Pai do 10: {pais3_dfs[10-1]} - Pai do 20: {pais3_dfs[20-1]} - Pai do 30: {pais3_dfs[30-1]}')

pais1_bfs = grafo_lista.busca_largura(1,'dump.txt',0)[0]
pais2_bfs = grafo_lista.busca_largura(2,'dump.txt',0)[0]
pais3_bfs = grafo_lista.busca_largura(3,'dump.txt',0)[0]
print(f'BFS_lista no 1: Pai do 10: {pais1_bfs[10-1]} - Pai do 20: {pais1_bfs[20-1]} - Pai do 30: {pais1_bfs[30-1]}')
print(f'BFS_lista no 2: Pai do 10: {pais2_bfs[10-1]} - Pai do 20: {pais2_bfs[20-1]} - Pai do 30: {pais2_bfs[30-1]}')
print(f'BFS_lista no 3: Pai do 10: {pais3_bfs[10-1]} - Pai do 20: {pais3_bfs[20-1]} - Pai do 30: {pais3_bfs[30-1]}')

pais1_dfs = grafo_lista.busca_profundidade(1,'dump.txt',0)
pais2_dfs = grafo_lista.busca_profundidade(2,'dump.txt',0)
pais3_dfs = grafo_lista.busca_profundidade(3,'dump.txt',0)
print(f'DFS_lista no 1: Pai do 10: {pais1_dfs[10-1]} - Pai do 20: {pais1_dfs[20-1]} - Pai do 30: {pais1_dfs[30-1]}')
print(f'DFS_lista no 2: Pai do 10: {pais2_dfs[10-1]} - Pai do 20: {pais2_dfs[20-1]} - Pai do 30: {pais2_dfs[30-1]}')
print(f'DFS_lista no 3: Pai do 10: {pais3_dfs[10-1]} - Pai do 20: {pais3_dfs[20-1]} - Pai do 30: {pais3_dfs[30-1]}')


#QUESTAO 5
#distancia10_20 = grafo_matriz.distancia(10,20)
#distancia10_30 = grafo_matriz.distancia(20,30)
#distancia20_30 = grafo_matriz.distancia(20,30)

distancia10_20l = grafo_lista.distancia(10,20)
distancia10_30l = grafo_lista.distancia(20,30)
distancia20_30l = grafo_lista.distancia(20,30)

#print(f'Matriz : (10,20) = {distancia10_20} - (10,30) = {distancia10_30} - (20,30) = {distancia20_30}\n') 
print(f'Lista : (10,20) = {distancia10_20l} - (10,30) = {distancia10_30l} - (20,30) = {distancia20_30l}')

# QUESTAO 6
#grafo_matriz.componentes_conexas(f'componentes_conexas_{grafo_atual}.txt')
grafo_lista.componentes_conexas(f'componentes_conexas_{grafo_atual}.txt')

###QUESTAO 7
diametro_lista = grafo_lista.diametro()
print(f'{diametro_lista}') 