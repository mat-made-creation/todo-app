import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    UserSelection = input('Type add, show, edit, complete, or exit to interact with your todo list:')
    UserSelection = UserSelection.strip()

    if UserSelection.startswith('add'):
        todo = UserSelection[4:]

        todos = functions.get_todos()

        todos.append(todo.capitalize() + "\n")

        functions.write_todos(todos, 'todos.txt')

    elif UserSelection.startswith('show'):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)

    elif UserSelection.startswith('edit'):
        try:
            number = int(UserSelection[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo.capitalize() + '\n'

            functions.write_todos(todos, 'todos.txt')

        except ValueError:
            print('Your command is not valid')
            continue

    elif UserSelection.startswith('complete'):
        try:
            number = int(UserSelection[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos, 'todos.txt')

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There are no items with that number.")
            continue

    elif UserSelection.startswith('exit'):
        break

    else:
        print('Command is not valid')

print('Thank you for using our todo list!')
