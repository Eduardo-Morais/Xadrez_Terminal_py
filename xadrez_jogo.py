from constantes import *
def cria_tabuleiro(LINHA,COLUNA):#cria o tabuleiro com todas as peças ja localizada
    matriz = []
    for x in range(COLUNA):
        matriz.append([])
    for x in range(LINHA):
        linhas = []
        for i in range(COLUNA):
            if  x>1 and x <6:
                linhas.append(TAB)
            else:   linhas.append('')
        matriz[x]=linhas
    for x in range(len(matriz)):
        for i in range(len(matriz)):
            if x == 1:
                matriz[x][i]+=PEAO_B
            elif x ==6:
                matriz[x][i] += PEAO_P
            if x==0 and i ==0 or x==0 and i==7:
                matriz[x][i]+=TOR_B
            elif x==7 and i==0 or x ==7 and i ==7:
                matriz[x][i]+=TOR_P
            if x == 0 and i == 1 or x == 0 and i == 6:
                matriz[x][i] += CAV_B
            elif x==7 and i==1  or x ==7 and i==6:
                matriz[x][i]+=CAV_P
            if x==0 and i==2 or x==0 and i ==5:
                matriz[x][i]+=BIS_B
            elif x==7 and i==2 or x==7 and i ==5:
                matriz[x][i]+=BIS_P
            if x==0 and i==3:
                matriz[x][i]+=REI_B
            elif x==7 and i==3:
                matriz[x][i]+=REI_P
            if x==0 and i==4:
                matriz[x][i]+=RAI_B
            elif x ==7 and i ==4:
                matriz[x][i]+=RAI_P
    return matriz

def imprime_tabuleiro(matriz):#imprime o tabuleiro do xadrez
    print('  0| 1| 2|3| 4|5 |6| 7|')
    for x in range(len(matriz)):
        for i in range(len(matriz)):
            if i == 0:
                print(end='{}|{}|'.format(x,matriz[x][i]))
            else:
                print(matriz[x][i], end='|')
        print()
    return

def jogada(linha,coluna,linha_f,coluna_f):#realiza a jogada depois de ter passado pela verificação
        matriz[linha_f][coluna_f]=matriz[linha][coluna]
        matriz[linha][coluna]=TAB

def verifica_jogada(linha, coluna, l_f, c_f):#verifica se a jogada da peça escolhida é possivel
    if matriz[linha][coluna]== PEAO_B:#peão branco movimentação
        if l_f == linha+1 and (c_f == coluna+1 or c_f== coluna-1):
            return matriz[l_f][c_f] in PECAS_P
        if matriz[linha][coluna]== matriz[1][coluna]:
                return l_f - linha <= 2  and c_f==coluna
        else:
                return l_f-linha <= 1 and c_f==coluna
    elif matriz[linha][coluna]==PEAO_P:#peão preto movimentação
        if l_f==linha-1 and (c_f==coluna +1 or c_f== coluna-1):
            return matriz[l_f][c_f] in PECAS_B
        if matriz[linha][coluna]==matriz[6][coluna]:
            return linha - l_f <=2 and c_f==coluna
        else:
            return linha-l_f <=1 and c_f==coluna
    elif matriz[linha][coluna]==BIS_B:#movimentação do bispo branco
        if abs(c_f - coluna) == abs(l_f - linha) :
            return verififica_bis(linha,coluna,l_f,c_f)
    elif matriz[linha][coluna]==BIS_P:#movimentação do bispo preto
        if abs(c_f - coluna) == abs(l_f- linha):
            return verififica_bis(linha, coluna, l_f, c_f)
    elif matriz[linha][coluna]==TOR_B:#movimentação torre branca
        if c_f==coluna and l_f != linha:
            return verifica_tor(linha, coluna, l_f, c_f)
        elif c_f!=coluna and l_f==linha:
            return verifica_tor(linha, coluna, l_f, c_f)
    elif matriz[linha][coluna]==TOR_P:#movimentação torre preta
        if c_f==coluna and l_f != linha:
            return verifica_tor(linha, coluna, l_f, c_f)
        elif c_f!=coluna and l_f==linha:
            return verifica_tor(linha, coluna, l_f, c_f)
    elif matriz[linha][coluna]==CAV_B:#movimentação cavalo branco
        if abs(linha-l_f)==2 and (c_f== coluna+1 or c_f==coluna-1):
            if matriz[l_f][c_f] in PECAS_B:
                return False
            else:
                return True
        elif abs(coluna-c_f)==2 and (l_f==linha+1 or l_f==linha-1):
            if matriz[l_f][c_f] in PECAS_B:
                return False
            else:
                return True
    elif matriz[linha][coluna]== CAV_P:#movimentação cavalo preto
        if abs(linha-l_f)==2 and (c_f== coluna+1 or c_f==coluna-1):
            if matriz[l_f][c_f] in PECAS_P:
                return False
            else:
                return True
        elif abs(coluna-c_f)==2 and (l_f==linha+1 or l_f==linha-1):
            if matriz[l_f][c_f] in PECAS_P:
                return False
            else:
                return True
    elif matriz[linha][coluna]==RAI_B:#movimentação dama branca
        if abs(c_f - coluna) == abs(l_f - linha):
            return verififica_bis(linha,coluna,l_f,c_f)
        if c_f == coluna and l_f != linha:
            return verifica_tor(linha, coluna, l_f, c_f)
        elif c_f != coluna and l_f == linha:
            return verifica_tor(linha, coluna, l_f, c_f)
    elif matriz[linha][coluna]==RAI_P:#movimentação dama preta
        if abs(c_f - coluna) == abs(l_f - linha):
            return verififica_bis(linha,coluna,l_f,c_f)
        if c_f == coluna and l_f != linha:
            return verifica_tor(linha, coluna, l_f, c_f)
        elif c_f != coluna and l_f == linha:
            return verifica_tor(linha, coluna, l_f, c_f)

def verifica_tor(linha, coluna, l_f, c_f):#faz o caminho cima baixo realizada pela torre e pela dama
    retorno=True
    anterior=True
    cont=0
    if c_f == coluna and l_f != linha:
        if l_f < linha:
            vezes=abs(l_f - linha)
            for x in range(1,vezes+1):
                if matriz[linha-x][coluna] in PECAS_B or matriz[linha-x][coluna] in PECAS_P:
                    retorno=False
                    cont+=1
                if matriz[linha-x][coluna] == matriz[l_f+1][c_f]:
                    if matriz[linha - x][coluna] in PECAS_B or matriz[linha - x][coluna] in PECAS_P:
                        anterior=False
        if l_f > linha:
            vezes = abs(l_f - linha)
            for x in range(1,vezes+1):
                if matriz[linha +x][coluna] in PECAS_B or matriz[linha + x][coluna] in PECAS_P:
                    retorno= False
                    cont+=1
                if matriz[linha+x][coluna] == matriz[l_f-1][c_f]:
                    if matriz[linha + x][coluna] in PECAS_B or matriz[linha + x][coluna] in PECAS_P:
                        anterior=False

    elif c_f != coluna and l_f == linha:
        if c_f < coluna:
            vezes=abs(coluna- c_f)
            for x in range(1,vezes+1):
                if matriz[linha][coluna-x] in PECAS_B or matriz[linha][coluna-x] in PECAS_P:
                    retorno= False
                    cont+=1
                if matriz[linha][coluna-x] == matriz[l_f][c_f+1]:
                    if matriz[linha][coluna-x] in PECAS_B or matriz[linha][coluna-x] in PECAS_P:
                        anterior=False
        if c_f > coluna:
            vezes = abs(coluna - c_f)
            for x in range(1,vezes+1):
                if matriz[linha][coluna+x] in PECAS_B or matriz[linha][coluna+x] in PECAS_P:
                    retorno= False
                    cont+=1
                if matriz[linha][coluna+x] == matriz[l_f][c_f-1]:
                    if matriz[linha][coluna+x] in PECAS_B or matriz[linha][coluna+x] in PECAS_P:
                        anterior=False
    if matriz[linha][coluna] in PECAS_B and matriz[l_f][c_f] not in PECAS_B:
        if anterior == True and retorno == False and cont <2:
            return anterior
        else:
            return retorno
    elif matriz[linha][coluna] in PECAS_P and matriz[l_f][c_f] not in PECAS_P:
        if anterior == True and retorno == False and cont <2:
            return anterior
        else:
            return retorno
    else:
        return retorno

def verififica_bis(linha,coluna,l_f,c_f):#faz a verificação do caminho da diagonal realizada pelo bispo e pela dama
    retorno=True
    anterior=True
    cont=0
    if l_f > linha and c_f<coluna:
        vezes=abs(l_f-linha)
        for x in range(1,vezes+1):
            if matriz[linha+x][coluna -x] in PECAS_B or matriz[linha+x][coluna - x] in PECAS_P:
                retorno=False
                cont+=1
            if matriz[linha+x][coluna-x] == matriz[l_f-1][c_f+1]:
                if matriz[linha + x][coluna - x] in PECAS_B or matriz[linha + x][coluna - x] in PECAS_P:
                    anterior=False
    elif l_f < linha and c_f>coluna:
        vezes=abs(l_f-linha)
        for x in range(1,vezes+1):
            if matriz[linha-x][coluna + x] in PECAS_B or matriz[linha-x][coluna + x] in PECAS_P:
                retorno=False
                cont+=1
            if matriz[linha-x][coluna+x] == matriz[l_f+1][c_f-1]:
                if matriz[linha - x][coluna + x] in PECAS_B or matriz[linha - x][coluna + x] in PECAS_P:
                    anterior=False
    elif l_f > linha and c_f>coluna:
        vezes=abs(l_f-linha)
        for x in range(1,vezes+1):
            if matriz[linha+x][coluna + x] in PECAS_B or matriz[linha+x][coluna + x] in PECAS_P:
                retorno=False
                cont+=1
            if matriz[linha+x][coluna+x] == matriz[l_f-1][c_f-1]:
                if matriz[linha + x][coluna + x] in PECAS_B or matriz[linha + x][coluna + x] in PECAS_P:
                    anterior=False
    elif l_f < linha and c_f<coluna:
        vezes=abs(l_f-linha)
        for x in range(1,vezes+1):
            if matriz[linha-x][coluna - x] in PECAS_B or matriz[linha-x][coluna - x] in PECAS_P:
                retorno=False
                cont+=1
            if matriz[linha-x][coluna-x] == matriz[l_f+1][c_f+1]:
                if matriz[linha - x][coluna - x] in PECAS_B or matriz[linha - x][coluna - x] in PECAS_P:
                    anterior=False
    if matriz[linha][coluna] in PECAS_B and matriz[l_f][c_f] not in PECAS_B:
        if anterior == True and retorno == False and cont <2:
            return anterior
        else:
            return retorno
    elif matriz[linha][coluna] in PECAS_P and matriz[l_f][c_f] not in PECAS_P:
        if anterior == True and retorno == False and cont <2:
            return anterior
        else:
            return retorno
    else:
        return retorno

matriz=cria_tabuleiro(LINHA,COLUNA)
imprime_tabuleiro(matriz)
while True:
    l,c=map(int, input('coloque a posição inicial da peça na mesma linha e separado por espaço').split())
    l_f,c_f=map(int, input('coloque a posição final da peça da mesma forma que a anterior').split())
    verifica=verifica_jogada(l, c, l_f, c_f)
    if verifica is True:
        jogada(l,c,l_f,c_f)
        imprime_tabuleiro(matriz)
    else:
        print(colored('A JOGADA FEITA NÃO PODE SER REALIZADA', 'magenta'))