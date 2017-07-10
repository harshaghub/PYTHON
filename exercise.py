"""Create a list to hold the to-do tasks"""
to_do_list=[]
finished=False
while not finished:
    task = input('enter a task for your to-do list. Press <enter> when done: ')

    if len(task) == 0:
        finished=True
    else:
        to_do_list.append(task)
        print('Task added')

    """Display to-do list"""

    print()
    print('your to-do list: ')
    print('-' * 16)
    for task in to_do_list:
               print(task)
