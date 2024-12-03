from application.task.error import NotFoundByIdError
from application.task.service import ServiceTask
from presenter.cli_client.view.common import get_category


def delete_task(task_service: ServiceTask):
    print()
    print("Вы желаете удалить по номеру задачи или удалить всю категорию? ")
    print("1. По ID.")
    print("2. Категорию.")
    while True:
        command = input("Укажите номер действия: ")
        match command:
            case "1":
                delete_task_by_id(task_service)
            case "2":
                delete_task_by_category(task_service)
            case _:
                print("Некорректный ввод, попробуйте снова. ")
                continue
        break


def delete_task_by_category(task_service: ServiceTask):
    print()
    print("Удаление задачи. ")
    category = get_category()
    task_service.delete_task_by_category(category.value)
    print("Удаление прошло успешно. ")


def delete_task_by_id(task_service: ServiceTask):
    print()
    print("Удаление задачи. ")
    while True:
        task_id = input("Введите id: ")
        if task_id.isdigit():
            break
        else:
            print("Некорректный ввод, попробуйте снова. ")
    try:
        task_service.delete_task_by_id(int(task_id))
    except NotFoundByIdError as e:
        print(e.message())
    print("Удаление прошло успешно")
