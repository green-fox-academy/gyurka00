input_file = open('encoded_zen_lines.txt')
out_file = open('out_encoded_zen_lines.txt', 'w')
output_txt = ''
input_txt =input_file.read()
lines = input_txt.split('\n')
for i in lines:
    for j in range(0,len(i)):
        if i[j] == ' ':
            output_txt += ' '
        else:
            output_txt += chr(ord(i[j])-1)
    output_txt += '\n'
out_file.write(output_txt)
input_file.close()
out_file.close()
