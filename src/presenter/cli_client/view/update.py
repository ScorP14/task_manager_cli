from application.task.error import NotFoundByIdError
from presenter.cli_client.view.common import (
    get_category,
    get_deadline,
    get_priority,
    get_status,
)
from presenter.cli_client.view.print import print_task
from application.task.service import ServiceTask


def update_view(task_server: ServiceTask):
    print("Обновление задачи: ")
    while True:
        try:
            id_task = input("Укажите номер задачи: ")
            task = task_server.get_task_by_id(int(id_task))
            break
        except NotFoundByIdError as e:
            print(e.message())

    print_task(task)
    print("Изменение задачи.")
    print("1. Название.")
    print("2. Описание.")
    print("3. Категория.")
    print("4. Срок выполнения.")
    print("5. Приоритет.")
    print("6. Статус.")
    number_field = input("Укажите номер поля которое надо изменить: ")
    mapper = {
        "1": "title",
        "2": "description",
        "3": "category",
        "4": "deadline",
        "5": "priority",
        "6": "status",
    }
    if not mapper.get(number_field):
        print("Некорректный ввод, попробуйте снова. ")

    match number_field:
        case "3":
            new_value = get_category()
        case "4":
            new_value = get_deadline()
        case "5":
            new_value = get_priority()
        case "6":
            new_value = get_status()
        case _:
            new_value = input("Новое значение: ")

    task_server.update_task(int(id_task), mapper[number_field], new_value)
