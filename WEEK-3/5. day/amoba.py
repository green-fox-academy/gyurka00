def name_input():
    input_string = ''
    while input_string == '' :
        try:
            input_string = input('Write your name: ')
            if not input_string:
                raise ValueError('empty string')
        except ValueError:
            print('Your entered a wrong value')
    return input_string

def amoba():
    player1=name_input()
    player2=name_input()
    if player1 == player2:
        print ('This name is already taken')
        player2=name_input()
    table=[[[] for i in range(4)] for i in range(4)]
    table[0][0] = '0'
    table[0][1] = '1'
    table[0][2] = '2'
    table[0][3] = '3'
    table[1][0] = '1'
    table[2][0] = '2'
    table[3][0] = '3'
    i = 1
    while i < 4:
        j = 1
        while j < 4:
            table[i][j] = u"\u25A0"
            j += 1
        i += 1
    drav_table(table)

    user_round=9
    player = player1
    while user_round < 10:
        print(player + ' turn')
        put_row = input('Write a row number: ')
        put_column = input('Write a column number: ')
        if player == player1:
            put(table,'X',int(put_row),int(put_column))
            player = player2
        else:
            put(table,'O',int(put_row),int(put_column))
            player = player1


def put(table,symbol,i, j):
    table[i][j] = symbol
    drav_table(table)


def drav_table(matrix):
    for n in matrix:
        print(n)








amoba()
