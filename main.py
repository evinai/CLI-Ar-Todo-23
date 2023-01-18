# ____ Date standard modules time constants ____
from functions import get_todos, write_todos, FILEPATH
# from modules import functions
import functions
import time


now = time.strftime("%Y-%m-%d %H:%M:%S")
print("It is", now)
while True:
    user_action = input("Type add, show, edit, complete or quit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)


    elif user_action.startswith("show"):
        todos = functions.get_todos(filepath=FILEPATH)

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])

            index = number - 1

            todos = functions.get_todos()

            len_todos = len(todos)
            if index > len_todos:
                print("Invalid number")
                print("Please enter a number between 1 and", len(todos))
                continue

            new_todo = input("Enter the new todo: ")
            todos[index] = new_todo + "\n"

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index]
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove.strip()} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number")

    elif user_action.startswith("quit"):
        break

    else:
        print("Invalid input")


