file = open('todos.txt', 'r')
todos = file.readlines()
file.close()

def todos :
    while True:
        user_action = input('Type add, show, edit, complete or exit : ')
        user_action = user_action.strip()

        match user_action:
            case 'add':
                todo = input ('enter a todo :') + '\n'
                todos.append(todo)
                file = open('todos.txt', 'w')
                file.writelines(todos)
                file.close()
            case 'show' :
                for index, item in enumerate(todos) :
                    row = f'{index+1}-{item}'
                    print(row)
            case 'edit':
                number = int(input('Number of todo to edit:'))
                number = number -1
                new_todo = input("new todo : ")
                todos[number] = new_todo
                print(todos[number])
            case 'complete' :
                number = int(input("Number of todo to complete : "))
                todos.pop(number-1)
            case 'exit' :
                break
print ('bye!')

print('git is usefull ')