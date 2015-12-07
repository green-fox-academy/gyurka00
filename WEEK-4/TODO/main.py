import open_write
from lists import *
import removes

def add_todo(new_task = ''):
    if new_task == '':
        new_task = input('UUPPS! No input! Please, write your task, and press enter:\n')
        return add_todo(new_task)
    todo_items = open_write.open_file().split('\n')
    todo_items.append(new_task)
    open_write.write_file(todo_items)
    print('Your new task successfully added')

def completed_todo(task_id = ''):
    items = removes.remove_helper()
    output = []
    task_ids =[]
    if task_id == '':
        list_todo()
        task_id = input('Choose a number: ')
        return completed_todo(task_id)
    task_id = int(task_id)
    task_ids=list_for_completed_helper()
    for i in range(len(task_ids)):
        if task_id == i+1:
            for j in range(len(items)):
                if j == task_ids[i]:
                    output.append(items[task_ids[i]] + 'X')
                else:
                    output.append(items[j])
    open_write.write_file(output)

def uncompleted_todo(task_id = ''):
    items = removes.remove_helper()
    output = []
    task_ids =[]
    if task_id == '':
        list_todo_only_ch()
        task_id = input('Choose a number: ')
        return uncompleted_todo(task_id)

    task_id = int(task_id)
    task_ids=list_for_uncompleted_helper()
    for i in range(len(task_ids)):
        if task_id == i+1:
            for j in range(len(items)):
                if j == task_ids[i]:
                    output.append(items[task_ids[i]][0:-1])
                else:
                    output.append(items[j])
    open_write.write_file(output)

def search_todo():
    items = removes.remove_helper()
    search_word = input('What are you looking for?: ')
    a=0
    for i in range(len(items)):
        if search_word==items[i]:
            print(str(items[i])+" is the " + str(i+1)+ ". on your list")
            break
        elif search_word==items[i][:-1] and items[i][-1]=='*':
            print(str(items[i][:-1])+ ' is already removed')
            break
        elif search_word==items[i][:-1] and items[i][-1]=='X':
            print(str(items[i][:-1])+ ' is already done')
            break
        elif search_word==items[i][:-2] and items[i][-1]=='*' and items[i][-2]=='X':
            print(str(items[i][:-2])+ ' is already done and removed')
            break
        else:
            a+=1
    if a==len(items):
        print("It is not on your todo list")
