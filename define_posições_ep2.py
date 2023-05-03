def  define_posicoes(linha, coluna, orientacao, tamanho):


    grid = [[0]*10 for _ in range (10)]
    linha_tamanho = linha + tamanho
    coluna_tamanho = coluna + tamanho

    lista_retorno = []
    lista_padrao = [0,0,0,0,0,0,0,0,0,0] 

    if orientacao == 'vertical':
      
      
        while linha < linha_tamanho:
            grid [linha][coluna] = coluna
            lista_retorno.append([linha,coluna])
            linha += 1
        

    elif orientacao == 'horizontal':
        
        while coluna < coluna_tamanho:

            grid [linha][coluna] = coluna
            lista_retorno.append([linha,coluna])
            coluna += 1
    return lista_retorno