input_file = open('duplicated_chars.txt')
out_file = open('out_duplicated_chars.txt', 'w')
output_txt = ''
input_txt =input_file.read()
lines = input_txt.split('\n')
for i in lines:
    for j in range(0,len(i),2):
        output_txt += i[j]
    output_txt += '\n'
out_file.write(output_txt)
input_file.close()
out_file.close()
