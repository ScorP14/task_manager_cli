from application.task.service import ServiceTask
from domain.task.entity import Task
from presenter.cli_client.view.common import get_category
from typing import Sequence


def get_all_task(task_server: ServiceTask) -> Sequence[Task]:
    return task_server.get_all_task()


def get_all_by_category_task(task_server: ServiceTask) -> Sequence[Task]:
    category = get_category()

    return task_server.get_task_by_category(category)


def search_task(task_server: ServiceTask) -> Sequence[Task]:
    print("Поиск задач. ")
    search_key = input("Введите ключевое слово: ")
    return task_server.search_task(search_key)
