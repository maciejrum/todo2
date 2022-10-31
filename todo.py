from pprint import pprint as pp


def sort_todo(key):
    def wrapper(fn):
        def inner(*args, **kwargs):
            return sorted(fn(*args, **kwargs), key=lambda item: item[key], reverse=True)

        return inner

    return wrapper


def todo():
    todo_data = []

    def inner(fn=None, **kwargs):
        return fn(todo_data, **kwargs) if fn is not None else todo_data

    return inner


def get_task(todo_data, task_name, task_status):
    task = None
    for task_instance in todo_data:
        if task_instance['task_name'] == task_name and task_instance['task_status'] == task_status:
            task = task_instance
            break
    return task


def add_task(todo_data, task):
    todo_data.append(task)
    return todo_data


def delete_task(todo_data, task_name, task_status):
    task = get_task(todo_data, task_name, task_status)

    if task is None:
        raise ValueError(f'Cannot delete {task_name} with status {task_status}')

    todo_data.remove(task)

    return todo_data


def update_task(todo_data, task_name, task_status, updates):
    task = get_task(todo_data, task_name, task_status)

    if task is None:
        raise ValueError(f'Cannot update {task_name} with status {task_status}')

    task.update(updates)


todo_instance = todo()
todo_instance(add_task, task={'task_name': 'Zrobić porządek', 'task_status': 'Not started'})
todo_instance(add_task, task={'task_name': 'Wyjąc naczynia ze zmywarki', 'task_status': 'Done'})
todo_instance(add_task, task={'task_name': 'Kupić mleko', 'task_status': 'In progress'})

todo_instance(update_task, task_name='Zrobić porządek', task_status='Not started',
              updates={'task_status': 'In progress'})
pp(todo_instance())
