from todo import *

filename="tester_list.txt"

def write_file(todo_items):
    output_file = open(filename, 'w')
    output_file.write('\n'.join(todo_items))
    output_file.close()

def open_file():
    input_file = open(filename)
    input_text = input_file.read()
    input_file.close()
    return input_text

def test_assert(expected, actual, message):
    if expected == actual:
        print('check')
    else:
        print('Error: ' + message)

test_assert(add_todo("Test task"), "Test task",'It should handle "Test task"')


#def list_todo():
#def list_helper():
#def remove_helper():
#def remove_todo(task_id=''):
#def list_removed_todo():
#def completed_todo(task_id = ''):
#def uncompleted_todo(task_id = ''):
#def write_file(todo_items):
#def open_file():
