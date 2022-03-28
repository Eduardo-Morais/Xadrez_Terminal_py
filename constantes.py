from termcolor import colored
LINHA = 8
COLUNA = 8
PEAO_P = colored('♟', 'blue')
BIS_P = colored('♝', 'blue')
TOR_P = colored('♜', 'blue')
CAV_P = colored('♞', 'blue')
REI_P = colored('♚', 'blue')
RAI_P = colored('♛', 'blue')
PEAO_B = colored('♙', 'red')
BIS_B = colored('♝', 'red')
TOR_B = colored('♜', 'red')
CAV_B = colored('♞', 'red')
REI_B = colored('♚', 'red')
RAI_B = colored('♛', 'red')
TAB = colored('🏿', 'white')
PEOES = [PEAO_P, PEAO_B]
BISS = [BIS_P, BIS_B]
TORS = [TOR_P, TOR_B]
CAVS = [CAV_P, CAV_B]
REIS = [REI_P, REI_B]
RAIS = [RAI_P, RAI_B]
PECAS_P = [PEAO_P, TOR_P, BIS_P, CAV_P, REI_P, RAI_P]
PECAS_B = [PEAO_B, TOR_B, BIS_B, CAV_B, REI_B, RAI_B]
ROQUE_P = [PEAO_P, TOR_P, BIS_P, CAV_P, RAI_P]
ROQUE_B = [PEAO_B, TOR_B, BIS_B, CAV_B, RAI_B]
PEOES_E_CAVALOS = [CAV_B, CAV_P, PEAO_B, PEAO_P]
permite_roque_B = True
permite_roque_P = True
permite_E_TOR_B = True
permite_D_TOR_B = True
permite_E_TOR_P = True
permite_D_TOR_P = True
LETRA = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
BRANCAS = "branca"
PRETAS = "preta"
movimentos_rainha_rei = [
    ["reto", "", "cima"],
    ["diagonal", "direita", "cima"],
    ["reto", "direita", ""],
    ["diagonal", "direita", "baixo"],
    ["reto", "", "baixo"],
    ["diagonal", "esquerda", "baixo"],
    ["reto", "esquerda", ""],
    ["diagonal", "esquerda", "cima"],
]
movimentos_bispo = [
    ["diagonal", "direita", "baixo"],
    ["diagonal", "esquerda", "baixo"],
    ["diagonal", "esquerda", "cima"],
    ["diagonal", "direita", "cima"]
]
movimentos_torre = [
    ["reto", "", "baixo"],
    ["reto", "esquerda", ""],
    ["reto", "", "cima"],
    ["reto", "direita", ""]
]
movimentos_cavalo = [
    ["cima", "direita"],
    ["cima", "esquerda"],
    ["direita", "baixo"],
    ["direita", "cima"]
]
