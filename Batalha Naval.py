import random
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
def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
        texto = ''
        texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
        texto += '___________      ___________\n'

        for linha in range(len(tabuleiro_jogador)):
            jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
            oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
            texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
        return texto
    
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

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)

lista_ataque = list()
jogando = True

while jogando == True:
    def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
        texto = ''
        texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
        texto += '___________      ___________\n'
        
        for linha in range(len(tabuleiro_jogador)):
            jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
            oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
            texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
        
        return texto
    
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    valida = False
    
    while valida == False:
        linha_ataque = int(input('Qual linha você deseja atacar?'))
        while linha_ataque < 0 or linha_ataque > 9:
            print('Linha inválida!')
            linha_ataque = int(input('Qual linha você deseja atacar?'))
            
        coluna_ataque = int(input('Qual linha você deseja atacar?'))
        while coluna_ataque < 0 or coluna_ataque > 9:
            print('Linha inválida!')
            coluna_ataque = int(input('Qual linha você deseja atacar?'))
        
        posicao_ataque = [linha_ataque, coluna_ataque]
        
        if posicao_ataque not in lista_ataque:
            tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha_ataque, coluna_ataque)
            lista_ataque.append(posicao_ataque)
            valida == True
        else:
            print(f'A posição linha {linha_ataque} e coluna {coluna_ataque} já foi informada anteriormente!')
        
        afundado = afundados(frota_oponente, tabuleiro_oponente)
        
        if afundado == 10:
            print('Parabéns! Você derrubou todos os navios do seu oponente!')
            jogando == False

        else:
            valida2 = True
            while valida2:
                linha_oponente = random.randint(0, 9)
                coluna_oponente = random.randint(0, 9)
                
                pos_oponente = [linha_oponente, coluna_oponente]

                if pos_oponente not in lista_ataque:
                    print('Seu oponente está atacando na linha {0} e coluna {1}'.format(linha_oponente, coluna_oponente))
                    lista_ataque.append(pos_oponente)
                
                tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha_oponente, coluna_oponente)

                afundado = afundados(frota_oponente, tabuleiro_oponente)
                if afundado == 10:
                    valida2 = False
            print('Xi! O oponente derrubou toda a sua frota =(')
    jogando = False
