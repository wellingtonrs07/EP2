def define_posicoes(linha, coluna, orientacao, tamanho):
    posicao = []
    if orientacao == 'horizontal':
        for i in range(tamanho):
            posicao.append([linha, coluna + i])
    elif orientacao == 'vertical':
        for i in range(tamanho):
            posicao.append([linha + i, coluna])
    return posicao

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    lista_posicoes = []
    lista_posicoes.append(define_posicoes(linha, coluna, orientacao, tamanho))

    if nome_navio not in frota:
        frota[nome_navio] = lista_posicoes
    else:
        frota[nome_navio] += lista_posicoes
    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    elif tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    return tabuleiro

def posiciona_frota(frota):
    tabuleiro = [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
  ]
    for nome, lista_navio in frota.items():
        for navio in lista_navio:
            for coord in navio:
                linha = coord[0]
                coluna = coord[1]
                tabuleiro[linha][coluna] = 1
    return tabuleiro

def afundados(frota, tabuleiro):
    i = 0
    for nome, lista_navio in frota.items():
        for navio in lista_navio:
            afundado = True
            for coord in navio:
                linha = coord[0]
                coluna = coord[1]

                if tabuleiro[linha][coluna] != 'X':
                    afundado = False
            if afundado == True:
                i += 1
    return i

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    tabuleiro = posiciona_frota(frota)
    if orientacao == 'horizontal':
        for i in range(tamanho):
            if linha > 9 or coluna + i > 9:
                return False
            elif tabuleiro[linha][coluna + i] == 1:
                return False
        return True
    if orientacao == 'vertical':
        for i in range(tamanho):
            if linha + i > 9 or coluna > 9:
                return False
            if tabuleiro[linha + i][coluna] == 1:
                return False
        return True
    
navios = {'porta-aviões': [4, 1], 'navio-tanque': [3, 2], 'contratorpedeiro': [2, 3], 'submarino': [1, 4]}
for nome_navio, lista in navios.items():
    i = 0
    while i < lista[1]:
        print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(nome_navio, lista[0]))
        
        linha = int(input('Qual a linha? '))
        coluna = int(input('Qual a coluna? '))
        
        if nome_navio != 'submarino':
            orientacao = int(input('Qual a orientação? '))
        
        if orientacao == 1:
            orientacao = 'vertical'
        elif orientacao == 2:
            orientacao = 'horizontal'
        
        tamanho = lista[0]
        
        if posicao_valida(frota, linha, coluna, orientacao, tamanho) == False:
            print('Esta posição não está válida!')
        else:
            lista_posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
            frota = preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)
            i += 1
print(frota)