from application.task.error import NotFoundByIdError


def set_completed_task(task_service):
    print("Измени статус : ")
    while True:
        task_id = input("Введите id: ")
        if task_id.isdigit():
            break
        else:
            print("Некорректный ввод, попробуйте снова. ")
    try:
        task_service.set_completed_task(int(task_id))
    except NotFoundByIdError as e:
        print(e.message())
        print("Попробуйте снова. ")
        set_completed_task(task_service)
