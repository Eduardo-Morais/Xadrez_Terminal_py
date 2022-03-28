import constantes
from constantes import *

def cria_tabuleiro(LINHA, COLUNA):  # cria o tabuleiro com todas as peças ja localizada
    '''
    :param LINHA: constante contendo quantas linhas o tabuleiro deve ter.
    :param COLUNA: constante contendo quantas colunas o tabuleiro deve ter.
    :return: retorna o tabuleiro ja criado e com as peças alocadas em seus devidos lugares.
    '''
    matriz = []
    for x in range(COLUNA):
        matriz.append([])
    for x in range(LINHA):
        linhas = []
        for i in range(COLUNA):
            if x > 1 and x < 6:
                linhas.append(TAB)
            else:
                linhas.append('')
        matriz[x] = linhas
    for x in range(len(matriz)):
        for i in range(len(matriz)):
            if x == 1:
                matriz[x][i] += PEAO_B
            elif x == 6:
                matriz[x][i] += PEAO_P
            if x == 0 and i == 0 or x == 0 and i == 7:
                matriz[x][i] += TOR_B
            elif x == 7 and i == 0 or x == 7 and i == 7:
                matriz[x][i] += TOR_P
            if x == 0 and i == 1 or x == 0 and i == 6:
                matriz[x][i] += CAV_B
            elif x == 7 and i == 1 or x == 7 and i == 6:
                matriz[x][i] += CAV_P
            if x == 0 and i == 2 or x == 0 and i == 5:
                matriz[x][i] += BIS_B
            elif x == 7 and i == 2 or x == 7 and i == 5:
                matriz[x][i] += BIS_P
            if x == 0 and i == 3:
                matriz[x][i] += REI_B
            elif x == 7 and i == 3:
                matriz[x][i] += REI_P
            if x == 0 and i == 4:
                matriz[x][i] += RAI_B
            elif x == 7 and i == 4:
                matriz[x][i] += RAI_P
    return matriz


def imprime_tabuleiro(matriz):  # imprime o tabuleiro do xadrez
    '''
    :param matriz: pega o tabuleiro criado pelo função cria_tabuleiro.
    :return: retorna o tabuleiro com as modificações feitas pelo jogo.
    '''
    print('  0| 1| 2|3| 4|5 |6| 7|')
    for x in range(len(matriz)):
        for i in range(len(matriz)):
            if i == 0:
                print(end='{}|{}|'.format(x, matriz[x][i]))
            else:
                print(matriz[x][i], end='|')
        print()
    return


def jogada(linha, coluna, linha_f, coluna_f):  # realiza a jogada depois de ter passado pela verificação
    '''
    :param linha: linha inicial dada pelo jogador.
    :param coluna: coluna inicial dada pelo jogador.
    :param linha_f: linha final dada pelo jogador.
    :param coluna_f: linha final dada pelo jogador.
    :return: retorna a movimentação após todas as verificações feitas, se der verdadeiras vai realizar
    a jogada, se não essa função não é usada.
    '''
    matriz[linha_f][coluna_f] = matriz[linha][coluna]
    matriz[linha][coluna] = TAB


def pega_movimentos(peca, linha, coluna, cor, defesa=False):
    '''
    :param peca: posição onde a linha inicial e a coluna inicial esta, se for uma peça irá retorna ela.
    :param linha: linha inicial dada pelo for de outra função.
    :param coluna: coluna inicial dada pelo for de outra função.
    :param cor: cor da peça que foi encontrada.
    :param defesa: se for para defender o rei.
    :return: retorna os movimentos que a peça encontrada pode realizar.
    '''
    movimentos = []
    if peca in RAIS or peca in REIS:
        movimentos = constantes.movimentos_rainha_rei
    elif peca in BISS:
        movimentos = constantes.movimentos_bispo
    elif peca in TORS:
        movimentos = constantes.movimentos_torre
    elif peca in CAVS:
        movimentos = alcance_do_cavalo(linha, coluna)
    elif peca == PEAO_B:
        movimentos = alcance_do_peao(linha, coluna, cor, defesa)
    elif peca == PEAO_P:
        movimentos = alcance_do_peao(linha, coluna, cor, defesa)
    return movimentos


def alcance_do_cavalo(linha, coluna):
    '''
    :param linha: linha dada pelo for de outra função.
    :param coluna: coluna dada pelo for de outra função.
    :return: retorna para onde o cavalo pode ir quando tiver fazendo a checagem do xeque e da defesa do xeque.
    '''
    coordenadas = []
    if (linha - 2 >= 0) and (coluna + 1 <= 7):
        coordenadas.append(((linha - 2), (coluna + 1)))
    if (linha - 2 >= 0) and (coluna - 1 >= 0):
        coordenadas.append(((linha - 2), (coluna - 1)))
    if (linha + 2 <= 7) and (coluna + 1 <= 7):
        coordenadas.append(((linha + 2), (coluna + 1)))
    if (linha + 2 <= 7) and (coluna - 1 >= 0):
        coordenadas.append(((linha + 2), (coluna - 1)))
    if (linha - 1 >= 0) and (coluna + 2 <= 7):
        coordenadas.append(((linha - 1), (coluna + 2)))
    if (linha + 1 <= 7) and (coluna + 2 <= 7):
        coordenadas.append(((linha + 1), (coluna + 2)))
    if (linha - 1 >= 0) and (coluna - 2 >= 0):
        coordenadas.append(((linha - 1), (coluna - 2)))
    if (linha + 1 <= 7) and (coluna - 2 >= 0):
        coordenadas.append(((linha + 1), (coluna - 2)))
    return coordenadas


def alcance_do_peao(linha, coluna, cor, defesa=False):
    '''
    :param linha: linha dada pelo for de outra função.
    :param coluna: coluna dada pelo for de outra função
    :param cor: cor do peão encontrado.
    :param defesa:se ele esta defendendo ou atacando, para saber se ele esta procurando o xeque ou defendendo ele.
    :return:retorna para onde o peão pode ir se estiver atacando ou defendendo.
    '''
    coordenadas = []
    if cor == BRANCAS:
        if defesa:
            # Se o parâmetro 'defesa' for passado, é por que é um movimento simples
            # (para frente)
            if linha == 1:
                coordenadas.append((linha + 2, coluna))
                coordenadas.append((linha + 1, coluna))
            elif linha <= 7:
                coordenadas.append((linha + 1, coluna))
        else:
            # Caso contrário, é um ataque
            # (para diagonais)
            if (linha + 1 <= 7) and (coluna + 1 <= 7):
                coordenadas.append(((linha + 1), (coluna + 1)))
            if (linha + 1 <= 7) and (coluna - 1 >= 0):
                coordenadas.append(((linha + 1), (coluna - 1)))
    else:
        if defesa:
            if linha == 6:
                coordenadas.append((linha - 2, coluna))
                coordenadas.append((linha - 1, coluna))
            elif linha >= 0:
                coordenadas.append((linha - 1, coluna))
        else:
            if (linha - 1 >= 0) and (coluna + 1 <= 7):
                coordenadas.append(((linha - 1), (coluna + 1)))
            if (linha - 1 >= 0) and (coluna - 1 >= 0):
                coordenadas.append(((linha - 1), (coluna - 1)))
    return coordenadas


def eh_check_mate(matriz, caminho_a_bloquear, cor_em_check):
    '''
    :param matriz: pega a matriz criada pela cria_tabuleiro, com suas atuais modificações.
    :param caminho_a_bloquear: procura o caminho que deve bloquear do xeque.
    :param cor_em_check: pega a cor do jogador que esta em xeque.
    :return: retorna se é possivel sair do xeque ou se foi xeque-mate.
    '''
    pecas_liberadas = list()
    check_mate = True
    for linha in range(len(matriz)):
        for coluna in range(len(matriz)):

            peca = matriz[linha][coluna]
            pecas_a_verificar = PECAS_P if cor_em_check == PRETAS else PECAS_B
            if peca == TAB or peca not in pecas_a_verificar:
                continue

            cor = BRANCAS if peca in PECAS_B else PRETAS
            movimentos = pega_movimentos(peca, linha, coluna, cor, defesa=True)

            distancia = 2 if peca in REIS else len(matriz)
            for mov in movimentos:
                if peca not in PEOES_E_CAVALOS:
                    eh_rei = peca in REIS
                    pode_bloquear = verifica_caminho(linha, coluna, mov[0], mov[1], mov[2], cor_em_check,
                                                                    distancia,
                                                                    protege_rei=(not eh_rei),
                                                                    escapar_rei=eh_rei,
                                                                    caminho_a_verificar=caminho_a_bloquear)
                else:
                    # Pode bloquear se o movimento coincidir com alguma das coordenadas da lista de caminho a bloquear,
                    # caso seja um peão, a coordenada do movimnento também não pode ser a coordenada da peça que está
                    # "checkando" o rei, pois os peões não podem comer peças em seu movimento padrão (para frente)
                    pode_bloquear = mov in (caminho_a_bloquear[1:] if peca in PEOES else caminho_a_bloquear)
                if pode_bloquear:
                    pecas_liberadas.append(peca)
                    check_mate = False

    # Se não for check mate, retorna também, uma lista contendo as peças que podem proteger o rei
    # Caso seja check mate, retorna uma lista vazia
    return check_mate, pecas_liberadas


def check(matriz):
    '''
    :param matriz: pega a matriz criada pela função cria_tabuleiro com suas atuais modificações.
    :return: retorna se existe o xeque no tabuleiro.
    '''
    encontrou_rei = False
    check_mate = False
    pecas_validas, caminho_a_defender = [], []
    jogador_em_check = 0

    for linha in range(len(matriz)):
        for coluna in range(len(matriz)):

            peca = matriz[linha][coluna]
            if peca == TAB:
                continue

            cor = BRANCAS if peca in PECAS_B else PRETAS
            movimentos = pega_movimentos(peca, linha, coluna, cor)

            for mov in movimentos:
                if peca not in PEOES_E_CAVALOS:
                    encontrou_rei = verifica_caminho(linha, coluna, mov[0], mov[1], mov[2], cor, 7, True)
                else:
                    encontrou_rei = matriz[mov[0]][mov[1]] == REI_P if (peca == CAV_B or peca == PEAO_B) \
                        else matriz[mov[0]][mov[1]] == REI_B

                if encontrou_rei:
                    if peca not in PEOES_E_CAVALOS:
                        caminho_ate_o_rei = pega_caminho_ate_o_rei(linha, coluna, mov[0], mov[1], mov[2], 7)
                    else:
                        caminho_ate_o_rei = [(linha, coluna)]
                    caminho_a_defender = caminho_ate_o_rei
                    cor_em_check = PRETAS if cor == BRANCAS else BRANCAS
                    jogador_em_check = 1 if cor_em_check == BRANCAS else 2
                    check_mate, pecas_validas = eh_check_mate(matriz, caminho_ate_o_rei, cor_em_check)
                    return encontrou_rei, check_mate, pecas_validas, caminho_a_defender, jogador_em_check

    return encontrou_rei, check_mate, pecas_validas, caminho_a_defender, jogador_em_check


def verifica_jogada(linha, coluna, l_f, c_f):  # verifica se a jogada da peça escolhida é possivel
    '''
    :param linha:linha inicial dada pelo jogador.
    :param coluna:coluna inicial dada pelo jogador.
    :param l_f:linha final dada pelo jogador.
    :param c_f:coluna final dada pelo jogador.
    :return:retorna se a jogada dada pelo jogador podera ser realizada, se sim chama a função jogada() e modifica
    o tabuleiro.
    '''
    if matriz[linha][coluna] == PEAO_B:  # peão branco movimentação
        if l_f == linha + 1 and (c_f == coluna + 1 or c_f == coluna - 1) and matriz[l_f][c_f] != REI_P:
            return matriz[l_f][c_f] in PECAS_P
        if matriz[linha][coluna] == matriz[1][coluna] and l_f > linha :
                if matriz[l_f][c_f] in PECAS_P:
                    return False
                else:
                    return l_f - linha <= 2 and c_f == coluna
        else:
            if l_f > linha and matriz[l_f][c_f]not in (PECAS_P or PECAS_B):
                if matriz[l_f][c_f]  in PECAS_P:
                    return False
                else:
                    return l_f - linha <= 1 and c_f == coluna
    elif matriz[linha][coluna] == PEAO_P:  # peão preto movimentação
        if l_f == linha - 1 and (c_f == coluna + 1 or c_f == coluna - 1) and matriz[l_f][c_f] != REI_B:
            return matriz[l_f][c_f] in PECAS_B
        if matriz[linha][coluna] == matriz[6][coluna] and l_f < linha:
            if matriz[l_f][c_f] in PECAS_B:
                return False
            else:
                return linha - l_f <= 2 and c_f == coluna
        else:
            if l_f < linha:
                if matriz[l_f][c_f]:
                    return linha - l_f <= 1 and c_f == coluna
    elif matriz[linha][coluna] == BIS_B:  # movimentação do bispo branco
        if abs(c_f - coluna) == abs(l_f - linha):
            andar = abs(c_f - coluna)
            caminho, captura = False, False

            if linha < l_f and coluna < c_f:
                caminho, captura = verifica_caminho(linha, coluna, "diagonal", "direita", "baixo", BRANCAS, andar, )
            elif linha < l_f and coluna > c_f:
                caminho, captura = verifica_caminho(linha, coluna, "diagonal", "esquerda", "baixo",
                                                    BRANCAS, andar, )
            elif l_f < linha and coluna < c_f:
                caminho, captura = verifica_caminho(linha, coluna, "diagonal", "direita", "cima", BRANCAS, andar)
            elif l_f < linha and coluna > c_f:
                caminho, captura = verifica_caminho(linha, coluna, "diagonal", "esquerda", "cima", BRANCAS, andar)

            if caminho is True:
                if matriz[l_f][c_f] in PECAS_P or matriz[l_f][c_f] in PECAS_B:
                    return captura
                else:
                    return caminho

    elif matriz[linha][coluna] == BIS_P:  # movimentação do bispo preto
        if abs(c_f - coluna) == abs(l_f - linha):
            andar = abs(c_f - coluna)
            caminho, captura = False, False
            if linha < l_f and coluna < c_f:
                caminho, captura = verifica_caminho(linha, coluna, "diagonal", "direita", "baixo",
                                                    PRETAS, andar)
            elif linha < l_f and coluna > c_f:
                caminho, captura = verifica_caminho(linha, coluna, "diagonal", "esquerda", "baixo",
                                                    PRETAS, andar)
            elif l_f < linha and coluna < c_f:
                caminho, captura = verifica_caminho(linha, coluna, "diagonal", "direita", "cima",
                                                    PRETAS, andar)
            elif l_f < linha and coluna > c_f:
                caminho, captura = verifica_caminho(linha, coluna, "diagonal", "esquerda", "cima",
                                                    PRETAS, andar)
            if caminho is True:
                if matriz[l_f][c_f] in PECAS_B or matriz[l_f][c_f] in PECAS_P:
                    return captura
                else:
                    return caminho
    elif matriz[linha][coluna] == TOR_B:  # movimentação torre branc
        caminho, captura = False, False
        if c_f == coluna and l_f != linha:
            andar = abs(linha - l_f)
            if linha < l_f:
                caminho, captura = verifica_caminho(linha, coluna, "reto", "", "baixo", BRANCAS, andar)
            elif linha > l_f:
                caminho, captura = verifica_caminho(linha, coluna, "reto", "", "cima", BRANCAS, andar)
        elif c_f != coluna and l_f == linha:
            andar = abs(coluna - c_f)
            if coluna < c_f:
                caminho, captura = verifica_caminho(linha, coluna, "reto", "direita", "", BRANCAS, andar)
            elif coluna > c_f:
                caminho, captura = verifica_caminho(linha, coluna, "reto", "esquerda", "", BRANCAS, andar)
        if caminho is True:
            if linha == 0 and coluna == 0:
                constantes.permite_E_TOR_B = False
            if linha == 0 and coluna == 7:
                constantes.permite_D_TOR_B = False
            if matriz[l_f][c_f] in PECAS_B or matriz[l_f][c_f] in PECAS_P:
                return captura
            else:
                return caminho
    elif matriz[linha][coluna] == TOR_P:  # movimentação torre preta
        caminho, captura = False, False
        if c_f == coluna and l_f != linha:
            andar = abs(linha - l_f)
            if linha < l_f:
                caminho, captura = verifica_caminho(linha, coluna, "reto", "", "baixo", PRETAS, andar)
            elif linha > l_f:
                caminho, captura = verifica_caminho(linha, coluna, "reto", "", "cima", PRETAS, andar)
        elif c_f != coluna and l_f == linha:
            andar = abs(coluna - c_f)
            if coluna < c_f:
                caminho, captura = verifica_caminho(linha, coluna, "reto", "direita", "", PRETAS, andar)
            elif coluna > c_f:
                caminho, captura = verifica_caminho(linha, coluna, "reto", "esquerda", "", PRETAS, andar)
        if caminho is True:
            if linha == 7 and coluna == 0:
                constantes.permite_E_TOR_P = False
            if linha == 7 and coluna == 7:
                constantes.permite_D_TOR_P = False
            if matriz[l_f][c_f] in PECAS_B or matriz[l_f][c_f] in PECAS_P:
                return captura
            else:
                return caminho
    elif matriz[linha][coluna] == CAV_B:  # movimentação cavalo branco
        if abs(linha - l_f) == 2 and (c_f == coluna + 1 or c_f == coluna - 1):
            if matriz[l_f][c_f] in PECAS_B or matriz[l_f][c_f] == REI_P:
                return False
            else:
                return True
        elif abs(coluna - c_f) == 2 and (l_f == linha + 1 or l_f == linha - 1):
            if matriz[l_f][c_f] in PECAS_B or matriz[l_f][c_f] == REI_P:
                return False
            else:
                return True
    elif matriz[linha][coluna] == CAV_P:  # movimentação cavalo preto
        if abs(linha - l_f) == 2 and (c_f == coluna + 1 or c_f == coluna - 1):
            if matriz[l_f][c_f] in PECAS_P:
                return False
            else:
                return True
        elif abs(coluna - c_f) == 2 and (l_f == linha + 1 or l_f == linha - 1):
            if matriz[l_f][c_f] in PECAS_P:
                return False
            else:
                return True
    elif matriz[linha][coluna] == RAI_B:  # movimentação dama branca
        caminho, captura = False, False
        if abs(c_f - coluna) == abs(l_f - linha):
            andar = abs(c_f - coluna)
            if linha < l_f and coluna < c_f:
                caminho, captura = verifica_caminho(linha, coluna, "diagonal", "direita", "baixo", BRANCAS, andar)
            elif linha < l_f and coluna > c_f:
                caminho, captura = verifica_caminho(linha, coluna, "diagonal", "esquerda", "baixo",
                                                    BRANCAS, andar)
            elif l_f < linha and coluna < c_f:
                caminho, captura = verifica_caminho(linha, coluna, "diagonal", "direita", "cima", BRANCAS, andar)
            elif l_f < linha and coluna > c_f:
                caminho, captura = verifica_caminho(linha, coluna, "diagonal", "esquerda", "cima", BRANCAS, andar)
        if c_f == coluna and l_f != linha:
            andar = abs(linha - l_f)
            if linha < l_f:
                caminho, captura = verifica_caminho(linha, coluna, "reto", "", "baixo", BRANCAS, andar)
            elif linha > l_f:
                caminho, captura = verifica_caminho(linha, coluna, "reto", "", "cima", BRANCAS, andar)
        elif c_f != coluna and l_f == linha:
            andar = abs(coluna - c_f)
            if coluna < c_f:
                caminho, captura = verifica_caminho(linha, coluna, "reto", "direita", "", BRANCAS, andar)
            elif coluna > c_f:
                caminho, captura = verifica_caminho(linha, coluna, "reto", "esquerda", "", BRANCAS, andar)
        if caminho is True:
            if matriz[l_f][c_f] in PECAS_B or matriz[l_f][c_f] in PECAS_P:
                return captura
            else:
                return caminho
    elif matriz[linha][coluna] == RAI_P:  # movimentação dama preta
        caminho, captura = False, False
        if abs(c_f - coluna) == abs(l_f - linha):
            andar = abs(c_f - coluna)
            if linha < l_f and coluna < c_f:
                caminho, captura = verifica_caminho(linha, coluna, "diagonal", "direita", "baixo", PRETAS, andar)
            elif linha < l_f and coluna > c_f:
                caminho, captura = verifica_caminho(linha, coluna, "diagonal", "esquerda", "baixo", PRETAS, andar)
            elif l_f < linha and coluna < c_f:
                caminho, captura = verifica_caminho(linha, coluna, "diagonal", "direita", "cima", PRETAS, andar)
            elif l_f < linha and coluna > c_f:
                caminho, captura = verifica_caminho(linha, coluna, "diagonal", "esquerda", "cima", PRETAS, andar)
        if c_f == coluna and l_f != linha:
            andar = abs(linha - l_f)
            if linha < l_f:
                caminho, captura = verifica_caminho(linha, coluna, "reto", "", "baixo", PRETAS, andar)
            elif linha > l_f:
                caminho, captura = verifica_caminho(linha, coluna, "reto", "", "cima", PRETAS, andar)
        elif c_f != coluna and l_f == linha:
            andar = abs(coluna - c_f)
            if coluna < c_f:
                caminho, captura = verifica_caminho(linha, coluna, "reto", "direita", "", PRETAS, andar)
            elif coluna > c_f:
                caminho, captura = verifica_caminho(linha, coluna, "reto", "esquerda", "", PRETAS, andar)
        if caminho is True:
            if matriz[l_f][c_f] in PECAS_B or matriz[l_f][c_f] in PECAS_P:
                return captura
            else:
                return caminho
    elif matriz[linha][coluna] == REI_B:  # movimentação do Rei Branco
        if l_f == linha and (c_f == coluna + 1 or c_f == coluna - 1) and matriz[l_f][c_f] not in PECAS_B:
            constantes.permite_roque_B = False
            return True
        elif c_f == coluna and (l_f == linha + 1 or l_f == linha - 1) and matriz[l_f][c_f] not in PECAS_B:
            constantes.permite_roque_B = False
            return True
        elif abs(c_f - coluna) == 1 and abs(l_f - linha) == 1 and matriz[l_f][c_f] not in PECAS_B:
            constantes.permite_roque_B = False
            return True
        elif matriz[linha][coluna] == matriz[0][3] and (
                matriz[l_f][c_f + 1] == TOR_B or matriz[l_f][c_f - 1] == TOR_B) and permite_roque_B == True:
            andar = abs(coluna - c_f)
            if coluna > c_f:
                caminho = roque(linha, coluna, 'reto', 'esquerda', '', 'branca', andar)
                if caminho is True and matriz[l_f][
                    c_f - 1] == TOR_B and constantes.permite_roque_B == True and constantes.permite_E_TOR_B == True:
                    matriz[l_f][c_f - 1] = TAB
                    matriz[l_f][c_f] = REI_B
                    matriz[l_f][c_f + 1] = TOR_B
                    constantes.permite_roque_B = False
                    return caminho
            elif coluna < c_f:
                caminho = roque(linha, coluna, 'reto', 'direita', '', 'branca', andar)
                if caminho is True and matriz[l_f][
                    c_f + 1] == TOR_B and constantes.permite_roque_B == True and constantes.permite_D_TOR_B == True:
                    matriz[l_f][c_f + 1] = TAB
                    matriz[l_f][c_f] = REI_B
                    matriz[l_f][c_f - 1] = TOR_B
                    constantes.permite_roque_B = False
                    return caminho
    elif matriz[linha][coluna] == REI_P:  # movimentação do Rei Preto
        andar = abs(coluna - c_f)
        if l_f == linha and (c_f == coluna + 1 or c_f == coluna - 1) and matriz[l_f][c_f] not in PECAS_P:
            constantes.permite_roque_P = False
            return True
        elif c_f == coluna and (l_f == linha + 1 or l_f == linha - 1) and matriz[l_f][c_f] not in PECAS_P:
            constantes.permite_roque_P = False
            return True
        elif abs(c_f - coluna) == 1 and abs(l_f - linha) == 1 and matriz[l_f][c_f] not in PECAS_P:
            constantes.permite_roque_P = False
            return True
        if matriz[linha][coluna] == matriz[7][3] and (
                matriz[l_f][c_f + 1] == TOR_P or matriz[l_f][c_f - 1] == TOR_P) and permite_roque_P == True:
            if coluna > c_f:
                caminho = roque(linha, coluna, 'reto', 'esquerda', '', 'preta', andar)
                if caminho is True and matriz[l_f][
                    c_f - 1] == TOR_P and constantes.permite_roque_P == True and constantes.permite_E_TOR_P == True:
                    matriz[l_f][c_f - 1] = TAB
                    matriz[l_f][c_f] = REI_P
                    matriz[l_f][c_f + 1] = TOR_P
                    constantes.permite_roque_P = False
                    return caminho
            elif coluna < c_f:
                caminho = roque(linha, coluna, 'reto', 'direita', '', 'preta', andar)
                if caminho is True and matriz[l_f][
                    c_f + 1] == TOR_P and constantes.permite_roque_P and constantes.permite_D_TOR_P == True:
                    matriz[l_f][c_f + 1] = TAB
                    matriz[l_f][c_f] = REI_P
                    matriz[l_f][c_f - 1] = TOR_P
                    constantes.permite_roque_P = False
                    return caminho


def incrementa_linha_coluna(linha, coluna, reto_ou_diagonal, esquerda_ou_direita, cima_ou_baixo):
    '''
    :param linha: linha inicial dada pelo jogador ou linha dada pelo for de uma função.
    :param coluna: coluna inicial dada pelo jogador ou coluna dada pelo for de uma função.
    :param reto_ou_diagonal: se o movimento da peça é reto ou na diagonal.
    :param esquerda_ou_direita: se a peça esta indo para esquerda ou direita.
    :param cima_ou_baixo: se a peça esta indo para cima ou para baixo.
    :return: retorna o caminho que a peça vai realizar.
    '''
    if reto_ou_diagonal == "diagonal":
        if cima_ou_baixo == "baixo":
            linha += 1
        elif cima_ou_baixo == "cima":
            linha -= 1
        if esquerda_ou_direita == "direita":
            coluna += 1
        elif esquerda_ou_direita == "esquerda":
            coluna -= 1
    elif reto_ou_diagonal == "reto":
        if cima_ou_baixo == "baixo":
            linha += 1
        elif cima_ou_baixo == "cima":
            linha -= 1
        elif esquerda_ou_direita == "direita":
            coluna += 1
        elif esquerda_ou_direita == "esquerda":
            coluna -= 1
    return linha, coluna


def pega_caminho_ate_o_rei(
        linha_origem,
        coluna_origem,
        reto_ou_diagonal,
        esquerda_ou_direita,
        cima_ou_baixo,
        distancia=7
):
    '''
    :param linha_origem: linha inicial dada pelo jogador ou pelo for.
    :param coluna_origem: coluna inicial dada pelo jogador ou pelo for.
    :param reto_ou_diagonal: se o movimento da peça é reto ou na diagonal.
    :param esquerda_ou_direita: se a peça esta indo para esquerda ou direita.
    :param cima_ou_baixo: se a peça esta indo para cima ou para baixo.
    :param distancia: distancia que a peça ira percorrer.
    :return: retorna se o cmainho esta livre e se a captura é possivel, além de procurar xeque, se pode defender o rei
    ou se o rei pode escapar por si só.
    '''
    caminho_percorrido = [(linha_origem, coluna_origem)]  # Armazena cada coordenada de cada casa visitada
    linha, coluna = incrementa_linha_coluna(linha_origem, coluna_origem, reto_ou_diagonal, esquerda_ou_direita,
                                            cima_ou_baixo)
    for pos in range(distancia):
        casa_verificando = matriz[linha][coluna]
        if casa_verificando == TAB:
            caminho_percorrido.append((linha, coluna))
            linha, coluna = incrementa_linha_coluna(linha, coluna, reto_ou_diagonal, esquerda_ou_direita, cima_ou_baixo)
        else:
            # encontrou o rei
            return caminho_percorrido


def verifica_caminho(
        linha_origem,
        coluna_origem,
        reto_ou_diagonal,
        esquerda_ou_direita,
        cima_ou_baixo,
        preta_ou_branca,
        distancia=7,
        procura_rei=False,
        protege_rei=False,
        escapar_rei=False,
        caminho_a_verificar=[]
):
    linha, coluna = incrementa_linha_coluna(linha_origem, coluna_origem, reto_ou_diagonal, esquerda_ou_direita,
                                            cima_ou_baixo)

    if procura_rei:
        for pos in range(distancia):
            if (linha > 7 or coluna > 7) or (linha < 0 or coluna < 0):
                return False
            casa_verificando = matriz[linha][coluna]
            if casa_verificando != TAB:
                if preta_ou_branca == BRANCAS and casa_verificando in PECAS_P \
                        or preta_ou_branca == PRETAS and casa_verificando in PECAS_B:
                    return casa_verificando == REI_P if preta_ou_branca == BRANCAS else casa_verificando == REI_B
                else:
                    return False
            linha, coluna = incrementa_linha_coluna(linha, coluna, reto_ou_diagonal, esquerda_ou_direita, cima_ou_baixo)

    elif protege_rei:
        for pos in range(distancia):
            if (linha > 7 or coluna > 7) or (linha < 0 or coluna < 0):
                return False
            casa_verificando = matriz[linha][coluna]
            if casa_verificando != TAB and not (linha, coluna) in caminho_a_verificar:
                return False
            if (linha, coluna) in caminho_a_verificar:
                # peça pode bloquear
                return True

    else:
        caminho_livre = True if ((linha <= 7 and coluna <= 7) and (linha >= 0 and coluna >= 0)) else False
        pode_capturar = False

        for pos in range(distancia):
            # if (linha > 7 or coluna > 7) or (linha < 0 or coluna < 0):
            #     break
            if not caminho_livre:
                break
            casa_verificando = matriz[linha][coluna]
            if casa_verificando != TAB and pos < distancia - 1:
                if escapar_rei:
                    pecas_rei_nao_tem_medo = [PEAO_B if preta_ou_branca == PRETAS else PEAO_P]
                    if casa_verificando not in pecas_rei_nao_tem_medo:
                        caminho_livre = False
                else:
                    caminho_livre = False
            elif pos == distancia - 1:
                if escapar_rei and (linha, coluna) in caminho_a_verificar:
                    # Procurando escapatoria para o rei
                    caminho_livre = False
                else:
                    if preta_ou_branca == BRANCAS and casa_verificando in PECAS_P and casa_verificando != REI_P \
                            or preta_ou_branca == PRETAS and casa_verificando in PECAS_B and casa_verificando != REI_B:
                        pode_capturar = True
                    else:
                        pode_capturar = False
            linha, coluna = incrementa_linha_coluna(linha, coluna, reto_ou_diagonal, esquerda_ou_direita, cima_ou_baixo)

        if escapar_rei:
            return caminho_livre
        else:
            return caminho_livre, pode_capturar


def roque(linha_origem, coluna_origem, reto_ou_diagonal, esquerda_ou_direita, cima_ou_baixo, preta_ou_branca,
          distancia=7):
    '''
    :param linha_origem: linha de origem dada pelo jogador.
    :param coluna_origem: coluna de origem dada pelo jogador.
    :param reto_ou_diagonal: se esta indo reto ou na diagonal, como essa função é especifica para o roque sempra vai
    ser reto.
    :param esquerda_ou_direita: se esta indo para a esquerda ou direita, esquerda=roque menor e direita=roque maior.
    :param cima_ou_baixo: se esta indo para cima ou baixo, como essa função é especifica do roque não sera utilizada.
    :param preta_ou_branca:se é uma peça preta ou branca
    :param distancia:e a distancia que vai percorrer se esta de acordo com um roque.
    :return:retorna se o caminho do roque esta livre e se ele pode ser realizado.
    '''
    caminho_livre = True
    linha, coluna = incrementa_linha_coluna(linha_origem, coluna_origem, reto_ou_diagonal, esquerda_ou_direita,
                                            cima_ou_baixo)
    for pos in range(distancia):
        if linha > 7 or coluna > 7:
            break
        casa_verificando = matriz[linha][coluna]
        if casa_verificando != TAB and pos < distancia - 1:
            caminho_livre = False
        linha, coluna = incrementa_linha_coluna(linha, coluna, reto_ou_diagonal, esquerda_ou_direita, cima_ou_baixo)
    return caminho_livre


matriz = cria_tabuleiro(LINHA, COLUNA)
imprime_tabuleiro(matriz)
jogador_atual = 1

ck, pecas_validas, caminho_a_defender, jogador_em_check = False, [], [], 0
while True:
    print(colored(f'Vez do jogador {jogador_atual} ({"vermelha" if jogador_atual == 1 else "azul"})', 'yellow'))
    while True:
        try:
            l, c = map(int, input('coloque a posição inicial da peça na mesma linha e separado por espaço').split())
            break
        except:
            print(colored('ENTRADA FORA DOS PARAMETROS, PORFAVOR INSIRA CORRETAMENTE:', 'magenta'))
    while True:
        try:
            l_f, c_f = map(int, input('coloque a posição final da peça da mesma forma que a anterior').split())
            break
        except:
            print(colored('ENTRADA FORA DOS PARAMETROS, PORFAVOR INSIRA CORRETAMENTE:', 'magenta'))
    if jogador_atual == 1 and matriz[l][c] in PECAS_B or jogador_atual == 2 and matriz[l][c] in PECAS_P:
        verifica = verifica_jogada(l, c, l_f, c_f)
        if verifica is True:
            verifica_pos_check = True
            if ck and jogador_atual == jogador_em_check:
                if matriz[l][c] not in pecas_validas or (l_f, c_f) not in caminho_a_defender :
                    verifica_pos_check = False  # Jogada pos check inválida
                    imprime_tabuleiro(matriz)
                    print(f'Você está em check e deve proteger o seu rei! Você pode mexer apenas: ')
                    for x in range(len(pecas_validas)):
                        print(f'- {pecas_validas[x]}')
                else:
                    verifica_pos_check = True
                    ck = False
            if jogador_atual != jogador_em_check or ( not ck and verifica_pos_check):
                jogada(l, c, l_f, c_f)
                imprime_tabuleiro(matriz)
                jogador_atual = jogador_atual - 1 if jogador_atual == 2 else jogador_atual + 1
                ck, cm, pecas_validas, caminho_a_defender, jogador_em_check = check(matriz)
                if ck is True and not cm:
                    print(colored(f'O jogador {jogador_em_check} está em check!','red'))
                elif cm:
                    print(colored(
                        f'Check Mate! O jogador {jogador_atual - 1 if jogador_atual == 2 else jogador_atual + 1} venceu!','yellow'))
                    exit(1)
        else:
            print(colored('A JOGADA FEITA NÃO PODE SER REALIZADA', 'magenta'))
    else:
        print(colored('NAO EH A SUA VEZ', 'magenta'))