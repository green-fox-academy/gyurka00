#from termcolor import colored
import sys
import os
import main
import lists
import removes


def menu_table():
    # os.system('clear') # on linux / os x
    # # os.system('cls')  # on windows
    print('')
    print('')
    print('---------------------------------------------------------------------------------')
    print('|                                         					|')
    print('|                    ODOT - TODO Menu for strange Developers                    |')
    print('|                                         					|')
    print('|       1  Add task to todo list           					|')
    print('|       2  Check complated task	        					|')
    print('|       3  Delete database      						|')
    print('|       4  List all incompleted tasks from todo list      			|')
    print('|       5  List all completed tasks from todo list        			|')
    print('|       6  List all completed and incompleted tasks from todo list              |')
    print('|	7  List all completed, incompleted and removed tasks from todo list	|')
    print('|       8  Remove list element from todo list (revocable)           		|')
    print('|       9  Remove list element from todo list and database (not revocable)      |')
    print('|       10 Search              							|')
    print('|	11 Uncheck already checked task						|')
    print('|       12 Exit              	 	   					|')
    print('|                                          					|')
    print('---------------------------------------------------------------------------------')
    print('')
    print('')

def menu_input(n):
    if n == True:
        menu_table()
        sbody_input = input('Choose a number from menu: ')

        if int(sbody_input) == 1:
            main.add_todo()
        elif int(sbody_input) == 2:
            main.completed_todo()
        elif int(sbody_input) == 3:
            removes.delete_database()
        elif int(sbody_input) == 4:
            lists.list_todo()
        elif int(sbody_input) == 5:
            lists.list_todo_only_ch()
        elif int(sbody_input) == 6:
            lists.list_todo_ch()
        elif int(sbody_input) == 7:
            lists.list_todo_all()
        elif int(sbody_input) == 8:
            removes.remove_todo()
        elif int(sbody_input) == 9:
            removes.remove_todo_ultimate()
        elif int(sbody_input) == 10:
            main.search_todo()
        elif int(sbody_input) == 11:
            main.uncompleted_todo()
        elif int(sbody_input) == 12:
            exit()
        else:
            print('This is not correct number!')
            other_input = input('Choose a number from menu: ')
    while n == True:
        menu_input(True)
