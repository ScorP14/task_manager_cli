from application.task.service import ServiceTask
from infrastructure.repository.task.json_repo import TaskRepositoryJson
from presenter.cli_client.controller import get_command_for_menu
from presenter.cli_client.view.status import set_completed_task
from presenter.cli_client.view.update import update_view
from settings.config import PATH_JSON_DB
from presenter.cli_client.view.add import add_view
from presenter.cli_client.view.print import print_task, print_tasks
from presenter.cli_client.view.get import (
    get_all_task,
    get_all_by_category_task,
    search_task,
)
from presenter.cli_client.view.delete import delete_task


def start():
    repository = TaskRepositoryJson(PATH_JSON_DB)
    task_server = ServiceTask(repository)

    while True:
        command = get_command_for_menu()
        match command:
            case 1:  # Просмотр всех текущих задач
                tasks = get_all_task(task_server)
                print_tasks(tasks)
            case 2:  # Просмотр задач по категориям
                tasks = get_all_by_category_task(task_server)
                print_tasks(tasks)
            case 3:  # Добавление новой задачи
                task = add_view(task_server)
                print_task(task)
            case 4:  # Изменение существующей задачи
                update_view(task_server)
            case 5:  # Отметка задачи как выполненной
                set_completed_task(task_server)
            case 6:  # Удаление задачи
                delete_task(task_server)
            case 7:  # Поиск задач
                tasks = search_task(task_server)
                print_tasks(tasks)
            case 8:
                break
            case _:
                print("Не известная команда, попробуйте снова. ")


if __name__ == "__main__":
    start()
