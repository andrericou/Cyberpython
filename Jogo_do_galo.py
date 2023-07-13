#
# função que devolve um lista com as células livres
# as células livres são as que ainda têm um algarismo
#
def get_free_cells(board):
    free_cells=set()
    for row in board:
        for value in row:
            if value not in (X,O):
                free_cells.add(value)
    return free_cells
          
#
# função que marca uma posição para um jogador
# as posições são marcadas de 1 a 9
# da esquerda para a direita
# e de cima para baixo
#
def set_cell(board,move,player):
    global free_cells
    row=(move-1)//3
    column=(move-1)-3*row
    board[row][column]=player
    free_cells=get_free_cells(board)

#
# função que pede a jogada ao jogador humano
# esta função invoca outra função para marcar a jogada
#
def enter_move(board):
    move=0
    while move not in free_cells:
        move=int(input("Please enter a move: "))
        if move not in free_cells:
            print("That move is not available!")
            print("Available moves:",free_cells)
    print(f"User chooses {move}.")
    set_cell(board,move,O)

#
# função que seleciona uma jogada para o computador
# esta função invoca outra função para marcar a jogada
#
def draw_move(board):
    move=0
    # vamos procurar a melhor jogada
    # procurar a vencer - linhas, colunas ou diagonais com dois X
    # depois não perder - linhas, colunas ou diagonais com dois O
    for player in (O,X):
        # testa as três linhas e as três colunas
        for i in range(3):
            # testa linha i
            if board[i][1] == board[i][2] == player != board[i][0] not in (O,X): move=board[i][0]
            if board[i][0] == board[i][2] == player != board[i][1] not in (O,X): move=board[i][1]
            if board[i][0] == board[i][1] == player != board[i][2] not in (O,X): move=board[i][2]
            # testa coluna i
            if board[1][i] == board[2][i] == player != board[0][i] not in (O,X): move=board[0][i]
            if board[0][i] == board[2][i] == player != board[1][i] not in (O,X): move=board[1][i]
            if board[0][i] == board[1][i] == player != board[2][i] not in (O,X): move=board[2][i]
        # testa as duas diagonais
        if board[1][1] == board[2][2] == player != board[0][0] not in (O,X): move=board[0][0]
        if board[2][0] == board[1][1] == player != board[0][2] not in (O,X): move=board[0][2]
        if board[0][0] == board[2][2] == player != board[1][1] not in (O,X): move=board[1][1]
        if board[2][0] == board[0][2] == player != board[1][1] not in (O,X): move=board[1][1]
        if board[1][1] == board[0][2] == player != board[2][0] not in (O,X): move=board[2][0]
        if board[0][0] == board[1][1] == player != board[2][2] not in (O,X): move=board[2][2]
    # se ainda não houver uma opção, escolhe ao calhas
    if move==0:
        if 5 in free_cells: move=5
        else:
            while move not in free_cells:
                move=randrange(1,10)
    set_cell(board,move,X)
    print(f"Computer chooses {move}.")

#
# função que identifica vencedor
#
def check_win(board):
    # testa as três linhas e as três colunas
    for i in range(3):
        # testa linha i
        if board[i][0]==board[i][1]==board[i][2]: return board[i][1]
        # test coluna i
        if board[0][i]==board[1][i]==board[2][i]: return board[1][i]
    # testa as duas diagonais
    if board[0][0]==board[1][1]==board[2][2] or board[2][0]==board[1][1]==board[0][2]: return board[1][1]
    # ainda não há vencedor
    return False

#
# função que apresenta o estado do jogo
#
def display_board(board):
    def print_line():
        print("+  -  +  -  +  -  +")
    print()
    for row in board:
        print_line()
        for column in row: print(f"|  {column}  ",end="")
        print("|")
    else: print_line()
    print()

###
### MAINBODY
###

from random import randrange

# simplifica utilizar as variáveis X e O em vez das strings
# o computador joga sempre com o X
X='X'
O='O'

# o board é uma lista de 3 listas com algarismos de 1 a 9
board=[[] for i in range(3)]
board[0],board[1],board[2]=[1,2,3],[4,5,6],[7,8,9]

# lista de jogadas possíveis
free_cells=get_free_cells(board)

# sorteia quem começa a jogar
if randrange(0,2):
    print(f"\nComputer starts and is player X.")
    player=X
else:
    print(f"\nUser starts and is player O.")
    player=O

winner=False

# jogamos até haver vencedor ou acabarem as jogadas possíveis
while not(winner) and len(free_cells):
    display_board(board)
    if player==X:
        draw_move(board)
        player=O
    else:
        enter_move(board)
        player=X
    winner=check_win(board)

display_board(board)

if winner==X: print("Computer wins!")
elif winner==O: print("User wins!")
else: print("We have a draw!")