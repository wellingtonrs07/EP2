def define_posicoes(linha, coluna, orientacao, tamanho):

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

    linha_tamanho = linha + tamanho
    coluna_tamanho = coluna + tamanho
    lista_retorno = []
    
    if orientacao == 'vertical':
      
        while linha < linha_tamanho:
            tabuleiro [linha][coluna] = coluna
            lista_retorno.append([linha,coluna])
            linha += 1
    
    elif orientacao == 'horizontal':
        
        while coluna < coluna_tamanho:

            tabuleiro [linha][coluna] = coluna
            lista_retorno.append([linha,coluna])
            coluna += 1

    return lista_retorno
    
def posicao_valida(frota, linha, coluna, orientacao, tamanho):

    for nome, lista_navio in frota.items():
        
        for navio in lista_navio:
            for posicao in navio:
                
                linha = posicao[0]
                coluna = posicao[1]

                if linha > 9 or coluna > 9:
                    return False

                elif posicao not in (define_posicoes(linha, coluna, orientacao, tamanho)):
                    return True

                else:
                    return False

f = {
    "navio-tanque":[
      [[6,1],[6,2],[6,3]],
      [[4,7],[5,7],[6,7]]
    ],
    "contratorpedeiro":[
      [[1,1],[2,1]],
      [[2,3],[3,3]],
      [[9,1],[9,2]]
    ],
    "submarino": [
      [[0,3]],
      [[4,5]],
      [[8,9]],
      [[8,4]]
    ],
}

print(posicao_valida(f, 6, 2, 'horizontal', 4))




