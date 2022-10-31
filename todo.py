def todo():
    todo_data = []

    def inner(fn, task):
        return fn(todo_data, task)

    return inner


def add_task(todo_data, task):
    todo_data.append(task)
    return todo_data


todo_instance = todo()
print(todo_instance(add_task, 'example'))
