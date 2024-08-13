#from functions import get_todos, write_todos
import functions

while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith('add'):
            todo = user_action[4:] + "\n"

            todos = functions.get_todos()

            todos.append(todo)

            functions.write_todos(todos)

    elif user_action.startswith('show'):

            todos = functions.get_todos()

            new_todos = []

            new_todos = [item.strip('\n') for item in todos] # This is a "list comprehension"

            for index, item in enumerate(new_todos) :
                # item = item.strip('\n')
                # Alternative way to strip off the line breaks
                row = f"{index + 1}-{item}"
                print(row)

    elif user_action.startswith('edit'):
        try:
                number = int(user_action[5:])
                number = number - 1

                todos = functions.get_todos()

                new_todo = input("Enter new todo:")
                todos[number] = new_todo + '\n'

                functions.write_todos(todos)

        except ValueError:
            print("your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            index = number - 1

            todos = functions.get_todos()

            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

        except IndexError:
            print("There is no command with that number")
            continue

    elif user_action.startswith('exit'):
            break

    else:
        print("Command is not valid")

print("bye!")



