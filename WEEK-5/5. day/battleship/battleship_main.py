import battleship
reference = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10}
out_default_table = [[[] for i in range(11)] for i in range(11)]
out_default_table[0][0] = '  '
out_default_table[0][1] = 'A'
out_default_table[0][2] = 'B'
out_default_table[0][3] = 'C'
out_default_table[0][4] = 'D'
out_default_table[0][5] = 'E'
out_default_table[0][6] = 'F'
out_default_table[0][7] = 'G'
out_default_table[0][8] = 'H'
out_default_table[0][9] = 'I'
out_default_table[0][10] = 'J'
out_default_table[1][0] = ' 1'
out_default_table[2][0] = ' 2'
out_default_table[3][0] = ' 3'
out_default_table[4][0] = ' 4'
out_default_table[5][0] = ' 5'
out_default_table[6][0] = ' 6'
out_default_table[7][0] = ' 7'
out_default_table[8][0] = ' 8'
out_default_table[9][0] = ' 9'
out_default_table[10][0] = '10'
i = 1
while i < 11:
    j = 1
    while j < 11:
        out_default_table[i][j] = u"\u25A0"
        j += 1
    i += 1

ref_table = battleship.Table()

table = battleship.Table(out_default_table)
table.lives = 1
while table.lives > 0:
    table.drav_table()
    put_row = input('Write a row number: ')
    put_column = input('Write a column letter: ')
    row_number = int(put_row)
    column_number = reference[put_column.upper()]
    if ref_table.attack(row_number-1, column_number-1):
        table.lives -= 1
        table.table[row_number][column_number] = 'X'
    else:
        table.table[row_number][column_number] = 'O'

print('You are win!')
