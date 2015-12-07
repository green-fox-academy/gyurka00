filename = 'alma.txt'

def wc(filename):
    input_file=open(filename)
    input_txt=input_file.read()
    chars_num = len(input_txt)
    lines_number = len(input_txt.split('\n'))
    input_file.close()
    return (chars_num,lines_number)

print(wc(filename))
