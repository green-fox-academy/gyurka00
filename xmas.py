def xmas_tree():
    output = ''
    output += ' '*13 + '*' + '\n' + ' '*12 + '*'*3 + '\n'
    output += ' '*10 + '*'*7 + '\n' + ' '*8 + '*'*11 + '\n'
    output += ' '*6 + '*'*15 + '\n' + ' '*10 + '*'*7 + '\n'
    output += ' '*8 + '*'*11 + '\n' + ' '*6 + '*'*15 + '\n'
    output += ' '*4 + '*'*19 + '\n' + ' '*8 + '*'*11 + '\n'
    output += ' '*6 + '*'*15 + '\n' + ' '*4 + '*'*19 + '\n'
    output += ' '*2 + '*'*23 + '\n' + ' '*6 + '*'*15 + '\n'
    output += ' '*4 + '*'*19 + '\n' + ' '*2 + '*'*23 + '\n'
    output += '*'*27 + '\n' + (' '*10 + '*'*7 + '\n')*3
    return output
print(xmas_tree(),'\nMerry Xmas and all the best!')
