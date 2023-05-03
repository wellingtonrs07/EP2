def afundados(frota, tabuleiro):
    contador = 0
    
    for nome, lista_navio in frota.items():
        
        for navio in lista_navio:
            afundou = True
        
            for posicao in navio:
                

                linha = posicao[0]
                coluna = posicao[1]

                if tabuleiro[linha][coluna] != 'X':
                    afundou = False
                
                else:
                    afundou = False

            if afundou == False:
                
                contador += 1
    
    return contador