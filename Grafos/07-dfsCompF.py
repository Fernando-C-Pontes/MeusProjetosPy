def visitaDFS (adj, u, d, f, cor, tempo, BRANCO, CINZA, PRETO):
  # descoberta
  saidaTexto = "(%d " % u
  tempo[0] += 1
  d[u] = tempo[0]
  cor[u] = CINZA
  for v in adj[u]:
    if cor[v] == BRANCO:
      saidaTexto += visitaDFS (adj, v, d, f, cor, tempo, BRANCO, CINZA, PRETO)
  # finaliza
  saidaTexto += "%d) " % u
  tempo[0] += 1
  f[u] = tempo[0]
  cor[u] = PRETO
  return saidaTexto

def dfs (n, adj, verticesOrdenados):
  # inicializacao
  BRANCO = 1
  CINZA = 2
  PRETO = 3
  cor = [0] * n
  d = [0] * n
  f = [0] * n
  for u in range(n):
    cor[u] = BRANCO
  tempo = [0]
  saidaTexto = ""
  for u in verticesOrdenados:
    if cor[u] == BRANCO:
      saidaTexto += visitaDFS (adj, u, d, f, cor, tempo, BRANCO, CINZA, PRETO)
  return d, f, saidaTexto

# leitura dos dados de entrada do EP
n, m = (int(tmp) for tmp in input().split(" "))

# cria matriz de adjacencia com zeros
matrizAdj = [[0 for col in range(n)] for row in range(n)]

# cria listas de adjacencias
adj = [[] for _ in range(n)]
for i in range (0, m):
  i, j = (int(tmp) for tmp in input().split(" "))
  adj[i].append(j)
  matrizAdj[i][j] = 1

adjT = [[] for _ in range(n)]
# imprime listas de adjacencias
for j in range (0, n):
  for i in range (0, n):
    if matrizAdj[i][j] > 0:
      # insere vizinho
      adjT[j].append (i)

# Algoritmo DFS(G)
d, f, saidaTexto = dfs (n, adj, range(n))

import numpy
s = numpy.array(f)
verticesOrdenados = numpy.argsort(s)[::-1]
d, f, saidaTexto = dfs (n, adjT, verticesOrdenados)

print (saidaTexto)