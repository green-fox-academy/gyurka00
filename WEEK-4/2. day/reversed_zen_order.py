input_file = open('reversed_zen_order.txt')
out_file = open('out_reversed_zen_order.txt', 'w')
input_txt =input_file.read()
input_lines = input_txt.split('\n')
for i in input_lines[::-1]:
    out_file.write(i + '\n')
input_file.close()
out_file.close()
