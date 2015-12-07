filename = 'datafile.txt' #production
# filename = 'test.txt' #for test

def write_file(todo_items):
    output_file = open(filename, 'w')
    output_file.write('\n'.join(todo_items))
    output_file.close()

def open_file():
    input_file = open(filename)
    input_text = input_file.read()
    input_file.close()
    return input_text
