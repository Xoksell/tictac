board_size = 3

board = [1,2,3,4,5,6,7,8,9] # I used list where will be save my information about position with tic-tac
i = 0
def draw_board():
    # here I drow the board where will be my game
    print('━━┌───┬───┬───┐━━')
    print('  │ '+str(board[i])+' │ '+str(board[i+1])+' │ ' +str(board[i+2])+' │')
    print('  ├───┼───┼───┤')
    print('  │ '+str(board[i+3])+' │ '+str(board[i+4])+' │ ' +str(board[i+5])+' │')
    print('  ├───┼───┼───│')
    print('  │ '+str(board[i+6])+' │ '+str(board[i+7])+' │ ' +str(board[i+8])+' │')
    print('━━└───┴───┴───┘━━')
    


def game_step(index, char):
    #make step
    if (index > 9 or index < 1 or board[index-1] in ('X', 'O')): #here I made strong 9 steps, and finsih game if it more then 9
        return False
    board[index-1] = char
    return True

def check_win(): #this block for check everytime who win, with using combination of all possible combination in the game

    win = False
    
    combination = (
        (0,1,2), (3,4,5),(6,7,8), #horizont lines
        (0,3,6), (1,4,7), (2,5,8), #vertical lines
        (0,4,8), (2,4,6)          #diagonal lines
    )

    for pos in combination:
		#here I check if number 1 and 2 the same, however they never can be the same, as result this is save me from write a lot of kind of similar lines. Then I still chekc if 2 and 3 are the same, and if they same, you win 
        if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]] and board[pos[1]] in ('X','O')):
            win = board[pos[0]] # and here you can just see easy who is win, and in the future print who win, what also save a lot from hard code

    return win

            
                  

    return False

def start_game(): #this block contain the gameplay, how game should work
    player = "X" #who fill be the first
    step = 1 #here i do not have time, but here you can easy make who will make first step
    draw_board()
    while (step<10) and (check_win() == False):
        index = input('Player ' + player + ' make step' + '. *enter number on the field(write 0 if you wanna exit):')
        
        if (index == '0'):
            break
        
        if (game_step(int(index), player)):
            print('secssess step')


            if (player == 'X'): #here I just started to made simple version, only with me, for check how work my programm, in the futere I can connect AI for not pllay alone
                player = 'O'
            else:
                player = 'X'
            draw_board()
        else:
            print('wrong number. Try again.')

        step += 1
    else:
        print('x win')

print('Welcome to the Tic-Tac')
start_game()
draw_board()
