from open_write import *
from main import *
import lists

def remove_helper():
    todo_items = open_file().split('\n')
    output = []
    for item in todo_items:
        if item != '':
            output.append(item)
    return output

def remove_todo(task_id=''):
    if task_id == '':
        lists.list_todo_all()
        task_id = input('Chose a number: ')
        return remove_todo(task_id)
    items = remove_helper()
    output = []
    task_id = int(task_id)
    for i in range(len(items)):
        if i != (task_id - 1):
            output.append(items[i])
        else:
            output.append(items[i] + '*')
    write_file(output)

def remove_todo_ultimate(task_id=''):
    if task_id == '':
        lists.list_todo_all()
        task_id = input('Chose a number: ')
        return remove_todo_ultimate(task_id)
    items = remove_helper()
    output = []
    task_id = int(task_id)
    for i in range(len(items)):
        if i != (task_id - 1):
            output.append(items[i])
    write_file(output)

def delete_database():
    realy = input('Are you reealy want to delete the database?(y/n)')
    if realy == 'y':
        open_file = open(filename, 'w')
        open_file.write('')
        open_file.close()
