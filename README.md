## Grafos 👩🏽‍💻👨🏻‍💻
### Primeira parte do Trabalho da disciplina Teoria dos Grafos:
- Implementação de uma biblioteca para manipulação de grafos por Pedro Glaser de Senna e Rafaella Lenzi Romano
##
### 🧠 Detalhes da Biblioteca:
Como pedido por nosso professor, criamos 2 classes em nosso código, uma para definir a estrutura de dados a ser utilizada (matriz ou lista) e outra para realizar as operações nos grafos.
##
#### Classe das operações ("GrafoMatriz()" e "GrafoLista()"):
- __init__(txt, r):
Esse é o construtor da classe, utilizado para receber um arquivo de texto que contenha o grafo.
- Funções requisitadas pelo professor:
número de vértices, número de arestas, grau mínimo, grau máximo, grau médio, mediana de grau, busca por largura, busca por profundidade, distância entre vértices, diâmetro do grafo e componentes conexos.

#### Tempo da Busca em Largura:
- Durante a execução, é criado um arquivo txt que contém o tempo de cada uma das 100 iterações. Para obter o tempo médio, o código imprime a soma dos tempos dividida pelo numero de execuções, nesse caso, 100.

#### Componentes Conexas:
- Durante a execução, é criado um arquivo txt que contém o número de componentes conexas, o tamanho de cada uma e uma lista com os vértices conectados.

#### Diâmetro do grafo:
- Dividimos a função que descobre o diâmetro dos grafos em duas partes, uma para grafos com menos de 1000 vértices, no qual é realizada uma busca em largura para todos os vértices e o caminho que tiver a maior largura será o diâmetro, e outra para grafos com 1000 ou mais vértices, na qual é realizada a busca em largura 1500 vezes, em vértices aleatórios, repetindo o mesmo método.
