# create a dictionary to keep track of values in the board
board = {'1': ' ' , '2' : ' ' , '3' : ' ',
        '4' : ' ', '5': ' ', '6': ' ',
        '7' : ' ', '8' : ' ', '9' : ' '}
posBoard = {'1': '1' , '2' : '2' , '3' : '3',
        '4' : '4', '5': '5', '6': '6',
        '7' : '7', '8' : '8', '9' : '9'}
keys_board = []

for key in board:
    keys_board.append(key)

## function to print out the board
def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

## check to see if there is a winner when the board is at its current state
def checkValid(board):
    if board['1'] == board['2'] == board['3'] != ' ':
        printBoard(board)
        print("Gameover")
        return 1
    elif board['4'] == board['5'] == board['6'] != ' ':
        printBoard(board)
        return 1
    elif board['7'] == board['8'] == board['9'] != ' ':
        printBoard(board)
        return 1
    elif board['1'] == board['4'] == board['7'] != ' ':
        printBoard(board)
        return 1
    elif board['2'] == board['5'] == board['8'] != ' ':
        printBoard(board)
        return 1
    elif board['3'] == board['6'] == board['9'] != ' ':
        printBoard(board)
        return 1
    elif board['1'] == board['5'] == board['9'] != ' ':
        printBoard(board)
        return 1
    elif board['3'] == board['5'] == board['7'] != ' ':
        printBoard(board)
        return 1

def instructions():
    print("Welcome to TicTacToe, to play this game you need two players.")
    print("Each player will take it in turn to place X and O on the board in order to be the first to get three in a row.")
    print("The board positions are numbered as so:")
    printBoard(posBoard)
    print("Let's play the game!!")

## run the game
def game():
    turn ='X'
    count = 0

    for i in range(10):
        printBoard(board)
        print("Its " + turn + "'s turn, pick a space")
        move = input()

        if board[move] == ' ':
            board[move] = turn
            count += 1
        else: 
            print("someones already there, pick another place")
            continue

        if count >= 5:
            if checkValid(board) == 1:
                print(turn + " won the game")
                break

        if count == 9:
            print("game over, its a tie")

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    ## ask if the user's would like to play again
    again = input("Would you like to play again?(y/n)")
    if again == "y" or again == "Y":
        for key in keys_board:
            board[key] = ' '
        game()

if __name__ == "__main__":
    instructions()
    game()