input_file = open('reversed_zen_lines.txt')
out_file = open('out_reversed_zen_lines.txt', 'w')
output_txt = ''
input_txt =input_file.read()
lines = input_txt.split('\n')
for i in lines:
    for j in range(len(i)-1,-1,-1):
        output_txt += i[j]
    output_txt += '\n'
out_file.write(output_txt)
input_file.close()
out_file.close()
