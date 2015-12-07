import os
from open_write import *
from removes import *

def clear():
    os.system('clear') # on linux / os x
    # os.system('cls')  # on windows

def list_helper():
    todo_items = open_file().split('\n')
    output = []
    for item in todo_items:
        if item != '' and item[-1] != '*':
            output.append(item)
    return output

def list_todo(): # only unchecked
    input_list = list_helper()
    clear()
    print('\n')
    print('***************************************************')
    if len(input_list) == 0:
        print(' WOOOW, Congratulate, You haven\'t incompleted task')
        print('***************************************************')

    else:
        output = []
        print('Your incompleted tasks:')
        print('***************************************************')
        for i in range(len(input_list)):
            if input_list[i][-1] != 'X':
                output.append(input_list[i])
        for i in range(len(output)):
            print(i+1, '. ',output[i], sep='')

def list_todo_only_ch(): # only checked, need for uncompleted method
    input_list = list_helper()
    output = []
    print('Completed tasks:')
    for i in range(len(input_list)):
        if input_list[i][-1] == 'X':
            output.append(input_list[i])
    for i in range(len(output)):
        print(i+1, '. ',output[i][0:-1], sep='')

def list_todo_ch(): # checked and unchecked
    output = list_helper()
    print('Your current tasks:')
    for i in range(len(output)):
        if output[i][-1] == 'X':
            print(i+1, '. [X] ',output[i][0:-1], sep='')
        else:
            print(i+1, '. [ ] ',output[i], sep='')

def list_todo_all(): # checked, unchecked, and removed
    output = remove_helper()
    print('All tasks in system:')
    for i in range(len(output)):
        if output[i] != '' and output[i][-1] == 'X':
            print(i+1, '. [X] ',output[i][0:-1], sep='')
        elif output[i] != '' and output[i][-1] == '*':
            if output[i][-2] == 'X':
                print(i+1, '. [-] ',output[i][0:-2], sep='')
            elif output[i][-1] == '*':
                print(i+1, '. [*] ',output[i][0:-1], sep='')
        elif output[i ]!= '':
            print(i+1, '. [ ] ',output[i], sep='')

def list_removed_todo():
    todo_items = open_file().split('\n')
    output = []
    print('Removed elements:')
    for item in todo_items:
        if item != '' and item[-1] == '*':
            if item != '' and item[-2] == 'X':
                output.append(item[:-2])
            else:
                output.append(item[:-1])
    for i in range(len(output)):
        print(output[i][0:-1])

def list_for_completed_helper():
    input_list = remove_helper()
    database_position = []
    for i in range(len(input_list)):
        if input_list[i][-1] != 'X'and input_list[i][-1] != '*':
            database_position.append(i)
    return database_position

def list_for_uncompleted_helper():
    input_list = remove_helper()
    database_position = []
    for i in range(len(input_list)):
        if input_list[i][-1] == 'X':
            database_position.append(i)
    return database_position
